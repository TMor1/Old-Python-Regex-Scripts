#! python3
#T.M 11/07/21

import sys, re

print('This is a collection of 3 script\'s to verify or find a mobile number.\n\n')

#===== Script 1 =====
#Develop a script to find a mobile number with the prefix XXX-XXXXXXX without using Regex
#Included comments used to test script below

print('Script 1'.center(20, '='))

def isMobile(text):
    if len(text)!=11:
        print('This is not the correct length for a mobile number.\nPlease try again.')
        return False #Not a mobile number
    for i in range(0, 3):
#       print(text[i]) #Printing 'text[i]' code used for testing to ensure all characters are being checked.
        if not text[i].isdecimal():
            print('This number is missing the first 3 digits.\nPlease try again.')
            return False #Missing first 3 digits
    if text[3] != '-':
#       print(text[i])
        print('This number does not include a dash at the correct place.\nPlease try again.')
        return False #Missing dash 
    for i in range(4, 11):
#       print(text[i])
        if not text[i].isdecimal():
            print('This number is missing the last 7 digits.\nPlease try again.')
            return False #Missing last 7 digits
    else:
        print('Yes that is a mobile number! :)')

print('Hello, I can confirm if a number follows the mobile format of \'XXX-XXXXXXX\'. Just enter one below :)')
number=input()
isMobile(number)


#===== Script 2 =====
#Develop a script to find all numbers within a given string below without using Regex
text='''Find the 5 numbers matching the correct number prefix within the text below.
Only 5/10 numbers are in the correct format.
Here are the first 5 :) = 085-1234561, 085-1234562, 85-12534562, 085-2145, 087-5134562
Here are the next 5 :) = 083-3214599, 087-9934332, 05-12524549, 0851352145, 083-613262'''

print('\n'+'Script 2'.center(20, '='))

def isMobileEither(text): #Updated from above to prevent spam messages
    if len(text)!=11:
        return False #Not a mobile number
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False #Missing first 3 digits
    if text[3] != '-':
        return False #Missing dash 
    for i in range(4, 11):
        if not text[i].isdecimal():
            return False #Missing last 7 digits
    else:
        return True

isNumber=False
for i in range(len(text)):
    check=text[i:i+11]
    if isMobileEither(check):
        print('Phone number found: ' + check)
        isNumber=True
if not isNumber:
    print('No numbers were found within this text.')


#===== Script 3 =====
#Regex Time: Develop two scripts to find a single and multiple numbers (XXX-XXXXXXX) within text using Regex

print('\n\n'+'Script 3'.center(20, '='))

numberText='''Find the 5/10 numbers matching the correct number format within the text below.
This is altered from the text seen in script 2.
Here are the first 5 :) = 085-1234561, 085-1234562, 85-12534562, 085-2145, 087-51a4562
Here are the next 5 :) = 3214599, 087-9934332, 05-12524549, 0851352145, 083-6b13262'''

#Regex Script 3a - find a single number
mobileRegex=re.compile(r'\d{3}-\d{7}')
mo=mobileRegex.search('Find the phone number within this text! 085-1234567 :)')
print('The number hidden in the text was: ' + str(mo.group()) +'\n')

#Regex Script 3b - find 5 numbers withing a group of text matching XXX-XXXXXXX or XXXXXXX [no areas code or dash]
mobileRegexTwo=re.compile(r'(\d{3}-)?(\d{7})')
order=['1st', '2nd', '3rd', '4th', '5th']
numbers=mobileRegexTwo.findall(numberText)
for i in range (0, 5):
    print('The %s number hidden in the text is: %s' %(order[i], numbers[i][0]+numbers[i][1]))

#===== All Scripts Finished =====
print('\nExiting...')
sys.exit()
