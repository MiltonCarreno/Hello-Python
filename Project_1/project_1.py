print("For each day, enter the rain and wind data, separated by a space\n"
      "For 0.2 inches of rain and winds with speeds of 25 mph, enter '0.2 25'\n"
      "Once done, enter -1\n")
data = input()
days = 0
total_rain = 0
total_wind = 0

while data != "-1":
    data = data.split(" ")
    days += 1
    total_rain += float(data[0])
    total_wind += float(data[1])
    data = input()

print(f"The average rain is {total_rain/days:.1f} inches")
print(f"The average wind is {total_wind/days:.1f} mph")
print(f"The weather severity for these {days} readings is: {(total_rain/days * 10) + (total_wind/days):.1f}")