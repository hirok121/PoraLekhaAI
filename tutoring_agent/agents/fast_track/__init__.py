"""
Fast Track Module

Implements fast-track routing for simple educational queries to provide
immediate responses without complex processing.
"""

from .fast_track_agent import (
    fast_track_educational_agent,
    query_classifier_agent,
    calculator_tool,
    definition_tool,
)

__all__ = [
    "fast_track_educational_agent",
    "query_classifier_agent",
    "calculator_tool",
    "definition_tool",
]
