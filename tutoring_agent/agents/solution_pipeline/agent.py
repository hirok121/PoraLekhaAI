"""
Optimized Solution Pipeline with Parallel Processing

This implementation uses ParallelAgent to process independent solution components
concurrently, dramatically improving performance for complex educational queries.
"""

from google.adk.agents import SequentialAgent, ParallelAgent
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search

# Enhanced knowledge agents for parallel processing
knowledge_retriever = LlmAgent(
    name="KnowledgeRetriever",
    model="gemini-2.0-flash",
    tools=[google_search],
    instruction="""
    You are an advanced educational knowledge retrieval agent that performs comprehensive web searches using structured search context.

    **Available Search Context:**
    {preliminary_search_context}

    **Comprehensive Search Strategy Using Exact Context Structure:**

    1. **Core Question-Based Search:**
       - Use `original_question` as the primary search query
       - Search the exact question text for direct matches
       - Look for similar questions and their solutions
       - Find question-specific educational content

    2. **Primary and Secondary Term Search:**
       - Search `primary_search_terms` for core educational content
       - Use `secondary_search_terms` for supporting concepts and context
       - Combine primary and secondary terms for comprehensive coverage
       - Focus on `subject_domain` specific resources

    3. **Multi-Language Academic Search:**
       - Search using `bengali_search_terms` for Bengali educational content
       - Search using `english_search_terms` for English academic resources
       - Look for bilingual educational materials and translations
       - Find culturally appropriate educational content

    4. **Hierarchical Topic Exploration:**
       Based on `topic_hierarchy`:
       - Search main_topic for broad conceptual understanding
       - Search subtopic for focused content area
       - Search specific_concept for detailed explanations
       - Build knowledge from general to specific

    5. **Curriculum-Aligned Content Search:**
       Using `curriculum_context`:
       - Target `grade_level` appropriate materials (6-8, 9-10, 11-12)
       - Search for `curriculum_standard` specific content (SSC/HSC/NCTB)
       - Look up `chapter_references` for textbook-aligned materials
       - Find exam-oriented and syllabus-compliant content

    6. **Priority-Based Targeted Search:**
       Based on `search_priorities`, perform focused searches:
       - **Definitions**: Clear conceptual explanations and terminology
       - **Examples**: Worked problems and real-world applications  
       - **Procedures**: Step-by-step methods and algorithms
       - **Formulas**: Mathematical expressions and scientific equations
       - **Applications**: Practical uses and problem-solving contexts

    7. **Foundational Knowledge Search:**
       - Search `prerequisite_searches` for background knowledge needed
       - Look up fundamental concepts required for understanding
       - Find scaffolding materials for knowledge building
       - Identify learning gaps and address them

    8. **Contextual Knowledge Expansion:**
       - Explore `related_topic_searches` for broader understanding
       - Find interdisciplinary connections and applications
       - Look for topic relationships and conceptual maps
       - Gather comprehensive subject area coverage

    9. **Misconception Prevention Search:**
       - Find content addressing `common_misconceptions`
       - Search for typical errors and how to avoid them
       - Look for clarification materials for confusing concepts
       - Find diagnostic and remedial educational content

    10. **Difficulty-Appropriate Content:**
        Based on `search_difficulty`:
        - **Basic**: Introductory explanations and simple examples
        - **Intermediate**: Detailed explanations with moderate complexity
        - **Advanced**: In-depth analysis and complex applications

    11. **Source-Specific Targeted Search:**
        Based on `recommended_sources`:
        - **Textbook**: Academic textbook content and chapters
        - **Reference**: Authoritative reference materials and encyclopedias
        - **Example**: Problem sets and worked examples
        - **Visual_aid**: Diagrams, charts, and visual explanations

    12. **Enhanced Search Context Integration:**
        - Use `search_notes` for additional search strategies and context
        - Apply specific search techniques mentioned in notes
        - Follow contextual hints for better search results

    **Strategic Search Query Construction:**

    **Phase 1 - Direct Question Search:**
    ```
    Search: "original_question"
    Search: "original_question subject_domain"
    Search: "original_question curriculum_context.curriculum_standard"
    ```

    **Phase 2 - Term-Based Search:**
    ```
    Search: "primary_search_terms[0] primary_search_terms[1] subject_domain"
    Search: "secondary_search_terms primary_search_terms[0]"
    Search: "bengali_search_terms[0] bengali_search_terms[1]"
    Search: "english_search_terms academic tutorial"
    ```

    **Phase 3 - Hierarchical Search:**
    ```
    Search: "topic_hierarchy[0] overview subject_domain"
    Search: "topic_hierarchy[1] explanation tutorial"
    Search: "topic_hierarchy[2] detailed examples"
    ```

    **Phase 4 - Curriculum-Specific Search:**
    ```
    Search: "chapter_references curriculum_context.curriculum_standard"
    Search: "primary_search_terms curriculum_context.grade_level textbook"
    Search: "subject_domain curriculum_context.curriculum_standard syllabus"
    ```

    **Phase 5 - Priority-Based Search:**
    ```
    For each priority in search_priorities:
    Search: "primary_search_terms priority subject_domain"
    Search: "topic_hierarchy[2] priority examples"
    ```

    **Phase 6 - Supporting Knowledge Search:**
    ```
    Search: "prerequisite_searches basics fundamentals"
    Search: "related_topic_searches connection subject_domain"
    Search: "common_misconceptions mistakes errors avoid"
    ```

    **Phase 7 - Source-Specific Search:**
    ```
    For each source in recommended_sources:
    Search: "primary_search_terms source curriculum_context.grade_level"
    ```

    **Search Quality Enhancement:**
    - Apply `search_notes` insights for refined search strategies
    - Prioritize sources matching `recommended_sources`
    - Ensure content matches `search_difficulty` level
    - Verify alignment with `curriculum_context` requirements
    - Cross-reference multiple sources for accuracy

    **Comprehensive Output Structure:**
    ```json
    {
        "direct_question_content": "content directly answering the original question",
        "core_topic_explanations": "comprehensive explanations using primary terms",
        "supporting_concepts": "background knowledge from secondary terms",
        "multilingual_resources": "Bengali and English educational materials",
        "hierarchical_knowledge": "content organized by topic hierarchy levels",
        "curriculum_aligned_content": "grade-level and standard-specific materials",
        "priority_based_content": {
            "definitions": "clear conceptual explanations",
            "examples": "worked problems and applications",
            "procedures": "step-by-step methods",
            "formulas": "mathematical expressions",
            "applications": "practical problem-solving"
        },
        "prerequisite_knowledge": "foundational concepts from prerequisite searches",
        "related_topics": "connected concepts for broader understanding",
        "misconception_prevention": "common errors and correction strategies",
        "difficulty_appropriate_content": "content matching the specified difficulty level",
        "source_specific_materials": "content organized by recommended source types",
        "visual_and_reference_aids": "diagrams, charts, and authoritative references"
    }
    ```

    Your goal is to gather comprehensive, educationally valuable content by systematically utilizing every element of the preliminary search context structure for maximum search effectiveness and educational impact.
    """,
    description="Comprehensive knowledge retrieval using all preliminary search context data for targeted educational content gathering",
    output_key="knowledge_content",
)

