import random


class CasinoRoulette:
    # Class attributes to track winnings
    human_wins_list = []
    system_wins_list = []
    human_total = 0
    system_total = 0

    def __init__(self, rolls):
        # rolls = number of allocated spin-offs / balls
        self.rolls = rolls

    # ---------------- HUMAN OPERATIONS ----------------

    def humRolling(self):
        print("****** HUMAN PLAY ****")
        for i in range(1, self.rolls + 1):
            while True:
                user_input = input(f"HUMAN Enter throw rolling to a number [{i}]: ")

                # Validate input is an integer
                try:
                    num = int(user_input)
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
                    continue

                # Validate range 1–10
                if num < 1 or num > 10:
                    print("Invalid entry! The required input is between 1 and 10.")
                    continue

                # Valid roll
                CasinoRoulette.human_total = CasinoRoulette.humanWins(num)
                print(f"HUMAN rolled: {num}")
                print(f"List of HUMAN winnings {CasinoRoulette.human_wins_list}")
                break

    @classmethod
    def humanWins(cls, rolled_number):
        # Dictionary of winnings 1 → 1000, ..., 10 → 10000
        win_dict = {i: i * 1000 for i in range(1, 11)}

        # Look up winnings and append to human list
        win_amount = win_dict.get(rolled_number, 0)
        cls.human_wins_list.append(win_amount)

        # Compute total via static method
        total = cls.totalWins(cls.human_wins_list)
        return total

    @staticmethod
    def totalWins(win_list):
        total = sum(win_list)
        CasinoRoulette.takeHomeWin(total)
        return total

    @staticmethod
    def takeHomeWin(total):
        print(f"The total sum won by HUMAN is: {total}")

    # ---------------- SYSTEM OPERATIONS ----------------

    def sysRolling(self):
        print("****** SYSTEM PLAY ****")
        for i in range(1, self.rolls + 1):
            print(f"SYSTEM Enter throw rolling to a number [{i}]:")
            # System roll is random between 1 and 10
            num = random.randint(1, 10)
            CasinoRoulette.system_total = CasinoRoulette.sysWins(num)
            print(f"System rolled: {num}")
            print(f"List of SYSTEM winnings {CasinoRoulette.system_wins_list}")

    @classmethod
    def sysWins(cls, rolled_number):
        # Same winnings dictionary
        win_dict = {i: i * 1000 for i in range(1, 11)}

        win_amount = win_dict.get(rolled_number, 0)
        cls.system_wins_list.append(win_amount)

        total = cls.sysTotalWins(cls.system_wins_list)
        return total

    @staticmethod
    def sysTotalWins(win_list):
        total = sum(win_list)
        return CasinoRoulette.sysTakeHomeWin(total)

    @staticmethod
    def sysTakeHomeWin(total):
        print(f"The total sum won by the SYSTEM is: {total}")
        return total

    # ---------------- WINNER LOGIC ----------------

    @staticmethod
    def GameWinner():
        print("*** GAME WINNER ***")
        human_total = CasinoRoulette.human_total
        system_total = CasinoRoulette.system_total

        if human_total > system_total:
            margin = human_total - system_total
            print(f"Human Won by a Margin of £{margin}")
        elif system_total > human_total:
            margin = system_total - human_total
            print(f"Machine Won by a Margin of {margin}")
        else:
            print(
                f"It is a tie between human: £{human_total} and machine £{system_total}."
            )


# ---------------- MAIN PROGRAM ----------------

if __name__ == "__main__":
    # Initial totals (as in sample)
    print("The total sum won by the SYSTEM is: 0")
    print("The total sum won by HUMAN is: 0")

    # Ask for allocated spin-offs (balls)
    while True:
        try:
            rolls = int(input("Enter the allocated Roulette Spin-offs number: "))
            if 1 <= rolls <= 10:
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 10.")

    game = CasinoRoulette(rolls)

    # Human plays
    game.humRolling()

    # System plays
    game.sysRolling()

    # Decide winner
    CasinoRoulette.GameWinner()
