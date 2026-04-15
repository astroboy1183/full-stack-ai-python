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
from datetime import date # Keep this for date.today()

#
def generate_bio():
    print("Let's create your stylish social media bio!")
  
    name = input("Enter your Name: ").strip()
    name = " ".join(word.capitalize() for word in name.split()) # Capitalize first letter of every word

    profession = input("Enter your Profession: ").strip()
    profession = " ".join(word.capitalize() for word in profession.split()) 

    
    passion = input("Enter your one-liner passion or goal: ").strip()

    emoji = input("Enter your favorite emoji (optional, press Enter to skip): ").strip()

    website = input("Enter your website or handle (optional, e.g., @yourhandle or yourwebsite.com, press Enter to skip): ").strip()

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

    chosen_layout_key = input("Enter the number of your preferred layout style (1, 2, or 3): ").strip()
    chosen_layout = layouts.get(chosen_layout_key, layouts["1"]) # Default to layout 1 if invalid key is entered

    bio_lines = [chosen_layout["name"], chosen_layout["passion"]]
    if chosen_layout["website"]:
        bio_lines.append(chosen_layout["website"])
    final_bio = "\n".join(bio_lines)

    print("\n" + "*" * 50)
    print("Your Generated Bio:")
    print(final_bio)
    print("*" * 50)

    # Ask to save to file
    save_choice = input("\nDo you want to save this bio to a text file? (yes/no): ").strip().lower()

    if save_choice == 'yes':
        
        filename = input("Enter filename (e.g., my_bio.txt): ").strip()
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