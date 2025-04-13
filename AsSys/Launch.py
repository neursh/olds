def launch():
    import os
    os.system('AsSys.py')
def EULAT():
    import time
    print('I■■■■■■■■■■■■■■■■■■■■I Loading files...')
    time.sleep(5)
    print('I                    I Installing files...')
    time.sleep(4)
    print('I■■■■■■■■■■          I Checking system...')
    time.sleep(4)
    print('I■■■■■■■■■■■■■■■■■■■ I Loading AsSys...')
    time.sleep(6)
    AsSys = open('data002.pi','w')
    AsSys.write('true')
    AsSys.close()
    print('The program will close. Open it up again to start using AsSys!')
    time.sleep(7)
    exit()
def check():
    import os
    os.chdir('../AsSys/Data')
    print('Files located at:',os.getcwd())
    AsSys = open('data002.pi')
    Checker = AsSys.read()
    if Checker in ['false']:
        guide()
    if Checker in ['true']:
        launch()
def guide():
    print('Before start to use this Assistant Program. You have to know that:')
    print('This program is still developing. The program may have some bugs.')
    print('You have to extract the program folder following to README')
    print('REMEMBER! THE PROGRAM STILL DEVELOPING!')
    input()
    EULAT()
check()
