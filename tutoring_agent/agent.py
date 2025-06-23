"""
Main AI Tutoring Agent

Orchestrates the tutoring system with conversation routing and intelligent agent coordination.
Handles both general conversation and educational content efficiently.

This implementation includes performance optimizations for better speed and scalability.
"""

from .agents.optimized_system import (
    optimized_tutoring_system,
)

root_agent = optimized_tutoring_system
