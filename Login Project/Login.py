import json

def validate_login(username,password,dict):
    if username in dict and dict[username] == password:             # checks to see if username and password are paird in the dictionary
        print('Login successful')
        return 1

    elif username in dict and dict[username] != password:           # checks to see if username is correct, but password is incorrect
        print('Wrong password has been entered, try again')
        return 0

    else:
        print('Wrong username and password, try again')
        return 0

def create_login(username,password,dict):
    if username in dict:
        print('Username already in use, try again')
    
    else:
        dict[username] = password
        print('Login has been created')
        return 1
    

def main():

    with open('login.txt', 'r') as f:       # open txt file and read it
        try:
            dict = json.load(f)             # if there is stuff in the file load it in as a json file
        except:
            dict = {}                       # if it is empty create an empty dictionary

    Create_login = input("Do you have a login? (y/n): ")

    while True:
        if (Create_login == 'y'):
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            if(validate_login(username,password,dict) == 1):   # if the login is valid break out of the loop 
                break

        else:
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            if (create_login(username,password,dict) == 1):     # if login is created correctly add it to file
                with open('login.txt', 'w') as f:
                    json.dump(dict, f)                          # add the contents of the json dict to the file
                if (validate_login(username,password,dict) == 1):   # if login is valid break the loop
                    break
    f.close()                                                       # close the file
    return True

main()