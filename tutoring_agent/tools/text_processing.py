"""
Text processing tools for the AI tutoring system
Focuses on language detection, mathematical expression parsing, and educational text processing
"""

import re
import json
from typing import Dict, Any, List, Optional, Tuple


def detect_language(text: str) -> str:
    """
    Detect if the input text is primarily in Bengali or English

    Args:
        text: Input text to analyze

    Returns:
        'bengali', 'english', or 'mixed'
    """
    # Count Bengali Unicode characters (Bangla script range)
    bengali_chars = len(re.findall(r"[\u0980-\u09FF]", text))

    # Count English alphabet characters
    english_chars = len(re.findall(r"[a-zA-Z]", text))

    # Count total meaningful characters (exclude spaces, punctuation)
    total_chars = bengali_chars + english_chars

    if total_chars == 0:
        return "english"  # Default for non-text content

    bengali_ratio = bengali_chars / total_chars
    english_ratio = english_chars / total_chars

    # Determine language based on character distribution
    if bengali_ratio > 0.6:
        return "bengali"
    elif english_ratio > 0.6:
        return "english"
    else:
        return "mixed"


def normalize_text(text: str) -> str:
    """
    Normalize and clean input text for processing

    Args:
        text: Raw input text

    Returns:
        Cleaned and normalized text
    """
    # Remove extra whitespaces
    text = re.sub(r"\s+", " ", text.strip())

    # Normalize Bengali numerals to English numerals for mathematical processing
    bengali_to_english_digits = {
        "০": "0",
        "১": "1",
        "২": "2",
        "৩": "3",
        "৪": "4",
        "৫": "5",
        "৬": "6",
        "৭": "7",
        "৮": "8",
        "৯": "9",
    }

    for bengali, english in bengali_to_english_digits.items():
        text = text.replace(bengali, english)

    # Standardize mathematical operators
    text = text.replace("×", "*")
    text = text.replace("÷", "/")
    text = text.replace("−", "-")

    # Clean up common typos and formatting issues
    text = re.sub(r"([0-9])\s*([x])\s*([0-9])", r"\1*\3", text)  # "2 x 3" → "2*3"
    text = re.sub(r"([0-9])\s*\*\s*([a-zA-Z])", r"\1*\2", text)  # "2 * x" → "2*x"

    return text


def extract_mathematical_expressions(text: str) -> List[Dict[str, Any]]:
    """
    Extract mathematical expressions and equations from text

    Args:
        text: Input text containing math expressions

    Returns:
        List of dictionaries with expression information
    """
    expressions = []

    # Patterns for different types of mathematical expressions
    patterns = {
        "equation": r"[0-9a-zA-Z\+\-\*/\(\)\s]*=\s*[0-9a-zA-Z\+\-\*/\(\)\s]+",
        "algebraic": r"[0-9]*[a-zA-Z][0-9]*[\+\-\*/\^]*[0-9a-zA-Z\+\-\*/\(\)\s]*",
        "arithmetic": r"[0-9]+[\+\-\*/][0-9\+\-\*/\(\)\s]+",
        "function": r"\b(?:sin|cos|tan|log|ln|sqrt|exp)\s*\([^)]+\)",
        "fraction": r"[0-9]+/[0-9]+",
        "power": r"[0-9a-zA-Z]+\^[0-9]+",
    }

    for expr_type, pattern in patterns.items():
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            expressions.append(
                {
                    "type": expr_type,
                    "expression": match.group().strip(),
                    "start_pos": match.start(),
                    "end_pos": match.end(),
                }
            )

    # Remove duplicates and overlapping expressions
    expressions = sorted(
        expressions, key=lambda x: (x["start_pos"], -len(x["expression"]))
    )
    filtered_expressions = []

    for expr in expressions:
        # Check if this expression overlaps with any already added
        overlaps = False
        for existing in filtered_expressions:
            if (
                expr["start_pos"] < existing["end_pos"]
                and expr["end_pos"] > existing["start_pos"]
            ):
                overlaps = True
                break

        if not overlaps:
            filtered_expressions.append(expr)

    return filtered_expressions


