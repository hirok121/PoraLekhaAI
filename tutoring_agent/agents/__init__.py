"""
Core agents for the AI tutoring system
"""

# Import agents that actually exist in the current structure
from .conversation_router.agent import conversation_router, general_chat_agent
from .analysis_pipeline.agent import (
    analysis_pipeline_agent,
    analysis_pipeline_agent,
)
from .solution_pipeline.agent import solution_pipeline_agent
from .fast_track.fast_track_agent import (
    fast_track_educational_agent,
    query_classifier_agent,
)

__all__ = [
    # Current working agents
    "conversation_router",
    "general_chat_agent",
    "analysis_pipeline_agent",
    "analysis_pipeline_agent",
    "solution_pipeline_agent",
    "fast_track_educational_agent",
    "query_classifier_agent",
]
