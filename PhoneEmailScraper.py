#! Python 3
#T.M 14/07/21
# ===== Create an phone number and email scraper script =====
import re, sys, pyperclip

#Task 1: Create Phone Number Regex Expression
#Number formats will be XXX-XXX-XXXX, (XXX)-XXX-XXXX, (XXX) XXX-XXXX, XXX XXX-XXXX
numberRegex=re.compile(r'''
(
(\d{3}|\(\d{3}\))+     #First 3 Digits with or without brackets
(\s|-)?                #First Seperator (space or -)
\d{3}                  #Middle 3 Digits
-                      #Second Seperator
\d{4}                  #Last 4 Digits
)
''', re.VERBOSE)

#Task 2: Create Email Regex Expression
emailRegex=re.compile('''
[a-zA-Z0-9_.+-]+     #Name - Can include symbols _.+-
@                    #Symbol
[a-zA-Z0-9_.+-]+     #Domain
''', re.VERBOSE)

#Task 3: Copy text to scrap data from
#Script can be altered to use pyperclip to copy text from word documents using command: textTest=pyperclip.paste()
#Text below for demonstration purposes - randomly generated with 1 incorrect email/number to text regex expressions
textTest='''
T.Murphy, oberbrunner.sydnee@yahoo.com, 224-944-1169
Luciano Gillespie, ervin29@yahoo.com, 617 437-8920
Antione Medina, grant.rick@klocko.com, (207)-810-1937
S.Andrews, alysson60@hotmail.co.uk, 223-923-6484
Al Baird, doug26@casper.info, 301-566-6924
Kristopher Powers, williamson.cheyenne@brakus.net, (707) 351-1217
Kay Brennan, jayne65@hotmail.com, 412-225-9105
Rebecca Prince, rebeca.oberbrunner@yahoo.com, 602 728-1987
H.Donaldson, deckow.joan@doyle.org, 220-282-6394
Morgan Orozco, huels.lupe@hotmail.com, 219-943-1231
Tamera Chung, elmer.jaskolski@yahoo.com, (308)-227-3571
Gaston Jackson, beahan.elmira@yahoo.com, (219) 766-4027
Cat Wilkins, miller.hobart@hotmail.com, 405 646-7468
Fidel Owens, nolan.walker@bogisich.org, 228 452-1803
Collin Hahn, kaylee93@leffler.com, (424) 703-1853
Neal Hall, makenna78@yahoo.com, (406) 600-1318
Francis Welch, jarrell.dibbert@dietrich.com, (910)-771-8901
J.Bradford, marcelina.watsica@barrows.com, 309-843-4085
P.Miller, miller.gabriella@schiller.net, 703 932-9152
Roger B., znicolas@weimann.com, 252-171-7562
T. Burns, testing@\expression.ie, 123-4567 #Should not be copied, email no allowance for '\' and number incorrect format
'''

#Task 4: Gather numbers/emails
listNumbers=numberRegex.findall(textTest)
listEmails=emailRegex.findall(textTest)

getNumbers=[]
for i in listNumbers:
    getNumbers.append(i[0])
    
#Task 5: Print numbers and emails to the screen
numberFindings='\n'.join(getNumbers)
emailFindings='\n'.join(listEmails)
print('Here are the numbers found below:\n\n'+str(numberFindings)+'\n\nHere are the emails found below:\n\n'+str(emailFindings))
#Script can be altered to copy results to the clipboard using two lines below:
#allFindings='\n'.join(getNumbers)+'\n'+'\n'.join(listEmails)
#pyperclip.copy(allFindings)

#===== All Scripts Finished =====
print('\nScript finished, exiting...')
sys.exit()
