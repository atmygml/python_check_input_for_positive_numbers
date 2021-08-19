import string

def check_num():

  number_as_string = string.digits

  number_input = input("\nPlease enter a positive number.\n\n") 

  valid_input = False

  while valid_input == False:
      
    if number_input == "":
      print("\nYou have entered an invalid input.\n")
      number_input = input("Please enter a positive number again.\n\n")
      valid_input = False
    
    elif number_input[0] == "0":
      print("\nYou have entered an invalid input.\n")
      number_input = input("Please enter a positive number again.\n\n")
      valid_input = False

    else:
      for i in range(len(number_input)):
        if number_input[i] not in number_as_string:
          print("\nYou have entered an invalid input.\n")
          number_input = input("Please enter a positive number again.\n\n")
          valid_input = False
          break
        if i == (len(number_input)-1):
          print("\nYou have entered a valid input.\n")
          number_entered = int(number_input)
          print("You may proceed.\n")
          valid_input = True
          return number_entered

number_checked = check_num()
print(f"\nThe number you have entered is {number_checked}.\n")
print("\nProgram ends.\n")

