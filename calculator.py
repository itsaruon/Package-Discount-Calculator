import random
import math

def discount():
    number = random.randint(1,150)
    cost = 25 * number
    package = 25
    
    if (number > 0) and (number < 10):
        total = cost
        print("Number of Packages: ", number)
        print("Discount Amount: 0 ")
        print ("Total Amount: ", total)
    elif (number >= 10) and (number <= 19):
        rate = .20
        discountAmount = rate * cost
        total = cost - discountAmount
        print("Number of Packages: ", number)
        print("Discount Amount: ", discountAmount)
        print ("Total Amount: ", total)
    elif (number >= 20) and (number <= 49):
        rate = .30
        discountAmount = rate * cost
        total = cost - discountAmount
        print("Number of Packages: ", number)
        print("Discount Amount: ", discountAmount)
        print ("Total Amount: ", total)
    elif (number>= 50) and (number <=99):
        rate = .40
        discountAmount = rate * cost
        total = cost - discountAmount
        print("Number of Packages: ", number)
        print("Discount Amount: ", discountAmount)
        print ("Total Amount: ", total)
    else:
        rate = .50
        discountAmount = rate * cost
        total = cost - discountAmount
        print("Number of Packages: ", number)
        print("Discount Amount: ", discountAmount)
        print ("Total Amount: ", total)

discount()
