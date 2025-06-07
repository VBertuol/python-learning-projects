while True:
    while True:
        try:
            number = int(input("Enter a positive number or '0' to exit: "))
            if number >= 0:
                break
        except:
            print("invalid input, please enter a positive number or '0' to exit")
    if number == 0:
        break
    for i in range(1, number + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)