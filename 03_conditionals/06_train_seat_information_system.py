'''
You're building a ticket info system for a railway app.
Based on seat type, show its features.

Task:

Input: "sleeper", "AC", "general", "luxury"
Match using match-case
Unknown → show: "Invalid seat type"

'''
seat_type = input("Enter the seat type (sleeper, AC, general, luxury): ").lower()  # convert input to lowercase for case-insensitive comparison
print(f"Seat type entered: {seat_type}")
match seat_type:
    case "sleeper":
        print("Sleeper class: Basic amenities, non-AC, economical.")
    case "ac":
        print("AC class: Air-conditioned, comfortable seating, moderate price.")
    case "general":
        print("General class: No reserved seating, basic amenities, low cost.")
    case "luxury":
        print("Luxury class: Premium amenities, spacious seating, high price.")
    case _:
        print("Invalid seat type")

