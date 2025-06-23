# 🧠 AI-Based Multi-Agent Tutoring System (Text-Only, Agent-Centric Focus)

A comprehensive multi-agent AI tutoring system for Bangladeshi students (grades 6-12) built with Google's Agent Development Kit (ADK). This system focuses on **text-based interactions** and **intelligent agent orchestration**, providing science and math tutoring through Bangla and English text input/output.

## ✅ Design Goals

- ✅ Help students understand science and math concepts from NCTB-aligned curriculum
- ✅ Accept **text-based questions** in Bangla or English
- ✅ Return well-structured, student-friendly, accurate answers
- ✅ Use **multiple specialized agents**, working in **sequence and parallel**
- ✅ Format responses clearly, especially **math (LaTeX)** and **Bangla grammar**
- ✅ Be **modular and extendable**, future-proof for voice, image, PDF input

## 🎯 Core Features

### Agent-Centric Architecture

- **Sequential Agent Pipeline**: Step-by-step processing for consistent results
- **Google Search Integration**: Uses built-in ADK Google search for real-time information
- **No Database Required**: Session-based state management
- **Modular Agent Design**: Each agent has a specific responsibility
- **Agent Orchestration**: Intelligent coordination between specialized agents

### Educational Capabilities

- **Bilingual Support**: Bengali and English language support
- **Subject Coverage**: Math, Physics, Chemistry, Biology
- **Grade Level Adaptation**: Appropriate for grades 6-12
- **Cultural Sensitivity**: Designed for Bangladeshi educational context

### Text Processing Features

- **Language Detection**: Automatic detection of Bengali or English input
- **Text Normalization**: Clean and standardize input text
- **Mathematical Expression Recognition**: LaTeX formatting and equation parsing
- **Context-Aware Processing**: Maintains conversation history and context
- **Quality Assessment**: Confidence scoring for all processing steps

## 🧩 Core Agent Workflow

The system uses a **smart routing multi-agent architecture** with specialized agents working in sequence:

### 🔀 Smart Conversation Routing

**NEW: Efficient conversation handling with intelligent routing**

#### 1. **Conversation Router Agent**

**Description**: Determines if input is general conversation or educational content

- Classifies input as GENERAL (casual chat) or EDUCATIONAL (academic questions)
- Handles general conversation directly with friendly responses
- Routes educational content to specialized tutoring agents
- Supports bilingual Bengali/English input
- Provides immediate responses for casual interactions

#### 2. **Question Clarification Agent**

**Description**: Helps clarify unclear or incomplete educational questions

- Identifies vague or ambiguous questions
- Guides students to provide more specific information
- Asks targeted clarification questions with examples
- Ensures questions have enough context for meaningful help
- Prevents processing of unclear educational requests

### 🎓 Educational Processing Pipeline

**(Activated only for clear educational questions)**

#### 3. **Language Routing Agent**

**Description**: Detects input language and routes text to appropriate processing pipelines

- Detects Bengali vs English input
- Performs text normalization and tokenization
- Ensures output language matches input language
- Routes to language-specific processing chains

#### 4. **Question Analysis Agent**

**Description**: Analyzes and categorizes student questions for appropriate handling

- Determines subject area (Math, Physics, Chemistry, Biology)
- Identifies grade level (6-8, 9-10, 11-12)
- Classifies question type (Problem-solving, Conceptual, Definition)
- Extracts key concepts and mathematical expressions
- Assesses difficulty level and confidence

#### 5. **Knowledge Retrieval Agent**

**Description**: Searches for relevant educational content using Google Search integration

- Performs targeted searches for educational content
- Finds grade-appropriate materials and examples
- Discovers visual aids, diagrams, and explanations
- Retrieves curriculum-aligned information
- Synthesizes search results into key information

#### 6. **Solution Generation Agent**

**Description**: Creates step-by-step solutions and pedagogically sound explanations

- Generates step-by-step problem solutions
- Provides conceptual explanations with examples
- Uses Socratic questioning techniques
- Integrates cultural context and real-world applications
- Follows educational best practices for the identified grade level

#### 7. **Response Formatting Agent**

**Description**: Formats final responses with proper language, math, and educational structure

- Ensures correct Bengali/English grammar and formatting
- Renders mathematical expressions clearly
- Organizes content in student-friendly structure
- Adds visual elements and emphasis
- Performs final quality assurance

