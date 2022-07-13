#importing modules
import tkinter
#screen
screen = tkinter.Tk()
screen.geometry('150x225')
screen.configure(background = 'white')
screen.title('Fitness consultant')
#functions
low = True
medium = False
high = False
def fact_file():
    global f_m
    global normal
    global thin 
    global fat
    if fat == True:
        ty = 'Overweight'
    elif thin == True:
        ty = 'Too thin'
    else:
        ty = 'Normal'
    f_m = ''
    f_m = f_m + 'Name: ' + name_entry.get() + '\n'
    f_m = f_m + 'Age: ' + age_entry.get() + '\n'
    f_m = f_m + 'Weight: ' + weight_entry.get() + ' kg'+ '\n'
    f_m = f_m + 'Height: ' + height_entry.get() + ' cm' + '\n'
    f_m = f_m + 'Class: ' + ty
def advise():
    global a_m
    a_m = ''
    if normal == True:
        a_m = 'You are doing good, keep it up!!'
    elif fat  == True:
        a_m = a_m + 'Advise:' + '\n'
        if int(calorie_entry.get()) > 2500:
            a_m = a_m + 'You need to get a healthier diet. \n'
            a_m = a_m + 'You diet should have a balanced amount of each of the major 7 nutrients \n'
            a_m = a_m + '''
            -Carbohydrates eg. Bread,pasta,rice
            -Lipids eg. milk,cheese,vegetable oil
            -Proteins eg.meat,fish
            -Vitamins eg. A=Liver,C=Citrus fruit,D=Eggs
            -Minerals eg. Calcium = milk,cheese ,Iron = Red meat
            -Water eg. water,juice
            -Dietary fibre eg. wholemeal bread,fruits \n
            '''
        if low == True:
            a_m = a_m + 'You need to do more exercise like running and swimming.'
    else:
        a_m = a_m + 'Advise:' + '\n'
        if int(calorie_entry.get()) < 1200:
            a_m = a_m + 'You need to get a healthier diet. \n'
            a_m = a_m + 'You diet should have a balanced amount \n of each of the major 7 nutrients \n'
            a_m = a_m + '''
            -Carbohydrates eg. Bread,pasta,rice
            -Lipids eg. milk,cheese,vegetable oil
            -Proteins eg.meat,fish
            -Vitamins eg. A=Liver,C=Citrus fruit,D=Eggs
            -Minerals eg. Calcium = milk,cheese ,Iron = Red meat
            -Water eg. water,juice
            -Dietary fibre eg. wholemeal bread,fruits \n
            '''
def bmi(weight, height):
    global bmi
    heightsq = height / 100
    heightsq = heightsq ** 2
    bmi = weight / heightsq
def fat_thin():
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
def Low():
    low = True
    medium = False
    high = False
def Medium():
    low = False
    medium = True
    high = False
def High():
    low = False
    medium = False
    high = True
def finish():
    bmi(int(weight_entry.get()), int(height_entry.get()))
    fat_thin()
    advise()
    fact_file()
    msg = f_m + '\n' + a_m 
    top_frame.destroy()
    frame_2.destroy()
    frame_3.destroy()
    frame_4.destroy()
    frame_mid.destroy()
    frame_5.destroy()
    frame_6.destroy()
    frame_7.destroy()
    frame_8.destroy()
    frame_9.destroy()
    frame_10.destroy()
    bottom_frame.destroy()
    screen.geometry('250x350')
    msg_label = tkinter.Label(screen, text = msg)
    msg_label.pack(side = 'left')
            #widgets
#Frames
title_frame = tkinter.Frame(screen)
top_frame = tkinter.Frame(screen)
frame_2 = tkinter.Frame(screen)
frame_3 = tkinter.Frame(screen)
frame_4 = tkinter.Frame(screen)
frame_mid = tkinter.Frame(screen)
frame_5 = tkinter.Frame(screen)
frame_6 = tkinter.Frame(screen)
frame_7 = tkinter.Frame(screen)
frame_8 = tkinter.Frame(screen)
frame_9 = tkinter.Frame(screen)
frame_10 = tkinter.Frame(screen)
bottom_frame = tkinter.Frame(screen)
#frame packing
top_frame.pack()
frame_2.pack()
frame_3.pack()
frame_4.pack()
frame_mid.pack()
frame_5.pack()
frame_6.pack()
frame_7.pack()
frame_8.pack()
frame_9.pack()
frame_10.pack()
bottom_frame.pack()
#entry
name_entry = tkinter.Entry(top_frame)
age_entry = tkinter.Entry(frame_2)
weight_entry = tkinter.Entry(frame_3)
height_entry = tkinter.Entry(frame_4)
calorie_entry = tkinter.Entry(frame_mid)
#buttons
low_bt = tkinter.Button(frame_8, text = 'LOW', width=5, command=Low)
med_bt = tkinter.Button(frame_9, text = 'MEDIUM', width=10, command=Medium)
high_bt = tkinter.Button(frame_8, text = 'HIGH', width=5, command=High)
submit_button = tkinter.Button(frame_10, text = 'SUBMIT', width=10, command=finish)
quit_button = tkinter.Button(bottom_frame, text = 'QUIT', width=10, command=screen.destroy)
#labels
name_label = tkinter.Label(top_frame, text = 'Name:')
age_label = tkinter.Label(frame_2, text = 'Age:')
weight_label = tkinter.Label(frame_3, text = 'Weight(kg):')
height_label = tkinter.Label(frame_4, text = 'Height:')
calorie_label = tkinter.Label(frame_mid, text = 'Calorie intake:') 
activity_label = tkinter.Label(frame_5, text = 'Activity level' )
#packing
name_label.pack(side = 'left')
name_entry.pack(side = 'right')
age_label.pack(side = 'left')
calorie_label.pack(side = 'left')
calorie_entry.pack(side = 'right')
age_entry.pack(side = 'right')
weight_label.pack(side = 'left')
weight_entry.pack(side = 'right')
height_label.pack(side = 'left')
height_entry.pack(side = 'right')
activity_label.pack()
quit_button.pack(side = 'left')
low_bt.pack(side = 'left')
med_bt.pack()
high_bt.pack(side = 'right')
submit_button.pack()
screen.mainloop()
