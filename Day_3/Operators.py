#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@  WELCOME TO THE DAY 3  @@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 


#Great,I reached the day 3, thank Allah.

#☆ Here are some important information that I liked the share with you, friends:
#    ___________________________________________________________________________________________
#    = is not ==
#    T for True and F for F
#    ___________________________________________________________________________________________
 
#☆☆ Let us to do the exercises for the day 3:

## 💻 Exercises - Day 3

#1. Declare your age as integer variable:
my_age = 30
#2. Declare your height as a float variable:
my_hight = 1.50 
#3. Declare a variable that store a complex number:
value_one = 1 - 6j
#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h):
"""
```py
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
```
"""
print("we wanna calculate the area of your triangle:")
base= input('Enter the base:')
int_base = int(base)
height = input('Enter the height:')
int_height = int(height)
area = 0.5 * int_height * int_base
print("The area of triangle is",area)

print("\n"+"*"*45,"\n")

#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
"""
```py
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
```
"""
print('We are going to calculate the perimeter of the traingle:')
side_a = input("Enter side a:")
side_a_int = int(side_a)
side_b = input("Enter side b:")
side_b_int = int(side_b)
side_c = input('Enter side c:')
side_c_int = int(side_c)
perimeter=(side_a_int + side_b_int + side_c_int)
print('The perimeter of the triangle is',perimeter)

print("\n"+"*"*45,"\n")

#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width)):
 
print("Now, we want to calculate the width and perimeter of a rectangle:")   
length = int(input("Enter the length:"))
width = int(input("Enter the width:"))
area = length * width
perimeter = 2*( length + width)
print("The area is",area)
print("The perimeter",perimeter)
 
print("\n"+"*"*45,"\n")

#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14:
print("we are going to calculate the area of a circle ")
radius = int(input("Enter the radius:"))
pi=3.14
area = pi * radius**2
circumference = 2* pi * radius
print("The area is",area)
print("The circumference",circumference)

print("\n"+"*"*45,"\n")

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2:

#For the equation y = 2x - 2 compared with y = mx + b:
# I deduce the following:
m,x,y = str(2) , str(1) , str(-2)
slope1= str(x)
print("Here are the slope, x-intercept and y-intercept for (y=2x - 2):")        
print('The slope is:',slope1)
print('x-intercept is:'+'(x,'+'0'+')')
print('y-intercept is:'+'('+'0'+','+y+')')

print("\n"+"*"*45,"\n")

#9. Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) between point 
#   (2, 2) and point (6,10) :
#     solution
y1 , y2 , x1 , x2 = 2 , 10 , 2 , 6 
slope2 = (y2 - y1) / (x2 - x1)
Euc_dist = ( ((y1 - y2)**2) + ((x1 - x2 )**2 ))**2
print("The slope is:",slope2)
print('The Euclidean distance between (2, 2) and (6, 10) is:',Euc_dist)

print("\n"+"*"*45,"\n")

#10. Compare the slopes in tasks 8 and 9.
slope1= float(slope1)
print('Does slope1 less than slope2?', slope1 < slope2 )
print('Does slope1 greater than slope2?', slope1 > slope2 )
print('Does slope1 equal to slope2?', slope1 == slope2 )

print("\n"+"*"*45,"\n")

#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

print('I am going to try x= (1, 2, 3, -1, -2,-3)')
print('when x = 1')
x=1
print('y=(1)^2 + 6*(1)+9',"y=",(1)**2 + (6*1) + 9) #
print("when x = -1")
x=-1
print('y=(-1)^2 + 6*(-1) + 9',"y=",(-1)**2 + (6*-1) + 9) #
print("when x = 2")
x=2
print('y=(2)^2 + 6*(2) + 9',"y=",(2)**2 + (6*2) + 9)     #
print("when x = -2")
x=-2
print('y=(-2)^2 + 6*(-2)+9',"y=",(-2)**2 + (6*-2) + 9)   #
print("when x = 3")
x=3
print('y=(3)^2 + 6*(3)+9',"y=",(3)**2 + (6*3) + 9)       #
print("when x = -1")
x=-3
print('y=(-3)^2 + 6*(-3) + 9',"y=",(-3)**2 + 6*(-3) + 9) #     
print("y=0 when x = -3")

