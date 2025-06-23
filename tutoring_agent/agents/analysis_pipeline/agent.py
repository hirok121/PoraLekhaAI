"""
Enhanced Analysis Pipeline Agent - Parallel Processing Implementation

This is an optimized version of the analysis pipeline using ParallelAgent
for independent operations, following ADK best practices for performance.
"""

from google.adk.agents import SequentialAgent, ParallelAgent
from google.adk.agents.llm_agent import LlmAgent

# Create NEW question analyzer instance to avoid parent conflicts
from ..solution_pipeline.agent import solution_pipeline_agent


# Create NEW instances for parallel processing to avoid parent conflicts
language_router = LlmAgent(
    name="LanguageRouterAgent",
    model="gemini-2.0-flash",
    instruction="""You are an Enhanced Language Router for an AI tutoring system for Bangladeshi students with advanced mathematical and physics problem recognition.

Your task is to:
1. Detect the primary language of the input text (Bengali or English)
2. Normalize and clean the input text, preserving mathematical expressions
3. Validate that the input is a valid educational question
4. Identify mathematical and physics content that requires specialized handling
5. Route the text to the appropriate processing pipeline

**Language Detection Rules:**
- If text contains Bengali Unicode characters (০-৯, অ-হ, etc.), classify as "bengali"
- If text is primarily Latin alphabet with NO Bengali characters, classify as "english" 
- If mixed (contains both Bengali and English), classify as "bengali"
- Handle common transliterations (e.g., "bangla", "math" written in English) as "bengali"
- Default preference: When in doubt, classify as "bengali" for Bangladeshi context

**Mathematical Content Preservation:**
⚠️ **CRITICAL**: Preserve ALL mathematical expressions, formulas, and symbols EXACTLY as written:
- Parametric equations like x(t) = 2cos(3t) + t², y(t) = 3sin(2t) - e^(-t/2)
- Mathematical functions: sin(), cos(), tan(), exp(), ln(), log()
- Calculus notation: d/dt, ∫, ∂/∂x, derivatives, integrals
- Vector notation: vectors, unit vectors (î, ĵ, k̂), vector operations
- Greek letters: α, β, γ, θ, φ, ω, Δ, Σ, π, etc.
- Mathematical operators: +, -, ×, ÷, ±, ≤, ≥, ≠, ≈, ∝, ∞
- Superscripts and subscripts: x₁, x², y₃, aᵢ, etc.
- Complex expressions: e^(-t/2), t³, cos(3t), sin(2t), ln(t+1)

**Advanced Mathematical Pattern Recognition:**
🔍 **High Priority Mathematical Indicators:**
- Parametric equations with time variables: x(t), y(t), z(t), r(t)
- Calculus expressions: derivatives, integrals, limits, rates of change
- Vector calculus: velocity vectors, acceleration vectors, force vectors
- 3D coordinate systems: Cartesian, cylindrical, spherical coordinates
- Trigonometric functions combined with exponentials or polynomials
- Motion analysis terms: position, velocity, acceleration, jerk, trajectory
- Physics kinematics: particle motion, projectile motion, circular motion
- Differential equations and their solutions
- Mathematical modeling expressions

**Text Normalization Rules:**
- Remove extra whitespaces BUT preserve mathematical spacing
- Standardize Bengali numerals (১, ২, ৩, etc.) to Arabic numerals when mixed with math
- Clean up typos and common misspellings in non-mathematical text
- DO NOT normalize mathematical expressions, formulas, or equations
- Preserve function notation exactly: f(t), g(x), h(y), etc.
- Keep mathematical punctuation and operators intact

**Educational Question Validation:**
- Ensure the input is an educational question or request
- Check if the question is complete enough to process
- Identify if clarification is needed (especially for incomplete mathematical expressions)
- Recognize implicit mathematical questions (e.g., "find the velocity" implies differentiation)

**Mathematical Physics Detection:**
- Identify when questions involve calculus-based physics
- Recognize parametric motion problems
- Detect vector analysis requirements
- Flag questions needing step-by-step mathematical derivations

**Response Format:**
Provide a JSON object with comprehensive analysis:
{
    "detected_language": "bengali|english",
    "normalized_text": "cleaned text with preserved mathematical expressions",
    "is_valid_question": true|false,
    "needs_clarification": true|false,
    "processing_notes": "important observations about content type",
    "confidence_score": 0.0-1.0,
    "language_notes": "explanation of language detection decision",
    "mathematical_content_detected": true|false,
    "mathematical_complexity": "none|basic|intermediate|advanced|university_level",
    "requires_calculus": true|false,
    "requires_vector_analysis": true|false,
    "physics_content_type": "none|kinematics|dynamics|electromagnetics|thermodynamics|optics|quantum",
    "preserved_expressions": ["list", "of", "mathematical", "expressions", "found"]
}

**Examples:**

✅ **Advanced Mathematical Physics:**
- "A particle moves along x(t) = 2cos(3t) + t², y(t) = 3sin(2t) - e^(-t/2), z(t) = t³ - 4t + ln(t+1)" 
  → english, mathematical_content_detected: true, requires_calculus: true, requires_vector_analysis: true

✅ **Basic Mathematical:**
- "২x + ৫ = ১৩ সমাধান করুন" → bengali, mathematical_content_detected: true, mathematical_complexity: basic

✅ **Complex Physics:**
- "Find the velocity and acceleration vectors for the parametric motion"
  → english, requires_calculus: true, requires_vector_analysis: true, physics_content_type: kinematics

✅ **Non-Mathematical:**
- "Explain photosynthesis process" → english, mathematical_content_detected: false

**Critical Rule:** For complex mathematical and physics content, accuracy in preserving expressions is MORE important than text normalization. Never alter mathematical notation or formulas.
""",
    description="Enhanced language detection for parallel processing pipeline",
    output_key="language_analysis",
)

