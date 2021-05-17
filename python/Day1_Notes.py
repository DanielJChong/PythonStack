# # var_name = "Some value";
# # "=" this is NOT and equals, it means "set as"

# # Primitive

# some_string = "Some value"  # string
# some_number = 123  # integer
# some_decimal = 1.23  # floats
# some_boolean = True  # boolean
# some_boolean_2 = False  # boolean
# some_none = None  # None == null

# # Composite

# some_list = []  # Lists, NOT Arrays, in Python
# some_list.append(1)  # Adding something to the "List"; use instead of "push"
# some_list.pop()

# some_dictionary = {
#     'some_key': "Some value",
#     'some_other': 123
# }
# some_dictionary ['some_key']


# # Built-Ins

# # console.log("Something");
# print("The exact same thing")

# len()  # how many characters are in the string or list

# print(len(some_list))
# print(len())


# # If Statements, for Python (same as before...)

# # if(5 > 2){
# #   console.log("5 is bigger than 2")
# # }
# if 5 > 2:
#     print('5 is bigger than 2')
# elif 2 > 5:
# # elif: = else if:


# # For Loops, for Python

# # for = range
# # "JavaScript"
# # for(i = 0; i < arr.length; i++){
# #   console.log(i);
# # }

# print(range(2, 12, 1))
# # "2" is a starting point
# # "12" is the ending point, not including that number
# # "1" is how many numbers it is going up or down by
# # answer would be [2,3,4,5,6,7,8,9,10,11]


# #Example of for statement in Python
# for i in range (0, 12, 1):
#     print(i)


# listy_list = [0, 4, 6]
# sum = 0

# # Modify list
# for i in range(len(listy_list)):
#     listy_list[i] = 3

# # Use/Reference list
# for i in listy_list:
#     sum += i
# # OR
# for i in range(len(listy_list)):
#     sum += listy_list[i]

# print(sum)


# # "for i in range(len(listy_list)):"" is exactly the same as "for(i = 0; i < arr.length; i++)"



# # Functions

# # "JavaScript" =
# # function funcName(parameter) {
# #   console.log(parameter);
# # };

# # funcName(123)

# # "Python" = 
# def func_name(parameter):
#     print(parameter)

# func_name(123)


first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.