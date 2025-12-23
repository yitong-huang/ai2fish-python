import random


class SecurityPass:
    """
    Helper class: handles login checking, registration, and security level assignment.
    """

    # Class-level dictionary to store registered members: {username: password}
    members_db = {}

    def checkLogin(self, username, password):
        """
        Check login credentials, handle registration, and assign security level.
        """

        # 1) Handle empty username or password
        if username == "" or password == "":
            print("Username and Password cannot be empty.")
            choice = input("Do you wish to try again (yes/no): ").strip().lower()
            if choice == "yes":
                print("To exit the program enter (finish or 0)")
                new_user = input("Enter Username: ").strip()
                if new_user == "finish":
                    self.exit_program()
                    return

                new_pass = input("Enter Password: ").strip()
                if new_pass == "0":
                    self.exit_program()
                    return

                # Recursive call to checkLogin with new input
                self.checkLogin(new_user, new_pass)
            else:
                print("Goodbye! Do visit our club again!!")
            return

        # 2) Check if user is already a member
        if username in SecurityPass.members_db and SecurityPass.members_db[username] == password:
            # Existing registered member (or previously registered guest)
            self.welcome_user(username, is_new=False)
        else:
            # Not a member yet
            print("Login failed. You're not a member of the exclusive club.")
            register = input("Do you want to register (Yes or No): ").strip().lower()

            if register in ("yes", "y"):
                # Add username and password to the members database
                SecurityPass.members_db[username] = password
                print("The user database is now updated.")
                # Welcome as new member / guest
                self.welcome_user(username, is_new=True)
            else:
                # Do not register; return to main loop
                return

    def welcome_user(self, username, is_new=False):
        """
        Assign security level and print welcome message.

        Guests ("Guest") get level 1–3.
        Club members get level 4–200.
        """
        if username.lower() == "guest":
            # Guest user: low security level (1–3)
            sec_num = random.randint(1, 3)
            print(f"Welcome, {username}, you are now a guest member of the exclusive club!")
            print(f"Your guest security number is: {sec_num}")
        else:
            # Regular club member: higher security level (4–200)
            sec_num = random.randint(4, 200)
            print(f"Welcome, {username}, you are now a member of the exclusive club!")
            print(f"Your security number is: {sec_num}")

    def exit_program(self):
        """
        Standard exit message for the program.
        """
        print("You are exiting the program!")
        input("Press the enter key to exit the program.")
        print("Thank you for visiting!")


class Members(SecurityPass):
    """
    Members class inherits from SecurityPass.
    It prints the club header and calls checkLogin() in the constructor.
    """

    club_doc = "Exclusive Club Network 5*\n Registered Club Members Only."

    def __init__(self, username, password):
        self.username = username
        self.password = password
        # Call the parent class method to handle login / registration / security
        self.checkLogin(self.username, self.password)


def main():
    # Display club header at the start
    print(Members.club_doc)

    while True:
        print("To exit the program enter (finish or 0)")
        username = input("Enter Username: ").strip()

        # Sentinel control: "finish" → exit program
        if username == "finish":
            sp = SecurityPass()
            sp.exit_program()
            break

        password = input("Enter Password: ").strip()

        # Sentinel control: "0" → exit program
        if password == "0":
            sp = SecurityPass()
            sp.exit_program()
            break

        # Create a Members instance; constructor will trigger login flow
        member = Members(username, password)
        # No further action needed here; all logic happens inside the classes


if __name__ == "__main__":
    main()

