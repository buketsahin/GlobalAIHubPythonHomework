Name=input("Please,enter your name:")
Surname=input("Please,enter your surname:")
Age=int(input("Please,enter your age:"))
Birthyear=input("Please,enter your birth year:")
x=[Name,Surname,Age,Birthyear]
for i in x:
    print(i)
if Age<18:
    print("You can't go out because it's too dangerous.")
else:
    print("You can go out to street.")