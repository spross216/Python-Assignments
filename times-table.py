#-------------------------------------------------------------------------#
#       _____ _                          _____     _     _                #
#      |_   _(_)                        |_   _|   | |   | |               # 
#       | |  _ _ __ ___   ___  ___ ______| | __ _| |__ | | ___  ___       #
#       | | | | '_ ` _ \ / _ \/ __|______| |/ _` | '_ \| |/ _ \/ __|      #
#       | | | | | | | | |  __/\__ \      | | (_| | |_) | |  __/\__ \      #
#       \_/ |_|_| |_| |_|\___||___/      \_/\__,_|_.__/|_|\___||___/      #
#                                                                         #
#-------------------------------------------------------------------------#



# Below is a function that checks if user input is an integer

def integerTest(num):
    if num.isdigit():
        return
    else:
        num = input("Please enter a positive whole number. ")
        integerTest(num)



def queryAndCalculate():
    num = input('What number would you like to review? (enter 0 to exit) ')
    integerTest(num)
    if int(num) == 0:
        print('Thank you for using the calculator!')
        quit()
   


    minRange = input('Minimum calculated range: ')
    integerTest(minRange)
    maxRange = input('Maximum calculated range: ')
    integerTest(maxRange)
    if int(maxRange) - int(minRange) > 10:
        while int(maxRange) - int(minRange) > 10:
            maxRange = input('The range must not exceed a value 10. Please enter another maximum calculated range: ')
            integerTest(maxRange)
   


    while int(minRange) <= int(maxRange):
        print(num, ' x ',  minRange, ' = ', (int(num) * int(minRange)))
        minRange = int(minRange) + 1
        continue


    while num != 0:
        queryAndCalculate()

queryAndCalculate()


    
    

