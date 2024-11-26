class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} {self.price}"

class VendingMachine:
    def __init__(self, beverage_list):
        self.beverages = beverage_list

    def _promptUser(self):
        print("\nPlease select a beverage by entering the number and cash")
        print("(e.g. select the second beverage and pay $5.25: '2 5.25')")
        for idx, b in enumerate(self.beverages):
            print(f"\t{idx + 1}. {b}")
        print("\n")

    def _parseInput(self, user_input):
        user_input = user_input.split()
        if len(user_input) != 2:
            return False

        selection = int(user_input[0])
        cash = float(user_input[1])

        if selection > 0 and selection < 7:
            if self.beverages[selection-1].price <= cash:
                return True

        return False

    def turnOn(self):
        while True:
            self._promptUser()
            choice = input("Selection: ")
            correct_input = self._parseInput(choice)
            while not correct_input:
                print("\n\nWrong user input, please enter both the selected beverage number and cash")
                self._promptUser()
                choice = input("Selection: ")
                correct_input = self._parseInput(choice)
            choice = choice.split()
            soda_idx = int(choice[0]) - 1
            print("\n\n*********************************")
            print(f"Thank you for buying beverage a '{self.beverages[soda_idx].name}'")
            print("*********************************")


if __name__ == "__main__":
    sodas = [
        Beverage("CocaCola", 2.5),
        Beverage("Sprit", 2.0),
        Beverage("Pepsi", 1.99),
        Beverage("Fanta", 2.75),
        Beverage("MTN Dew", 2.99),
        Beverage("7Up", 1.75)
    ]

    sodaMachine = VendingMachine(sodas)
    sodaMachine.turnOn()