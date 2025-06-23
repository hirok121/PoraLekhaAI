"""
Main AI Tutoring Agent

Orchestrates the tutoring system using sequential agents for step-by-step processing.
Focuses on text-based interactions with intelligent agent coordination.
"""

from google.adk.agents import SequentialAgent

from .agents.language_router import language_router_agent
from .agents.question_analyzer import question_analyzer_agent
from .agents.knowledge_retriever import knowledge_retriever_agent
from .agents.solution_generator import solution_generator_agent
from .agents.response_formatter import response_formatter_agent

# Create the main tutoring pipeline with text-focused processing
root_agent = SequentialAgent(
    name="AITutoringSystem",
    sub_agents=[
        language_router_agent,  # Step 1: Language detection and text routing
        question_analyzer_agent,  # Step 2: Analyze and categorize the question
        knowledge_retriever_agent,  # Step 3: Search for relevant information
        solution_generator_agent,  # Step 4: Generate solution/explanation
        response_formatter_agent,  # Step 5: Format the final response
    ],
    description="""
    AI-Based Multi-Agent Tutoring System for Bangladeshi students (grades 6-12).
    
    This system processes student questions through a sequential pipeline of specialized agents:
    
    1. Language Router Agent: 
       - Detects input language (Bengali/English/Mixed)
       - Normalizes and validates text input
       - Routes to appropriate processing pipeline
    
    2. Question Analyzer Agent:
       - Determines subject area (Math, Physics, Chemistry, Biology)
       - Identifies grade level (6-8, 9-10, 11-12)
       - Classifies question type (problem-solving, conceptual, homework help)
       - Extracts key concepts and mathematical expressions
    
    3. Knowledge Retriever Agent:
       - Searches for relevant educational content using Google Search
       - Finds grade-appropriate materials and examples
       - Gathers cultural context and real-world applications
       - Synthesizes information from multiple sources
    
    4. Solution Generator Agent:
       - Creates step-by-step solutions using pedagogical best practices
       - Provides conceptual explanations with examples
       - Uses Socratic questioning and scaffolding techniques
       - Integrates cultural context appropriate for Bangladeshi students
    
    5. Response Formatter Agent:
       - Formats responses with proper Bengali/English text
       - Renders mathematical expressions clearly
       - Organizes content in student-friendly educational structure
       - Ensures cultural appropriateness and grade-level alignment
    
    Core Features:
    - Text-only input processing with advanced language detection
    - Bilingual support for Bengali and English
    - Subject coverage: Math, Physics, Chemistry, Biology
    - Grade-level adaptive responses (6-12)
    - Cultural sensitivity for Bangladeshi educational context
    - Google Search integration for current information
    - Pedagogically sound explanations and problem-solving
    - Session-based state management (no database required)
    """,
)
