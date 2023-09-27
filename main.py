from menu import menu, create, find, find_accounts
import os
from dotenv import load_dotenv
# menu
# 1. create new password for a site
# 2. find password for a site
# 3. Find all sites connected to an email

passw = input('Please provide the master password: ')
load_dotenv()
if passw == os.getenv('SECRET'):
    print('You\'re in')

else:
    print('no luck')
    exit() 

choice = menu()
while choice != 'Q' and choice != 'q':
    if choice == '1':
        create()
    if choice == '2':
        find_accounts()
    if choice == '3':
        find()
    else:
        choice = menu()
exit()