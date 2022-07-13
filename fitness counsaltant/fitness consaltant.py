while True:
    print('Welcome to the fitness consultant!!')
    #defining functions
    def Input():
        global height
        global weight
        global age
        global name
        name = input('What is your name?')
        age = input('What is your age ?')
        weight = int(input('What is your weight ?')) 
        height = int(input('What is your height ?'))
    def bmi():
        global bmi
        heightsq = height / 100
        heightsq = heightsq ** 2
        bmi = weight / heightsq
        print('Your bmi is ' + str(bmi))
    def fat_thinn():
        global normal
        global thin 
        global fat
        if bmi >= 24:
            fat = True
            thin = False
            normal = False
        elif bmi <= 18:
            fat = False
            thin = True
            normal = False
        else:
            fat = False
            thin = False
            normal = True
    def fatt():
        print("You are overweight")
        global exercise
        global food
        active_level = input("What is your activity level?(high[a], medium[b], low[c])")
        if active_level == "a" or active_level == "b":
            exercise = True
        else:
            exercise = False
        while True:
            calorie_intake = int(input("How much calories do eat daily(1200-2500)?"))
            if calorie_intake > 2500 or calorie_intake < 1200:
                print("Please enter a value between 1800 and 2500")
                continue
            else:
                if calorie_intake >= 1800:
                    food = True
                else:
                    food = False
                break
                    
    def thinn():
        print("You are to thin")
        global food
        while True:
            calorie_intake = int(input("How much calories do eat daily(1200-2500)?"))
            if calorie_intake > 2500 or calorie_intake < 1200:
                print("Please enter a value between 1800 and 2500")
                continue
            else:
                if calorie_intake < 1800:
                    food = False
                else:
                    food = True
                break
                

    def advise1():
        if food == False:
            print("")
            print("Advise:")
            print("You need to eat more food")
            print('Also you need to get a healthier diet')
            print('You diet should have a balanced amount of each of the major 7 nutrients')
            print('''
            -Carbohydrates eg. Bread,pasta,rice
            -Lipids eg. milk,cheese,vegetable oil
            -Proteins eg.meat,fish
            -Vitamins eg. A=Liver,C=Citrus fruit,D=Eggs
            -Minerals eg. Calcium = milk,cheese ,Iron = Red meat
            -Water eg. water,juice
            -Dietary fibre eg. wholemeal bread,fruits
            ''')
        else:
            print("")
            print("Advise:")
            print('Also you need to get a healthier diet')
            print('You diet should have a balanced amount of each of the major 7 nutrients')
            print('''
            -Carbohydrates eg. Bread,pasta,rice
            -Lipids eg. milk,cheese,vegetable oil
            -Proteins eg.meat,fish
            -Vitamins eg. A=Liver,C=Citrus fruit,D=Eggs
            -Minerals eg. Calcium = milk,cheese ,Iron = Red meat
            -Water eg. water,juice
            -Dietary fibre eg. wholemeal bread,fruits
            ''')
            
    def advise2():
        if exercise == False and food == True and int(age) < 30:
            print("")
            print("Advise:")
            print("Do more exercise like running and swimming")
            print('Also you need to get a healthier diet')
            print('You diet should have a balanced amount of each of the major 7 nutrients')
            print('''
            -Carbohydrates eg. Bread,pasta,rice
            -Lipids eg. milk,cheese,vegetable oil
            -Proteins eg.meat,fish
            -Vitamins eg. A=Liver,C=Citrus fruit,D=Eggs
            -Minerals eg. Calcium = milk,cheese ,Iron = Red meat
            -Water eg. water,juice
            -Dietary fibre eg. wholemeal bread,fruits
            ''')
        elif exercise == False and food == True and int(age) > 30:
            print("")
            print("Advise:")
            print("Do more exercise like running and swimming")
            print('Also you need to get a healthier diet')
            print('You diet should have a balanced amount of each of the major 7 nutrients')
            print('''
            -Carbohydrates eg. Bread,pasta,rice
            -Lipids eg. milk,cheese,vegetable oil
            -Proteins eg.meat,fish
            -Vitamins eg. A=Liver,C=Citrus fruit,D=Eggs
            -Minerals eg. Calcium = milk,cheese ,Iron = Red meat
            -Water eg. water,juice
            -Dietary fibre eg. wholemeal bread,fruits
            ''')    
        elif exercise == True and food == True:
            print("")
            print("Advise:")
            print('Also you need to get a healthier diet')
            print('You diet should have a balanced amount of each of the major 7 nutrients')
            print('''
            -Carbohydrates eg. Bread,pasta,rice
            -Lipids eg. milk,cheese,vegetable oil
            -Proteins eg.meat,fish
            -Vitamins eg. A=Liver,C=Citrus fruit,D=Eggs
            -Minerals eg. Calcium = milk,cheese ,Iron = Red meat
            -Water eg. water,juice
            -Dietary fibre eg. wholemeal bread,fruits
            ''')
        else:
            print("Do more exercise like running and swimming.")
             
    #Main loop
    Input()
    bmi()
    fat_thinn()
    if fat == True:
        fatt()
        advise2()
    elif thin == True:
        thinn()
        advise1()
    else:
        print("You are healthy and at a goood weight.")
        print("Keep it up!")
    repeat = input('Do you want to repeat(Y/N)?')
    if repeat == 'Y' or 'y':
        pass
    else:
        break
    
            
            
