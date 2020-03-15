def login_check(driver):
    elements = driver.find_elements_by_name('logout')
    return len(elements) == 1


def get_message(driver):
    return driver.find_element_by_class_name('note').text


def middle_stuff(driver, uname, passwd):
    username_field = get_username(driver)
    password_field = get_password(driver)

    username_field.clear()
    password_field.clear()

    click_on_agreebox(driver)
    username_field.send_keys(uname)
    password_field.send_keys(passwd)
    click_on_login(driver)


def message_print(uname, passwd):
    print('\tPASSWORD FOUND!')
    print('\tUsername -> ', uname)
    print('\tPassword -> ', passwd)
    print('-------------------------------')


def final_login_check(driver):
    message = get_message(driver)
    if login_check(driver) == 1:
        return True

    return message != 'Wrong username/password' and message != ''


def click_on_logout(driver):
    driver.find_element_by_name('logout').click()


def get_username(driver):
    return driver.find_element_by_name('username')


def get_password(driver):
    return driver.find_element_by_name('password')


def click_on_agreebox(driver):
    driver.find_element_by_id('agreepolicy').click()


def click_on_login(driver):
    driver.find_element_by_id('loginbtn').click()
