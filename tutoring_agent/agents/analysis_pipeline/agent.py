"""
Analysis Pipeline Agent

Sequential agent that combines language routing and question analysis.
First stage: Language detection and text normalization
Second stage: Question analysis and categorization
"""

from google.adk.agents import SequentialAgent
from ..language_router.agent import language_router_agent
from ..question_analyzer.agent import question_analyzer_agent

analysis_pipeline_agent = SequentialAgent(
    name="EducationalAgent_AnalysisPipelineAgent",
    description="First stage of educational processing: combines language detection/normalization with comprehensive question analysis to prepare content for solution generation pipeline.",
    sub_agents=[
        language_router_agent,  # Stage 1: Detects language (Bengali/English) and normalizes text
        question_analyzer_agent,  # Stage 2: Analyzes subject, grade level, difficulty, and routes to solution pipeline
    ],
)
