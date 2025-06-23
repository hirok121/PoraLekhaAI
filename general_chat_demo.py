"""
General Chat Agent Demo

Demonstrates the General Chat Agent functionality for handling
casual conversations, greetings, and non-academic interactions.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def display_banner():
    """Display the general chat demo banner"""
    banner = """
    💬 General Chat Agent Demo
    ==========================
    
    Testing casual conversation handling:
    ✅ Greetings and introductions
    ✅ Bengali & English support
    ✅ Educational topic encouragement
    ✅ Friendly, supportive responses
    
    Note: This demo shows the agent structure.
    Actual functionality requires Google ADK setup.
    """
    print(banner)


def demo_general_chat_responses():
    """Demonstrate expected general chat agent responses"""

    print("\n🔄 Sample General Chat Interactions:")
    print("=" * 50)

    # English examples
    test_cases_english = [
        {
            "input": "Hello! How are you?",
            "expected": "Hello! I'm doing wonderful, thank you for asking! I'm excited to help you with your studies today. What subject interests you most - Math, Physics, Chemistry, or Biology?",
        },
        {
            "input": "What's your name?",
            "expected": "I'm your AI tutor! You can just call me your study buddy. I'm here to help make learning fun and easy for you. What grade are you in, and what subject would you like to work on?",
        },
        {
            "input": "Can you help me?",
            "expected": "Absolutely! I'd love to help you. That's exactly what I'm here for! Are you working on homework, preparing for exams, or do you have questions about any particular subject?",
        },
    ]

    # Bengali examples
    test_cases_bengali = [
        {
            "input": "আপনার নাম কি?",
            "expected": "আমি আপনার AI টিউটর! আপনি আমাকে আপনার পড়াশোনার বন্ধু বলে ডাকতে পারেন। আমি এখানে আছি আপনার পড়াশোনাকে সহজ এবং মজার করে তুলতে। আপনি কোন ক্লাসে পড়েন এবং কোন বিষয়ে সাহায্য চান?",
        },
        {
            "input": "আপনি কি করতে পারেন?",
            "expected": "আমি আপনাকে গণিত, পদার্থবিজ্ঞান, রসায়ন এবং জীববিজ্ঞানে সাহায্য করতে পারি! আমি সমস্যা সমাধান, ধারণা ব্যাখ্যা এবং পরীক্ষার প্রস্তুতিতে সহায়তা করি। আপনার কোন বিষয়ে সাহায্য প্রয়োজন?",
        },
    ]

    print("\n📝 English Conversations:")
    print("-" * 30)
    for i, case in enumerate(test_cases_english, 1):
        print(f"\n{i}. User: \"{case['input']}\"")
        print(f"   Agent: \"{case['expected']}\"")

    print("\n📝 Bengali Conversations:")
    print("-" * 30)
    for i, case in enumerate(test_cases_bengali, 1):
        print(f"\n{i}. User: \"{case['input']}\"")
        print(f"   Agent: \"{case['expected']}\"")


def show_agent_capabilities():
    """Display the general chat agent's capabilities"""

    print("\n🎯 General Chat Agent Capabilities:")
    print("=" * 40)

    capabilities = [
        "✅ Friendly greetings in English and Bengali",
        "✅ Personal questions about AI identity and purpose",
        "✅ Social chitchat and casual conversation",
        "✅ Encouragement and motivation for learning",
        "✅ Natural transitions to educational topics",
        "✅ Cultural awareness for Bangladeshi students",
        "✅ Support for mixed language (Banglish) conversations",
    ]

    for capability in capabilities:
        print(f"   {capability}")

    print("\n🚀 Educational Transition Strategies:")
    print("-" * 35)

    strategies = [
        "• 'That's great! Since you're here, is there any subject you'd like to explore?'",
        "• 'I'd love to help you with your studies! What grade are you in?'",
        "• 'Are you working on any homework or have questions about Math, Physics, Chemistry, or Biology?'",
    ]

    for strategy in strategies:
        print(f"   {strategy}")


def simulate_conversation_flow():
    """Simulate how the conversation router works with general chat agent"""

    print("\n🔄 Conversation Flow Simulation:")
    print("=" * 35)

    flow_steps = [
        "1. User Input: 'Hello! How are you?'",
        "2. Conversation Router: Classifies as 'GENERAL' → Routes to General Chat Agent",
        "3. General Chat Agent: Provides friendly response + educational encouragement",
        "4. System: Returns response to user",
    ]

    for step in flow_steps:
        print(f"   {step}")

    print(f"\n   📤 Final Response: Warm greeting + study topic suggestion")


def demo_agent_structure():
    """Show the agent structure and configuration"""

    print("\n🏗️  Agent Structure:")
    print("=" * 20)

    print(
        """
    tutoring_agent/
    └── agents/
        ├── general_chat/
        │   ├── __init__.py
        │   └── agent.py          # ← New General Chat Agent
        ├── conversation_router/
        │   └── agent.py          # ← Updated to route to general chat
        └── __init__.py           # ← Updated imports
    """
    )

    print("\n⚙️  Agent Configuration:")
    print("-" * 22)
    print("   • Name: GeneralChatAgent")
    print("   • Model: gemini-2.0-flash")
    print("   • Purpose: Handle casual conversations")
    print("   • Language Support: English + Bengali")
    print("   • Integration: Routes via ConversationRouterAgent")


def main():
    """Main demo function"""
    try:
        display_banner()
        demo_general_chat_responses()
        show_agent_capabilities()
        simulate_conversation_flow()
        demo_agent_structure()

        print("\n" + "=" * 50)
        print("✅ General Chat Agent Demo Complete!")
        print("📋 Next Steps:")
        print("   1. Set up Google ADK environment")
        print("   2. Configure API keys in .env file")
        print("   3. Test with actual conversations")
        print("   4. Integrate with main tutoring system")
        print("=" * 50)

    except Exception as e:
        print(f"❌ Demo error: {e}")
        print("💡 This is expected if Google ADK is not set up yet.")


if __name__ == "__main__":
    main()
