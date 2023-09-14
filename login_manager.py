data_dict = {}

with open('master_file.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(':')
        if len(parts) >= 2:
            key = parts[0].strip()  # The string before the colon
            values = parts[1].strip().split(',')  # Split values by comma (you can use another separator if needed)
            data_dict[key] = values
    

def write_data(filename, data_dict):
    with open(filename, "a") as file:
        for key, value in data_dict.items():
            file.write(f"{key}: {value}\n")


def return_usernamepassword():
    prompt = 'What website are you looking for\n'
    x = input(prompt)
    result = x.lower()
    if result in data_dict:
        print(f'Your Username for {result} is:\t{data_dict[result][0]} \nYour password for {result} is:\t{data_dict[result][1]}')
    else:
        print('There is no username and password for that website in your password manager.')
        return False


def add_websitelogin():
    prompt = 'What website would you like to add to your login manager\n'
    x = input(prompt)
    key = x.lower()
    value = []
    if key not in data_dict:
        username = input(f'Please enter in a username for {key}:\t')
        password = input(f'Please enter in a password for {key}:\t')
        value = [username,password]
        dict_update = {}
        dict_update[key] = value
        data_dict.update(dict_update)
        write_data('master_file.txt', dict_update)
        print(f'The username and password for {key} was stored in the password manager')
    else:
        print(f'You already have a login for {key}')
        

def check_website_valid():
    prompt = 'What website would you like to check to see if you have a login for?\n'
    x = input(prompt)
    if x in data_dict:
        print('You have a login for this website')
    else:
        print("You don't have a login for this website")
        return False

def re_run_program():
    prompt = 'Would you like to go back to the main menu (Yes or No)?\n'
    x = input(prompt)
    if x.lower() == 'yes':
       print("User entered 'yes'")
       check_task()
    elif x.lower() == 'no':
        print("User entered 'no'\n")
        print('Thank you and goodbye')
        return False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


def check_task():
    prompt1 = 'Please enter a number correlating to what task you would like completed.\n(1)\t Look up a username and password to a website \n(2)\t Add website username and password to the password manager. \n(3)\t Check to see if you have an email and password associated with a website. \n(4)\t End program\nPlease Enter input here:\t'
    x = input(prompt1)
    if x == '1':
        return_usernamepassword()
        re_run_program()
    elif x == '2':
        add_websitelogin()
        re_run_program()
    elif x == '3':
        check_website_valid()   
        re_run_program()
    elif x == '4':
        print('Thank you and goodbye')
        return False
    else:
        return False


check_task()
