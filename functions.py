# FUNCTIONS
# - CONSISTS OF FUNCTION NAME, PARAMETERS.
# - STARTS "DEF" KEYWORD.
# - OPTIMIZED AND MAKE A BLOCK OF CODE REUSABLE.


# VOID FUNCTION
# def averageOfThreeNumbers(num1, num2, num3):
#     # CODES ...
#     average = (num1 + num2 + num3) / 3
#     print("Average: ", average)

# SHORTCUT FOR COPYING HIGHLIGHTED/SINGLE LINE = alt + shift + ArrowDown/ArrowUp

# averageOfThreeNumbers(89, 76, 81)
# averageOfThreeNumbers(89, 76, 81)
# averageOfThreeNumbers(89, 76, 81)

# RETURN FUNCTION
title = "Ang Alamat ni Loude"
title2 = ": Bagsakan Era"

def stringToTitle(title):
    return title.title()

def stringToUppercase(message):
    return message.upper()

def stringToLowercase(message):
    return message.lower()

def joinString(message, message2):
    return message.join(message2)

def countLetters(message):
    return len(message)

print(stringToTitle(title))
print(stringToUppercase(title))
print(stringToLowercase(title))
# print(joinString(title, title2))
print(countLetters(title))