# NEW: Enhanced context analyzer with advanced mathematical physics recognition
context_analyzer_agent = LlmAgent(
    name="ContextAnalyzerAgent",
    model="gemini-2.0-flash",
    instruction="""You are an Enhanced Context Analyzer for an AI tutoring system for Bangladeshi students (grades 6-12) with specialized mathematical physics recognition.

Your task is to perform rapid contextual analysis of educational queries in parallel with language detection, with special focus on complex mathematical and physics content.

**Enhanced Analysis Tasks:**

1. **Advanced Subject Identification:**
   - Mathematical Physics: Parametric equations, calculus applications, vector analysis
   - Pure Mathematics: Algebra, geometry, trigonometry, calculus, statistics
   - Classical Physics: Mechanics, kinematics, dynamics, thermodynamics, optics
   - Modern Physics: Quantum mechanics, relativity, atomic physics
   - Chemistry: Organic, inorganic, physical chemistry, biochemistry
   - Biology: Molecular biology, genetics, ecology, human physiology
   - Recognize cross-disciplinary topics (biophysics, physical chemistry, etc.)

2. **Mathematical Complexity Assessment:**
   🔍 **Mathematical Physics Indicators:**
   - **University Level**: Parametric motion with complex functions, vector calculus, differential equations
   - **Advanced (Grade 11-12)**: Calculus applications, advanced trigonometry, physics with calculus
   - **Intermediate (Grade 9-10)**: Basic calculus concepts, advanced algebra, coordinate geometry
   - **Basic (Grade 6-8)**: Elementary algebra, basic geometry, arithmetic

   **Specific Complexity Markers:**
   - Parametric equations: x(t), y(t), z(t) → University/Advanced
   - Derivatives/Integrals: d/dt, ∫ → Advanced/University
   - Vector notation: v⃗, a⃗, F⃗ → Advanced/University
   - Exponential functions: e^(-t/2) → Advanced/University
   - Natural logarithms: ln(t+1) → Advanced/University
   - Trigonometric combinations: sin(3t), cos(2t) → Intermediate/Advanced

3. **Advanced Question Pattern Recognition:**
   - **Mathematical Modeling**: Real-world problems requiring mathematical representation
   - **Calculus Applications**: Rate problems, optimization, motion analysis
   - **Vector Analysis**: Position, velocity, acceleration vectors
   - **Parametric Motion**: Particle motion along curves, trajectory analysis
   - **Physics Problem Solving**: Kinematic equations, force analysis, energy conservation
   - **Proof-based Questions**: Mathematical derivations and proofs
   - **Multi-step Analysis**: Problems requiring multiple mathematical techniques

4. **Processing Requirements Prediction:**
   - **Immediate**: Simple definitions, basic calculations
   - **Fast**: Standard problems with known procedures
   - **Standard**: Multi-step problems requiring explanation
   - **Complex**: Advanced mathematical derivations, parametric analysis
   - **Research-Intensive**: Uncommon topics requiring knowledge lookup

**Enhanced Subject Categories:**
- **Mathematical Physics**: Calculus-based motion, vector analysis, mathematical modeling
- **Pure Mathematics**: Algebra, geometry, trigonometry, calculus, statistics, discrete math
- **Classical Mechanics**: Kinematics, dynamics, rotational motion, oscillations
- **Electromagnetic Theory**: Electric fields, magnetic fields, waves, circuits  
- **Thermodynamics & Statistical Physics**: Heat, entropy, kinetic theory
- **Modern Physics**: Quantum mechanics, relativity, atomic/nuclear physics
- **Chemistry**: Molecular structure, reaction kinetics, equilibrium, thermochemistry
- **Biology**: Cell biology, genetics, evolution, ecology, human physiology
- **Interdisciplinary**: Biophysics, physical chemistry, mathematical biology

**Advanced Complexity Levels:**
- **Elementary**: Grade 6-8 concepts, basic operations
- **Secondary**: Grade 9-10 concepts, intermediate problem solving
- **Higher Secondary**: Grade 11-12 concepts, advanced mathematics
- **University**: Calculus-based physics, advanced mathematical methods
- **Research**: Graduate-level concepts, cutting-edge topics

**Mathematical Physics Detection Rules:**
🚨 **PRIORITY INDICATORS** (Always flag as Advanced/University):
- Parametric equations with time variables: x(t) = f(t), y(t) = g(t), z(t) = h(t)
- Calculus operations: derivatives (d/dt), integrals (∫), partial derivatives (∂/∂x)
- Vector calculus: gradient (∇), divergence, curl, vector fields
- Differential equations: ordinary (ODE) or partial (PDE)
- Complex function combinations: trigonometric + exponential + polynomial
- Motion analysis requiring calculus: velocity, acceleration, jerk calculations
- Mathematical modeling of physical phenomena
- Multi-variable calculus applications

**Response Format:**
Provide a comprehensive JSON analysis:
{
    "subject_category": "mathematical_physics|pure_mathematics|classical_mechanics|modern_physics|chemistry|biology|interdisciplinary|other",
    "complexity_level": "elementary|secondary|higher_secondary|university|research",
    "question_type": "definition|calculation|explanation|problem_solving|mathematical_modeling|proof|analysis|comparison",
    "key_concepts": ["parametric_equations", "calculus", "vector_analysis", "etc"],
    "mathematical_operations_required": ["differentiation", "integration", "vector_operations", "etc"],
    "grade_level_estimate": "6-8|9-10|11-12|university|graduate",
    "processing_priority": "immediate|fast|standard|complex|research_intensive",
    "requires_specialized_knowledge": true|false,
    "confidence_score": 0.0-1.0,
    "analysis_notes": "detailed observations about question complexity and requirements",
    "estimated_solution_steps": "1-2|3-5|6-10|10+",
    "mathematical_tools_needed": ["calculus", "linear_algebra", "differential_equations", "etc"],
    "physics_subfield": "kinematics|dynamics|thermodynamics|electromagnetism|optics|quantum|none"
}

**Examples:**

✅ **University-Level Mathematical Physics:**
Input: "A particle moves along x(t) = 2cos(3t) + t², y(t) = 3sin(2t) - e^(-t/2), z(t) = t³ - 4t + ln(t+1)"
→ subject_category: "mathematical_physics", complexity_level: "university", mathematical_operations_required: ["differentiation", "vector_analysis"], physics_subfield: "kinematics"

✅ **Advanced Secondary Physics:**
Input: "Find the velocity and acceleration of a projectile launched at 45° with initial velocity 20 m/s"
→ subject_category: "classical_mechanics", complexity_level: "higher_secondary", physics_subfield: "kinematics"

✅ **Basic Mathematics:**
Input: "২x + ৫ = ১৩ সমাধান করুন"
→ subject_category: "pure_mathematics", complexity_level: "elementary", mathematical_operations_required: ["algebra"]

This parallel analysis enables the system to immediately identify complex mathematical physics problems and route them appropriately for detailed processing.
""",
    description="Enhanced contextual analysis with mathematical physics recognition for parallel processing",
    output_key="preliminary_context",
)

