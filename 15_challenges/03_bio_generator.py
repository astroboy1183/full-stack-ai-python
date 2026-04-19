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
from datetime import date

def generate_bio():
    print("Create your stylish bio:\n")

    # Inputs
    name = " ".join(input("Name: ").title().split())
    profession = " ".join(input("Profession: ").title().split())
    passion = " ".join(input("One-liner passion or goal: ").title().split())
    emoji = input("Emoji (optional): ")
    website = input("Website/handle (optional): ")

    # Layouts dictionary (cleaner than if-else)
    layouts = {
        "1": lambda: f"{emoji} {name} | {profession}\n💡 {passion}" + (f"\n🔗 {website}" if website else ""),
        "2": lambda: f"✨ {name} - {profession} {emoji}\n🚀 {passion}" + (f"\n🌐 {website}" if website else ""),
        "3": lambda: f"{emoji*5}\n👋 Hi, I'm {name}!\n{profession} | {passion}\n{emoji*5}" + (f"\n🔗 {website}" if website else "")
    }

    # Choose layout
    choice = input("\nChoose layout (1.Simple Lines\n/2.Vertical Flair\n/3.Emoji Sandwich\n): ")
    final_bio = layouts.get(choice, layouts["1"])()

    print("\nGenerated Bio:\n")
    print(final_bio)

    save = input("\nSave to file? (y/yes/n/no): ").lower().strip()

    if save in ["y", "yes"]:
        filename = input("Filename: ")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(final_bio + f"\n\nGenerated on: {date.today()}")
        print("Saved successfully!")

if __name__ == "__main__":
    generate_bio()


#old code, little long.

# from datetime import date


# def generate_bio():
#     print("Let's create your stylish social media bio!")

#     # Inputs
#     name = input("Enter your Name: ").strip()
#     name = " ".join(word.capitalize() for word in name.split())

#     profession = input("Enter your Profession: ").strip()
#     profession = " ".join(word.capitalize() for word in profession.split())

#     passion = input("Enter your one-liner passion or goal: ").strip()

#     emoji = input("Enter your favorite emoji (optional, press Enter to skip): ").strip()

#     website = input(
#         "Enter your website or handle (optional, press Enter to skip): "
#     ).strip()

#     # Layout selection
#     print("\nChoose a bio layout style:")
#     print("1. Simple Lines")
#     print("2. Vertical Flair")
#     print("3. Emoji Sandwich")

#     layout_choice = input("Enter the number of your choice: ").strip()

#     # Generate bio (store in variable for reuse)
#     if layout_choice == '1':
#         final_bio = f"{emoji} {name} | {profession}\n💡 {passion}"
#         if website:
#             final_bio += f"\n🔗 {website}"
#         print(final_bio)

#     elif layout_choice == '2':
#         final_bio = f"✨ {name} - {profession} {emoji}\n🚀 {passion}"
#         if website:
#             final_bio += f"\n🌐 {website}"
#         print(final_bio)

#     elif layout_choice == '3':
#         final_bio = f"{emoji*6}\n"+f"👋 Hi, I'm {name}!\nI'm a {profession} passionate about {passion}."+f"\n{emoji*6}"
#         if website:
#             final_bio += f"\nFind me here: {website}"
#         print(final_bio)

#     else:
#         print("Invalid choice. Defaulting to Simple Lines.")
#         final_bio = f"{emoji} {name} | {profession}\n💡 {passion}"
#         if website:
#             final_bio += f"\n🔗 {website}"
#         print(final_bio)

#     # Print output
#     print("\nGenerated Bio:")
#     print(final_bio)

#     # Ask to save
#     save_choice = input("\nDo you want to save this bio to a text file? (yes/no): ").strip().lower()

#     if save_choice == 'yes':
#         filename = input("Enter filename (e.g., my_bio.txt): ").strip()

#         try:
#             with open(filename, "w", encoding="utf-8") as f:
#                 f.write("Your Generated Bio:\n\n")
#                 f.write(final_bio)
#                 f.write(f"\n\nGenerated on: {date.today().strftime('%Y-%m-%d')}")

#             print(f"Bio successfully saved to {filename}")

#         except IOError as e:
#             print(f"Error saving file: {e}")


# if __name__ == "__main__":
#     generate_bio()