def classify_subject(text: str) -> Dict[str, Any]:
    """
    Classify the subject area of a question based on keywords and context

    Args:
        text: Question text

    Returns:
        Dictionary with subject classification and confidence
    """
    text_lower = text.lower()

    # Define subject keywords (Bengali and English)
    subject_keywords = {
        "math": {
            "keywords": [
                # English keywords
                "algebra",
                "geometry",
                "trigonometry",
                "calculus",
                "equation",
                "solve",
                "graph",
                "function",
                "derivative",
                "integral",
                "triangle",
                "circle",
                "square",
                "rectangle",
                "angle",
                "area",
                "volume",
                "perimeter",
                "quadratic",
                "linear",
                "polynomial",
                "matrix",
                "vector",
                # Bengali keywords
                "বীজগণিত",
                "জ্যামিতি",
                "ত্রিকোণমিতি",
                "সমীকরণ",
                "সমাধান",
                "ত্রিভুজ",
                "বৃত্ত",
                "চতুর্ভুজ",
                "কোণ",
                "ক্ষেত্রফল",
                "আয়তন",
                "পরিসীমা",
                "দ্বিঘাত",
                "রৈখিক",
                "বহুপদী",
                "ম্যাট্রিক্স",
            ],
            "weight": 1.0,
        },
        "physics": {
            "keywords": [
                # English keywords
                "force",
                "motion",
                "velocity",
                "acceleration",
                "energy",
                "power",
                "electricity",
                "magnetism",
                "light",
                "sound",
                "wave",
                "pressure",
                "temperature",
                "heat",
                "mechanics",
                "optics",
                "thermodynamics",
                # Bengali keywords
                "বল",
                "গতি",
                "বেগ",
                "ত্বরণ",
                "শক্তি",
                "ক্ষমতা",
                "বিদ্যুৎ",
                "চুম্বক",
                "আলো",
                "শব্দ",
                "তরঙ্গ",
                "চাপ",
                "তাপমাত্রা",
                "তাপ",
                "বলবিদ্যা",
            ],
            "weight": 1.0,
        },
        "chemistry": {
            "keywords": [
                # English keywords
                "atom",
                "molecule",
                "element",
                "compound",
                "reaction",
                "acid",
                "base",
                "salt",
                "chemical",
                "periodic",
                "bond",
                "electron",
                "ion",
                "catalyst",
                "organic",
                "inorganic",
                "oxidation",
                "reduction",
                # Bengali keywords
                "পরমাণু",
                "অণু",
                "মৌল",
                "যৌগ",
                "বিক্রিয়া",
                "অ্যাসিড",
                "ক্ষার",
                "লবণ",
                "রাসায়নিক",
                "পর্যায়",
                "বন্ধন",
                "ইলেকট্রন",
                "আয়ন",
            ],
            "weight": 1.0,
        },
        "biology": {
            "keywords": [
                # English keywords
                "cell",
                "tissue",
                "organ",
                "system",
                "plant",
                "animal",
                "human",
                "genetics",
                "evolution",
                "ecosystem",
                "photosynthesis",
                "respiration",
                "protein",
                "dna",
                "rna",
                "chromosome",
                "enzyme",
                # Bengali keywords
                "কোষ",
                "টিস্যু",
                "অঙ্গ",
                "তন্ত্র",
                "উদ্ভিদ",
                "প্রাণী",
                "মানুষ",
                "বংশগতি",
                "বিবর্তন",
                "বাস্তুতন্ত্র",
                "সালোকসংশ্লেষণ",
                "শ্বসন",
                "প্রোটিন",
                "ডিএনএ",
                "আরএনএ",
                "ক্রোমোজোম",
                "এনজাইম",
            ],
            "weight": 1.0,
        },
    }

    # Calculate scores for each subject
    subject_scores = {}

    for subject, data in subject_keywords.items():
        score = 0
        matched_keywords = []

        for keyword in data["keywords"]:
            if keyword in text_lower:
                score += data["weight"]
                matched_keywords.append(keyword)

        subject_scores[subject] = {"score": score, "matched_keywords": matched_keywords}

    # Determine the most likely subject
    max_score = max([data["score"] for data in subject_scores.values()])

    if max_score == 0:
        return {
            "subject": "general",
            "confidence": 0.1,
            "matched_keywords": [],
            "all_scores": subject_scores,
        }

    # Find subject(s) with maximum score
    top_subjects = [
        subj for subj, data in subject_scores.items() if data["score"] == max_score
    ]

    # If tie, prefer based on expression types found
    math_expressions = extract_mathematical_expressions(text)
    if len(top_subjects) > 1 and math_expressions:
        if "math" in top_subjects:
            primary_subject = "math"
        elif "physics" in top_subjects:
            primary_subject = "physics"
        else:
            primary_subject = top_subjects[0]
    else:
        primary_subject = top_subjects[0]

    # Calculate confidence based on score and context
    total_possible_score = len(subject_keywords[primary_subject]["keywords"])
    confidence = min(max_score / total_possible_score, 1.0)

    return {
        "subject": primary_subject,
        "confidence": confidence,
        "matched_keywords": subject_scores[primary_subject]["matched_keywords"],
        "all_scores": subject_scores,
    }


