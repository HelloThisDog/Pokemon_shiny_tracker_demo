#the counter bit
class Count:
    number = 0

    print(number)

    def basic_menu():
        print("")
        print("add")
        print("")
        print("subtract")
        print("")

    counting = True
    while counting == True:
        basic_menu()
        while True:    
            up_or_down = input("add or subtract? ")
            if up_or_down == "add":
                number +=1
                print(number)
                basic_menu()
            elif up_or_down == "subtract":
                number -=1
                print(number)
                basic_menu()

