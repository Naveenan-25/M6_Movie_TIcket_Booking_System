import random

global f
f = 0
A = 'y'
B = 0


def t_movie():
    
    global f
    f = f \
        + 1
    
    print("**********************************")
    print("***********  MOVIES  ************")
    print("**********************************")
    print("which movie do you want to watch?")
    file = open('Movies.txt', "r")
    content = file.readlines()
    print(content)
    print("11.FOOD")
    print("12.BILL")
    print("13.CANCEL")
    print("14.BACK")

    movie = int(input("choose your movie: "))

    if movie == 1:
        
        print("you have selected BEAST")
        print("you have to select the Screen in the theatre")
        
    elif movie == 2:
        
        print("you have selected RRR")
        print("you have to select the Screen in the theatre")
        
    elif movie == 3:
        
        print("you have selected KGF 2")
        print("you have to select the Screen in the theatre")
        
    elif movie == 4:
        
        print("you have selected Doctor Strange 2")
        print("you have to select the Screen in the theatre")
        
    elif movie == 5:
        
        print("you have selected Thor Love and Thunder")
        print("you have to select the Screen in the theatre")
        
    elif movie == 6:
        
        print("you have selected Black Adam")
        print("you have to select the Screen in the theatre")
        
    elif movie == 7:
        
        print("you have selected SPIDER-MAN ACROSS THE SPIDER VERSE")
        print("you have to select the Screen in the theatre")
        
    elif movie == 8:
        
        print("you have selected BLACK PANTHER 2")
        print("you have to select the Screen in the theatre")
        
    elif movie == 9:
        
        print("you have selected THE MARVELS")
        print("you have to select the Screen in the theatre")
        
    elif movie == 10:
        
        print("you have selected THE FLASH")
        print("you have to select the Screen in the theatre")

    elif movie == 11:
        food()

    elif movie == 12:
        
        print("**********************************")
        print("************ Payment *************")
        print("**********************************")
        D = int(input("The total ticket cost is: "))
        B = int(input("The total Food cost is: "))
        Amount = D + B
        print("The total price is", Amount)
        exit()

    elif movie == 13:
        
        C='a'

        print("**********************************")
        print("************ Cancel **************")
        print("**********************************")
        while (C == 'a'):
            
           Q = input("Did you want to cancel your ticket(y/n)?: ")
           
           if(Q == 'n'):
               
               print("Your ticket has been canceled!!!!!!")
               print("Your fair will be refunded shortly!!!!")
               print("Thank you.....")
               print("Have a nice day.......")
               
           else:
               
               print("invalid choice.....")
               print("return to main menu........")
               Theatre()

    elif movie == 14:
        
        Theatre()
        Screen()
        return 0

    if f == 1:
        Screen()


def Screen():
    
    C = 200

    print("**********************************")
    print("***********  SCREENS  ***********")
    print("**********************************")
    print("which screen do you want to watch movie:")
    print("1.SCREEN 1")
    print("2.SCREEN 2")
    print("3.SCREEN 3")
    print("**********************************")

    a = int(input("choose your screen: "))
    ticket = int(input("number of ticket do you want?: "))
    D = C * ticket
    print("Total cost of the ticket is: ", D)
    timing(a)


def timing(a):
    
    time1 = {
        "1": "10.00-1.00",
        "2": "1.10-4.10",
        "3": "4.20-7.20",
        "4": "7.30-10.30"
    }
    time2 = {
        "1": "10.15-1.15",
        "2": "1.25-4.25",
        "3": "4.35-7.35",
        "4": "7.45-10.45"
    }
    time3 = {
        "1": "10.30-1.30",
        "2": "1.40-4.40",
        "3": "4.50-7.50",
        "4": "8.00-10.45"
    }
    if a == 1:
        
        print("choose your time:")
        print(time1)
        t = input("select your time:")
        x = time1[t]
        print("your ticket has been booked successfully!!")
        print("Enjoy movie at " + x)
        print("Have a nice day")
        
    elif a == 2:
        
        print("choose your time:")
        print(time2)
        t = input("select your time:")
        x = time2[t]
        print("your ticket has been booked successfully!!")
        print("Enjoy movie at " + x)
        print("Have a nice day")
        
    elif a == 3:
        
        print("choose your time:")
        print(time3)
        t = input("select your time:")
        x = time3[t]
        print("your ticket has been booked successfully!!")
        print("Enjoy movie at " + x)
        print("Have a nice day")

    return 0


def movie(Screen):
    
    if Screen == 1:
        t_movie()
    elif Screen == 2:
        t_movie()
    elif Screen == 3:
        t_movie()
    elif Screen == 4:
        city()
    else:
        print("wrong choice")