def assess_grade_level(text: str, subject: str) -> Dict[str, Any]:
    """
    Assess the appropriate grade level for a question

    Args:
        text: Question text
        subject: Subject area

    Returns:
        Dictionary with grade level assessment
    """
    text_lower = text.lower()

    # Define grade level indicators
    grade_indicators = {
        "6-8": {
            "math": [
                "addition",
                "subtraction",
                "multiplication",
                "division",
                "fraction",
                "decimal",
                "percentage",
                "basic",
                "simple",
                "যোগ",
                "বিয়োগ",
                "গুণ",
                "ভাগ",
                "ভগ্নাংশ",
                "দশমিক",
                "শতকরা",
            ],
            "physics": ["basic", "simple", "elementary", "speed", "distance", "time"],
            "chemistry": ["basic", "simple", "states of matter", "mixture", "solution"],
            "biology": ["basic", "simple", "plant parts", "animal parts", "food chain"],
        },
        "9-10": {
            "math": [
                "quadratic",
                "trigonometry",
                "logarithm",
                "coordinate",
                "দ্বিঘাত",
                "ত্রিকোণমিতি",
                "লগারিদম",
                "স্থানাঙ্ক",
            ],
            "physics": [
                "force",
                "motion",
                "electricity",
                "light",
                "sound",
                "বল",
                "গতি",
                "বিদ্যুৎ",
                "আলো",
                "শব্দ",
            ],
            "chemistry": [
                "atomic structure",
                "periodic table",
                "chemical bonding",
                "acid base",
                "পরমাণু গঠন",
                "পর্যায় সারণি",
            ],
            "biology": [
                "cell",
                "tissue",
                "genetics",
                "evolution",
                "কোষ",
                "টিস্যু",
                "বংশগতি",
            ],
        },
        "11-12": {
            "math": [
                "calculus",
                "derivative",
                "integral",
                "limits",
                "matrix",
                "vector",
                "statistics",
                "ক্যালকুলাস",
                "অন্তরকরণ",
                "সমাকলন",
            ],
            "physics": [
                "advanced",
                "quantum",
                "relativity",
                "electromagnetic",
                "thermodynamics",
                "modern physics",
            ],
            "chemistry": [
                "organic",
                "physical chemistry",
                "chemical kinetics",
                "equilibrium",
                "জৈব রসায়ন",
            ],
            "biology": [
                "molecular biology",
                "biotechnology",
                "ecology",
                "advanced genetics",
            ],
        },
    }

    # Score each grade level
    grade_scores = {}

    for grade, subjects in grade_indicators.items():
        score = 0
        matched_terms = []

        if subject in subjects:
            for term in subjects[subject]:
                if term in text_lower:
                    score += 1
                    matched_terms.append(term)

        grade_scores[grade] = {"score": score, "matched_terms": matched_terms}

    # Determine most likely grade level
    max_score = max([data["score"] for data in grade_scores.values()])

    if max_score == 0:
        # Default based on complexity heuristics
        word_count = len(text.split())
        math_expr_count = len(extract_mathematical_expressions(text))

        if word_count < 10 and math_expr_count <= 1:
            estimated_grade = "6-8"
            confidence = 0.3
        elif word_count < 20 and math_expr_count <= 2:
            estimated_grade = "9-10"
            confidence = 0.4
        else:
            estimated_grade = "11-12"
            confidence = 0.5
    else:
        # Find grade level with highest score
        top_grades = [
            grade for grade, data in grade_scores.items() if data["score"] == max_score
        ]
        estimated_grade = (
            top_grades[0] if len(top_grades) == 1 else "9-10"
        )  # Default to middle
        confidence = min(max_score / 3, 1.0)  # Normalize confidence

    return {
        "grade_level": estimated_grade,
        "confidence": confidence,
        "matched_terms": (
            grade_scores[estimated_grade]["matched_terms"] if max_score > 0 else []
        ),
        "all_scores": grade_scores,
    }


