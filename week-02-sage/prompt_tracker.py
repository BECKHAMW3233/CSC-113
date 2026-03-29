# prompt_tracker.py
# A simple menu-based system to manage and organize AI prompts

import os

# File to store prompts (will be created if it doesn't exist)
PROMPT_FILE = "my-prompts.txt"

def display_menu():
    """Show the main menu options"""
    print("\n=== Prompt Tracker ===")
    print("1. Add Prompt")
    print("2. View Prompts")
    print("3. Search Prompts")
    print("4. Quit")
    print("======================")

def add_prompt():
    """Add a new prompt to the tracker"""
    print("\n=== Add New Prompt ===")
    
    # Get user input for each field
    prompt_text = input("Enter your prompt: ")
    category = input("Choose category (learning/creating/evaluating/other): ").lower()
    
    # Validate category input
    while category not in ["learning", "creating", "evaluating", "other"]:
        print("Invalid category. Please choose from: learning, creating, evaluating, other")
        category = input("Choose category: ").lower()
    
    note = input("Add a short note about when to use this: ")
    
    # Save to file with comma-separated values
    with open(PROMPT_FILE, "a") as f:
        f.write(f"{prompt_text},{category},{note}\n")
    
    print("✅ Prompt added successfully!")

def view_prompts():
    """Display all prompts organized by category"""
    print("\n=== Your Prompts ===")
    
    # Create a dictionary to group prompts by category
    categories = {"learning": [], "creating": [], "evaluating": [], "other": []}
    
    # Read and organize prompts
    if os.path.exists(PROMPT_FILE):
        with open(PROMPT_FILE, "r") as f:
            for line in f:
                if line.strip():  # Skip empty lines
                    parts = line.strip().split(",")
                    if len(parts) >= 3:
                        prompt, category, note = parts[0], parts[1], parts[2]
                        categories[category].append((prompt, note))
    
    # Display each category's prompts
    for cat, items in categories.items():
        if items:
            print(f"\n--- {cat.capitalize()} ---")
            for i, (prompt, note) in enumerate(items, 1):
                print(f"{i}. {prompt} | {note}")

def search_prompts():
    """Search prompts by keyword"""
    print("\n=== Search Prompts ===")
    keyword = input("Enter keyword to search: ").lower()
    
    matches = []
    
    if os.path.exists(PROMPT_FILE):
        with open(PROMPT_FILE, "r") as f:
            for line in f:
                if line.strip() and keyword in line.lower():
                    parts = line.strip().split(",", 2)  # Split into 3 parts max
                    if len(parts) >= 3:
                        prompt, category, note = parts[0], parts[1], parts[2]
                        matches.append((prompt, category, note))
    
    if matches:
        print(f"\nFound {len(matches)} match(es):")
        for i, (prompt, cat, note) in enumerate(matches, 1):
            print(f"{i}. [{cat}] {prompt} | {note}")
    else:
        print("❌ No matching prompts found.")

def main():
    """Main program loop"""
    while True:
        display_menu()
        
        try:
            choice = int(input("\nChoose an option (1-4): "))
            
            if choice == 1:
                add_prompt()
            elif choice == 2:
                view_prompts()
            elif choice == 3:
                search_prompts()
            elif choice == 4:
                print("👋 Goodbye!")
                break
            else:
                print("Please choose a number between 1 and 4")
                
        except ValueError:
            print("Please enter a valid number")

# Run the program
if __name__ == "__main__":
    main()