def Theatre():
    
    print("**********************************")
    print("***********  THEATRES  ***********")
    print("**********************************")
    print("Please enter the Theatre name.....")
    print("Famous theatres are listed below!!")
    file = open('theatres.txt', "r")
    content = file.readlines()
    print(content)
    print("**********************************")
    a = int(input("choose your option: "))
    movie(a)
    return 0

def food():
    
    print("**********************************")
    print("*************  FOOD  *************")
    print("**********************************")
    print("\t\t\tMenu\n1.vegetarian\n2.Non-vegetarian")
    A = 'y'
    B = 0
    while (A == 'y'):
        
        A1 = int(input("please Enter your Choice (1,2): "))
        if (A1 == 1):
            
            print("Welcome to vegetarian menu")
            print("1.veg puff Rs.60\n2.veg burger Rs.80\n3.ved pizza Rs.100\n4.fresh juice Rs.90\n5.popcorn Rs.180")
            A11 = int(input("Enter your choice(1,2,3,4,5): "))
            if (A11 == 1):
                
                print("you have selected veg puff")
                B += 60
                A = input("order again(y/n)?: ")
                print("your Bill is:", B)
                print("Thank you and visit again")
                
            elif (A11 == 2):
                
                print("you have selected veg burger")
                B += 80
                A = input("order again(y/n)?: ")
                print("your Bill is:", B)
                print("Thank you and visit again")
                
            elif (A11 == 3):
                
                print("you have selected veg pizza")
                B += 100
                A = input("order again(y/n)?: ")
                print("your Bill is:", B)
                print("Thank you and visit again")
                
            elif (A11 == 4):
                
                print("you have selected fresh juice")
                B += 90
                A = input("order again(y/n)?: ")
                print("your Bill is:", B)
                print("Thank you and visit again")
                
            elif (A11 == 5):
                
                print("you have selected Popcorn")
                B += 180
                A = input("order again(y/n)?: ")
                print("your Bill is:", B)
                print("Thank you and visit again")
                
            else:
                
                print("Invalid option")
                
        elif (A1 == 2):
            
            print("Welcome to Non-vegetarian Menu")
            print("1.Chicken burger Rs.250\n2.Chicken pizza Rs.200\n3.Chicken Puffs Rs.150\n4.Chicken roll Rs.120")
            A12 = int(input("please select an option(1,2,3,4): "))
            
            if (A12 == 1):
                
                print("you have selected Chicken burger")
                B += 250
                A = input("order again(y/n)?: ")
                print("your Bill is:", B)
                print("Thank you and visit again")
                
            elif (A12 == 2):
                
                print("you have selected Chicken pizza")
                B += 200
                A = input("order again(y/n)?: ")
                print("your Bill is:", B)
                print("Thank you and visit again")
                
            elif (A12 == 3):
                
                print("you have selected Chicken Puffs")
                B += 150
                A = input("order again(y/n)?: ")
                print("your Bill is:", B)
                print("Thank you and visit again")
                
            elif (A12 == 4):
                
                print("you have selected Chicken roll")
                B += 120
                A = input("order again(y/n)?: ")
                print("your Bill is:", B)
                print("Thank you and visit again")
                
            else:
                
                print("Invalid option")


def city():


    print("**************************************************")
    print("**   WELCOME TO MOVIE TICKET BOOKING SYSTEM   **")
    print("**************************************************")
    print("Please enter the location to watch the movie:")
    file = open('place.txt', "r")
    content = file.readlines()
    print(content)
    print("**************************************************")


    place = int(input("choose your option: "))
    
    if place == 1:
        
        print("you have selected Chennai")
        print("you have to select the theatres in the location")
        Theatre()
        
    elif place == 2:
        
        print("you have selected Coimbatore")
        print("you have to select the theatres in the location")
        Theatre()
        
    elif place == 3:
        
        print("you have selected Erode")
        print("you have to select the theatres in the location")
        Theatre()
        
    elif place == 4:
        print("you have selected Namakkal")
        print("you have to select the theatres in the location")
        Theatre()
 
 
    elif place == 5:
        
        print("you have selected madurai")
        print("you have to select the theatres in the location")
        Theatre()
        
    elif place == 6:
        
        print("you have selected tirunelveli")
        print("you have to select the theatres in the location")
        Theatre()
        
    elif place == 7:
        
        print("you have selected karur")
        print("you have to select the theatres in the location")
        Theatre()
        
    elif place == 8:
        
        print("you have selected tanjore")
        print("you have to select the theatres in the location")
        Theatre()
        
    elif place == 9:
        
        print("you have selected kannyakumari")
        print("you have to select the theatres in the location")
        Theatre()
        
    elif place == 10:
        
        print("you have selected salem")
        print("you have to select the theatres in the location")
        Theatre()
        
    else:
        
        print("wrong choice")

city()

