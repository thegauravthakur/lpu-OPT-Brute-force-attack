name = ''

while True:
    name = input('Enter the name: ')
    if name == 'exit':
        print('exiting the program')
        exit()
    with open('dictionary', 'r') as file:
        found = False
        hello = file.readlines()
        for i in hello:
            if i == name + '\n':
                print('Already there!')
                found = True
                break
        if not found:
            with open('dictionary', 'a') as file2:
                file2.write('\n'+name)
                print('added to the file')