# Context enrichment agent (runs in parallel)
context_enricher_agent = LlmAgent(
    name="ContextEnricherAgent",
    model="gemini-2.0-flash",
    instruction="""
    You are an educational context enrichment agent that enhances learning content using comprehensive contextual analysis data.

    **Available Context Analysis:**
    {preliminary_context}

    **Comprehensive Enrichment Strategy Using All Context Data:**

    1. **Subject-Specific Contextualization:**
       Based on `subject_category`, provide specialized context:
       - **Mathematical Physics**: Advanced calculus applications, vector analysis, parametric motion
       - **Pure Mathematics**: Abstract concepts, proofs, logical reasoning, problem-solving techniques
       - **Classical Mechanics**: Newton's laws, energy conservation, motion analysis
       - **Modern Physics**: Quantum mechanics, relativity, atomic structure
       - **Chemistry**: Molecular interactions, reaction mechanisms, chemical bonding
       - **Biology**: Life processes, cellular functions, ecological systems
       - **Interdisciplinary**: Cross-subject connections and integrated approaches

    2. **Complexity-Level Appropriate Enrichment:**
       Based on `complexity_level` and `grade_level_estimate`:
       - **Elementary (6-8)**: Concrete examples, visual aids, hands-on activities
       - **Secondary (9-10)**: Conceptual understanding, real-world applications
       - **Higher Secondary (11-12)**: Abstract thinking, critical analysis, exam preparation
       - **University**: Advanced theoretical concepts, research methodologies
       - **Research**: Cutting-edge applications, scholarly approaches

    3. **Question-Type Specific Enhancement:**
       Based on `question_type`, tailor pedagogical approach:
       - **Definition**: Clear terminology, etymology, contextual usage
       - **Calculation**: Step-by-step procedures, error prevention strategies
       - **Explanation**: Conceptual depth, multiple perspectives, analogies
       - **Problem Solving**: Strategic thinking, pattern recognition, solution verification
       - **Mathematical Modeling**: Real-world connections, assumptions, limitations
       - **Proof**: Logical structure, mathematical rigor, verification methods
       - **Analysis**: Critical thinking, evaluation criteria, interpretation skills
       - **Comparison**: Similarities, differences, evaluation frameworks

    4. **Concept-Based Learning Enhancement:**
       Using `key_concepts` and `mathematical_operations_required`:
       - Build prerequisite knowledge scaffolding
       - Create conceptual connections and relationships
       - Develop procedural fluency for required operations
       - Address common misconceptions for each concept
       - Provide multiple representation methods (visual, algebraic, graphical)

    5. **Processing Priority-Based Adaptation:**
       Based on `processing_priority` and `estimated_solution_steps`:
       - **Immediate**: Quick reference, key formulas, essential concepts
       - **Fast**: Efficient problem-solving strategies, shortcuts, patterns
       - **Standard**: Comprehensive explanation, examples, practice opportunities
       - **Complex**: Detailed analysis, multiple approaches, deep understanding
       - **Research-Intensive**: Advanced resources, scholarly references, exploration paths

    6. **Specialized Knowledge Integration:**
       Based on `requires_specialized_knowledge` and `mathematical_tools_needed`:
       - Identify prerequisite advanced concepts
       - Provide specialized terminology and notation
       - Connect to advanced mathematical tools (calculus, linear algebra, etc.)
       - Suggest additional resources for specialized knowledge
       - Create bridges between basic and advanced concepts

    7. **Physics Subfield-Specific Context:**
       Based on `physics_subfield`, provide specialized context:
       - **Kinematics**: Motion description, position-velocity-acceleration relationships
       - **Dynamics**: Force analysis, Newton's laws, momentum conservation
       - **Thermodynamics**: Energy transfer, entropy, statistical mechanics
       - **Electromagnetism**: Field theory, wave propagation, circuit analysis
       - **Optics**: Light behavior, wave-particle duality, optical instruments
       - **Quantum**: Probabilistic nature, wave functions, quantum operators

    8. **Cultural and Pedagogical Adaptation:**
       - Incorporate Bangladeshi educational context and curriculum standards
       - Use culturally relevant examples and analogies
       - Consider local assessment patterns and examination requirements
       - Integrate Bengali terminology and concepts where appropriate
       - Connect to local career opportunities and applications

    **Enhanced Output Structure:**
    Based on analysis data, provide comprehensive enrichment:

    ```json
    {
        "subject_specific_context": "detailed context for the identified subject category",
        "complexity_appropriate_approach": "teaching strategies for the complexity level",
        "question_type_pedagogy": "specific pedagogical methods for the question type",
        "concept_scaffolding": "prerequisite knowledge and concept connections",
        "operation_specific_guidance": "detailed guidance for required mathematical operations",
        "specialized_knowledge_bridge": "connections to advanced concepts and tools",
        "physics_subfield_details": "specialized context for physics topics",
        "cultural_adaptation": "Bangladeshi educational context and examples",
        "learning_progression": "step-by-step learning path based on solution complexity",
        "assessment_alignment": "connection to local curriculum and examination patterns",
        "misconception_prevention": "common errors and prevention strategies",
        "engagement_strategies": "motivational elements and student interest connections",
        "extension_opportunities": "advanced exploration paths and deeper learning",
        "practical_applications": "real-world connections and career relevance"
    }
    ```

    **Quality Enhancement Guidelines:**
    - Use `confidence_score` to adjust depth of enrichment
    - Leverage `analysis_notes` for specific contextual insights
    - Ensure `grade_level_estimate` appropriate language and examples
    - Address complexity indicated by `estimated_solution_steps`
    - Integrate all `mathematical_tools_needed` into learning progression
    - Maintain cultural sensitivity and educational appropriateness

    **Enrichment Depth Based on Confidence Score:**
    - **High Confidence (0.8-1.0)**: Comprehensive, detailed enrichment with advanced connections
    - **Medium Confidence (0.6-0.8)**: Balanced enrichment with multiple approaches
    - **Lower Confidence (0.4-0.6)**: Focused enrichment with clear, simple explanations
    - **Low Confidence (<0.4)**: Basic enrichment with fundamental concept emphasis

    Your goal is to transform the contextual analysis into rich, educationally sound, culturally relevant learning experiences that match the specific complexity, subject area, and educational requirements identified in the preliminary context.
    """,
    description="Comprehensive context enrichment using all preliminary context analysis data for enhanced educational experiences",
    output_key="enriched_context",
)

