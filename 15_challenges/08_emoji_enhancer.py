'''
💡 Challenge: Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
I love to code and drink tea when I'm happy.

Output:
I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)
'''
import re
# Test case - I am jayanth. i love food and music. i also love to code.
def add_emojis(message):
    emoji_word = { "happy": "😊", "love": "❤️", "code": "💻", "tea": "🍵", "music": "🎵", "food": "🍔"}

    for word, emoji in emoji_word.items():
        message = re.sub(rf"\b{word}\b", f"{word} {emoji}", message, flags=re.IGNORECASE)

    return message

if __name__ == "__main__":
    message = input("Enter a message: ")
    enhanced_message = add_emojis(message)
    print(enhanced_message)
