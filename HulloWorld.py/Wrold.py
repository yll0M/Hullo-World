import random
def displaynumber(number):
    print("Your number is "+str(number))


print ("Hullo World")
displaynumber(random.randint(1,9999))
displaynumber(input ("Type a random number"))
name=input ("What is your name?")
print ("Hello "+name)
response=input ("Type end to close or type joke for a joke")
while not response.lower()=="end":
    if response.lower()== "joke":
        print ("You")
    else:
        print ("Invalid input")
    response=input ("Type end to close or type joke for a joke")
