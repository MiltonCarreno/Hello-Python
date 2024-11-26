class Sit:
    def __init__(self, sit_number, first_class=False, emergency=False):
        self._number = sit_number
        self._firstClass = first_class
        self._emergency = emergency
        self._isAvailable = True
        self._selected = False
        self._cost = 100
        if first_class:
            self._fee = 50
        else:
            self._fee = 0

    def get_cost(self):
        return self._cost

    def get_fee(self):
        return self._fee

    def get_number(self):
        return self._number

    def is_first_class(self):
        return self._firstClass

    def is_emergency(self):
        return self._emergency

    def is_available(self):
        return self._isAvailable and not self._selected

    def select(self):
        if self._emergency:
            msg = "You have selected and emergency row sit.\n"
            msg += "In order to purchase this sit, one must accept responsibility in case of an emergency.\n"
            msg += "Type 'Y' to accept. Type 'N' to deny\n"
            accept_emergency = input(msg)
            if accept_emergency == "Y":
                self._selected = True
        else:
            self._selected = True

    def purchase(self):
        self._selected = False
        self._isAvailable = False

    def __str__(self):
        if self._selected:
            return '{: >4}'.format("SL")
        elif self._isAvailable:
            return f"{self.get_number(): >4}"
        return '{: >4}'.format("XX")


class Plane:
    def __init__(self, sits):
        self.sits = sits

    def showSits(self):
        print("\n*===============Sitting Chart===============*")
        print("'XX' = Unavailable, 'SL' = Selected\n")
        for idx, row in enumerate(sits):
            print_str = '{: <8}'.format(f"\tRow {idx+1}:")
            print_str += f"{row[0]} {row[1]}"
            if row[0].is_first_class():
                print_str += " <-- First Class Row"
            elif row[0].is_emergency():
                print_str += " <-- Emergency Row"
            else:
                print_str += " <-- Economy Row"
            print(print_str)

        print("\n*===========================================*")

    def promptUser(self):
        self.showSits()
        selected_dict = {}
        print(f"Selected sits: {selected_dict}")
        print("*===========================================*\n")

        selection_msg = "Please select a sit (e.g. type 'B3' for the economy 3rd row B sit.)\n"
        selection_msg += "Type 'q' to exit sit selection and purchase the selected sits\n"
        selection_msg += "\nSelection: "
        sit_selection = input(selection_msg)

        while sit_selection != "q":
            for rows in sits:
                first_selected = (rows[0].get_number() == sit_selection)
                second_selected = (rows[1].get_number() == sit_selection)
                if first_selected and rows[0].is_available():
                    rows[0].select()
                    if not rows[0].is_available():
                        selected_dict[sit_selection] = [rows[0].get_cost(), rows[0].get_fee()]
                elif second_selected and rows[1].is_available():
                    rows[1].select()
                    if not rows[1].is_available():
                        selected_dict[sit_selection] = [rows[1].get_cost(), rows[1].get_fee()]
                elif ((first_selected and not rows[0].is_available()) or
                      (second_selected and not rows[1].is_available())):
                    print(f"******Selected sit is not available******\n")

            self.showSits()
            print(f"Selected sits: {list(selected_dict.keys())}")
            print("*===========================================*\n")
            sit_selection = input(selection_msg)

        self._finishPurchase(selected_dict)

    def _finishPurchase(self, selected_dict):
        total_costs = 0
        total_fees = 0
        for sit_num in selected_dict:
            cost = selected_dict[sit_num][0]
            fee = selected_dict[sit_num][1]
            print(f"{sit_num}: ${cost} (Cost) + ${fee} (Fee)")
            total_costs += cost
            total_fees += fee

        print(f"Total costs: {total_costs}\nTotal fees: {total_fees}\nTotal: {total_costs + total_fees}")

        for row in sits:
            if row[0].get_number() in selected_dict:
                row[0].purchase()
            elif row[1].get_number() in selected_dict:
                row[1].purchase()

        self.showSits()


if __name__ == "__main__":
    a1 = Sit("A1", first_class=True)
    a2 = Sit("A2", first_class=True)
    a3 = Sit("A3")
    a4 = Sit("A4")
    a5 = Sit("A5", emergency=True)
    a6 = Sit("A6", emergency=True)
    a7 = Sit("A7")
    a8 = Sit("A8")
    a9 = Sit("A9")
    a10 = Sit("A10")

    b1 = Sit("B1", first_class=True)
    b2 = Sit("B2", first_class=True)
    b3 = Sit("B3")
    b4 = Sit("B4")
    b5 = Sit("B5", emergency=True)
    b6 = Sit("B6", emergency=True)
    b7 = Sit("B7")
    b8 = Sit("B8")
    b9 = Sit("B9")
    b10 = Sit("B10")

    sits = [
        [a1, b1], [a2, b2], [a3, b3], [a4, b4], [a5, b5],
        [a6, b6], [a7, b7], [a8, b8], [a9, b9], [a10, b10]
    ]

    plane = Plane(sits)
    plane.promptUser()





