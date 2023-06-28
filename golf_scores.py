"""
Problem Statement Golf Scores
The Springfork Amateur Golf Club has a tournament every weekend. The club president
has asked you to write two programs:
A program that will read each player’s name and golf score as keyboard input, and then
save these as records in a file named golf.txt. (Each record will have a field for the
player’s name and a field for the player’s score.)
 A program that reads the records from the golf.txt file and displays them

"""

import os



def clear_screen():
    # Check if the operating system is Windows or Unix/Linux
    if os.name == 'nt':
        _ = os.system('cls')  # Clear screen for Windows
    else:
        _ = os.system('clear')  # Clear screen for Unix/Linux


def save_player_records():
    # Open the file in append mode to add records
    with open("golf.txt", "a") as file:
        while True:
            # Get player's name and score from user
            while True:
                name = input("Enter player's name (or 'q' to quit): ")
                if name.lower() == 'q':
                    return

                # Validate name input
                if not name or name.isspace() or name.isdigit() or len(name) == 1:
                    print("Invalid name. Please try again.")
                else:
                    break

            while True:
                score = input("Enter player's score: ")

                # Validate score input
                if not score.isdigit():
                    print("Invalid score. Please enter a valid integer score.")
                else:
                    # Write the record to the file
                    file.write(f"{name},{score}\n")
                    break

    print("Player records saved in golf.txt.")


def display_player_records():
    # Read and display records from the file
    with open("golf.txt", "r") as file:
        records = file.readlines()

    if not records:
        print("No player records found.")
    else:
        for record in records:
            name, score = record.strip().split(",")
            print(f"Player: {name}\tScore: {score}")


def delete_player_records():
    # Read and display records from the file
    with open("golf.txt", "r") as file:
        records = file.readlines()

    if not records:
        print("No player records found.")
        return

    print("Existing player records:")
    for i, record in enumerate(records, start=1):
        name, score = record.strip().split(",")
        print(f"{i}. Player: {name}\tScore: {score}")

    while True:
        try:
            choice = int(input("Enter the number of the player you want to delete (or '0' to cancel): "))
            if choice == 0:
                return

            if 1 <= choice <= len(records):
                # Remove the selected player record
                del records[choice - 1]
                print("Player record deleted.")
                break
            else:
                print("Invalid choice. Please enter a valid player number.")
        except ValueError:
            print("Invalid choice. Please enter a valid player number.")

    # Rewrite the updated records to the file
    with open("golf.txt", "w") as file:
        for record in records:
            file.write(record)


# Main program
while True:
    clear_screen()

    choice = input("Choose an option:\n1. Save player records\n2. Display player records\n3. Delete player record\n4. Quit\nEnter your choice: ")

    if choice == "1":
        save_player_records()
    elif choice == "2":
        display_player_records()
    elif choice == "3":
        delete_player_records()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

    input("Press Enter to continue...")
