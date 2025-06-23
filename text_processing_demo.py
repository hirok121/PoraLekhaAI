"""
Text Processing Demo for AI Tutoring System

Demonstrates the text-only capabilities and agent architecture
without requiring Google ADK setup for development purposes.
"""

import json
from typing import Dict, Any

# Import our text processing tools
from tutoring_agent.tools import (
    detect_language,
    normalize_text,
    extract_mathematical_expressions,
    classify_subject,
    assess_grade_level,
    validate_question_completeness,
    generate_clarifying_questions,
    extract_educational_context,
)


def display_banner():
    """Display the system banner"""
    banner = """
    🧠 AI-Based Multi-Agent Tutoring System
    ========================================
    
    Text-Only Processing Demo
    Focuses on intelligent agent orchestration for educational content
    
    Features:
    ✅ Bengali & English language detection
    ✅ Mathematical expression extraction
    ✅ Subject classification (Math, Physics, Chemistry, Biology)
    ✅ Grade level assessment (6-8, 9-10, 11-12)
    ✅ Question completeness validation
    ✅ Educational context analysis
    
    """
    print(banner)


def analyze_question(question: str) -> Dict[str, Any]:
    """
    Comprehensive analysis of a student question using text processing tools

    Args:
        question: Student's question text

    Returns:
        Dictionary with complete analysis results
    """
    print(f"\n📝 Analyzing Question: '{question}'\n")
    print("=" * 60)

    # Step 1: Language Detection and Normalization
    print("🔍 Step 1: Language Analysis")
    detected_language = detect_language(question)
    normalized_text = normalize_text(question)

    print(f"   Language: {detected_language}")
    print(f"   Original: {question}")
    print(f"   Normalized: {normalized_text}")

    # Step 2: Mathematical Expression Extraction
    print("\n🧮 Step 2: Mathematical Expression Analysis")
    math_expressions = extract_mathematical_expressions(normalized_text)

    if math_expressions:
        print("   Mathematical Expressions Found:")
        for i, expr in enumerate(math_expressions, 1):
            print(f"   {i}. Type: {expr['type']}, Expression: {expr['expression']}")
    else:
        print("   No mathematical expressions detected")

    # Step 3: Subject Classification
    print("\n📚 Step 3: Subject Classification")
    subject_analysis = classify_subject(normalized_text)

    print(f"   Primary Subject: {subject_analysis['subject']}")
    print(f"   Confidence: {subject_analysis['confidence']:.2f}")
    print(f"   Matched Keywords: {', '.join(subject_analysis['matched_keywords'][:5])}")

    # Step 4: Grade Level Assessment
    print("\n🎓 Step 4: Grade Level Assessment")
    grade_analysis = assess_grade_level(normalized_text, subject_analysis["subject"])

    print(f"   Estimated Grade Level: {grade_analysis['grade_level']}")
    print(f"   Confidence: {grade_analysis['confidence']:.2f}")
    if grade_analysis["matched_terms"]:
        print(f"   Grade Indicators: {', '.join(grade_analysis['matched_terms'])}")

    # Step 5: Question Completeness Validation
    print("\n✅ Step 5: Question Completeness Check")
    completeness = validate_question_completeness(normalized_text)

    print(f"   Is Complete: {completeness['is_complete']}")
    print(f"   Confidence: {completeness['confidence']:.2f}")

    if completeness["issues"]:
        print(f"   Issues: {', '.join(completeness['issues'])}")

    if completeness["suggestions"]:
        print("   Suggestions:")
        for suggestion in completeness["suggestions"]:
            print(f"   - {suggestion}")

    # Step 6: Educational Context Analysis
    print("\n🎯 Step 6: Educational Context Analysis")
    context = extract_educational_context(normalized_text)

    if context["question_types"]:
        print(f"   Question Types: {', '.join(context['question_types'])}")

    if context["difficulty_indicators"]:
        print(
            f"   Difficulty Indicators: {', '.join(context['difficulty_indicators'])}"
        )

    # Step 7: Generate Clarifying Questions (if needed)
    if not completeness["is_complete"]:
        print("\n❓ Step 7: Clarifying Questions")
        analysis_summary = {
            "language": detected_language,
            "subject": subject_analysis["subject"],
            "issues": completeness["issues"],
        }

        clarifying_questions = generate_clarifying_questions(analysis_summary)

        if clarifying_questions:
            print("   Suggested clarifying questions:")
            for i, q in enumerate(clarifying_questions, 1):
                print(f"   {i}. {q}")

    # Return comprehensive analysis
    return {
        "language": detected_language,
        "normalized_text": normalized_text,
        "mathematical_expressions": math_expressions,
        "subject_analysis": subject_analysis,
        "grade_analysis": grade_analysis,
        "completeness": completeness,
        "educational_context": context,
    }