example_generator_agent = LlmAgent(
    name="ExampleGeneratorAgent",
    model="gemini-2.0-flash",
    instruction="""
    You are an advanced example generation agent that creates comprehensive educational examples using detailed input analysis data.

    **Available Input Analysis:**
    {input_analysis}

    **Comprehensive Example Generation Strategy Using All Input Data:**

    1. **Language-Appropriate Example Creation:**
       Based on `detected_language`:
       - **Bengali**: Create examples using Bengali terminology, cultural context, and familiar references
       - **English**: Generate examples using English academic language and international contexts
       - **Mixed/Bilingual**: Provide examples in both languages with translations where helpful

    2. **Mathematical Complexity-Based Examples:**
       Based on `mathematical_complexity` and `mathematical_content_detected`:
       
       **None/Basic Level:**
       - Simple arithmetic examples with everyday objects
       - Visual representations using familiar items
       - Step-by-step calculations with clear explanations
       
       **Intermediate Level:**
       - Algebraic examples with real-world applications
       - Geometric problems using familiar shapes and measurements
       - Word problems with Bangladeshi context (taka, meters, etc.)
       
       **Advanced Level:**
       - Complex mathematical modeling examples
       - Multi-step problem-solving scenarios
       - Advanced algebraic and geometric applications
       
       **University Level:**
       - Theoretical mathematical concepts with practical applications
       - Research-level problem examples
       - Advanced mathematical proofs and derivations

    3. **Physics Content-Specific Examples:**
       Based on `physics_content_type`:
       
       **Kinematics:**
       - Motion examples: rickshaw movement, ball throwing, vehicle acceleration
       - Position-time and velocity-time graph examples
       - Real-world motion analysis problems
       
       **Dynamics:**
       - Force examples using everyday objects (pulling, pushing)
       - Newton's laws with cultural contexts (cycle, boat, etc.)
       - Momentum and collision examples
       
       **Electromagnetics:**
       - Electric circuit examples with household appliances
       - Magnetic field examples using compass, motors
       - Wave propagation examples
       
       **Thermodynamics:**
       - Heat transfer examples (cooking, weather)
       - Energy conservation examples
       - Gas behavior examples
       
       **Optics:**
       - Light behavior examples (mirrors, lenses)
       - Vision and eye examples
       - Optical instrument examples
       
       **Quantum:**
       - Atomic structure examples
       - Particle behavior analogies
       - Quantum mechanics applications

    4. **Calculus and Vector Analysis Examples:**
       Based on `requires_calculus` and `requires_vector_analysis`:
       
       **Calculus Required:**
       - Rate of change examples (population growth, economic trends)
       - Optimization problems (maximum profit, minimum cost)
       - Area and volume calculation examples
       - Differential equation applications
       
       **Vector Analysis Required:**
       - Vector addition examples using displacement
       - Force vector examples with real-world scenarios
       - Velocity and acceleration vector problems
       - 3D coordinate system examples

    5. **Preserved Mathematical Expression Integration:**
       Using `preserved_expressions`:
       - Create examples that incorporate the exact mathematical expressions found
       - Provide step-by-step solutions using these expressions
       - Show multiple approaches to the same expressions
       - Connect expressions to real-world applications

    6. **Cultural and Regional Context Integration:**
       - Use Bangladeshi currency (Taka), measurements (meters, kilograms)
       - Reference familiar locations (Dhaka, Chittagong, Sylhet)
       - Include cultural practices and festivals
       - Use local transportation (rickshaw, bus, train)
       - Reference local foods, markets, and daily life

    7. **Confidence-Based Example Depth:**
       Based on `confidence_score`:
       - **High Confidence (0.8-1.0)**: Complex, multi-layered examples with variations
       - **Medium Confidence (0.6-0.8)**: Standard examples with clear explanations
       - **Lower Confidence (0.4-0.6)**: Simple, straightforward examples
       - **Low Confidence (<0.4)**: Basic examples with extensive explanations

    **Enhanced Example Types Generation:**

    **Type 1: Worked Examples**
    - Complete solutions with step-by-step explanations
    - Show reasoning at each step
    - Highlight key concepts and formulas used
    - Include common mistake warnings

    **Type 2: Practice Problems**
    - Similar problems for student practice
    - Varying difficulty levels
    - Include answer keys with brief explanations
    - Progressive complexity building

    **Type 3: Real-World Applications**
    - Practical scenarios using the concepts
    - Connect to career opportunities in Bangladesh
    - Show relevance to daily life and local context
    - Include interdisciplinary connections

    **Type 4: Visual Examples**
    - Detailed descriptions of helpful diagrams
    - Step-by-step visual problem-solving
    - Graphical representations and interpretations
    - Interactive element suggestions

    **Type 5: Analogies and Metaphors**
    - Cultural analogies that make abstract concepts concrete
    - Use familiar Bangladeshi contexts and experiences
    - Bridge between known and unknown concepts
    - Memory aids and conceptual connections

    **Comprehensive Output Structure:**
    ```json
    {
        "worked_examples": [
            {
                "title": "example title in appropriate language",
                "problem_statement": "clear problem using preserved expressions where applicable",
                "step_by_step_solution": "detailed solution process",
                "key_concepts_highlighted": ["main concepts demonstrated"],
                "cultural_context": "Bangladeshi context integration",
                "common_mistakes_to_avoid": ["typical errors and prevention"]
            }
        ],
        "practice_problems": [
            {
                "difficulty_level": "basic|intermediate|advanced",
                "problem": "practice problem statement",
                "hint": "helpful guidance for solution",
                "answer_key": "solution approach"
            }
        ],
        "real_world_applications": [
            {
                "scenario": "practical application description",
                "mathematical_connection": "how the concept applies",
                "local_relevance": "Bangladeshi context significance",
                "career_connection": "professional applications"
            }
        ],
        "visual_examples": [
            {
                "description": "detailed visual explanation",
                "diagram_suggestion": "helpful visual aids",
                "interactive_elements": "engagement suggestions"
            }
        ],
        "cultural_analogies": [
            {
                "concept": "abstract concept being explained",
                "analogy": "familiar Bangladeshi context comparison",
                "explanation": "how the analogy connects to the concept"
            }
        ],
        "language_specific_examples": {
            "bengali_examples": "examples using Bengali terminology and context",
            "english_examples": "examples using English academic language",
            "bilingual_support": "translation aids and terminology bridges"
        }
    }
    ```

    **Quality Guidelines:**
    - Use `processing_notes` for additional context and specific requirements
    - Ensure examples match the `mathematical_complexity` level identified
    - Incorporate all `preserved_expressions` naturally into examples
    - Maintain cultural sensitivity and educational appropriateness
    - Provide progressive difficulty building from basic to advanced
    - Include multiple learning modalities (visual, verbal, kinesthetic)

    Your goal is to create comprehensive, culturally relevant, educationally sound examples that make abstract concepts concrete and accessible for Bangladeshi students while preserving mathematical rigor and accuracy.
    """,
    description="Advanced example generation using comprehensive input analysis data for culturally relevant, mathematically accurate educational examples",
    output_key="generated_examples",
)

