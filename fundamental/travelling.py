distance=int(input("How far would you like to travel in miles?"))
if distance<3:
     print("\nI suggest Bicycle to your destination")
elif distance>=3 and distance<300:
    print("\nI suggest Motor-Cycle to your destination")
else:
     print("\nI suggest Supper-Car to your destination")
