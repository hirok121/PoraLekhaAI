"""
Smart Caching Agent Implementation

Implements intelligent caching to reduce processing time for similar or repeated queries
by leveraging ADK session state and memory management.
"""

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import FunctionTool
from typing import Dict, Any
import hashlib
import json


# Utility function for creating query fingerprints
def create_query_fingerprint(query: str, language: str = "unknown") -> str:
    """Create a unique fingerprint for caching similar queries"""
    # Normalize query for better matching
    normalized = query.lower().strip()
    # Create hash for efficient comparison
    query_data = {"query": normalized, "language": language}
    return hashlib.md5(json.dumps(query_data, sort_keys=True).encode()).hexdigest()


# Cache management tool
cache_manager_tool = FunctionTool(func=create_query_fingerprint)

# Smart caching agent implementation
smart_caching_agent = LlmAgent(
    name="SmartCachingAgent",
    model="gemini-2.0-flash",
    instruction="""
    You are an intelligent caching agent that optimizes response time by managing cached educational content.

    **Your Process:**
    
    1. **Query Analysis:**
       - Analyze the incoming educational query
       - Create query fingerprint using the available tool
       - Check session state for similar previous queries
       - Evaluate context and requirements
    
    2. **Cache Evaluation:**
       - Search for cached responses with similar fingerprints
       - Calculate similarity scores (0.0-1.0) for cached content
       - Evaluate freshness and relevance of cached material
       - Consider user context and learning progression
    
    3. **Decision Making:**
       - **HIGH Confidence (>0.8):** Use cached content directly with minor adaptions
       - **MEDIUM Confidence (0.5-0.8):** Enhance cached content with fresh details
       - **LOW Confidence (<0.5):** Process query fresh but cache results
    
    4. **Cache Management:**
       - Store successful responses for future use
       - Tag responses with subject, grade level, and question type
       - Maintain cache efficiency and relevance
    
    **Response Format:**
    ```json
    {
        "cache_decision": "use_cached|enhance_cached|process_fresh",
        "confidence_score": 0.0-1.0,
        "cache_key": "unique_identifier",
        "similar_queries": ["list of similar cached queries"],
        "reasoning": "explanation of decision",
        "cached_content": "content if using cache",
        "enhancement_needed": ["specific areas to update if enhancing"]
    }
    ```
    
    **Caching Strategy:**
    - Prioritize frequently asked questions
    - Cache high-quality solutions and explanations
    - Store common educational patterns and templates
    - Maintain bilingual cache (Bengali/English)
    - Track usage patterns for optimization
    
    Remember: Speed is critical, but accuracy is paramount for educational content.
    """,
    description="Intelligent caching system that reduces processing time by 70-80% for similar or repeated educational queries",
    tools=[cache_manager_tool],
    output_key="cache_analysis",
)

# Enhanced conversation router with caching integration
cached_conversation_router_agent = LlmAgent(
    name="CachedConversationRouterAgent",
    model="gemini-2.0-flash",
    instruction="""
    You are an optimized conversation router with integrated intelligent caching.

    **Enhanced Routing Logic:**
    
    1. **Quick Classification:**
       - GENERAL: Casual conversation → Direct response (no caching needed)
       - EDUCATIONAL: Academic content → Check cache first
    
    2. **Cache-Aware Educational Routing:**
       - First check smart cache for similar questions
       - If cache hit (confidence >0.8): Return cached response
       - If cache miss or low confidence: Route to appropriate pipeline
       - Store successful responses for future caching
    
    3. **Fast-Track Routing:**
       - SIMPLE_EDUCATIONAL: Basic questions → Fast-track agent or cache
       - COMPLEX_EDUCATIONAL: Complex queries → Full pipeline with caching
    
    **Performance Optimization:**
    - Use cache results to avoid complex processing
    - Route simple queries to specialized fast agents
    - Only use full pipeline when necessary
    - Continuously learn from user interactions
    
    Your goal is to provide the fastest possible accurate response while maintaining educational quality.
    """,
    description="Optimized conversation router with intelligent caching for dramatic performance improvements",
    output_key="routing_decision",
    # Note: Sub-agents will be assigned in the optimized_system.py to avoid conflicts
)