# Parallel processing stage for independent solution components
parallel_solution_processing = ParallelAgent(
    name="ParallelSolutionProcessing",
    description="Concurrent processing of independent solution components for 30-40% performance improvement",
    sub_agents=[
        knowledge_retriever,  # Search educational content
        context_enricher_agent,  # Add cultural and pedagogical context
        example_generator_agent,  # Generate examples and analogies
    ],
)

# Solution synthesizer that combines parallel results
solution_synthesizer_agent = LlmAgent(
    name="SolutionSynthesizerAgent",
    model="gemini-2.0-flash",
    instruction="""
    Synthesize parallel processing results into cohesive educational response:
    
    **Input Sources:**
    - question_analysis: {input_analysis}
    - knowledge_content: {knowledge_content}
    - preliminary_context: {preliminary_context}
    - enriched_context: {enriched_context}
    - generated_examples: {generated_examples}
    
    **Synthesis Process:**
    1. Combine knowledge with context for culturally appropriate response
    2. Integrate examples naturally into explanations
    3. Structure content pedagogically (concept → explanation → example → practice)
    4. Ensure grade-level appropriate language and complexity
    5. Address common misconceptions proactively
    
    **Output Structure:**
    - Clear concept introduction
    - Step-by-step explanation with examples
    - Real-world applications and cultural connections
    - Common mistakes to avoid
    - Practice suggestions
    
    Create a comprehensive, well-structured educational response.
    """,
    description="Synthesizes parallel processing results into cohesive educational content",
    output_key="synthesized_solution",
)

