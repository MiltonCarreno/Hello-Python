kilowatts_hours = int(input("\nEnter the KW hours used: "))
price = 0

if kilowatts_hours <= 1000 and kilowatts_hours > 0:
    price = kilowatts_hours * 7.633 / 100
elif kilowatts_hours > 1000:
    price = 1000 * 7.633 / 100
    price = price + (((kilowatts_hours - 1000) * 9.259) / 100)

print(f"Amount owed is ${price}\n")