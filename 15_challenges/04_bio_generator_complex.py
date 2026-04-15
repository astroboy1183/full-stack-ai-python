'''
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2–3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer
  💡 Making things beautiful
  🔗 @riya.design

Bonus:
- Let the user pick from 2–3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
'''

import sys
from datetime import date

def get_validated_input(prompt, validation_func=None, error_message="Invalid input. Please try again.", is_optional=False, max_invalid_attempts=13):
    """
    Prompts the user for input and validates it based on provided criteria.
    Includes retry logic and an option to exit after multiple invalid attempts.
    """
    attempts = 0
    while attempts < max_invalid_attempts:
        user_input = input(prompt).strip()

        if not user_input:
            if is_optional:
                return "" # Return empty string for optional empty input
            else:
                print("Input cannot be empty. Please try again.")
        elif validation_func and not validation_func(user_input):
            print(error_message)
        else:
            return user_input
        
        attempts += 1
        
        if attempts >= 10 and attempts < max_invalid_attempts:
            attempts_left = max_invalid_attempts - attempts
            print(f"You have entered an invalid format {attempts} times. You have {attempts_left} more attempts left.")
            
            if attempts >= (max_invalid_attempts - 3): # Warn from 3rd to last attempt
                exit_choice = input("You are about to reach the maximum number of invalid attempts. Do you want to exit? (yes/no): ").strip().lower()
                if exit_choice == 'yes':
                    sys.exit("Exiting program due to user input.")
        elif attempts == max_invalid_attempts:
            sys.exit(f"Exiting program due to persistent invalid inputs after {max_invalid_attempts} attempts.")

# Validation functions
def validate_alpha_space(value):
    """Validates if a string contains only alphabetic characters and spaces."""
    return all(char.isalpha() or char.isspace() for char in value)

def validate_any_string(value):
    """Always returns True for any non-empty string."""
    return True

def validate_filename(value):
    """Basic validation for a filename to prevent common invalid characters."""
    invalid_chars = r'<>:"/\|?*'
    return value.strip() != "" and not any(c in invalid_chars for c in value)

# Main script logic
def generate_bio():
    print("Let's create your stylish social media bio!")

    name = get_validated_input(
        "Enter your Name: ",
        validation_func=validate_alpha_space,
        error_message="Invalid input. Please enter text (letters and spaces only).",
        is_optional=False
    )
    name = " ".join(word.capitalize() for word in name.split()) # Capitalize first letter of every word

    profession = get_validated_input(
        "Enter your Profession: ",
        validation_func=validate_alpha_space,
        error_message="Invalid input. Please enter text (letters and spaces only).",
        is_optional=False
    )
    profession = " ".join(word.capitalize() for word in profession.split()) # Capitalize first letter of every word

    passion = get_validated_input(
        "Enter your one-liner passion or goal: ",
        validation_func=validate_any_string,
        error_message="Input cannot be empty.",
        is_optional=False
    )

    emoji = get_validated_input(
        "Enter your favorite emoji (optional, press Enter to skip): ",
        is_optional=True
    )

    website = get_validated_input(
        "Enter your website or handle (optional, e.g., @yourhandle or yourwebsite.com, press Enter to skip): ",
        is_optional=True
    )

    # Define layout styles
    layouts = {
        "1": {"name": f"{emoji} {name} | {profession}", "passion": f"💡 {passion}", "website": f"🔗 {website}"},
        "2": {"name": f"✨ {name} - {profession} {emoji}", "passion": f"🚀 {passion}", "website": f"🌐 {website}"},
        "3": {"name": f"👋 Hi, I'm {name}!", "passion": f"I'm a {profession} passionate about {passion}.", "website": f"Find me here: {website}"}
    }

    print("\nChoose a bio layout style:")
    for key, val in layouts.items():
        print(f"  [{key}]")
        print(f"    {val['name']}")
        print(f"    {val['passion']}")
        if val['website']: # Only print website line if it's provided
            print(f"    {val['website']}")
        print("-" * 20)

    chosen_layout_key = get_validated_input(
        "Enter the number of your preferred layout style (1, 2, or 3): ",
        validation_func=lambda x: x in layouts,
        error_message="Invalid layout choice. Please enter 1, 2, or 3.",
        is_optional=False
    )
    chosen_layout = layouts[chosen_layout_key]

    # Construct the final bio
    bio_lines = [chosen_layout["name"], chosen_layout["passion"]]
    if chosen_layout["website"]:
        bio_lines.append(chosen_layout["website"])
    final_bio = "\n".join(bio_lines)

    print("\n" + "*" * 50)
    print("Your Generated Bio:")
    print(final_bio)
    print("*" * 50)

    # Ask to save to file
    save_choice = get_validated_input(
        "\nDo you want to save this bio to a text file? (yes/no): ",
        validation_func=lambda x: x.lower() in ['yes', 'no'],
        error_message="Please enter 'yes' or 'no'.",
        is_optional=False
    ).lower()

    if save_choice == 'yes':
        filename = get_validated_input(
            "Enter filename (e.g., my_bio.txt): ",
            validation_func=validate_filename,
            error_message="Invalid filename. Cannot be empty or contain special characters like <, >, :, \", /, \\, |, ?, *.",
            is_optional=False
        )
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("Your Generated Bio:\n")
                f.write(final_bio)
                f.write(f"\n\nGenerated on: {date.today().strftime('%Y-%m-%d')}")
            print(f"Bio successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving file: {e}")

if __name__ == "__main__":
    generate_bio()