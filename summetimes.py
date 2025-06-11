Temperature = int(input("Hello! What is the temperature right now? Please only give the number! "))

if Temperature>40 or Temperature<5:
    print("You should stay inside!")
elif Temperature>20:
    print("Have some fun outside! It's good weather!")
else:
    print("Enjoy your day!")