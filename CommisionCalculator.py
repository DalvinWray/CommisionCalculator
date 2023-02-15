import csv
import os.path

salesPersonNumber=0
amountMadeFromSales=0
salesPersonClass=0
commision=0


#Function that will be used to collect the sales Person Information From The User
#then stores that information into variables
def salesPersonInfo():
    global salesPersonNumber
    global amountMadeFromSales
    global salesPersonClass
    
    salesPersonNumber=int(input("Please input the sales person number: "))
    amountMadeFromSales=int(input("Please input the amount made from sales: "))
    salesPersonClass=int(input("Please input the class the Sales Person Belongs: "))



#Function that calculates sales persons from class 1
def classOne():
    global commision
    if 1000>=amountMadeFromSales:
        commision=amountMadeFromSales*.06
    
    elif 2000 > amountMadeFromSales > 1000:
        commision=amountMadeFromSales*.07
    
    elif amountMadeFromSales>2000:
        commision=amountMadeFromSales*.1

    

#Function that calculates sales persons from class 2
def classTwo():
    global commision
    if 1000>amountMadeFromSales:
        commision=amountMadeFromSales*.04
    
    elif amountMadeFromSales>1000:
        commision=amountMadeFromSales*.06


#Function that calculates sales persons from class 3
def classThree():
    global commision
    commision= amountMadeFromSales * .045


#Function that prints a message to the user containing the sales Person's number and id
def commisionMessageFunc():
    commisionMessage="Sales person with an id of {} should recieve {} as commision"
    print(commisionMessage.format(salesPersonNumber,commision))


#Function that inputs the sales info into a csv file
#the program allows the user to name the csv file
#based on that file name the program will check to see if the file exists
#if the file exists the program will simply open the file and append the sales person info
#if it does not exist the program will createa new file, add headers to it and add the sales person info
def appendToCSV():
    info=[salesPersonNumber, salesPersonClass, amountMadeFromSales,  commision]
    title=["Sales Person Number","Sales Person Class", "Amount Made From Sales", "Commision"]
    fileName=input("Please input the file name you wish to use for your csv file: ")
    path= fileName+".csv"
    
    if(os.path.isfile(path)==True):
        with open(path,"a") as file:
            append = csv.writer(file)
            append.writerow(info)
            file.close()

    else:
        with open(path,"w") as file:
            write= csv.writer(file)
            write.writerow(title)
            write.writerow(info)
            file.close()

#While loop will keep running until the user decides to end it
#Using the sales person class that the user inputs, a respective fucntion call will be made to calculate their commision 
#and print a message contaning their id number and commision 
#also  the sales person info will be stored to a csv file

while True:


    salesPersonInfo()

    if salesPersonClass == 1:
        classOne()
        appendToCSV()
        commisionMessageFunc()
        
    elif salesPersonClass == 2:
        classTwo()
        appendToCSV()
        commisionMessageFunc()
        
    
    elif salesPersonClass == 3:
        classThree()
        appendToCSV()
        commisionMessageFunc()
        
    
    else:
        print("Invalid Class Please Try Again")
        salesPersonClass.type()
    
    continueCheck=int(input("Enter '1' if you wish to terminate this program, and press any other key to continue: "))
    
    if continueCheck==1:
        break
    


    

    

