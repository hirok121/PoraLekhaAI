"""
Main AI Tutoring Agent

Orchestrates the tutoring system with conversation routing and intelligent agent coordination.
Handles both general conversation and educational content efficiently.
"""

from google.adk.agents import SequentialAgent

from .agents.conversation_router import conversation_router_agent
from .agents.question_clarification import question_clarification_agent
from .agents.language_router import language_router_agent
from .agents.question_analyzer import question_analyzer_agent
from .agents.knowledge_retriever import knowledge_retriever_agent
from .agents.solution_generator import solution_generator_agent
from .agents.response_formatter import response_formatter_agent


# Create the main system as a sequential agent for ADK compatibility
root_agent = SequentialAgent(
    name="AITutoringSystem",
    sub_agents=[
        conversation_router_agent,  # Step 1: Route conversation type
        question_clarification_agent,  # Step 2: Clarify if needed
        language_router_agent,  # Step 3: Language processing
        question_analyzer_agent,  # Step 4: Question analysis
        knowledge_retriever_agent,  # Step 5: Knowledge retrieval
        solution_generator_agent,  # Step 6: Solution generation
        response_formatter_agent,  # Step 7: Response formatting
    ],
    description="""
    AI-Based Multi-Agent Tutoring System for Bangladeshi students (grades 6-12).
    
    This system intelligently routes conversations and processes student questions:

    Architecture:
    1. Conversation Router: Determines if input is general chat or educational
    2. Question Clarification: Helps clarify unclear educational questions  
    3. Language Router: Handles bilingual Bengali/English processing
    4. Question Analyzer: Categorizes educational content by subject/grade
    5. Knowledge Retriever: Searches for relevant information
    6. Solution Generator: Creates pedagogically sound explanations
    7. Response Formatter: Formats final response appropriately

    Key Features:
    - Smart routing: General chat handled quickly, educational content gets full processing
    - Bilingual support: Bengali and English with mixed language handling
    - Subject coverage: Math, Physics, Chemistry, Biology (grades 6-12)
    - Cultural sensitivity: Aligned with Bangladeshi educational context
    - Question clarification: Helps students ask better questions
    - Efficient processing: Complex agents only activated when needed

    Usage:
    - General conversation: "Hello", "How are you?" → Quick friendly response
    - Educational questions: "Solve 2x + 5 = 13" → Full tutoring pipeline
    - Unclear questions: "Help with math" → Clarification prompts
    """,
)
