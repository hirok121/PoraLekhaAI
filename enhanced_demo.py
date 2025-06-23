"""
Enhanced Demo - Smart Conversation Routing

Demonstrates the new conversation routing system that handles:
1. General conversation (quick, friendly responses)
2. Educational questions (full tutoring pipeline)
3. Question clarification (helps improve unclear questions)
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def check_environment():
    """Check if the environment is properly configured."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("⚠️  Warning: GOOGLE_API_KEY environment variable not found.")
        print("Please set your Google API key:")
        print("   export GOOGLE_API_KEY=your_api_key_here")
        print("   or create a .env file with GOOGLE_API_KEY=your_api_key_here")
        print()
        return False

    print("✅ Environment configured successfully!")
    print(f"📡 Using API key: {api_key[:10]}...")
    print()
    return True


def demonstrate_routing_concepts():
    """Demonstrate the conversation routing concepts."""
    print("🔄 Smart Conversation Routing System")
    print("=" * 50)
    print()

    # Example inputs and expected routing
    test_cases = [
        {
            "input": "Hello! How are you?",
            "expected_route": "GENERAL",
            "description": "Friendly greeting - handled quickly without complex processing",
        },
        {
            "input": "আপনার নাম কি?",
            "expected_route": "GENERAL",
            "description": "Bengali greeting - quick response in Bengali",
        },
        {
            "input": "Solve 2x + 5 = 13",
            "expected_route": "EDUCATIONAL",
            "description": "Clear math problem - full tutoring pipeline activated",
        },
        {
            "input": "Explain photosynthesis for class 9",
            "expected_route": "EDUCATIONAL",
            "description": "Clear biology question - full educational processing",
        },
        {
            "input": "Help with math",
            "expected_route": "CLARIFICATION",
            "description": "Vague request - clarification agent asks for specifics",
        },
        {
            "input": "I don't understand this chapter",
            "expected_route": "CLARIFICATION",
            "description": "Unclear question - system helps student be more specific",
        },
    ]

    print("📋 Routing Examples:")
    print()

    for i, case in enumerate(test_cases, 1):
        print(f"{i}. Input: \"{case['input']}\"")
        print(f"   Route: {case['expected_route']}")
        print(f"   Logic: {case['description']}")
        print()

    print("🎯 Key Benefits:")
    print("• General chat gets immediate friendly responses")
    print("• Educational questions get full expert processing")
    print("• Unclear questions get helpful clarification")
    print("• Efficient resource usage - complex agents only when needed")
    print("• Bilingual support for Bengali and English")
    print()


def demonstrate_agent_architecture():
    """Show the new agent architecture."""
    print("🏗️  New Agent Architecture")
    print("=" * 50)
    print()

    print("🔀 Routing Agents (Lightweight & Fast):")
    print("   1. Conversation Router - Determines general vs educational")
    print("   2. Question Clarification - Improves unclear questions")
    print()

    print("🎓 Educational Pipeline (Full Processing):")
    print("   3. Language Router - Bengali/English processing")
    print("   4. Question Analyzer - Subject/grade categorization")
    print("   5. Knowledge Retriever - Information gathering")
    print("   6. Solution Generator - Pedagogical explanations")
    print("   7. Response Formatter - Final response preparation")
    print()

    print("⚡ Processing Flow:")
    print("   General Chat: Router → Quick Response (Steps 1-2 only)")
    print("   Educational: Router → Full Pipeline (All 7 steps)")
    print("   Unclear: Router → Clarification → User Revision")
    print()


def show_usage_examples():
    """Show practical usage examples."""
    print("💬 Usage Examples")
    print("=" * 50)
    print()

    conversations = [
        {
            "title": "General Conversation",
            "exchanges": [
                ("Student", "Hi there!"),
                (
                    "AI",
                    "Hello! I'm doing great, thank you! I'm here to help with your studies. What subject would you like to explore today?",
                ),
                ("Student", "What's your name?"),
                (
                    "AI",
                    "I'm your AI tutor! My job is to help you learn Math, Physics, Chemistry, and Biology. What are you working on?",
                ),
            ],
        },
        {
            "title": "Educational Question",
            "exchanges": [
                ("Student", "Solve for x: 3x - 7 = 14"),
                (
                    "AI",
                    "[Full tutoring pipeline activated] Let me help you solve this step by step...\n\n3x - 7 = 14\nAdd 7 to both sides: 3x = 21\nDivide by 3: x = 7\n\nThe answer is x = 7. Would you like me to explain any of these steps?",
                ),
            ],
        },
        {
            "title": "Question Clarification",
            "exchanges": [
                ("Student", "I need help with this problem"),
                (
                    "AI",
                    "I'd love to help! Could you please:\n1. Share the complete problem statement\n2. Let me know which subject (Math, Physics, Chemistry, Biology)\n3. Tell me your grade level\n\nFor example: 'Solve 2x + 5 = 13 for my grade 9 math homework'",
                ),
            ],
        },
    ]

    for conv in conversations:
        print(f"🗨️  {conv['title']}:")
        print("-" * 30)
        for speaker, message in conv["exchanges"]:
            print(f"{speaker}: {message}")
        print()


def main():
    """Run the enhanced demo."""
    print("🚀 Enhanced AI Tutoring System Demo")
    print("🎯 Smart Conversation Routing & Question Clarification")
    print("=" * 60)
    print()

    # Check environment
    if not check_environment():
        print("❌ Cannot run live demo without API key.")
        print(
            "Run this demo again after setting up your API key to see routing in action!"
        )
        print()
    else:
        print(
            "🎉 System ready! The routing agents would handle conversations as shown below."
        )
        print()

    # Show concepts and examples
    demonstrate_routing_concepts()
    demonstrate_agent_architecture()
    show_usage_examples()

    print("✨ Demo Complete!")
    print()
    print("🔄 What's New:")
    print("• Smart routing prevents unnecessary processing for casual chat")
    print("• Question clarification helps students ask better questions")
    print("• Efficient resource usage - complex AI only when needed")
    print("• Better user experience with appropriate response types")
    print()
    print("Next steps:")
    print("1. Test the system with various input types")
    print("2. Customize agent responses for your specific needs")
    print("3. Add more routing logic or specialized agents")
    print("4. Monitor performance and user satisfaction")


if __name__ == "__main__":
    main()
