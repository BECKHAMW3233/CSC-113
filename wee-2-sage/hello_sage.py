# hello_sage.py
# My first Python script for CSC-113
# This script introduces SAGE and collects basic info

def main():
    print("=" * 40)
    print("  Welcome to SAGE")
    print("  Study Assistant & Guide Engine")
    print("=" * 40)
    print()

    # Get the user's name
    name = input("What's your name? ")
    print(f"\nHi {name}! Welcome to CSC-113.")

    # Ask what they want to learn
    print("\nWhat are you most interested in learning this semester?")
    print("  1. How AI works behind the scenes")
    print("  2. How to use AI tools effectively")
    print("  3. How to build things with AI")
    print("  4. All of the above")

    choice = input("\nPick a number (1-4): ")

    responses = {
        "1": "Great — we'll dig into the mechanics of AI systems.",
        "2": "Perfect — prompt engineering will be your superpower.",
        "3": "Awesome — you'll be building real projects soon.",
        "4": "Love it — you're going to get all of that and more."
    }

    print(f"\n{responses.get(choice, 'Good choice! We will figure it out together.')}")
    print(f"\nSAGE is ready to help you learn, {name}. Let's get started.")

if __name__ == "__main__":
    main()
