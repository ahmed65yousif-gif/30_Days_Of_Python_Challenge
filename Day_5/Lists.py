# 💻 Exercises: Day 5
### Exercises: Level 1
#1. Declare an empty list
problems = list() # I hope so.

#2. Declare a list with more than 5 items.

friends = ['Mohammed', 'Asaad', 'Jabra', 'Adem', 'Musa', 'Murad']

#3. Find the length of your list
length = len(friends)
print(f'The length of my list is: {length}')

#4. Get the first item, the middle item and the last item of the list

print(f'the first item in friends is: {friends[0]}')
print(f'the middle item in friends is: {friends[ (len(friends)-1)//2: len(friends)//2 +1  ]}') 
print(f'the last item in friends is: {friends[-1]}')

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["Ahmed", 30, 1.6, "single", "Sennar-Elizaez"]

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7. Print the list using _print()_

print(it_companies)

#8. Print the number of companies in the list

print("the number of companies is: ",len(it_companies))

#9. Print the first, middle and last company:

first = it_companies[0 ]
last =  it_companies[-1]
middle = it_companies[(len(it_companies)-1)//2:len(it_companies)//2 + 1]

print("the first company is :",first)
print('the middle countries are :',middle)
print("the last country is :",last)

#10. Print the list after modifying one of the companies

it_companies[5] = "Nokia" # modifying
print(it_companies)

#11. Add an IT company to it_companies

it_companies.append("Samsung")
print(it_companies)

#12. Insert an IT company in the middle of the companies list

middle=(len(it_companies)+1)//2
it_companies.insert(middle,"Hawwi")
print(it_companies)

#13. Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[0]=it_companies[0].upper()
print(it_companies)

#14. Join the it_companies with a string '#;  '

result = '#; '.join(it_companies)
print(result)

# Facebook#; Google#; Microsoft#; Apple#; IBM
#15. Check if a certain company exists in the it_companies list.

test = "Tesla" in it_companies
print("Tesla is in companies, True or False?",test)
   
#16. Sort the list using sort() method

it_companies.sort()
print("The companies after sorting is:",it_companies)

#17. Reverse the list in descending order using reverse() method
#companies.sort()

it_companies.sort(reverse=True)
print("The companies in descending order is:",it_companies)

#18. Slice out the first 3 companies from the list

items = it_companies[:3]
print(items)

#19. Slice out the last 3 companies from the list

print(it_companies[-3:])

#20. Slice out the middle IT company or companies from the list

start = (len(it_companies) - 1) // 2
end = len(it_companies) // 2 + 1
middle_companies = it_companies[start:end]
print("the middle companies: ",middle_companies)

# Facebook#; Google#; Microsoft#; Apple#; IBM

#21. Remove the first IT company from the list

it_companies.pop(0)
print(it_companies)

#22. Remove the middle IT company or companies from the list

start = (len(it_companies) - 1) // 2
end = len(it_companies) // 2 + 1
del it_companies[start:end]
print(it_companies)

#23. Remove the last IT company from the list

it_companies.pop()
print(it_companies)

#24. Remove all IT companies from the list

it_companies.clear()
print(it_companies)

#25. Destroy the IT companies list

del it_companies
# If I try to print the list it_companies, O will get Error.

#26. Join the following lists:
#```py
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
#```
front_end.extend(back_end)
print(front_end)

#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

full_stack = front_end[::]
print('Full stack is:',full_stack)

### Exercises: Level 2

#1. The following is a list of 10 students ages:

#```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#```

#- Sort the list and find the min and max age

#sort it in descending order:
ages.sort()
max , min = ages[-1] , ages[0]
print(f"the max item is {max} and the min item is {min}")

#- Add the min age and the max age again to the list

min_and_max = min + max 
ages.append(min_and_max)
print(ages)

#- Find the median age (one middle item or two middle items divided by two)
#sorted_ages = sorted(ages)

median = ages[(len(ages)-1)//2 : len(ages)//2 + 1 ]
print(f'the median age is: {median}')

#- Find the average age (sum of all items divided by their number )

sum_items = sum(ages)
average = sum_items / len(ages)
print(f'the average of ages is: {average:.2f}')

#- Find the range of the ages (max minus min)

print(f'the range of ages is: {max - min}')

#- Compare the value of (min - average) and (max - average), use _abs()_ method
#I got the average , mim and max earlier, so:

diff_min = abs(min - average)
diff_max = abs(max - average)
print("the diff_min is: %.2f "%(diff_min))
print("the diff_max is: %.2f "%(diff_max))

#1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
# let 
countries = ['Sudan', 'Egypt' , 'Oman' , 'Yemen' , 'Finland' , 'Qatar' , 'Bahrain' , 'Iran' , 'Saudi Arabia']
middle = countries[(len(countries)-1)//2 : len(countries)//2 + 1]
print('the middle country is:',middle)

#1. Divide the countries list into two equal lists if it is even if not one more country for the first half.

half = (len(countries) + 1) // 2
first_half = countries[ : half ]
second_half = countries[half : ]

print(f'the first half is: {first_half} and the second half is: {second_half}')

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'] #Unpack the first three countries and the rest as scandic countries.

first, second, third , *rest = countries
print(f'the first conutry is: {first}')
print(f'the second country is: {second}')
print(f'the third country is: {third}')
print(f'the rest is: {rest}')

#🎉 CONGRATULATIONS ! 🎉
