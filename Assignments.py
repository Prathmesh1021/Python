#Q1 Accept two numbers and print the greatest between them
a=12
b=14

if a<b:
    print("b is greater than a")
else:
    print("a is greater than b ")
    
#Question2 ==>Accept two numbers from user and print the greatest number    

num1=int(input("Enter The First Number"))
num2=int(input("Enter The Second Number"))

if num1>num2:
     print(f"{num1} is the greater than {num2}")
else:
     print(f"{num2} is the greater than {num1}")
    

    
#Q3 Accept The Gender From User as character and print the respective greeting meassage (EX:-Good Morning Sir/Madam)
gender=str(input("Enter your Gender :"))

if gender =="Male" or gender=="male " :
     print("Good Morning sir")
elif gender =="Female" or gender =="female ":
     print("Good Morning Madam")
else:
     print("Good morning")
     
#Q4 Accept an integer and check whether it is even or odd number
num=int(input("Enter The Number :"))    
if num%2==0:
     print(f"{num} is Even Number") 
else:
     print(f"{num} is Odd Number")  
    
#Q5 Accept name and age from user.Cheack if the user is a valid voter or not?EX->Hello Rahul you are a valid voter  

name=str(input("Enter Your Name:"))
age=int(input("Enter Your Age :"))

if age>=18:
     print(f"Hello {name} you are a valid voter")
else:
     print(f"Hello {name} you are not a valid voter")
     
#Question 6==>Accept a year from user and check whether it is a leap year or not?
year=int(input("Enter The Year ="))

if year%400==0 or year % 4 == 0 and year%100!=0:
     print("Leap Year ")
else:
     print("Not a Leap year")

#Question 7==> You cna also create if elif ladder using multiple conditions of elif For understanding solve this question take the input of temperature in celsius.
# Below 0°C → "Freezing Cold 11
#0°C to 10°C → "Very Cold
#10°C to 20°C → "Cold 11
#20°C to 30°C "Pleasant
#30°C to 40°C → "Hot
#Above 40°C → "Very Hot

temp=int(input("Enter Temperature : "))

if temp< 0 :
   print("Freezing Cool")
elif temp>0 and temp<10:
   print("Very Cool")
elif temp>10 and temp<20:
   print("Cold")
elif temp>20 and temp<30:
   print("Pleasant")
elif temp>30 and temp<40:
   print("Hot")
elif temp >40:
   print("Very Hot")
else:
    print(" warning!!! Please Enter the Temparature ")