#the counter bit

class Count:
    #number setter
    number = 0

    print(number)

    def basic_menu(): #basic menu for the counting
        print("")
        print("add")
        print("")
        print("subtract")
        print("")

    while True: #this is the counting bit
        basic_menu()
        while True:    
            up_or_down = input("what would you like to do? ")
            if up_or_down == "add":
                number +=1
                print(number)
                basic_menu()
            elif up_or_down == "subtract":
                number -=1
                print(number)
                basic_menu()