## 🏗️ Agent Architecture

The system uses a **smart routing sequential agent pipeline** with intelligent orchestration:

```
Root Tutoring Agent (Sequential)
│
├── 1. Conversation Router Agent
│   ├── Input Classification (General vs Educational)
│   ├── Quick Response Generation (for General)
│   ├── Educational Routing Decision
│
├── 2. Question Clarification Agent
│   ├── Clarity Assessment
│   ├── Clarification Question Generation
│   ├── Continuation Decision
│
├── 3. Language Routing Agent
│   ├── Language Detection (Bengali/English)
│   ├── Text Normalization & Tokenization
│   ├── Input Validation & Enhancement
│   └── Language-Specific Processing Pipeline Setup
│
├── 4. Question Analysis Agent
│   ├── Subject Classification (math, physics, chemistry, biology)
│   ├── Grade Level Detection (6-8, 9-10, 11-12)
│   ├── Question Type Analysis (problem_solving, conceptual, homework_help)
│   ├── Mathematical Expression Extraction
│   └── Difficulty Assessment & Confidence Scoring
│
├── 5. Knowledge Retrieval Agent
│   ├── Google Search Integration
│   ├── Educational Content Discovery
│   ├── Grade-Appropriate Resource Finding
│   ├── Example and Explanation Retrieval
│   └── Information Synthesis & Relevance Scoring
│
├── 6. Solution Generation Agent
│   ├── Step-by-Step Problem Solving
│   ├── Conceptual Explanations with Examples
│   ├── Socratic Questioning Implementation
│   ├── Cultural Context Integration
│   └── Pedagogical Best Practices Application
│
└── 7. Response Formatting Agent
    ├── Bengali/English Text Formatting
    ├── Mathematical Expression Rendering (LaTeX)
    ├── Educational Structure Organization
    ├── Visual Element Integration
    └── Final Quality Assurance & Validation
```

### 🔄 Processing Flow

**General Conversation Flow:**

- Input → Conversation Router → Quick Response (Steps 1-2 only)
- Efficient, immediate responses for casual chat

**Educational Question Flow:**

- Input → Conversation Router → Question Clarification → Full Pipeline (All 7 steps)
- Complete educational processing for academic questions

**Unclear Question Flow:**

- Input → Conversation Router → Question Clarification → Clarification Response
- Helps students refine their questions before processing

### Agent Orchestration

- **Sequential Processing**: Each agent builds on the previous agent's output
- **Session State**: Information is passed between agents in the same session
- **Error Handling**: Graceful degradation when agents encounter issues
- **Confidence Tracking**: Each agent provides confidence scores for its processing
- **Loop Detection**: Prevents infinite loops in agent processing chains

## 📁 Project Structure

Clean modular structure focused on agent architecture:

```
poralekhAI/
├── tutoring_agent/
│   ├── __init__.py
│   ├── agent.py                    # Main sequential agent orchestrator
│   │
│   ├── agents/                     # Core agent modules
│   │   ├── __init__.py
│   │   ├── conversation_router/    # NEW: General vs educational routing
│   │   │   ├── __init__.py
│   │   │   └── agent.py
│   │   ├── question_clarification/ # NEW: Question clarification and improvement
│   │   │   ├── __init__.py
│   │   │   └── agent.py
│   │   ├── language_router/        # Language detection and routing
│   │   │   ├── __init__.py
│   │   │   └── agent.py
│   │   ├── question_analyzer/      # Question analysis and categorization
│   │   │   ├── __init__.py
│   │   │   └── agent.py
│   │   ├── knowledge_retriever/    # Google search and content discovery
│   │   │   ├── __init__.py
│   │   │   └── agent.py
│   │   ├── solution_generator/     # Solution and explanation generation
│   │   │   ├── __init__.py
│   │   │   └── agent.py
│   │   └── response_formatter/     # Final response formatting
│   │       ├── __init__.py
│   │       └── agent.py
│   │
│   └── tools/                      # Utility functions and text processing tools
│       ├── __init__.py             # Educational utility functions
│       └── text_processing.py      # Language detection, math parsing, formatting
│
├── requirements.txt                # Core dependencies for ADK and text processing
├── enhanced_demo.py               # NEW: Smart routing demonstration
├── simple_demo.py                 # Basic architecture demonstration
├── text_processing_demo.py        # Text processing capabilities demo
└── README.md
```

