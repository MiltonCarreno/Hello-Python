def menu():
    menu_options = "1. Tacos\n2. Burritos\n3. Nachos\n4. Quesadillas\n5. Quit"
    print(menu_options)

def get_selection_price():
    price = 0
    if client_choice == 1:
        price = 3.5
    elif client_choice == 2:
        price = 5
    elif client_choice == 3:
        price = 2.5
    else:
        price = 3
    return price

print("Please view the menu below and enter the number that represents your selection.")
print("Welcome to Taco Palace!")
total_order = 0
menu()
client_choice = int(input())
order_list = []

while client_choice != 5:
    if client_choice == 4:
        order_list.append("Tacos")
        print("You have selected Tacos")
    elif client_choice == 3:
        order_list.append("Burritos")
        print("You have selected Burritos")
    elif client_choice == 2:
        order_list.append("Nachos")
        print("You have selected Nachos")
    else:
        order_list.append("Quesadillas")
        print("you have selected Quesadillas")

    total_order += get_selection_price()

    menu()
    client_choice = int(input())

print("\n\nYou ordered: ")
for item in order_list:
    print("\tan order of " + item)

print("Your total is $" + str(total_order))


