#1.Create Functions without parameters
def greetings():
     print("Welcome to the python course by Sourav Sharma")

#Call function
greetings()

#2.Create Function by add 2 Numbers using parameter
def add2numbers(a,b): #parameters (a,b)
     result = a + b
     print("The sum is: ", result)

#call Above sum function
add2numbers(5,3)  #arguments(5,3)

#3.Create Function by add 3 Numbers
def add3numbers(a,b,c): #parameters (a,b,c)
     result = a + b + c
     print("The sum is: ", result)

#call Above sum function
add3numbers(10,20,100) #arguments (10,20,100)


#4. function with return statement
def add2num(a,b):
     return a+b
     return a-b  #after return statement function end or will not be continuation.
sum2num = add2num(10,1)
print(sum2num) 

# Example for return statement :- why we use return statement?
#Function to convert celsius to Fahrenheit with use of return statement :-
def celsius_to_fahrenheit(celsius):
     fahrenheit = (celsius * 9/5) + 32
     return fahrenheit 
#call Function
temp_f = celsius_to_fahrenheit(25)
print(temp_f)
print("with return: ", type(temp_f))

#Function to convert celsius to Fahrenheit without use of return statement :-
def celsius_to_fahrenheit(celsius):
     fahrenheit = (celsius * 9/5) + 32
     print(fahrenheit)
#call Function
celsius_to_fahrenheit(25)
print("without return: ", type(celsius_to_fahrenheit(25)))

#Summary = return ka hum log is liye use karte hai kyuki uske result ka data type <float> me ho jata hai isliye hum usko kahi bhi use 
# kar sakte hai but jahape hum return ka use nahi karte hai vaha par us function ke result ka data type <none> show hota hai jisse hum 
# us value ko kabhi use ya fir consider nahi kar sakte is liye return ko use karna samjhadaari hai :) 