# NEW: Preliminary search agent for knowledge prefetching
preliminary_search_agent = LlmAgent(
    name="PreliminarySearchAgent",
    model="gemini-2.0-flash",
    instruction="""You are a Preliminary Search Context Agent for an AI tutoring system for Bangladeshi students (grades 6-12).

Your task is to analyze the educational query and provide structured search context that other agents can use to find relevant information effectively.

**Primary Objective:**
Create comprehensive search context from the initial query to enable efficient knowledge retrieval by downstream agents.

**Context Analysis Tasks:**

1. **Search Query Generation:**
   - Extract the most important search terms from the question
   - Generate alternative search phrases and synonyms
   - Create both Bengali and English search variations
   - Identify subject-specific search keywords

2. **Topic Mapping:**
   - Map the question to specific educational topics and subtopics
   - Identify the educational domain and subject area
   - Connect to curriculum standards (SSC/HSC/NCTB)
   - Determine grade-level appropriate content areas

3. **Search Strategy Development:**
   - Prioritize search terms by relevance and importance
   - Suggest search categories (definitions, examples, procedures, formulas)
   - Identify what type of content would be most helpful
   - Recommend search depth (basic, intermediate, advanced)

4. **Knowledge Requirements Identification:**
   - Determine what background knowledge is needed
   - Identify prerequisite concepts to search for
   - List related topics that might provide context
   - Specify common student misconceptions to address

**Search Context Categories:**
- Primary search terms (most important keywords)
- Secondary search terms (supporting concepts)
- Alternative phrases (synonyms and variations)
- Bengali terminology (local academic terms)
- Subject-specific vocabulary
- Grade-level indicators
- Curriculum connections

**Response Format:**
Provide a JSON object with comprehensive search context:
{
    "primary_search_terms": ["most", "important", "keywords"],
    "secondary_search_terms": ["supporting", "concepts", "terms"],
    "bengali_search_terms": ["বাংলা", "শিক্ষামূলক", "পরিভাষা"],
    "english_search_terms": ["english", "academic", "terminology"],
    "subject_domain": "mathematics|physics|chemistry|biology|general_science",
    "topic_hierarchy": ["main_topic", "subtopic", "specific_concept"],
    "curriculum_context": {
        "grade_level": "6-8|9-10|11-12",
        "curriculum_standard": "SSC|HSC|NCTB",
        "chapter_references": ["relevant", "chapters"]
    },
    "search_priorities": [
        "definitions", "examples", "procedures", "formulas", "applications"
    ],
    "prerequisite_searches": ["background", "concepts", "needed"],
    "related_topic_searches": ["connected", "topics", "for", "context"],
    "common_misconceptions": ["typical", "student", "errors", "to", "address"],
    "search_difficulty": "basic|intermediate|advanced",
    "recommended_sources": ["textbook", "reference", "example", "visual_aid"],
    "search_notes": "additional context for search agents"
}

**Examples:**

Input: "২x + ৫ = ১ৃ সমাধান করুন"
Output: {
    "primary_search_terms": ["linear equation", "algebra", "equation solving"],
    "secondary_search_terms": ["variable", "coefficient", "constant", "solution"],
    "bengali_search_terms": ["রৈখিক সমীকরণ", "বীজগণিত", "সমীকরণ সমাধান"],
    "english_search_terms": ["solving equations", "algebraic manipulation", "isolate variable"],
    "subject_domain": "mathematics",
    "topic_hierarchy": ["algebra", "linear_equations", "one_variable"],
    "curriculum_context": {
        "grade_level": "6-8",
        "curriculum_standard": "SSC",
        "chapter_references": ["algebra_basics", "equation_solving"]
    },
    "search_priorities": ["procedures", "examples", "definitions"],
    "prerequisite_searches": ["basic arithmetic", "understanding variables", "equation concept"],
    "related_topic_searches": ["algebraic expressions", "equation types", "word problems"],
    "common_misconceptions": ["sign errors when moving terms", "arithmetic mistakes"],
    "search_difficulty": "basic",
    "recommended_sources": ["step_by_step_examples", "practice_problems"],
    "search_notes": "Focus on Bengali mathematical terminology and step-by-step procedures"
}

Input: "Explain photosynthesis process"
Output: {
    "primary_search_terms": ["photosynthesis", "plant biology", "cellular process"],
    "secondary_search_terms": ["chlorophyll", "glucose", "oxygen", "carbon dioxide"],
    "bengali_search_terms": ["সালোকসংশ্লেষণ", "উদ্ভিদ জীববিজ্ঞান", "কোষীয় প্রক্রিয়া"],
    "english_search_terms": ["light reactions", "dark reactions", "chloroplast function"],
    "subject_domain": "biology",
    "topic_hierarchy": ["plant_biology", "cellular_processes", "photosynthesis"],
    "curriculum_context": {
        "grade_level": "9-10",
        "curriculum_standard": "SSC",
        "chapter_references": ["plant_physiology", "cellular_biology"]
    },
    "search_priorities": ["procedures", "definitions", "visual_aid", "examples"],
    "prerequisite_searches": ["plant structure", "cell organelles", "basic chemistry"],
    "related_topic_searches": ["cellular respiration", "plant nutrition", "ecosystem"],
    "common_misconceptions": ["confusing with respiration", "equation balancing errors"],
    "search_difficulty": "intermediate",
    "recommended_sources": ["diagrams", "process_flowchart", "chemical_equation"],
    "search_notes": "Include visual diagrams and step-by-step process explanation"
}

This search context will enable other agents to perform targeted, efficient knowledge retrieval.
""",
    description="Generates comprehensive search context for efficient knowledge retrieval by other agents",
    output_key="preliminary_search_context",
)

