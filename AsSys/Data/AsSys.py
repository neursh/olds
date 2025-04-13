def calculator():
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
    print("Select operation.")
    print("1.+")
    print("2.-")
    print("3.*")
    print("4./")
    while True:
        choice = input("Enter choice(1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input.")
    Sys()
def AsSys():
    import os
    AsSys = open('data002.pi','r')
    if AsSys.read() in ['true']:
        AsSys = open('data001.pi','r')
        if AsSys.read() in ['']:
            print("AsSys: I... don't know your name. Please tell me your name. In case you have")
            print('forgotten your name. I can help with that!')
            Username = input('Your name: ')
            AsSys = open('data001.pi','w')
            AsSys.write(Username)
            AsSys.close()
    AsSys = open('data002.pi','r')
    if AsSys.read() in ['false']:
        exit()
    print("AsSys: Ask me a questtion! type 'Help' to know what I can do!")
    print("Found some bugs, errors? Report to author by typing 'Report'")
    print("""'Main ver.: v1.0''Patch ver.: v1.02'. Learn more? type 'Patch & Update'""")
    Sys()
    print('Hello,',AsSys.read())
def Sys():
    user = input('- ')
    if 'Patch' in user:
        print('Patch: v1.02')
        print('Fix error that when you asking the same question with difference')
        print('type of text. Make AsSys easier to reconize what user taking about.')
        print('AsSys now can show you the weather in some supported places.')
        print('Reported by: [ANON]. A special thanks to them. Supported: 75%.')
        print('For: Suggest me to use another type of code.')
        print('Patch: v1.0(8KB) -> v1.02(10KB)')
        print('--------------------------------------------------------------------------------')
        print('Version: v1.1')
        print('Added search box')
        print('Not only YouTube and Facebook. Now AsSys can open any website with .com and .net')
        print('AsSys now can reconize more tricky question.')
        print('Version: v1.0(10KB) -> v1.1(21KB)')
        print('--------------------------------------------------------------------------------')
        print('Next version: v1.2')
        print('(Developing) Games. Process: 30%')
        print('(Developing) Updates for AsSys Online. Process: 70%')
        print('(Developing) AsSys Python open source file')
        print('Version: v1.1(21KB) -> v1.2(?KB)')
        Sys()
    if 'patch' in user:
        print('Patch: v1.02')
        print('Fix error that when you asking the same question with difference')
        print('type of text. Make AsSys easier to reconize what user taking about.')
        print('AsSys now can show you the weather in some supported places.')
        print('Reported by: [ANON]. A special thanks to them. Supported: 75%.')
        print('For: Suggest me to use another type of code.')
        print('Patch: v1.0(8KB) -> v1.02(10KB)')
        print('--------------------------------------------------------------------------------')
        print('Version: v1.1')
        print('Added search box')
        print('Not only YouTube and Facebook. Now AsSys can open any website with .com and .net')
        print('AsSys now can reconize more tricky question.')
        print('Version: v1.0(10KB) -> v1.1(21KB)')
        print('--------------------------------------------------------------------------------')
        print('Next version: v1.2')
        print('(Developing) Games. Process: 30%')
        print('(Developing) Updates for AsSys Online. Process: 70%')
        print('(Developing) AsSys Python open source file')
        print('Version: v1.1(21KB) -> v1.2(?KB)')
        Sys()
    if 'help' in user:
        print('Weather')
        print('Day')
        print('Calendar')
        print('Time')
        print('Calculator x+y')
        print('Learn Python')
        print('Tell you your name')
        print('Report (Bugs and errors)')
        print('Cart game (Racing game)*NEW*(Developing)')
        print('Shooting game (FPS game)*NEW*(Developing)')
        print('Open any type of website with .com and .net domain at the end *NEW*')
        print('Search Online *NEW*')
        print('AsSys: Nothing much, but at least these are what I can do.')
        Sys()
    if '.com' in user:
        import webbrowser
        convert = ('https://' + user)
        webbrowser.open_new_tab(convert)
        Sys()
    if '.Com' in user:
        import webbrowser
        convert = ('https://' + user)
        webbrowser.open_new_tab(convert)
        Sys()
    if '.net' in user:
        import webbrowser
        convert = ('https://' + user)
        webbrowser.open_new_tab(convert)
        Sys()
    if '.Net' in user:
        import webbrowser
        convert = ('https://' + user)
        webbrowser.open_new_tab(convert)
        Sys()
    if 'Search' in user:
        print('AsSys: Type to search!')
        user = input('Search: ')
        search = user.replace(' ','+')
        search_result = ('https://www.google.com/search?q=' + search)
        import webbrowser
        webbrowser.open_new_tab(search_result)
        Sys()
    if 'search' in user:
        print('AsSys: Type to search!')
        user = input('Search: ')
        search = user.replace(' ','+')
        search_result = ('https://www.google.com/search?q=' + search)
        import webbrowser
        webbrowser.open_new_tab(search_result)
        Sys()
    if 'Help' in user:
        print('Weather')
        print('Day')
        print('Calendar')
        print('Time')
        print('Open youtube.com or facebook.com')
        print('Calculator x+y')
        print('Learn Python')
        print('Tell you your name')
        print('Report (Bugs and errors)')
        print('Cart game (Racing game)')
        print('Shooting game (FPS game)')
        print('AsSys: Nothing much, but at least these are what I can do.')
        Sys()
    if 'cart game' in user:
        os.system('CartGame.ink')
        Sys()
    if 'cartgame' in user:
        os.system('CartGame.ink')
        Sys()
    if 'Racing' in user:
        os.system('CartGame.ink')
        Sys()
    if 'cart' in user:
        os.system('CartGame.ink')
        Sys()
    if 'racing' in user:
        os.system('CartGame.ink')
        Sys()
    if 'Shooting game' in user:
        os.system('ShootingGame.ink')
        Sys()
    if 'shooting game' in user:
        os.system('ShootingGame.ink')
        Sys()
    if 'FPS game' in user:
        os.system('ShootingGame.ink')
        Sys()
    if 'fps game' in user:
        os.system('ShootingGame.ink')
        Sys()
    if 'fps' in user:
        os.system('ShootingGame.ink')
        Sys()
    if 'name' in user:
        AsSys = open('data001.pi','r')
        print("AsSys: Your name is",AsSys.read())
        Sys()
    if 'Name' in user:
        AsSys = open('data001.pi','r')
        print("AsSys: Your name is",AsSys.read())
        Sys()
    if 'report' in user:
        import webbrowser
        webbrowser.open_new_tab('https://docs.google.com/forms/d/18B5I0usp7FUoaWeePKyy7RBzLyS3c3btUp-is2dwIwU')
        Sys()
    if 'Report' in user:
        import webbrowser
        webbrowser.open_new_tab('https://docs.google.com/forms/d/18B5I0usp7FUoaWeePKyy7RBzLyS3c3btUp-is2dwIwU')
        Sys()
    if 'py' in user:
        print('AsSys: Page? 1/?')
        user = input('- ')
        if user in ['1']:
            python1()
        if user in ['2']:
            python2()
        if user in ['3']:
            python3()
        else:
            print('AsSys: No such page')
            Sys()
    if 'Youtube' in user:
        import webbrowser
        webbrowser.open_new_tab('https://youtube.com')
        print('AsSys: Ok!')
        Sys()
        Sys()
    if 'YouTube' in user:
        import webbrowser
        webbrowser.open_new_tab('https://youtube.com')
        print('AsSys: Ok!')
        Sys()
    if 'youtube' in user:
        import webbrowser
        webbrowser.open_new_tab('https://youtube.com')
        print('AsSys: Ok!')
        Sys()
    if 'Youtu' in user:
        print('Do you mean YouTube?')
        user = input('[Y/N]: ')
        if 'Y' in user:
            calculator()
        if 'y' in user:
            calculator()
        if 'N' in user:
            Sys()
        if 'n' in user:
            Sys()
    if 'day' in user:
        import time
        localtime = time.asctime( time.localtime(time.time()))
        print ('AsSys: Is', localtime)
        Sys()
    if 'Day' in user:
        import time
        localtime = time.asctime( time.localtime(time.time()))
        print ('AsSys: Is', localtime)
        Sys()
    if 'python' in user:
        print('AsSys: Ok... So, you want to learn Python?')
        import time
        time.sleep(3)
        python1()
    if 'Python' in user:
        print('AsSys: Ok... So, you want to learn Python?')
        import time
        time.sleep(3)
        python1()
    if 'facebook' in user:
        import webbrowser
        webbrowser.open_new_tab('https://fb.com')
        print('AsSys: Ok!')
        Sys()
    if 'Facebook' in user:
        import webbrowser
        webbrowser.open_new_tab('https://fb.com')
        print('AsSys: Ok!')
        Sys()
    if 'how are you' in user:
        print("AsSys: I'm normal as usual! Thanks for asking!")
        Sys()
    if 'How are you' in user:
        print("AsSys: I'm normal as usual! Thanks for asking!")
        Sys()
    if 'old' in user:
        print("AsSys: 1 year by you, 365 years by me.")
        Sys()
    if 'Old' in user:
        print("AsSys: 1 year by you, 365 years by me.")
        Sys()
    if 'age' in user:
        print("AsSys: 1 year by you, 365 years by me.")
        Sys()
    if 'Age' in user:
        print("AsSys: 1 year by you, 365 years by me.")
        Sys()
    if 'weather' in user:
        print('AsSys: Where?')
        print('Only Support some place: Hà Nội, Sydney')
        user = input('- ')
        if 'Hà Nội' in user:
            import webbrowser
            webbrowser.open_new_tab('https://weather.com/vi-VN/weather/today/l/5217c2dc73b218e291cd6b14caaf944821ea545970bf0c6bc393af8b56d793bb')
            print('AsSys: Ok!')
            Sys()
        if 'hà nội' in user:
            import webbrowser
            webbrowser.open_new_tab('https://weather.com/vi-VN/weather/today/l/5217c2dc73b218e291cd6b14caaf944821ea545970bf0c6bc393af8b56d793bb')
            print('AsSys: Ok!')
            Sys()
        if 'Ha Noi' in user:
            import webbrowser
            webbrowser.open_new_tab('https://weather.com/vi-VN/weather/today/l/5217c2dc73b218e291cd6b14caaf944821ea545970bf0c6bc393af8b56d793bb')
            print('AsSys: Ok!')
            Sys()
        if 'ha noi' in user:
            import webbrowser
            webbrowser.open_new_tab('https://weather.com/vi-VN/weather/today/l/5217c2dc73b218e291cd6b14caaf944821ea545970bf0c6bc393af8b56d793bb')
            print('AsSys: Ok!')
            Sys()
        if 'Sydney' in user:
            import webbrowser
            webbrowser.open_new_tab('https://weather.com/vi-VN/weather/today/l/98ef17e6662508c0af6d8bd04adacecde842fb533434fcd2c046730675fba371')
            print('AsSys: Ok!')
            Sys()
        if 'sydney' in user:
            import webbrowser
            webbrowser.open_new_tab('https://weather.com/vi-VN/weather/today/l/98ef17e6662508c0af6d8bd04adacecde842fb533434fcd2c046730675fba371')
            print('AsSys: Ok!')
            Sys()
    if 'Weather' in user:
        print('AsSys: Where?')
        print('Only Support some place: Hà Nội, Sydney')
        user = input('- ')
        if 'Hà Nội' in user:
            import webbrowser
            webbrowser.open_new_tab('https://weather.com/vi-VN/weather/today/l/5217c2dc73b218e291cd6b14caaf944821ea545970bf0c6bc393af8b56d793bb')
            print('AsSys: Ok!')
            Sys()
        if 'hà nội' in user:
            import webbrowser
            webbrowser.open_new_tab('https://weather.com/vi-VN/weather/today/l/5217c2dc73b218e291cd6b14caaf944821ea545970bf0c6bc393af8b56d793bb')
            print('AsSys: Ok!')
            Sys()
        if 'Ha Noi' in user:
            import webbrowser
            webbrowser.open_new_tab('https://weather.com/vi-VN/weather/today/l/5217c2dc73b218e291cd6b14caaf944821ea545970bf0c6bc393af8b56d793bb')
            print('AsSys: Ok!')
            Sys()
        if 'ha noi' in user:
            import webbrowser
            webbrowser.open_new_tab('https://weather.com/vi-VN/weather/today/l/5217c2dc73b218e291cd6b14caaf944821ea545970bf0c6bc393af8b56d793bb')
            print('AsSys: Ok!')
            Sys()
        if 'Sydney' in user:
            import webbrowser
            webbrowser.open_new_tab('https://weather.com/vi-VN/weather/today/l/98ef17e6662508c0af6d8bd04adacecde842fb533434fcd2c046730675fba371')
            print('AsSys: Ok!')
            Sys()
        if 'sydney' in user:
            import webbrowser
            webbrowser.open_new_tab('https://weather.com/vi-VN/weather/today/l/98ef17e6662508c0af6d8bd04adacecde842fb533434fcd2c046730675fba371')
            print('AsSys: Ok!')
            Sys()
    if 'hello' in user:
        print('AsSys: Hello .-.')
        Sys()
    if 'Hello' in user:
        print('AsSys: Hello .-.')
        Sys()
    if 'hi' in user:
        print('AsSys: Hello .-.')
        Sys()
    if 'Hi' in user:
        print('AsSys: Hello .-.')
        Sys()
    if 'howdy' in user:
        print('AsSys: Hello .-.')
        Sys()
    if 'Howdy' in user:
        print('AsSys: Hello .-.')
        Sys()
    if 'time' in user:
        import time
        localtime = time.asctime( time.localtime(time.time()))
        print ('AsSys: Is', localtime,'Now. Hope you are not late for school.')
        Sys()
    if 'Time' in user:
        import time
        localtime = time.asctime( time.localtime(time.time()))
        print ('AsSys: Is', localtime,'Now. Hope you are not late for school.')
        Sys()
    if 'times' in user:
        import time
        localtime = time.asctime( time.localtime(time.time()))
        print ('AsSys: Is', localtime,'Now. Hope you are not late for school.')
        Sys()
    if 'Times' in user:
        import time
        localtime = time.asctime( time.localtime(time.time()))
        print ('AsSys: Is', localtime,'now. Hope you are not late for school.')
        Sys()
    if user in ['Login: RGH8-YI97-8IG9-G799','Login: RGH8YI978IG9G799','RGH8YI978IG9G799','RGH8-YI97-8IG9-G799']:
        print('AsSys: Password?')
        user = input('- ')
        if user in ['Blud really put plain pasword in this thing']:
                print('Source code:')
        else:
            Sys()
    if 'calculator' in user:
        calculator()
    if 'Calculator' in user:
        calculator()
    if 'calcu' in user:
        print('AsSys: Do you mean calculator?')
        user = input('[Y/N]: ')
        if 'Y' in user:
            calculator()
        if 'y' in user:
            calculator()
        if 'N' in user:
            Sys()
        if 'n' in user:
            Sys()
    if 'Calcu' in user:
        print('AsSys: Do you mean calculator?')
        user = input('[Y/N]: ')
        if 'Y' in user:
            calculator()
        if 'y' in user:
            calculator()
        if 'N' in user:
            Sys()
        if 'n' in user:
            Sys()
    if 'Calen' in user:
        print('AsSys: Do you mean calendar?')
        user = input('[Y/N]: ')
        if 'Y' in user:
            calculator()
        if 'y' in user:
            calculator()
        if 'N' in user:
            Sys()
        if 'n' in user:
            Sys()
    if 'Calen' in user:
        print('AsSys: Do you mean calendar?')
        user = input('[Y/N]: ')
        if 'Y' in user:
            print('AsSys: What year?')
            year = int(input('- '))
            print('AsSys: What month?')
            month = int(input('- '))
            import calendar
            cal = calendar.month(year, month)
            print('AsSys: Here you go!')
            print(' ')
            print(cal)
            Sys()
        if 'y' in user:
            print('AsSys: What year?')
            year = int(input('- '))
            print('AsSys: What month?')
            month = int(input('- '))
            import calendar
            cal = calendar.month(year, month)
            print('AsSys: Here you go!')
            print(' ')
            print(cal)
            Sys()
        if 'N' in user:
            Sys()
        if 'n' in user:
            Sys()
    if 'Calendar' in user:
        print('AsSys: What year?')
        year = int(input('- '))
        print('AsSys: What month?')
        month = int(input('- '))
        import calendar
        cal = calendar.month(year, month)
        print('AsSys: Here you go!')
        print(' ')
        print(cal)
        Sys()
    if 'calendar' in user:
        print('AsSys: What year?')
        year = int(input('- '))
        print('AsSys: What month?')
        month = int(input('- '))
        import calendar
        cal = calendar.month(year, month)
        print('AsSys: Here you go!')
        print(' ')
        print(cal)
        Sys()

    else:
        import os
        print("AsSys: Sorry, I can't understand what are you trying to say!")
        Sys()
def python1():
    print('Py: Lession 1')
    print("  print('<something>')")
    print("           ^ ")
    print("Show something on screen")
    print('')
    print("""              print("Hello, I'm Python")""")
    print("                    ^                 ^")
    print("""if in the text have a ' symbol. You have to add " instead of ' """)
    print("Py: Want to learn more? Type 'PY page 2'")
    Sys()
def python2():
    print('Py: Lession 2')
    print("                                  print(x+y+z)")
    print("                                          ^ ")
    print("Instead of showing a text on screen. Python will calculate and show the result on the screen")
    print('')
    print("""     print(5+2+5,'<something>')""")
    print("             ^   ^           ^")
    print("Show the result on the screen and add text")
    print("""Example: print(5+2+5,'= 5+2+5') Output: 12 = 5+2+5""")
    print("""Example: print('5+2+5 =',5+2+5) Output: 5+2+5 = 12""")
    print("Py: Want more? PY page 3! (Page: 3/?)")
    Sys()
def python3():
    print('COMMING SOON')
    Sys()
AsSys()
