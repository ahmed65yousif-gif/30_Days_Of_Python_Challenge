#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@  WELCOME TO THE DAY 2  @@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 

'''
Waw,I reached the day 2, thank Allah.

☆ Here are some important information that I liked the share with you, friends:
    ___________________________________________________________________________________________
      @ Assigning means storing data in a variable.                                            ♧                                         
      @ Declaration a variable is to assign a certain data type to it.                         ♧
      @ Casting is to convert one data type to another type.                                   ♧
      @ When it comes to converting between data types, must convert a string to float first,  ♧
        and then to int in case you want to convert from str to imt.                           ♧
    ___________________________________________________________________________________________
 '''   
#☆☆ Let us to do the exercises for the day 2;
 
#--------------------------------------------------
#---------------LEVEL ONE--------------------------
#--------------------------------------------------

#1. was practical....

#2.Writing a python comment saying 'Day 2: 30 Days of python programming':

     #Day 2: 30 Days of python programming         # I used a hash symbol.
    
#3.Declare a first name variable and assign a value to it:

first_name = 'Ahmed'
    
#4. Declare a last name variable and assign a value to it:

last_name = 'Yousif Hissain'
    
#5. Declare a full name variable and assign a value to it:

full_name = first_name + ' ' + last_name
    
#6. Declare a country variable and assign a value to it:

country = 'Sudan'  #A creat country in north Africa.
    
#7. Declare a city variable and assign a value to it:

city = 'Sennar'    #A great and histrical twon.
    
#8. Declare an age variable and assign a value to it:

age = 30
    
#9. Declare a year variable and assign a value to it:

year = 2026      #when I am studying now October 30, 2026.
    
#10. Declare a variable is_married and assign a value to it:

is_married = False   # I hope that I am married
    
#11. Declare a variable is_true and assign a value to it:

is_true = True
    
#12. Declare a variable is_light_on and assign a value to it:

is_light_on = True    # I love lights and hate the darkness.
    
#13. Declare multiple variable on one line:    

country, job , is_true, favorite_fruit = 'Sudan', 'teacher', False , ['orage', 'mangoes', 'banana']
    


#--------------------------------------------------
#--------------- LEVEL TWO -------------------------
#--------------------------------------------------

#1. Check the data type of all your variables using type() built-in function:

print('type(first_name)',type( first_name ))
print('type(last_name)',type( last_name))
print('type(full_name)',type( full_name ))
print('type(country)',type( country ))
print('type(age)',type( age ))
print('type( is_married )',type( is_married ))
print('type( year )',type( year ))
print('type(city)',type( city ))
print('type(is_true)',type( is_true ))
print('type(is_light_on)',type( is_light_on ))
print('type(job)',type(job))
print('type(favorite)',type(favorite_fruit))
    
#2. Using the _len()_ built-in function, find the length of your first name:

print('len( first_name)',len( first_name))
    
#3. Compare the length of your first name and your last name:

print("first_name > last_name", len(first_name) > len(last_name)   )   # False
print("first_name == last_name", len(first_name) == len( last_name))   # False
print("first_name < last_name", len(first_name) == len(last_name)  )   # True
    
#4. Declare 5 as num_one and 4 as num_two:
   
num_1 = 5
num_2 = 4
   
#5. Add num_one and num_two and assign the value to a variable total:

total = num_1 + num_2
   
#6. Subtract num_two from num_one and assign the value to a variable diff:

diff = num_1 - num_2
   
#7. Multiply num_two and num_one and assign the value to a variable product:
    
product = num_1 * num_2
    
#8. Divide num_one by num_two and assign the value to a variable division:
   
division = num_1 / num_2
   
#9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder:

remainder = num_2 % num_1
   
#10. Calculate num_one to the power of num_two and assign the value to a variable exp;
  
exp = num_1 ** num_2
   
#11. Find floor division of num_one by num_two and assign the value to a variable floor_division:

floor_division = num_1 // num_2
   
#12. The radius of a circle is 30 meters:
    #1. Calculate the area of a circle and assign the value to a variable name of _area_of_circle_:
         
pi = 3.14     # 22/7 .
radius = 30   # Given.
area_of_circle = pi * (radius) ** 2   # Mathematical formula to calculate a circle's area.
print('The area is : ', area_of_circle,'cm^2')  # to show the result on the screen.
        
    #2. Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_:
       
pi = 3.14  # 22/7 .
radius= 30 # Given.
circum_of_circle = 2 * pi * radius  # A mathematical formula to calculate the circumference of a circle.
print('The circumference is:',circum_of_circle,'cm')
        
    #3. Take radius as user input and calculate the area:
    
radius = input("Enter the radius, please:")
radius_int = int(radius)
area= 3.14 * radius_int ** 2
print("The area is:",area)
        
#13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names:
       
first_name = input('What is your first name?')
last_name = input('What is your last name, please?')
country= input('What is your country?')
age = input("How old are you?")
        
#14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords:

help('keywords')
   
   #The result that I have gotten is:
"""
   Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not

None
"""