## 🚀 Installation

### Core Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set up environment variables:

```bash
# Create .env file or set environment variable
GOOGLE_API_KEY=your_google_api_key_here
```

### Demo Scripts

Run the enhanced demo with conversation routing:

```bash
python enhanced_demo.py
```

Run the text processing capabilities demo:

```bash
python text_processing_demo.py
```

Or run the basic agent architecture demo (requires Google ADK setup):

```bash
python simple_demo.py
```

### 🎯 Key Benefits of New Architecture

**🔄 Smart Routing System:**

- General conversation handled instantly without complex processing
- Educational questions get full expert analysis
- Unclear questions receive helpful clarification
- Efficient resource usage - AI agents only activated when needed

**💬 Enhanced User Experience:**

- Friendly responses to casual greetings and chat
- Helpful guidance for unclear questions
- Seamless bilingual support (Bengali/English)
- Appropriate response types for different input types

**⚡ Performance Improvements:**

- Faster responses for general conversation
- Reduced API calls for non-educational content
- More efficient agent pipeline activation
- Better resource management

## 🔧 Technologies & Stack (Agent-Focused)

| Component           | Tools / Models Suggested                       |
| ------------------- | ---------------------------------------------- |
| Agent Orchestration | Google ADK (Agent Development Kit)             |
| LLM Engine          | Gemini 2.0 Flash (via ADK)                     |
| Language Detection  | `langdetect`, `indic-nlp-library`              |
| Bengali NLP         | `bnlp-toolkit`, `indic-nlp-library`            |
| Math Processing     | `sympy`, mathematical expression parsing       |
| Text Processing     | Custom tools for educational content analysis  |
| Search Integration  | Google Search (built into ADK)                 |
| Session Management  | ADK Session-based state (no database required) |

## 🧠 Agent Design Philosophy

### Individual Agent Responsibilities

Each agent in the system has a **single, well-defined responsibility**:

1. **Conversation Router Agent**:

   - **Single Purpose**: Classify input as general conversation or educational content
   - **Input**: Raw student input (any language)
   - **Output**: Route decision with immediate response for general chat
   - **Tools**: Classification algorithms, friendly response generation

2. **Question Clarification Agent**:

   - **Single Purpose**: Identify and clarify unclear educational questions
   - **Input**: Educational questions (routed from step 1)
   - **Output**: Clarification prompts or clear question confirmation
   - **Tools**: Question analysis, clarification question generation

3. **Language Router Agent**:

   - **Single Purpose**: Language detection and text routing
   - **Input**: Clear educational questions
   - **Output**: Normalized text with language metadata
   - **Tools**: Language detection algorithms, text normalization

4. **Question Analyzer Agent**:

   - **Single Purpose**: Question categorization and analysis
   - **Input**: Normalized text
   - **Output**: Structured analysis (subject, grade, type, concepts)
   - **Tools**: Educational classification algorithms

5. **Knowledge Retriever Agent**:

   - **Single Purpose**: Educational content discovery
   - **Input**: Question analysis results
   - **Output**: Relevant educational content and examples
   - **Tools**: Google Search integration

6. **Solution Generator Agent**:

   - **Single Purpose**: Educational response generation
   - **Input**: Question analysis + Retrieved knowledge
   - **Output**: Pedagogically sound explanation/solution
   - **Tools**: Educational best practices, cultural context

7. **Response Formatter Agent**:
   - **Single Purpose**: Final response formatting and quality assurance
   - **Input**: Generated solution content
   - **Output**: Polished, student-friendly response
   - **Tools**: Language formatting, mathematical rendering

### Agent Coordination

- **Sequential Processing**: Agents work in a defined order
- **State Passing**: Each agent enriches the session state
- **Error Handling**: Graceful degradation when agents encounter issues
- **Quality Gates**: Each agent validates its output before passing to the next

## 💻 Usage

### Basic Text Input

