class CharCounter:
    # CharCounter class with a private key and internal count
    def __init__(self, key=None):
        self.__key = key      # private key (character to observe)
        self.__count = 0      # private count

    # setter for key (mutator)
    def setKey(self, key):
        self.__key = key

    # reset count to 0
    def resetCount(self):
        self.__count = 0

    # observe() checks each character against the key
    def observe(self, observe):
        """
        If the key attribute is equal to the observe parameter,
        increase the count by one and return the current count.
        """
        if self.__key is not None and observe == self.__key:
            self.__count += 1
        return self.__count

    # getter for count (accessor)
    def getCount(self):
        return self.__count


class CharCounterTest(CharCounter):
    def __init__(self, dotCounter, starCounter):
        # initialise parent class without a key first
        super().__init__()
        # store the characters to count
        self._dotCounter = dotCounter
        self._starCounter = starCounter

    def display(self, dotCounter, starCounter):
        while True:
            sentence = input("Input a line of characters: ")

            # sentinel control to stop the program
            if sentence == "-1":
                print("Goodbye!")
                break

            # --- Count dots using a for-loop ---
            self.setKey(dotCounter)       # set key = dot character
            self.resetCount()             # reset internal count to 0

            for i in range(len(sentence)):
                currentChar = sentence[i]
                # count occurrence of the dot in this char
                count = currentChar.count(dotCounter)
                if count > 0:
                    # call observe() from CharCounter
                    self.observe(currentChar)

            dot_count = self.getCount()   # get final dot count

            # --- Count stars using another for-loop ---
            self.setKey(starCounter)      # set key = star character
            self.resetCount()             # reset internal count to 0

            for i in range(len(sentence)):
                currentChar = sentence[i]
                # count occurrence of the star in this char
                count = currentChar.count(starCounter)
                if count > 0:
                    # call observe() from CharCounter
                    self.observe(currentChar)

            star_count = self.getCount()  # get final star count

            # display result
            print(f"The {dotCounter} appears {dot_count} time(s)")
            print(f"The {starCounter} appears {star_count} time(s)")

# Class Object / Main Program
if __name__ == "__main__":
    # initialise star and dot counters with their characters
    _dotCounter = "."
    _starCounter = "*"

    # create CharCounterTest object with both characters
    test = CharCounterTest(_dotCounter, _starCounter)

    # call display method
    test.display(_dotCounter, _starCounter)

