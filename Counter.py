#the counter bit
import json
class Count:
    
    #number setter
        number = 0 #considering moving this one


        def basic_menu(): #basic menu for the counting
            print("")
            print("add")
            print("")
            print("subtract")
            print("")
            print("close")
            print("")

        def number_menu():#load and start menu
             print("")
             print("1. transfer a count")
             print("")
             print("2. Start a new")
             print("")
        
        def save_quit():#save menu
            print("")
            print("1. save and quit")
            print("")
            print("2. don't save")
            print("")

        while True: #this is the counting bit
            number_menu()
            counting_select = input("What would you like to do? ")#loads and starts new counts
            
            if counting_select == "1": #user can insert specific numbers if they're transfering from else here
                 input_number = int(input("please input your starting number. "))#made the input number a diffrent variable so that it can't mix up numbers

                 basic_menu()
                 while True:
                    print(input_number) 
                    up_or_down = input("what would you like to do? ")
                    if up_or_down == "add":
                        input_number +=1
                        print(input_number)
                        basic_menu()
                    elif up_or_down == "subtract":
                        input_number -=1
                        print(input_number)
                        basic_menu()
                
                    if input_number < 0: #prevents the count to go under 0
                        raise ValueError("count cannot be under 0")
        
                    def to_dict(input_number):
                         return {'amount': input_number}
            
            elif counting_select == "2":#new count starting
                 basic_menu()
                 while True:
                    print(number)    
                    up_or_down = input("what would you like to do? ")
                    if up_or_down == "add":
                        number +=1
                        print(number)
                        basic_menu()
                    elif up_or_down == "subtract":
                        number -=1
                        print(number)
                        basic_menu()
                
                    if number < 0: 
                        raise ValueError("count cannot be under 0")
                    elif up_or_down == "close":
                        save_quit()
                        saving = input("what do you want to do? ")
                        if saving == "1":
                            print(json.dumps(number))
                            
                           
                            break
                        elif saving == "2":
                            print("thank you for using this today")
                            break
            