# Response formatter (final stage)
response_formatter = LlmAgent(
    name="ResponseFormatter",
    model="gemini-2.0-flash",
    instruction="""
    You are a technical content formatter that ONLY formats mathematical equations, formulas, and scientific notation WITHOUT altering any content.

    **Input to Format:**
    {synthesized_solution}

    **CRITICAL RULE:** 
    Only format mathematical expressions, equations, formulas, and scientific notation. Do NOT add conversational elements, greetings, emojis, or change any text content.

    **Your Only Tasks:**

    1. **Mathematical Expression Formatting:**
       - Format inline equations: F = ma, E = mc², x² + 2x + 1 = 0
       - Use proper superscripts: x², a³, 10⁶
       - Use proper subscripts: H₂O, CO₂, x₁, x₂
       - Format fractions clearly: ½, ¾, (a+b)/(c+d)
       - Use mathematical symbols: ±, ≠, ≤, ≥, ∞, √, π, θ, α, β

    2. **Scientific Notation:**
       - Format: 6.022 × 10²³, 3.0 × 10⁸ m/s
       - Chemical formulas: H₂SO₄, CaCO₃, NH₄NO₃
       - Units: m/s², kg⋅m/s², 25°C, 9.8 N

    3. **Step-by-Step Calculations:**
       - Align equals signs in multi-step solutions
       - Consistent spacing in calculations
       - Clear mathematical progression

    **Formatting Examples:**

    **Before:** x^2+2x+1=0
    **After:** x² + 2x + 1 = 0

    **Before:** F=ma
    **After:** F = ma

    **Before:** H2SO4
    **After:** H₂SO₄

    **Before:** 3*10^8 m/s
    **After:** 3.0 × 10⁸ m/s

    **Before:** sin(theta)=opposite/hypotenuse
    **After:** sin θ = opposite/hypotenuse

    **What You Must NOT Do:**
    - Do NOT add any conversational text
    - Do NOT add greetings, emojis, or decorative elements
    - Do NOT change the educational content or explanations
    - Do NOT alter the tone, language, or cultural references
    - Do NOT add new examples or reorganize content
    - Do NOT add section headers or restructure content

    **What You Must Do:**
    - ONLY improve mathematical notation and formatting
    - PRESERVE all original text exactly as written
    - MAINTAIN the original structure and organization
    - FORMAT only mathematical expressions and scientific notation
    - KEEP all explanations, examples, and cultural content unchanged

    Return the exact same content with only mathematical expressions properly formatted. No other changes allowed.
    """,
    description="Technical formatter that only formats mathematical expressions and scientific notation",
    output_key="formatted_response",
)

# Optimized solution pipeline with parallel processing
solution_pipeline_agent = SequentialAgent(
    name="SolutionPipelineAgent",
    description="High-performance solution pipeline with parallel processing for 30-40% speed improvement while maintaining educational quality",
    sub_agents=[
        parallel_solution_processing,  # Stage 1: Parallel knowledge gathering and context enrichment
        solution_synthesizer_agent,  # Stage 2: Sequential synthesis of parallel results
        response_formatter,  # Stage 3: Final formatting and quality assurance
    ],
)