print("\n"+"*"*45,"\n")

#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement:
#     Great question..
     
#     >first, I will calcutate the length of both words:
length_python = len("python")
length_dragon = len("dragon")
#     >now, I am going to compare them and get an falsy comarison statement:
#       >I will get any Truthy comarison statement, then I'll use 'not' to reverse it:
        
#first  ==> length_python == length_dragon 
length_python == length_dragon       # True
print("length_python == length_dragon",length_python == length_dragon)
#then:
not(length_python) == (length_dragon)# False
print("length_python not equal to length_dragon",not(length_python) == (length_dragon)  )         

#Another solution:
     
    #using **!=** operator directly, because they are actually equal.
print(length_python != length_dragon) # False

print("\n"+"*"*45,"\n")

#13. Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
    
checking="on" in "python" and "on" in "dragon"
print("'on' in 'python' and 'on' in 'dragon'==> ",checking)

print("\n"+"*"*45,"\n")

#14. _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence:
test= "jargon" in "I hope this course is not full of jargon"
print('"Jargon" is in "I hope this course is not full of jargon"',test )

print("\n"+"*"*45,"\n")

#15. There is no 'on' in both dragon and python:

test= "on" not in "python" and "on" not in "dragon"  # False
print('There is no "on" in both dragon and python ==>',test)

print("\n"+"*"*45,"\n")
    
#16. Find the length of the text _python_ and convert the value to float and convert it to string:
#    Interesting question:
#    > Let's get the length first:
my_word = 'python'
length_my_word = len(my_word)
#    > Now it's time for converting from int to float and then to str:
float_length_my_word = float(length_my_word) 
print('float_length_my_word is:',float_length_my_word) # 6.0
str_length_my_word = str(float_length_my_word)
print("str_length_my_word is",str_length_my_word)

print("\n"+"*"*45,"\n")

      
#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?:
#    Okay:
     
#     I use the modulus to get the remainder from (number % 2), then use '==' operator to see if the remainder is equal to zero.
#     if the result is True, that means the number is Enven, else it's odd:
print("Do you want to check if a number is Even or not?")
number= input('Then, Enter a number:')
int_number= int(number)
remainder = int_number % 2
print('Is the number Even?',remainder == 0) # True or False
#           "I can use **if** but it is too early to that" I like to go step by step.

print("\n"+"*"*45,"\n")
           
#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7:

#first, I will convert 2.7 to integer:
conv_val = int(2.7)
#The floor division is:
floor_div = 7 // 3
#Lastly the checking:
checking = floor_div == conv_val 
print('floor_div == conv_val ==>',checking)

print("\n"+"*"*45,"\n")

#19. Check if type of '10' is equal to type of 10:

check= type('10') == type(10)
print('"10" is equal to type of 10 ==> "',check)

print("\n"+"*"*45,"\n")
     
#20. Check if int('9.8') is equal to 10:
# To conver '9.8' to int , first I need to convert it to float , then to int:

check = int(float('9.8')) ==  10
print("int('9.8') is equal to 10 ==>",check)

print("\n"+"*"*45,"\n")
     
#21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

"""py
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
"""
#The solution is:
hours = int (input("Enter hours: "))
rate_per_hour = int ( input("Enter rate per hour: "))
print('Your weekly earning is',hours * rate_per_hour)

print("\n"+"*"*45,"\n")

#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

""" py
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
"""
#     The solution is:
num_yrs = int ( input("Enter number of years you have lived: "))
print('You have lived for',num_yrs * 365 * 24 * 60 * 60,'seconds.')

print("\n"+"*"*45,"\n")

#23. Write a Python script that displays the following table:

"""py
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
#    The solution is:

n,x, y , z, h, i =0, 1, 2, 3, 4, 5

print(x, x**n , x**x , x**y , x**z)
print(y, y**n , y**x , y**y , y**z)
print(z, z**n , z**x , z**y , z**z)
print(h, h**n , h**x , h**y , h**z)
print(i, i**n , i**x , i**y , i**z)    

print("\n"+"*"*45,"\n")

print("**That's ALL for TODAY**")

print("\n"+"*"*45,"\n")

print('Conclusion:')
print('  It was hard but exciting and hulpfull.')
   
print('   October 31, 2026')
print('   11:53 pm')
