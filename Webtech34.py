print("===== WEATHER PREDICTION =====")

weather = (1, 0, 1, 1, 0, 1, 1)

days = ("Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday")

sunny = 0
rainy = 0

for i in range(len(weather)):
    if weather[i] == 0:
        rainy += 1
        print(days[i], "- Rainy")
    else:
        sunny += 1
        print(days[i], "- Sunny")

print("\nSunny Days:", sunny)
print("Rainy Days:", rainy)

if sunny > rainy:
    print("Good weather!")
else:
    print("Bad weather!")
    
    