def validate_question_completeness(text: str) -> Dict[str, Any]:
    """
    Assess if a question has sufficient information for a meaningful response

    Args:
        text: Question text

    Returns:
        Dictionary with completeness assessment
    """
    issues = []
    suggestions = []

    # Check for overly vague questions
    vague_patterns = [
        r"^(help|explain|what|how|tell)(\s+me)?(\s+about)?\s*$",
        r"^(math|physics|chemistry|biology|science)\s*$",
        r"^(homework|assignment|problem)\s*$",
    ]

    text_clean = text.strip().lower()

    for pattern in vague_patterns:
        if re.match(pattern, text_clean):
            issues.append("too_vague")
            suggestions.append(
                "Please be more specific about the topic or problem you need help with."
            )
            break

    # Check for incomplete mathematical problems
    if "solve" in text_clean:
        math_exprs = extract_mathematical_expressions(text)
        if not math_exprs:
            issues.append("missing_equation")
            suggestions.append(
                "Please provide the complete equation or mathematical expression to solve."
            )

    # Check for context-dependent references without context
    context_refs = ["this", "that", "it", "above", "previous", "following"]
    if any(ref in text_clean for ref in context_refs):
        # Check if there's actual context provided
        if len(text.split()) < 8:  # Very short text with references
            issues.append("missing_context")
            suggestions.append(
                "Please provide the complete context or reference material you are referring to."
            )

    # Check minimum length for meaningful questions
    if len(text.strip()) < 5:
        issues.append("too_short")
        suggestions.append("Please provide more details about what you need help with.")

    # Assess overall completeness
    is_complete = len(issues) == 0
    confidence = 1.0 - (len(issues) * 0.25)  # Reduce confidence by 25% per issue

    return {
        "is_complete": is_complete,
        "confidence": max(confidence, 0.1),
        "issues": issues,
        "suggestions": suggestions,
    }


