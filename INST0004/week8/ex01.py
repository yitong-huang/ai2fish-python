import sys
import string

class DrugRegimen:
    def drugRegimen(self, menu):
        # Symptoms associated with liver inflammation
        liver_symptoms = ["4", "5"]

        # Check if user selected any liver inflammation symptom
        if any(item in liver_symptoms for item in menu):
            print("Prescribed Drug regimen (9 Months):")
            print("1. Rifinah")
            print("2. Pyridoxine")
            print("3. Ethambutol")
        else:
            print("Prescribed Drug Regimen (6 Months):")
            print("1. Rifinah")
            print("2. Pyridoxine")
            print("3. Pyrazinamide")
            print("4. Ethambutol")


class TuberculosisTreatment(DrugRegimen):

    def __init__(self):
        self.menu = []  # store selected symptoms

    def menuOption(self):
        while True:
            print("*** Please select an option ***")
            print("1: Itching and skin rashes")
            print("2: Feeling nauseous")
            print("3: Stomach-ache")
            print("4: Nausea or vomiting")
            print("5: Abdominal pain")
            print("6: Exit")

            choice = input("Please select a symptom: ").strip()

            # EXIT option
            if choice == "6":
                print("You are exiting. Thank you!")
                break

            # VALID options
            if choice in ["1", "2", "3", "4", "5"]:
                self.menu.append(choice)
                options = {
                    "1": "Itching and skin rashes",
                    "2": "Feeling nauseous",
                    "3": "Stomach-ache",
                    "4": "Nausea or vomiting",
                    "5": "Abdominal pain"
                }
                print(f"Symptom: {options[choice]}")

            else:
                print("Symptom NOT in main menu option!")
                self.displayOptions()   # recursive error handler

        # After exit:
        self.menu_list()
        self.drugRegimen(self.menu)

    def menu_list(self):
        print(f"The selected menu(s) are/is: {self.menu}")

    def displayOptions(self):
        # Recursive method
        ans = input("Invalid option! Would you like to see the main menu again? (Y/N): ").lower()

        if ans == "y":
            self.menuOption()  # restart menu
        elif ans == "n":
            print("Goodbye!")
        else:
            # Recursively ask again
            self.displayOptions()


# Create instance & run program
tb1 = TuberculosisTreatment()
tb1.menuOption()
tb2 = TuberculosisTreatment()
tb2.menuOption()
