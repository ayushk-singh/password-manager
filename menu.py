from password_manager_db import insert_record,search_pass,find_user_name

def menu():
    print('-'*30)
    print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Create new password')
    print('2. Find password with username')
    print('3. Find a password with site name')
    print('Q. Exit')
    print('-'*30)
    return input(': ')

def create():
   print('Please proivide the name of the site or app you want to generate a password for: ')
   app_name = input()
   print('Please provide a simple password for this site: ')
   passw = input()
   user_email = input('Please provide a user email for this app or site: ')
   username = input('Please provide a username for this app or site (if applicable): ')
   if username == None:
       username = ''
   url = input('Please paste the url to the site that you are creating the password for: ')
   insert_record(passw, user_email, username, url, app_name)

def find_accounts():
   print('Please proivide the username that you want to find accounts for: ')
   user_email = input() 
   find_user_name(user_email)


def find():
   print('Please proivide the name of the site or app you want to find the password to: ')
   app_name = input()
   search_pass(app_name)

