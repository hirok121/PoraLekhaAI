"""
Main AI Tutoring Agent

Orchestrates the tutoring system with conversation routing and intelligent agent coordination.
Handles both general conversation and educational content efficiently.
"""

from google.adk.agents import SequentialAgent

from .agents.conversation_router import conversation_router_agent
from .agents.general_chat import general_chat_agent
from .agents.education_agent import education_agent
from .agents.analysis_pipeline import analysis_pipeline_agent
from .agents.solution_pipeline import solution_pipeline_agent


# Create the main system as a sequential agent for ADK compatibility
root_agent = SequentialAgent(
    name="AITutoringSystem",
    sub_agents=[
        conversation_router_agent,  # Main router that handles all conversation types and routing
    ],
    description="""
    AI-Based Multi-Agent Tutoring System for Bangladeshi students (grades 6-12).
    
    This system uses a main conversation router that intelligently handles all interactions:

    System Architecture:
    1. Conversation Router (Main Agent):
       - Determines if input is general chat or educational content
       - For general chat: Routes to general chat agent for friendly responses
       - For educational content: Routes through analysis and solution pipelines
       - Manages the complete conversation flow and agent coordination

    The conversation router acts as the central orchestrator that:
    - Routes general conversations to dedicated chat handling
    - Processes educational questions through specialized tutoring pipelines
    - Coordinates between language processing, question analysis, and solution generation
    - Ensures appropriate responses for both casual and academic interactions

    Key Features:
    - Centralized routing: Single entry point for all conversation types
    - Intelligent delegation: Router manages all sub-agent coordination
    - Bilingual support: Bengali and English with mixed language (Banglish) handling
    - Subject coverage: Math, Physics, Chemistry, Biology (grades 6-12)
    - Cultural sensitivity: Aligned with Bangladeshi educational context (NCTB standards)
    - Efficient processing: Optimized routing based on conversation type

    Usage Examples:
    - General conversation: "Hello", "আপনার নাম কি?" → Router handles via general chat agent
    - Educational questions: "Solve 2x + 5 = 13", "পদার্থবিজ্ঞান সম্পর্কে বলুন" → Router coordinates full tutoring pipeline
    """,
)
