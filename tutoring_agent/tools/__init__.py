"""
Text processing tools for the AI tutoring system
Focuses on language detection, mathematical expression parsing, and educational content analysis
"""

from .text_processing import (
    detect_language,
    normalize_text,
    extract_mathematical_expressions,
    classify_subject,
    assess_grade_level,
    validate_question_completeness,
    generate_clarifying_questions,
    format_mathematical_expression,
    extract_educational_context,
)

__all__ = [
    "detect_language",
    "normalize_text",
    "extract_mathematical_expressions",
    "classify_subject",
    "assess_grade_level",
    "validate_question_completeness",
    "generate_clarifying_questions",
    "format_mathematical_expression",
    "extract_educational_context",
]