```python
from tutoring_agent import root_tutoring_agent
from google.adk.sessions import Session

# Create a session
session = Session(
    id="tutoring_session",
    app_name="AI_Tutor",
    user_id="student_123"
)

# Ask a question in Bengali
response = session.run(
    agent=root_tutoring_agent,
    input_data="২x + ৫ = ১৫ সমীকরণটি সমাধান করো।"  # Solve 2x + 5 = 15
)

print(response)

# Ask a question in English
response = session.run(
    agent=root_tutoring_agent,
    input_data="Explain photosynthesis in simple terms"
)

print(response)
```

### Example Questions

The system is designed to handle:

- **Bengali Math**: `"২x + ৫ = ১৩ সমীকরণটি সমাধান করুন।"`
- **English Physics**: `"A ball is thrown upward with initial velocity 20 m/s. How high will it go?"`
- **Conceptual Biology**: `"Explain photosynthesis in simple terms"`
- **General Help**: `"Help me understand quadratic equations"`
- **Mixed Language**: `"Solve this equation: 3x + 7 = 22 এবং উত্তর ব্যাখ্যা করো"`

## 🔧 Technical Implementation

### Agent Configuration

Each agent is configured using Google ADK with:

- **Model**: Gemini 2.0 Flash (optimized for educational content)
- **Instructions**: Subject and role-specific guidance
- **Tools**: Google Search integration where needed
- **State Management**: Session-based information passing

### Example Agent Definition

```python
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search

knowledge_retriever_agent = LlmAgent(
    name="KnowledgeRetrieverAgent",
    model="gemini-2.0-flash",
    tools=[google_search],
    instruction="Search for relevant educational content...",
    description="Searches for and retrieves educational content using Google Search"
)
```

### Key Technical Features

- **Sequential Processing**: Each agent builds on the previous agent's output
- **Session State**: Information is passed between agents in the same session
- **No External Database**: Everything is handled in memory with ADK sessions
- **Built-in Tools**: Uses ADK's built-in Google search functionality
- **Error Resilience**: Graceful handling of processing failures
- **Confidence Tracking**: Each agent provides confidence scores

## 📚 Educational Approach

The system follows proven educational principles:

- **Scaffolding**: Building knowledge step by step from known to unknown
- **Constructivism**: Helping students construct their own understanding
- **Socratic Questioning**: Guiding students to discover answers through strategic questions
- **Cultural Relevance**: Using examples familiar to Bangladeshi students
- **Grade-Appropriate Content**: Matching complexity to student developmental level
- **Bilingual Support**: Seamless Bengali-English language handling
- **Active Learning**: Engaging students in the learning process

## 🎓 Demonstration

Run the text processing demo to see the analysis capabilities:

```bash
python text_processing_demo.py
```

This will demonstrate:

- Language detection and text normalization
- Mathematical expression extraction
- Subject classification and grade level assessment
- Question completeness validation
- Educational context analysis
- Agent workflow overview

Run the full system demo (requires Google ADK setup):

```bash
python simple_demo.py
```

## 🔍 How It Works

The system processes student questions through five specialized agents:

1. **Language Analysis**: The Language Router Agent analyzes the incoming question to understand:

   - What language it's written in (Bengali, English, or mixed)
   - Text normalization and cleaning requirements
   - Routing to appropriate processing pipeline

2. **Question Understanding**: The Question Analyzer Agent categorizes the question by:

   - Academic subject (Math, Physics, Chemistry, Biology)
   - Grade level complexity (6-8, 9-10, 11-12)
   - Question type (problem-solving, conceptual, homework help)
   - Key concepts and mathematical expressions involved

3. **Knowledge Discovery**: The Knowledge Retriever Agent searches for relevant information:

   - Educational content appropriate for the grade level
   - Examples and explanations from reliable sources
   - Cultural context and real-world applications
   - Visual aids and supplementary materials

4. **Solution Creation**: The Solution Generator Agent creates the educational response:

   - Step-by-step solutions for mathematical problems
   - Clear conceptual explanations with examples
   - Culturally appropriate analogies and references
   - Pedagogically sound teaching approaches

5. **Response Polishing**: The Response Formatter Agent formats everything properly:
   - Correct Bengali/English text formatting
   - Mathematical expression rendering
   - Educational structure and organization
   - Final quality assurance and validation

## 🌟 Benefits of This Architecture

