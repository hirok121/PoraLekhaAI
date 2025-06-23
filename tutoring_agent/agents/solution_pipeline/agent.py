"""
Solution Pipeline Agent

Sequential agent that combines knowledge retrieval, solution generation, and response formatting.
Second stage: Knowledge retrieval and content gathering
Third stage: Solution generation with pedagogical approach
Fourth stage: Response formatting and presentation
"""

from google.adk.agents import SequentialAgent
from ..knowledge_retriever.agent import knowledge_retriever_agent
from ..solution_generator.agent import solution_generator_agent
from ..response_formatter.agent import response_formatter_agent

solution_pipeline_agent = SequentialAgent(
    name="SolutionPipelineAgent",
    description="Final stage of educational processing: retrieves relevant knowledge, generates pedagogically sound solutions, and formats responses for optimal learning experience.",
    sub_agents=[
        knowledge_retriever_agent,  # Stage 1: Searches for relevant educational content and resources
        solution_generator_agent,  # Stage 2: Creates step-by-step solutions using educational best practices
        response_formatter_agent,  # Stage 3: Formats final response with proper language and mathematical notation
    ],
)
