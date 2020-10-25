#variable decelaration 

# name = "Daniel"
# age = "100"
# num = "24"

# name,age,num = "Daniel", 7 , 34
# print ("my name is ",name,"and i am ",age, " years old and my number is ",num)

#useing the input function
#get_name = input('what is your name?')

#get name
# print("what is your name", get_name)
#logical condition
# print(5 == 5 and 10 == 11)
# print(5 == 5 and 10 == 10)
# print(5 == 6 and 10 == 11)
# print(5 == 5 or 10 == 11)
# print(5 == 5 or 10 == 10)
# print(5 == 6 or 10 == 11)
#conditional operator
# name = "daniel"
# print("False !" if name != "daniel" else "True")

# name = "daniel"
# print("False !" if name != "Lawson" else "True")
#LIST
# players = ['Daniel','Messi','Ronaldo',1]
# print(players[3]) 
# mixed =["h1",[1,2,3],False]
# print(mixed[1])
# print(mixed[1]) 
name =input("What is my name ")
if name == "":
    print("please enter my Name.")
else:
    if name == "Daniel": 
        print("You are correct. \n My name is ",name)
    else:
        print("Wrong my name is not",name," Try again")  
        name =input("What is my name ")
        while name != "Daniel":
            print("Wrong my name is not",name," Try again")  
            name =input("What is my name ")   
        else:
            print("You are correct. \n My name is ",name)

  