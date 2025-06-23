"""
AI-Based Multi-Agent Tutoring System for Bangladeshi Students

This module contains a text-focused tutoring agent system built with Google's ADK,
following sequential agent architecture patterns for educational applications.

Features:
- Text-only input processing with advanced language detection
- Multi-agent orchestration for comprehensive educational responses
- Bilingual support for Bengali and English
- Subject coverage: Math, Physics, Chemistry, Biology
- Grade-adaptive responses (6-12)
- Cultural sensitivity for Bangladeshi educational context
"""

from .agent import root_agent

__all__ = ["root_agent"]