- **Agent Specialization**: Each agent focuses on what it does best
- **Modular Design**: Easy to understand, maintain, and extend
- **No Database Complexity**: Everything works with session-based state
- **Real-time Information**: Google search provides up-to-date content
- **Educational Focus**: Designed specifically for learning outcomes
- **Cultural Adaptation**: Made for Bangladeshi educational context
- **Scalable Design**: Can be easily extended with more agents or capabilities

## 📋 Requirements

- Python 3.8+
- Google ADK
- Google API key
- Internet connection for search functionality

## 🚧 Future Enhancements

### Text-Only Focus (Current) ✅

- ✅ Multi-agent architecture with Google ADK
- ✅ Advanced text processing and language detection
- ✅ Bengali and English bilingual support
- ✅ Mathematical expression recognition and formatting
- ✅ Educational content analysis and categorization
- ✅ Cultural context integration for Bangladeshi students

### Planned Enhancements 🚀

- **Advanced Agent Features**:
  - Clarification loop agents for incomplete questions
  - Parallel agent processing for complex problems
  - Memory agents for session context and learning history
- **Educational Improvements**:
  - Progress tracking and learning analytics
  - Personalized learning paths based on student performance
  - Integration with NCTB curriculum standards
  - Advanced mathematical visualization and rendering
- **Technical Enhancements**:
  - Offline processing capabilities
  - Real-time collaboration features
  - Mobile app development
  - Integration with local educational systems
- **Future Input Modalities** (when ready):
  - Voice input processing (speech-to-text)
  - Image input processing (OCR for textbooks)
  - PDF document processing (educational materials)

## 🛠️ Development Setup

### For Contributors

1. **Clone and Install**:

```bash
git clone <repository-url>
cd poralekhAI
pip install -r requirements.txt
```

2. **Environment Configuration**:

```bash
# Create .env file with required API keys
GOOGLE_API_KEY=your_google_api_key_here
```

3. **Test Installation**:

```bash
python text_processing_demo.py  # Text processing capabilities demo
python simple_demo.py           # Full agent system (requires ADK setup)
```

### Adding New Agents

Follow the established ADK patterns:

```python
# New agent template
from google.adk.agents.llm_agent import LlmAgent

my_new_agent = LlmAgent(
    name="MyNewAgent",
    model="gemini-2.0-flash",
    description="Clear description of agent's purpose and responsibility",
    instruction="Detailed instructions for the agent behavior...",
    tools=[relevant_tools]  # Optional ADK tools
)
```

### Best Practices for Agent Development

- **Single Responsibility**: Each agent should have one clear purpose
- **Educational Focus**: Always prioritize learning outcomes
- **Cultural Sensitivity**: Use appropriate examples and context for Bangladeshi students
- **Bilingual Support**: Handle Bengali and English seamlessly
- **Error Handling**: Provide graceful degradation for processing failures
- **Confidence Scoring**: Include confidence metrics for all agent outputs
- **Documentation**: Comment code thoroughly with educational clarity

## 🤝 Contributing

This project follows Google ADK best practices and agent architecture patterns. To contribute:

1. **Follow Agent Architecture Principles**:

   - Each agent should have a single, well-defined responsibility
   - Use clear, descriptive instructions for agent behavior
   - Implement proper error handling and confidence scoring
   - Maintain educational focus and cultural sensitivity

2. **Code Organization**:

   - Add new agents to the `tutoring_agent/agents/` directory
   - Follow the established directory structure pattern
   - Update the main sequential agent in `agent.py` as needed
   - Include comprehensive docstrings and comments

3. **Testing and Quality**:

   - Test agents individually and in the full pipeline
   - Verify bilingual support (Bengali and English)
   - Ensure grade-level appropriate responses
   - Validate mathematical accuracy and educational soundness

4. **Documentation**:
   - Update README.md for new features
   - Include agent descriptions and responsibilities
   - Provide usage examples and code samples
   - Document any new dependencies or setup requirements

---

**Built for Bangladeshi students with ❤️ using Google's Agent Development Kit**

_This system demonstrates the power of multi-agent orchestration for educational applications, focusing on intelligent text processing and culturally-aware educational content generation._

This project follows the same patterns as the LinkedIn post agent. To contribute:

1. Follow the existing agent structure
2. Add new agents to the subagents directory
3. Update the main sequential agent as needed
4. Maintain educational focus and cultural sensitivity

---

**Built for Bangladeshi students with ❤️ using Google's Agent Development Kit**
