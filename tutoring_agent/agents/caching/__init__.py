"""
Smart Caching Module

Implements intelligent caching for the AI tutoring system to improve response times
and reduce API calls for similar or repeated queries.
"""

from .smart_cache_agent import (
    smart_caching_agent,
    cached_conversation_router_agent,
    create_query_fingerprint,
)

__all__ = [
    "smart_caching_agent",
    "cached_conversation_router_agent",
    "create_query_fingerprint",
]