def generate_clarifying_questions(analysis: Dict[str, Any]) -> List[str]:
    """
    Generate appropriate clarifying questions based on question analysis

    Args:
        analysis: Combined analysis from other functions

    Returns:
        List of clarifying questions in appropriate language
    """
    questions = []
    language = analysis.get("language", "english")
    subject = analysis.get("subject", "general")
    issues = analysis.get("issues", [])

    # Language-specific question templates
    if language == "bengali":
        templates = {
            "too_vague": [
                f"{subject} বিষয়ের কোন নির্দিষ্ট টপিকে আপনার সাহায্য দরকার?",
                "আপনি কোন ধরনের সমস্যার সমাধান চান?",
            ],
            "missing_equation": [
                "দয়া করে সম্পূর্ণ সমীকরণ বা গাণিতিক রাশি দিন।",
                "কোন নির্দিষ্ট সমস্যাটি সমাধান করতে হবে?",
            ],
            "missing_context": [
                "আপনি কোন নির্দিষ্ট সমস্যা বা উদাহরণের কথা বলছেন?",
                "অনুগ্রহ করে সম্পূর্ণ প্রসঙ্গ বা রেফারেন্স দিন।",
            ],
        }
    else:  # English
        templates = {
            "too_vague": [
                f"Which specific topic in {subject} would you like help with?",
                "What type of problem or concept do you need assistance with?",
            ],
            "missing_equation": [
                "Please provide the complete equation or mathematical expression.",
                "What specific problem would you like me to solve?",
            ],
            "missing_context": [
                "Which specific problem or example are you referring to?",
                "Please provide the complete context or reference material.",
            ],
        }

    # Generate questions based on identified issues
    for issue in issues:
        if issue in templates:
            questions.extend(templates[issue])

    # Add subject-specific clarifying questions if needed
    if "too_vague" in issues:
        if subject == "math":
            if language == "bengali":
                questions.append(
                    "আপনার সমস্যাটি কি বীজগণিত, জ্যামিতি, নাকি অন্য কোন শাখার?"
                )
            else:
                questions.append(
                    "Is your question about algebra, geometry, trigonometry, or another area of math?"
                )
        elif subject == "physics":
            if language == "bengali":
                questions.append(
                    "পদার্থবিজ্ঞানের কোন বিষয়ে সাহায্য চান - বল ও গতি, তাপ, আলো, নাকি বিদ্যুৎ?"
                )
            else:
                questions.append(
                    "Which area of physics - mechanics, heat, light, electricity, or something else?"
                )

    return questions[:3]  # Return maximum 3 clarifying questions


def format_mathematical_expression(expr: str) -> str:
    """
    Format mathematical expressions for better display

    Args:
        expr: Mathematical expression

    Returns:
        Formatted expression
    """
    # Basic LaTeX-style formatting
    formatted = expr

    # Handle exponents
    formatted = re.sub(r"\^(\d+)", r"^{\1}", formatted)
    formatted = re.sub(r"\^([a-zA-Z])", r"^{\1}", formatted)

    # Handle fractions (simple cases)
    formatted = re.sub(r"(\d+)/(\d+)", r"\\frac{\1}{\2}", formatted)

    # Handle square roots
    formatted = re.sub(r"sqrt\(([^)]+)\)", r"\\sqrt{\1}", formatted)

    # Handle common functions
    for func in ["sin", "cos", "tan", "log", "ln"]:
        formatted = re.sub(f"\\b{func}\\b", f"\\{func}", formatted)

    return formatted


def extract_educational_context(text: str) -> Dict[str, Any]:
    """
    Extract educational context and learning objectives from question

    Args:
        text: Question text

    Returns:
        Dictionary with educational context information
    """
    context = {
        "question_types": [],
        "learning_objectives": [],
        "prerequisites": [],
        "difficulty_indicators": [],
    }

    text_lower = text.lower()

    # Identify question types
    if any(word in text_lower for word in ["solve", "calculate", "find", "compute"]):
        context["question_types"].append("problem_solving")

    if any(word in text_lower for word in ["explain", "describe", "what is", "define"]):
        context["question_types"].append("conceptual_understanding")

    if any(word in text_lower for word in ["how", "why", "when", "where"]):
        context["question_types"].append("analytical")

    if any(word in text_lower for word in ["prove", "derive", "show that"]):
        context["question_types"].append("proof_based")

    # Identify difficulty indicators
    if any(
        word in text_lower for word in ["basic", "simple", "elementary", "fundamental"]
    ):
        context["difficulty_indicators"].append("basic")

    if any(
        word in text_lower
        for word in ["advanced", "complex", "difficult", "challenging"]
    ):
        context["difficulty_indicators"].append("advanced")

    if any(word in text_lower for word in ["step by step", "detailed", "thorough"]):
        context["difficulty_indicators"].append("requires_detailed_explanation")

    return context
