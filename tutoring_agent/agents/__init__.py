"""
Core agents for the AI tutoring system
"""

from .conversation_router.agent import conversation_router_agent
from .general_chat.agent import general_chat_agent
from .analysis_pipeline.agent import analysis_pipeline_agent
from .solution_pipeline.agent import solution_pipeline_agent
from .question_clarification.agent import question_clarification_agent
from .language_router.agent import language_router_agent
from .question_analyzer.agent import question_analyzer_agent
from .knowledge_retriever.agent import knowledge_retriever_agent
from .solution_generator.agent import solution_generator_agent
from .response_formatter.agent import response_formatter_agent

# Import optimized components
from .optimized_system import (
    optimized_tutoring_system,
    performance_monitor_agent,
)
from .caching.smart_cache_agent import smart_caching_agent
from .fast_track.fast_track_agent import (
    fast_track_educational_agent,
    query_classifier_agent,
)
from .analysis_pipeline.enhanced_agent import enhanced_analysis_pipeline_agent
from .solution_pipeline.optimized_agent import optimized_solution_pipeline_agent

__all__ = [
    # Original agents
    "conversation_router_agent",
    "general_chat_agent",
    "analysis_pipeline_agent",
    "solution_pipeline_agent",
    "question_clarification_agent",
    "language_router_agent",
    "question_analyzer_agent",
    "knowledge_retriever_agent",
    "solution_generator_agent",
    "response_formatter_agent",
    # Optimized system components
    "optimized_tutoring_system",
    "gradual_optimization_system",
    "performance_monitor_agent",
    "smart_caching_agent",
    "fast_track_educational_agent",
    "query_classifier_agent",
    "enhanced_analysis_pipeline_agent",
    "optimized_solution_pipeline_agent",
]