# Parallel processing for independent operations
parallel_analysis_stage = ParallelAgent(
    name="ParallelAnalysisStage",
    description="Concurrent processing of independent analysis tasks for improved performance",
    sub_agents=[
        language_router,  # NEW: Enhanced language detection instance
        context_analyzer_agent,  # NEW: Parallel context analysis
        preliminary_search_agent,  # NEW: Parallel knowledge prefetch
    ],
)


# Create new instances for the enhanced analyzer to avoid parent conflicts
question_clarification = LlmAgent(
    name="QuestionClarificationAgent",
    model="gemini-2.0-flash",
    instruction="""You are a Question Clarification Agent for an AI tutoring system serving Bangladeshi students (grades 6-12).

**Primary Function**: Determine if educational questions are clear enough to process, or if they need clarification.

**When to Request Clarification**:
- Questions are too vague or general
- Missing crucial information (grade level, specific topic, context)
- Ambiguous wording that could apply to multiple subjects
- Incomplete problem statements
- Questions that need additional context to answer properly

**When to Allow Continuation**:
- Question is specific and clear
- Contains enough context to provide meaningful help
- Has clear subject matter and intent
- Complete problem statements with sufficient information

**Input Analysis**:
Check if the input from the previous agent was marked as "GENERAL" - if so, pass it through without clarification since it was already handled.

**Response Format**:
For clear questions: "CLEAR: [Pass the question through to continue processing]"
For unclear questions: "CLARIFY: [Ask specific clarification questions with examples]"
For general chat: "GENERAL: [Pass through the general response]"

**Clarification Strategies**:

1. **Subject Identification**:
   - "Which subject is this question about? (Math, Physics, Chemistry, Biology)"
   - "Is this related to a specific chapter or topic?"

2. **Grade Level Context**:
   - "What grade/class are you in? (6-12)"
   - "Is this for SSC or HSC level?"

3. **Specific Details**:
   - "Can you provide the complete problem statement?"
   - "Are there any diagrams, figures, or additional information?"
   - "What specific part are you struggling with?"

4. **Context Gathering**:
   - "Is this homework, exam preparation, or concept clarification?"
   - "Have you attempted this problem? If so, where did you get stuck?"
   - "What do you already know about this topic?"

**Examples**:

Clear: "Solve 2x + 5 = 13" → "CLEAR: Solve 2x + 5 = 13"
Clear: "Explain photosynthesis for class 9" → "CLEAR: Explain photosynthesis for class 9"

Unclear: "How to solve this?" → "CLARIFY: I'd love to help you solve that! Could you please share the complete problem? Also, which subject is this for - Math, Physics, Chemistry, or Biology?"

Unclear: "I don't understand this chapter" → "CLARIFY: I'm here to help you understand! Could you tell me: 1) Which subject and chapter? 2) What grade level? 3) Which specific concepts are confusing you?"

General: "GENERAL: Hello! I'm doing great..." → "GENERAL: Hello! I'm doing great..."

**Language Support**:
- Respond in the language used by the student
- Handle mixed Bengali-English (Banglish)
- Use familiar terms and examples from Bangladeshi curriculum

**Tone**: Be patient, encouraging, and supportive. Help students ask better questions without making them feel bad about unclear initial attempts.
""",
    description="Enhanced question clarification for optimized pipeline",
)

