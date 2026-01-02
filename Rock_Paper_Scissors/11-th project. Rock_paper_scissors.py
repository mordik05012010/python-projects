import random

def rock_paper_scissors():
    wins = 0
    losses = 0

    while True:
        computer_choice = random.choice(["rock", "paper", "scissors"])
        choice = input(
            "\nGame: Rock-Paper-Scissors\n"
            "Menu:\n"
            "1. Play\n"
            "2. Rules\n"
            "3. Exit\n"
            "Your choice: "
        )

        if choice == "1":
            r_p_s = input(
                "Choose rock (r), paper (p), or scissors (s): "
            ).lower().strip()

            if r_p_s == "r":
                if computer_choice == "rock":
                    print(f"Draw.\nWins: {wins}\nLosses: {losses}")
                elif computer_choice == "paper":
                    wins += 1
                    print(f"Well done! You won.\nWins: {wins}\nLosses: {losses}")
                elif computer_choice == "scissors":
                    losses += 1
                    print(f"You lost.\nWins: {wins}\nLosses: {losses}")

            elif r_p_s == "p":
                if computer_choice == "rock":
                    wins += 1
                    print(f"Well done! You won.\nWins: {wins}\nLosses: {losses}")
                elif computer_choice == "paper":
                    print(f"Draw.\nWins: {wins}\nLosses: {losses}")
                elif computer_choice == "scissors":
                    losses += 1
                    print(f"You lost.\nWins: {wins}\nLosses: {losses}")

            elif r_p_s == "s":
                if computer_choice == "rock":
                    losses += 1
                    print(f"You lost.\nWins: {wins}\nLosses: {losses}")
                elif computer_choice == "paper":
                    wins += 1
                    print(f"Well done! You won.\nWins: {wins}\nLosses: {losses}")
                elif computer_choice == "scissors":
                    print(f"Draw.\nWins: {wins}\nLosses: {losses}")
            else:
                print("Invalid option. Choose between 'r', 'p', or 's'.")

            continuing = input("Do you want to play again? (y/n): ").lower().strip()
            if continuing == "y":
                continue
            elif continuing == "n":
                break
            else:
                print("Invalid answer.")

        elif choice == "2":
            print(
                "\nRules of the game:\n"
                "Winning conditions:\n"
                "1. Rock beats Scissors.\n"
                "2. Scissors beats Paper.\n"
                "3. Paper beats Rock.\n"
                "Good luck!"
            )

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid menu option.")


rock_paper_scissors()
