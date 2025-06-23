"""
Fast-Track Educational Agent Implementation

Handles simple educational queries quickly without complex pipeline processing,
following ADK best practices for performance optimization.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import FunctionTool
import re


# Simple calculator function for basic math
def simple_calculator(expression: str) -> str:
    """
    Safely evaluate simple mathematical expressions
    """
    try:
        # Remove spaces and validate expression
        expr = expression.strip().replace(" ", "")

        # Only allow basic math operations and numbers
        if not re.match(r"^[0-9+\-*/().\s]+$", expr):
            return "Invalid expression - only basic math operations allowed"

        # Evaluate safely
        result = eval(expr)
        return f"{expression} = {result}"
    except:
        return f"Cannot calculate: {expression}"


# Quick definition lookup function
def quick_definition_lookup(term: str, subject: str = "general") -> str:
    """
    Provide quick definitions for common educational terms
    """
    definitions = {
        # Math terms
        "algebra": "A branch of mathematics that uses letters and symbols to represent numbers and quantities in formulas and equations.",
        "geometry": "The branch of mathematics concerned with the properties and relations of points, lines, surfaces, and solids.",
        "calculus": "Advanced mathematics involving rates of change and accumulation of quantities.",
        # Science terms
        "photosynthesis": "The process by which plants use sunlight to synthesize foods from carbon dioxide and water.",
        "gravity": "The force that attracts objects toward the center of the Earth or toward any other physical body having mass.",
        "atom": "The basic unit of a chemical element, consisting of protons, neutrons, and electrons.",
        # General academic terms
        "hypothesis": "A proposed explanation for a phenomenon, used as a starting point for investigation.",
        "analysis": "Detailed examination of the elements or structure of something.",
    }

    term_lower = term.lower()
    if term_lower in definitions:
        return f"{term}: {definitions[term_lower]}"
    else:
        return f"Quick definition not available for '{term}'. This may require detailed research."


# Create function tools
calculator_tool = FunctionTool(func=simple_calculator)
definition_tool = FunctionTool(func=quick_definition_lookup)

# Fast-track educational agent
fast_track_educational_agent = LlmAgent(
    name="FastTrackEducationalAgent",
    model="gemini-2.0-flash",
    instruction="""
    You are a fast-track educational agent designed to handle simple educational queries quickly and efficiently.

    **Your Purpose:**
    Provide immediate, accurate responses to basic educational questions without complex processing pipeline overhead.

    **Handle These Query Types Quickly:**
    
    1. **Simple Calculations:**
       - Basic arithmetic: addition, subtraction, multiplication, division
       - Simple algebraic equations: "solve 2x + 5 = 13"
       - Basic geometry: area, perimeter calculations
       - Use the calculator tool for mathematical expressions
    
    2. **Quick Definitions:**
       - Common academic terms and concepts
       - Basic scientific definitions
       - Mathematical terminology
       - Use the definition lookup tool when available
    
    3. **Factual Questions:**
       - Simple "what is..." questions
       - Basic scientific facts
       - Mathematical formulas and principles
       - Historical dates and events
    
    4. **Formula Requests:**
       - Area and volume formulas
       - Basic physics equations
       - Mathematical identities
       - Chemical formulas for common compounds
    
    **Response Guidelines:**
    - Provide direct, clear answers
    - Include brief explanations when helpful
    - Use appropriate academic language for the grade level
    - Support both Bengali and English responses
    - Be concise but complete
    - If the question is too complex, route to full pipeline
    
    **Routing Decision:**
    - If you can answer completely and confidently: Provide full response
    - If partial answer possible: Give what you can and suggest further help
    - If too complex: Return "ROUTE_TO_FULL_PIPELINE" for complex processing
    
    **Examples:**
    - "What is 15 × 8?" → Direct calculation
    - "Define photosynthesis" → Quick definition with brief explanation
    - "Area of rectangle formula" → A = length × width
    - "Solve complex differential equation" → ROUTE_TO_FULL_PIPELINE
    
    Remember: Speed and accuracy are your priorities. Provide immediate value to students.
    """,
    description="Fast-track agent for simple educational queries, providing 50-70% faster responses for basic questions",
    tools=[calculator_tool, definition_tool],
    output_key="fast_track_response",
)

# Simple query classifier to determine if fast-track is appropriate
query_classifier_agent = LlmAgent(
    name="QueryClassifierAgent",
    model="gemini-2.0-flash",
    instruction="""
    Classify educational queries for optimal routing:
    
    **Classification Categories:**
    
    1. **SIMPLE_EDUCATIONAL** (Route to Fast-Track):
       - Basic calculations and arithmetic
       - Simple definitions and explanations
       - Common formulas and facts
       - Single-concept questions
       - Questions answerable in 1-2 sentences
    
    2. **COMPLEX_EDUCATIONAL** (Route to Full Pipeline):
       - Multi-step problem solving
       - Detailed explanations required
       - Complex analysis or synthesis
       - Questions requiring research
       - Pedagogical step-by-step teaching needed
    
    3. **GENERAL** (Route to General Chat):
       - Casual conversation
       - Greetings and social interaction
       - Non-academic topics
    
    **Response Format:**
    ```json
    {
        "classification": "SIMPLE_EDUCATIONAL|COMPLEX_EDUCATIONAL|GENERAL",
        "confidence": 0.0-1.0,
        "reasoning": "brief explanation of classification",
        "estimated_processing_time": "immediate|fast|standard|complex"
    }
    ```
    
    **Optimization Goal:**
    Route as many queries as possible to fast-track processing while maintaining quality.
    """,
    description="Intelligent query classifier for optimal routing and performance",
    output_key="query_classification",
)