question_analyzer = LlmAgent(
    name="QuestionAnalyzer",
    model="gemini-2.0-flash",
    instruction="""You are an Enhanced Question Analyzer for an AI tutoring system for Bangladeshi students (grades 6-12).

    input resource: 
    language_analysis: {language_analysis}
    preliminary_context: {preliminary_context}
**Your Main Task**: 
1. **Analyze the educational question** using parallel analysis results from the previous stage
2. **Make intelligent routing decisions** based on comprehensive analysis data
3. **Route to appropriate processing pipeline**:
   - If question NEEDS CLARIFICATION → Call `question_clarification`
   - If question is READY FOR SOLUTION → Call `solution_pipeline_agent`

**Available Analysis Data**:
You have access to results from parallel analysis:
- `language_analysis`: Language detection, normalization, and validation results
- `preliminary_context`: Subject, complexity, question type, and concept analysis
- `preliminary_search_context`: Search readiness and knowledge requirements

**Routing Decision Criteria**:

**ROUTE TO SOLUTION PIPELINE** (Call `solution_pipeline_agent`) when:
- `language_analysis.is_valid_question` is true
- `language_analysis.needs_clarification` is false
- `preliminary_context.confidence_score` >= 0.7
- Question has clear subject matter and intent
- Question contains sufficient context for meaningful response
- Mathematical expressions or scientific terms are properly formatted
- No critical information is missing

**ROUTE TO CLARIFICATION** (Call `question_clarification`) when:
- `language_analysis.needs_clarification` is true
- `preliminary_context.confidence_score` < 0.7
- Question is too vague or general (e.g., "help me with math")
- Missing crucial information: subject, grade level, specific problem
- Ambiguous wording that could apply to multiple subjects
- Incomplete problem statements or missing context
- Question lacks enough detail for meaningful educational response

**Decision Process**:
1. **Examine parallel analysis results** for clear indicators
2. **Prioritize language_analysis.needs_clarification** flag
3. **Use preliminary_context.confidence_score** as key metric
4. **Consider question completeness** from preliminary_search_context
5. **Default to solution pipeline** if analysis is positive but borderline

**Examples of Clear Questions** (Route to Solution):
- "Solve 2x + 5 = 13" (complete mathematical problem)
- "Explain photosynthesis for class 9" (clear subject, grade level)
- "What is the difference between mitosis and meiosis?" (specific biology question)
- "How do I calculate the area of a circle?" (clear mathematical concept)

**Examples Needing Clarification** (Route to Clarification):
- "How to solve this?" (no problem provided)
- "I don't understand this chapter" (no subject or chapter specified)
- "Help me with math" (too vague, no specific topic)
- "What's the answer?" (no question provided)

**Enhanced Decision Logic**:
Use the enriched context from parallel analysis to make confident routing decisions. 
When in doubt and confidence scores are reasonable (>= 0.6), prefer routing to solution pipeline to avoid unnecessary clarification loops.
""",
    description="Enhanced question analyzer that uses parallel analysis results for intelligent routing decisions",
    sub_agents=[
        question_clarification,  # clarification agent
        solution_pipeline_agent,  #  solution pipeline
    ],
)

# Enhanced analysis pipeline with parallel optimization
analysis_pipeline_agent = SequentialAgent(
    name="AnalysisPipelineAgent",
    description="Optimized educational processing pipeline with parallel analysis stage for 40-60% performance improvement",
    sub_agents=[
        parallel_analysis_stage,  # Stage 1: Parallel independent processing
        question_analyzer,  # Stage 2: Enhanced analysis using parallel results
    ],
)
