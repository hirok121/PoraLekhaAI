"""
Education Agent Demo

This script demonstrates the capabilities of the Education Agent,
showing how it handles educational content and tutoring tasks.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def display_banner():
    """Display the education agent demo banner"""
    banner = """
    🎓 Education Agent Demo
    =======================
    
    Comprehensive Educational Support:
    ✅ Multi-subject tutoring (Math, Science, Languages)
    ✅ Step-by-step problem solving
    ✅ Bengali & English language support
    ✅ Academic writing assistance
    ✅ Exam preparation guidance
    
    Note: This demo shows the agent structure.
    Actual functionality requires Google ADK setup.
    """
    print(banner)


def show_agent_capabilities():
    """Display the education agent's capabilities"""
    print("📚 Education Agent Capabilities:")
    print("=" * 50)

    capabilities = [
        ("Mathematics", "Algebra, geometry, calculus, statistics"),
        ("Sciences", "Physics, chemistry, biology, earth science"),
        ("Languages", "English literature, grammar, Bengali"),
        ("Social Studies", "History, geography, civics, economics"),
        ("Computer Science", "Programming concepts, algorithms"),
        ("Study Skills", "Research methods, time management"),
    ]

    for subject, details in capabilities:
        print(f"🔹 {subject}: {details}")

    print("\n📝 Teaching Approach:")
    approaches = [
        "Socratic Method - Guided questioning",
        "Step-by-Step Explanations",
        "Multiple Learning Styles Support",
        "Encouraging and Patient Tone",
        "Error Analysis and Learning",
    ]

    for approach in approaches:
        print(f"  • {approach}")


def show_sample_interactions():
    """Show sample educational interactions"""
    print("\n💡 Sample Educational Questions:")
    print("=" * 50)

    samples = [
        {
            "question": "Explain photosynthesis in simple terms",
            "type": "Science Concept",
        },
        {
            "question": "Solve the equation 3x + 7 = 22",
            "type": "Mathematics",
        },
        {
            "question": "What is the difference between mitosis and meiosis?",
            "type": "Biology",
        },
        {
            "question": "How do I write a good thesis statement?",
            "type": "Academic Writing",
        },
        {
            "question": "ফটোসিন্থেসিস কি? (What is photosynthesis?)",
            "type": "Bengali Science",
        },
    ]

    for i, sample in enumerate(samples, 1):
        print(f"{i}. [{sample['type']}] {sample['question']}")


def demonstrate_educational_flow():
    """Demonstrate the educational agent's workflow"""
    print("\n🔄 Educational Agent Workflow:")
    print("=" * 50)

    workflow_steps = [
        "1. Analyze the educational question or topic",
        "2. Identify relevant subject area and complexity level",
        "3. Break down complex concepts into digestible parts",
        "4. Provide step-by-step explanations with examples",
        "5. Check student understanding with follow-up questions",
        "6. Offer additional practice or related concepts",
        "7. Encourage further learning and exploration",
    ]

    for step in workflow_steps:
        print(f"  {step}")


def check_environment():
    """Check if the required environment is set up"""
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("⚠️  Warning: GOOGLE_API_KEY environment variable not found.")
        print("Please set your Google API key to enable full functionality:")
        print("   export GOOGLE_API_KEY=your_api_key_here")
        print("   or create a .env file with GOOGLE_API_KEY=your_api_key_here")
        return False

    print("✅ Environment setup complete!")
    return True


def main():
    """Main demo function"""
    display_banner()

    # Check environment setup
    env_ready = check_environment()
    print()

    # Show agent capabilities
    show_agent_capabilities()

    # Show sample interactions
    show_sample_interactions()

    # Demonstrate workflow
    demonstrate_educational_flow()

    print("\n" + "=" * 50)
    print("🚀 Ready to enhance your learning experience!")

    if env_ready:
        print(
            "✅ The Education Agent is configured and ready to help with your studies."
        )
    else:
        print(
            "⚙️  Set up your environment to activate the Education Agent functionality."
        )

    print("\nTo use the Education Agent in your application:")
    print("```python")
    print("from tutoring_agent.agents.education_agent.agent import education_agent")
    print("# Use the agent for educational content and tutoring")
    print("```")


if __name__ == "__main__":
    main()
