#import clipboard functionality and regex
import re
import pyperclip

#Copy the clipboard
text = str(pyperclip.paste())

#Define regex patterns for email and phone numbers
#regex for phone numbers
regexPhone = re.compile(r'''(
(\d{3}|\(\d{3}\))?             #area code. 3 digits with or without parentheses
(\s|-|\.)?                     #Separator. space, dash, or dot
(\d{3})                        #First 3 digits manditory
(\s|-|\.)                     #Separator. space, dash, or dot
(\d{4})                        #Final 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? #Optional extension denoted with ext anf 2-5 digits
)''', re.VERBOSE)
#regex for email
regexEmail = re.compile(r'''(
[a-zA-Z0-9._%+-]+        #Username
@                        #@ symbol
[a-zA-z0-9.-]+           #Domain name
(\.[a-zA-z]{2,4})        #dot com/edu/etc
)''', re.VERBOSE)

#Search the clipboard for phone numbers and emails
matches = []
for groups in regexPhone.findall(text):
       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
       if groups[8] != '':
           phoneNum += ' x' + groups[8]
       matches.append(phoneNum)
for groups in regexEmail.findall(text):
       matches.append(groups[0])

#Paste results back into clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