def demonstrate_agent_workflow():
    """Demonstrate the multi-agent workflow conceptually"""
    print("\n🤖 Multi-Agent Workflow Overview")
    print("=" * 50)

    agents = [
        {
            "name": "Language Router Agent",
            "description": "Detects language and routes text to appropriate processing pipeline",
            "responsibilities": [
                "Language detection (Bengali/English)",
                "Text normalization and cleaning",
                "Input validation",
                "Processing pipeline routing",
            ],
        },
        {
            "name": "Question Analyzer Agent",
            "description": "Analyzes and categorizes questions for appropriate handling",
            "responsibilities": [
                "Subject classification",
                "Grade level assessment",
                "Question type identification",
                "Key concept extraction",
            ],
        },
        {
            "name": "Knowledge Retriever Agent",
            "description": "Searches for relevant educational content using Google Search",
            "responsibilities": [
                "Educational content discovery",
                "Grade-appropriate resource finding",
                "Cultural context integration",
                "Information synthesis",
            ],
        },
        {
            "name": "Solution Generator Agent",
            "description": "Creates pedagogically sound solutions and explanations",
            "responsibilities": [
                "Step-by-step problem solving",
                "Conceptual explanations",
                "Socratic questioning",
                "Educational best practices",
            ],
        },
        {
            "name": "Response Formatter Agent",
            "description": "Formats final responses with proper structure and language",
            "responsibilities": [
                "Language-appropriate formatting",
                "Mathematical expression rendering",
                "Educational structure organization",
                "Quality assurance",
            ],
        },
    ]

    for i, agent in enumerate(agents, 1):
        print(f"\n{i}. {agent['name']}")
        print(f"   Description: {agent['description']}")
        print(f"   Key Responsibilities:")
        for resp in agent["responsibilities"]:
            print(f"   • {resp}")


def main():
    """Main demo function"""
    display_banner()

    # Sample questions for demonstration
    sample_questions = [
        "২x + ৫ = ১৩ সমীকরণটি সমাধান করুন।",  # Bengali math problem
        "Explain the process of photosynthesis in plants",  # English biology question
        "A ball is thrown upward with initial velocity 20 m/s. How high will it go?",  # Physics problem
        "help me with math",  # Vague question requiring clarification
        "What is the molecular formula of water and explain its structure?",  # Chemistry question
    ]

    print("🎓 Sample Question Analysis")
    print("=" * 40)

    for i, question in enumerate(sample_questions, 1):
        print(f"\n📋 Example {i}/{len(sample_questions)}")
        analysis = analyze_question(question)

        if i < len(sample_questions):
            input("\nPress Enter to continue to next example...")

    # Demonstrate agent workflow
    demonstrate_agent_workflow()

    print("\n" + "=" * 60)
    print("✨ Demo Complete!")
    print(
        "\nThis demonstrates the text processing capabilities of the AI tutoring system."
    )
    print("In the full system, these analyses would guide the Google ADK agents")
    print("to provide comprehensive, culturally-appropriate educational responses.")
    print("\nNext steps:")
    print("1. Set up Google ADK environment")
    print("2. Configure Google API key")
    print("3. Run the full agent pipeline with: python simple_demo.py")


if __name__ == "__main__":
    main()
