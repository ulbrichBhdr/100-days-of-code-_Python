# def format_name(f_name,l_name) :

#   print(f_name.title()) 
#   print(l_name.title()) 


# format_name("AngelA","SDLDH LEmbmdd") 
# ...................................................
# def title_case(sentence):
#     words = sentence.split()  # Split the sentence into words
#     title_cased_words = []
#     for word in words:
#         if "'" in word:
#             parts = word.split("'")  # Split the word at apostrophes
#             title_cased_word = "'".join([part.capitalize() if not part.startswith("'") else part for part in parts])  # Capitalize each part if not preceded by an apostrophe
#             title_cased_words.append(title_cased_word)
#         else:
#             title_cased_words.append(word.capitalize())  # Capitalize the first letter of each word
#     return ' '.join(title_cased_words)  # Join the words back into a sentence

# # Example usage:
# sentence = "she's all right and she'll be good"
# print(title_case(sentence))  # Output: She's All Right And She'll Be Good
# ...........................................................
# import re

# def my_title(string):
#     return re.sub(
#               r"[A-Za-z]+('[A-Za-z]+)?",
#               lambda ch: ch.group(0)[0].upper() +
#               ch.group(0)[1:].lower() if not ch.group(0).startswith("'") else ch.group(0),
#               string
#     )

# text = "She's out of town, isn't she?"
# print(my_title(text))
# ................................................................
# def format_name(f_name, l_name):
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   return f"{formated_f_name} {formated_l_name}"

# print(format_name("AnGELA", "YU"))
# ...............................................................
# def format_name(f_name, l_name) :
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   return f"Result: {formated_f_name} {formated_l_name}"

# print(format_name(input("What is your first name? "),input("What is your last name?")))
# ................................................................
# DAys in Month Exercise :
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(year, month):
#     if month > 12 or month < 1:
#         return "Invalid month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29  
#     return month_days[month - 1]

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)
# .............................................
# def format_name(f_name, l_name) :
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   return f"Result: {formated_f_name} {formated_l_name}"

# formatted_name = format_name(input("Your first name: "), input("your last name: "))

# print(format_name(input("What is your first name? "),input("What is your last name?")))

# length = len(formatted_name)

# def format_name(f_name, l_name):
#   """Take a first and last name and format it to return the title case version of the name."""

#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   return f"Result: {formated_f_name} {formated_l_name}"

# format_name()
# # .............................................................
# # Calculator :

# # Add
# def add(n1, n2):
#   return n1 + n2

# # Subtract
# def Subtract(n1, n2):
#   return n1 - n2

# # Multiply
# def Multiply(n1, n2) :
#   return n1 * n2

# # Divide
# def Divide(n1, n2) :
#   return n1 / n2

# Operations = {
#   "+": add  ,
#   "-": Subtract,
#   "*": Multiply,
#   "/": Divide ,
# }

# num1 = int(input("What's the first number?: "))

# for symbol in Operations:
#   print(symbol)
# operation_symbol = input("Pick an operation from the line above: ")

# num2 = int(input("what's the second number?: "))

# calculation_function = Operations[operation_symbol]
# first_answer = calculation_function(num1, num2)

# print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# operation_symbol = input("Pick another operation: ")
# num3 = int(input("What's the next number?: "))
# calculation_function = Operations[operation_symbol]
# second_answer = calculation_function(calculation_function(num1,num2),num3)

# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
# ........................................................
# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def Subtract(n1, n2):
    return n1 - n2

# Multiply
def Multiply(n1, n2):
    return n1 * n2

# Divide
def Divide(n1, n2):
    return n1 / n2

Operations = {
    "+": add,
    "-": Subtract,
    "*": Multiply,
    "/": Divide,
}

def calculator():
  num1 = int(input("What's the first number?: "))

  for symbol in Operations:
      print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation : ")
    num2 = int(input("what's the second number?: "))

    calculation_function = Operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
