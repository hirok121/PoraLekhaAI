"""
Fast-Track Educational Agent Implementation

Handles simple educational queries quickly without complex pipeline processing,
following ADK best practices for performance optimization.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import FunctionTool
import re


# Simple calculator function for basic math with explanations
def simple_calculator(expression: str) -> str:
    """
    Safely evaluate simple mathematical expressions with step-by-step explanation
    """
    try:
        # Remove spaces and validate expression
        expr = expression.strip().replace(" ", "")

        # Only allow basic math operations and numbers
        if not re.match(r"^[0-9+\-*/().\s]+$", expr):
            return "Invalid expression - only basic math operations allowed"

        # Evaluate safely
        result = eval(expr)

        # Provide explanation based on operation type
        explanation = ""
        if (
            "+" in expr
            and expr.count("+") == 1
            and "*" not in expr
            and "/" not in expr
            and "-" not in expr
        ):
            parts = expr.split("+")
            explanation = f"Adding {parts[0]} and {parts[1]} together: "
        elif (
            "-" in expr
            and expr.count("-") == 1
            and "*" not in expr
            and "/" not in expr
            and "+" not in expr
        ):
            parts = expr.split("-")
            explanation = f"Subtracting {parts[1]} from {parts[0]}: "
        elif (
            "*" in expr
            and expr.count("*") == 1
            and "+" not in expr
            and "/" not in expr
            and "-" not in expr
        ):
            parts = expr.split("*")
            explanation = f"Multiplying {parts[0]} by {parts[1]}: "
        elif (
            "/" in expr
            and expr.count("/") == 1
            and "+" not in expr
            and "*" not in expr
            and "-" not in expr
        ):
            parts = expr.split("/")
            explanation = f"Dividing {parts[0]} by {parts[1]}: "
        else:
            explanation = f"Calculating the expression {expression}: "

        return f"{explanation}{expression} = {result}"
    except:
        return f"Cannot calculate: {expression}"


# Quick definition lookup function with detailed explanations
def quick_definition_lookup(term: str, subject: str = "general") -> str:
    """
    Provide quick definitions with explanations for common educational terms
    """
    definitions = {
        # Math terms with explanations
        "algebra": {
            "definition": "A branch of mathematics that uses letters and symbols to represent numbers and quantities in formulas and equations.",
            "explanation": "For example, in the equation 'x + 5 = 10', the letter 'x' represents an unknown number that we need to find. Algebra helps us solve for these unknowns systematically.",
        },
        "geometry": {
            "definition": "The branch of mathematics concerned with the properties and relations of points, lines, surfaces, and solids.",
            "explanation": "Geometry helps us understand shapes, sizes, and spatial relationships. For instance, it teaches us how to calculate the area of a rectangle (length × width) or the circumference of a circle (2πr).",
        },
        "calculus": {
            "definition": "Advanced mathematics involving rates of change and accumulation of quantities.",
            "explanation": "Calculus has two main parts: derivatives (which measure how fast something changes) and integrals (which measure total accumulation). It's used in physics, engineering, and many other fields.",
        },
        # Science terms with explanations
        "photosynthesis": {
            "definition": "The process by which plants use sunlight to synthesize foods from carbon dioxide and water.",
            "explanation": "This process occurs in chloroplasts and can be summarized as: 6CO₂ + 6H₂O + sunlight → C₆H₁₂O₆ + 6O₂. Plants essentially 'eat' sunlight and produce oxygen as a byproduct, which is why they're crucial for life on Earth.",
        },
        "gravity": {
            "definition": "The force that attracts objects toward the center of the Earth or toward any other physical body having mass.",
            "explanation": "Gravity is why objects fall downward and why we stay on the ground. The more massive an object, the stronger its gravitational pull. Earth's gravity accelerates falling objects at 9.8 m/s².",
        },
        "atom": {
            "definition": "The basic unit of a chemical element, consisting of protons, neutrons, and electrons.",
            "explanation": "Think of an atom like a tiny solar system: the nucleus (protons and neutrons) is at the center, and electrons orbit around it. The number of protons determines what element it is.",
        },
        # General academic terms with explanations
        "hypothesis": {
            "definition": "A proposed explanation for a phenomenon, used as a starting point for investigation.",
            "explanation": "A hypothesis is like an educated guess that can be tested. It should be specific and measurable. For example: 'Plants grow taller when given more sunlight' is a testable hypothesis.",
        },
        "analysis": {
            "definition": "Detailed examination of the elements or structure of something.",
            "explanation": "Analysis involves breaking down complex information into smaller parts to understand it better. In literature, you might analyze themes and characters; in science, you might analyze experimental data.",
        },
    }

    term_lower = term.lower()
    if term_lower in definitions:
        info = definitions[term_lower]
        return f"**{term}:** {info['definition']}\n\n**Explanation:** {info['explanation']}"
    else:
        return f"Quick definition not available for '{term}'. This may require detailed research."


# Formula explanation function
def formula_explainer(formula_name: str) -> str:
    """
    Provide common formulas with explanations of when and how to use them
    """
    formulas = {
        "area of rectangle": {
            "formula": "A = length × width",
            "explanation": "This formula calculates the space inside a rectangle. Multiply the length by the width to find how many unit squares fit inside.",
            "example": "For a rectangle that is 5 meters long and 3 meters wide: A = 5 × 3 = 15 square meters",
        },
        "area of circle": {
            "formula": "A = πr²",
            "explanation": "This calculates the area of a circle using its radius (r). π (pi) ≈ 3.14159.",
            "example": "For a circle with radius 4 cm: A = π × 4² = π × 16 ≈ 50.27 square cm",
        },
        "circumference of circle": {
            "formula": "C = 2πr",
            "explanation": "This finds the distance around a circle using its radius (r).",
            "example": "For a circle with radius 3 m: C = 2 × π × 3 ≈ 18.85 meters",
        },
        "pythagorean theorem": {
            "formula": "a² + b² = c²",
            "explanation": "In a right triangle, the square of the longest side (hypotenuse) equals the sum of squares of the other two sides.",
            "example": "If two sides are 3 and 4 units: 3² + 4² = 9 + 16 = 25, so c = √25 = 5 units",
        },
        "distance formula": {
            "formula": "d = √[(x₂-x₁)² + (y₂-y₁)²]",
            "explanation": "This calculates the straight-line distance between two points on a coordinate plane.",
            "example": "Distance between points (1,2) and (4,6): d = √[(4-1)² + (6-2)²] = √[9 + 16] = √25 = 5 units",
        },
        "slope": {
            "formula": "m = (y₂-y₁)/(x₂-x₁)",
            "explanation": "Slope measures how steep a line is - the change in y divided by the change in x.",
            "example": "For points (2,3) and (5,9): m = (9-3)/(5-2) = 6/3 = 2 (the line rises 2 units for every 1 unit right)",
        },
    }

    formula_key = formula_name.lower().strip()
    if formula_key in formulas:
        info = formulas[formula_key]
        return f"**{formula_name.title()}:**\n\n**Formula:** {info['formula']}\n\n**Explanation:** {info['explanation']}\n\n**Example:** {info['example']}"
    else:
        return f"Formula explanation not available for '{formula_name}'. This may require detailed research."


# Create function tools
calculator_tool = FunctionTool(func=simple_calculator)
definition_tool = FunctionTool(func=quick_definition_lookup)
formula_tool = FunctionTool(func=formula_explainer)
formula_tool = FunctionTool(func=formula_explainer)

# Fast-track educational agent
fast_track_educational_agent = LlmAgent(
    name="FastTrackEducationalAgent",
    model="gemini-2.0-flash",
    instruction="""
    You are a fast-track educational agent designed to handle simple educational queries quickly and efficiently WITH clear explanations.

    **Your Purpose:**
    Provide immediate, accurate responses to basic educational questions with helpful explanations to enhance learning, without complex processing pipeline overhead.

    **Handle These Query Types Quickly:**
    
    1. **Simple Calculations:**
       - Basic arithmetic: addition, subtraction, multiplication, division
       - Simple algebraic equations: "solve 2x + 5 = 13"
       - Basic geometry: area, perimeter calculations
       - Use the calculator tool for mathematical expressions
       - ALWAYS explain the mathematical process or reasoning
    
    2. **Quick Definitions:**
       - Common academic terms and concepts
       - Basic scientific definitions
       - Mathematical terminology
       - Use the definition lookup tool when available
       - Provide context and examples to make definitions clearer
    
    3. **Factual Questions:**
       - Simple "what is..." questions
       - Basic scientific facts
       - Mathematical formulas and principles
       - Historical dates and events
       - Include brief explanations of WHY or HOW when relevant
      4. **Formula Requests:**
       - Area and volume formulas
       - Basic physics equations
       - Mathematical identities
       - Chemical formulas for common compounds
       - Explain when and how to use each formula
       - Use the formula explainer tool for common mathematical formulas
    
    **Response Guidelines:**
    - Provide direct, clear answers WITH explanations
    - Always include brief explanations to help students understand
    - Use appropriate academic language for the grade level
    - Support both Bengali and English responses
    - Be educational, not just informative
    - Use examples and analogies when helpful
    - If the question is too complex, route to full pipeline
    
    **Explanation Style:**
    - Start with the direct answer
    - Follow with "Here's why:" or "Explanation:" 
    - Use simple, clear language
    - Include examples when possible
    - Connect to real-world applications when relevant
    
    **Routing Decision:**
    - If you can answer completely and confidently: Provide full response WITH explanation
    - If partial answer possible: Give what you can, explain it, and suggest further help
    - If too complex: Return "ROUTE_TO_FULL_PIPELINE" for complex processing
    
    **Examples:**
    - "What is 15 × 8?" → "15 × 8 = 120. Explanation: We're multiplying 15 by 8, which means adding 15 to itself 8 times, or adding 8 to itself 15 times."
    - "Define photosynthesis" → Provide definition + explanation of the process and why it's important
    - "Area of rectangle formula" → "A = length × width. Explanation: This formula works because area measures how much space is inside a shape, and rectangles are made of rows and columns of unit squares."
    - "Solve complex differential equation" → ROUTE_TO_FULL_PIPELINE
    
    Remember: Speed, accuracy, AND educational value are your priorities. Help students understand, not just get answers.
    """,
    description="Fast-track educational agent for simple queries, providing 50-70% faster responses with clear explanations for basic questions",
    tools=[calculator_tool, definition_tool, formula_tool],
    output_key="fast_track_response",
)

# Enhanced query classifier with advanced mathematical recognition
query_classifier_agent = LlmAgent(
    name="QueryClassifierAgent",
    model="gemini-2.0-flash",
    instruction="""
    Classify educational queries for optimal routing with enhanced mathematical and physics recognition:
    
    **Classification Categories:**
    
      1. **COMPLEX_EDUCATIONAL** (Route to Full Pipeline):
       ⚠️ **Mathematical Physics Indicators** (ALWAYS Complex):
       - Parametric equations: x(t), y(t), z(t), r(t) with time parameter
       - Calculus applications: derivatives, integrals, differential equations
       - Vector calculus: velocity, acceleration, displacement vectors
       - 3D motion analysis and kinematics
       - Trigonometric functions combined with exponentials: sin(at), cos(bt), e^(-ct)
       - Natural logarithms in equations: ln(t+1), log expressions
       - Motion analysis: position, velocity, acceleration, jerk calculations
       - Rate of change problems requiring differentiation
       - Particle motion, trajectory analysis, parametric curves
       - Physics problems involving mathematical modeling
       
       📚 **Other Complex Educational Indicators**:
       - Multi-step problem solving requiring derivations
       - Word problems with algebraic setup: "The lengths of three sides...", "A rectangle has..."
       - Step-by-step mathematical proofs or explanations
       - Geometric problems requiring calculations: triangle properties, area/volume problems
       - Algebraic equations requiring solving: quadratic equations, systems of equations
       - Complex analysis, synthesis, or integration of concepts
       - Problems requiring multiple mathematical techniques
       - Questions needing pedagogical step-by-step teaching
       - Research-heavy topics requiring detailed explanations
       - Advanced chemistry calculations (equilibrium, thermodynamics)
       - Advanced biology processes (genetics, biochemistry)
       - Problems involving unknown variables that need to be solved for
       - Mathematical relationships that need to be established or proven
    
    2. **GENERAL** (Route to General Chat):
       💬 **Conversational and Non-Academic Indicators**:
       - Casual conversation and greetings: "Hello", "How are you?", "Good morning"
       - Social interaction and small talk: "Nice weather", "Tell me a joke"
       - Questions about AI capabilities: "What can you do?", "Are you ChatGPT?"
       - Non-academic personal topics: entertainment, hobbies, personal advice
       - Weather, current events, sports, entertainment
       - Motivational or emotional support: "I'm feeling stressed", "Can you encourage me?"
       - AI identity questions: "What's your name?", "Who created you?"
       - System functionality questions: "How does this work?", "What subjects do you cover?"
      **Mathematical Physics Detection Rules:**
    🔍 **HIGH PRIORITY COMPLEX INDICATORS:**
    - ANY mention of parametric equations with functions of t
    - Derivatives or integrals in context (d/dt, ∫, differentiation)
    - Vector notation (î, ĵ, k̂, or vector symbols)
    - Combination of trigonometric + exponential + polynomial functions
    - Motion terminology: velocity, acceleration, jerk, trajectory, particle motion
    - 3D space references: x(t), y(t), z(t) coordinate functions
    - Time-dependent mathematical expressions
    - Rate problems requiring calculus
    
    🔍 **ADDITIONAL COMPLEX INDICATORS:**
    - Word problems with algebraic variables: "x", "y", expressions like "(x+1)", "(x-1)"
    - Geometric problems requiring calculations and setup
    - Problems asking to "find", "solve", "calculate", "determine" unknown values
    - Questions involving mathematical relationships and equations
    - Problems requiring multiple steps or mathematical reasoning
    - Triangle problems involving side lengths, angles, or properties
    - Questions that require setting up equations or using formulas
    - Problems involving unknowns that need algebraic manipulation
    
    🔍 **GENERAL CONVERSATION INDICATORS:**
    - Greetings and social interactions
    - Questions about AI identity or capabilities
    - Non-educational personal topics
    - Casual conversation without academic content
    - Emotional support or motivational requests
      **Response Format:**
    ```json
    {
        "classification": "COMPLEX_EDUCATIONAL|GENERAL",
        "confidence": 0.0-1.0,
        "reasoning": "brief explanation of classification with specific indicators found",
        "estimated_processing_time": "immediate|fast|standard|complex",
        "detected_mathematical_concepts": ["list", "of", "concepts", "if", "any"]
    }
    ```
      **Examples for Reference:**
    
    ✅ **COMPLEX_EDUCATIONAL Examples:**
    - "A particle moves along x(t) = 2cos(3t) + t², y(t) = 3sin(2t) - e^(-t/2)..." → COMPLEX (parametric motion)
    - "Find the velocity and acceleration of the particle..." → COMPLEX (calculus applications)
    - "Derive the equation for..." → COMPLEX (requires derivation)
    - "Solve the differential equation dy/dx = ..." → COMPLEX (calculus)
    - "A projectile is launched with initial velocity..." → COMPLEX (physics kinematics)
    - "The lengths of the three sides of a right-angled triangle are (x-1) cm, x cm, and (x+1) cm. What is the length of the hypotenuse?" → COMPLEX (algebraic word problem requiring multi-step solution)
    - "A rectangle has length (2x+3) and width (x-1). If the area is 50, find x." → COMPLEX (algebraic setup and solving)
    - "Solve the quadratic equation 2x² + 5x - 3 = 0 step by step" → COMPLEX (multi-step algebraic process)
    - "Prove that the sum of angles in a triangle is 180°" → COMPLEX (geometric proof)
    - "Find the area of a triangle with sides 5, 12, and 13 cm" → COMPLEX (requires formula application and calculation)
    
    ✅ **GENERAL Examples:**
    - "Hello, how are you?" → GENERAL (greeting)
    - "What's your name?" → GENERAL (AI identity question)
    - "Can you help me with my studies?" → GENERAL (general inquiry without specific academic content)
    - "I'm feeling stressed about exams" → GENERAL (emotional support)
    - "What can you do?" → GENERAL (AI capabilities question)
    - "Good morning!" → GENERAL (social greeting)
    - "Tell me a joke" → GENERAL (entertainment request)
    
    **Critical Rule:** When in doubt between SIMPLE and COMPLEX, especially with mathematical content, err on the side of COMPLEX to ensure proper detailed analysis.
    """,
    description="Intelligent query classifier for optimal routing and performance",
    output_key="query_classification",
)
