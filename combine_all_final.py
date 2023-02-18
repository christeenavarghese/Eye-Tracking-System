# Import the required libraries

import numpy as np
import cv2
from matplotlib import pyplot as plt
import pygame
from gaze_tracking import GazeTracking
import time
import math
import dlib
import pandas as pd
import tkinter 
from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import pygame
from pygame.locals import *
from PIL import Image, ImageTk
import requests
import os
from io import BytesIO
import multiprocessing

# This is the game part
class game:

    def __init__(self, master):

        # Window
        self.master = master

        # Some Usefull variables
        self.username = StringVar()

        self.password = StringVar()

        self.n_username = StringVar()

        self.n_password = StringVar()

        self.name = StringVar()

        self.age = StringVar()

        self.address = StringVar()

        self.phoneno = StringVar()

        self.pdesc = StringVar()

        self.radio_img = tkinter.StringVar()

        # Create Widgets
        self.widgets()



    # Login Function

    def home(self):
        self.logf.pack_forget()
        self.regpf.pack_forget()
        self.head['text'] = 'Hi ' + self.username.get() + ','
        self.d_homef.pack()



    def list_p(self):

        # Establish Connection
        with sqlite3.connect('demo.db') as db:
            c = db.cursor()



        # Find user If there is any take proper action
        find_user = ('SELECT * FROM patient WHERE doctor_name = ?')
        c.execute(find_user, [(self.username.get())])
        result = c.fetchall()
        if result:
            list_pf = tkinter.Tk()
            i = 0
            for patient in result:
                for j in range(2):
                    e = Label(list_pf, width=10, text=patient[j])
                    e.grid(row=i, column=j)
                i = i+1
        else:
            ms.showerror('Oops!', 'Patients Not Found.')

    def login(self):

        # Establish Connection
        with sqlite3.connect('demo.db') as db:
            c = db.cursor()

        # Find user If there is any take proper action

        find_user = (
            'SELECT * FROM doctor WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            self.home()

        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):
        # Establish Connection
        with sqlite3.connect('demo.db') as db:
            c = db.cursor()

        # Find Existing username if any take proper action

        find_user = ('SELECT username FROM doctor WHERE username = ?')
        c.execute(find_user, [(self.n_username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()

        # Create New Account
        insert = 'INSERT INTO doctor(username,password) VALUES(?,?)'
        c.execute(insert, [(self.n_username.get()), (self.n_password.get())])
        db.commit()



    def reg_p(self):

        self.d_homef.pack_forget()
        self.head['text'] = ""
        self.regpf.pack()



    def reg_p_save(self):

        # Establish Connection
        with sqlite3.connect('demo.db') as db:
            c = db.cursor()



        # Create New Patient
        insert = 'INSERT INTO patient(name,age,address,phoneno,pdesc,doctor_name) VALUES(?,?,?,?,?,?)'
        c.execute(insert, [(self.name.get()), (self.age.get()), (self.address.get(
        )), (self.phoneno.get()), (self.pdesc.get()), (self.username.get())])
        ms.showinfo('Success!', 'Saved!')
        db.commit()



    def therapy(self):
        frame = Frame(self.master, bg='#333333')
        self.root = Toplevel(frame)

        


        # Image urls

        url1 = 'https://aux2.iconspalace.com/uploads/3294896551693360939.png'
        url2 = 'https://aux4.iconspalace.com/uploads/8639213811613443208.png'
        url3 = 'https://aux.iconspalace.com/uploads/1215452205763786920.png'
        url4 = 'https://aux3.iconspalace.com/uploads/6502518841651936763.png'
        url5 = 'https://aux.iconspalace.com/uploads/1344275392089568798.png'        
        url6 = 'https://aux4.iconspalace.com/uploads/750397439839232010.png'



        # Get Images

        mypath1 = requests.get(
            "https://aux2.iconspalace.com/uploads/3294896551693360939.png")
        mypath2 = requests.get(
            "https://aux4.iconspalace.com/uploads/8639213811613443208.png")
        mypath3 = requests.get(
            "https://aux.iconspalace.com/uploads/1215452205763786920.png")       
        mypath4 = requests.get(
            "https://aux3.iconspalace.com/uploads/6502518841651936763.png")    
        mypath5 = requests.get(
            "https://aux.iconspalace.com/uploads/1344275392089568798.png")
        mypath6 = requests.get(
            "https://aux4.iconspalace.com/uploads/750397439839232010.png")



        img1 = Image.open(BytesIO(mypath1.content))
        img2 = Image.open(BytesIO(mypath2.content))
        img3 = Image.open(BytesIO(mypath3.content))
        img4 = Image.open(BytesIO(mypath4.content))
        img5 = Image.open(BytesIO(mypath5.content))
        img6 = Image.open(BytesIO(mypath6.content))

        

        glb_img1 = ImageTk.PhotoImage(img1)
        glb_img2 = ImageTk.PhotoImage(img2)
        glb_img3 = ImageTk.PhotoImage(img3)
        glb_img4 = ImageTk.PhotoImage(img4)
        glb_img5 = ImageTk.PhotoImage(img5)
        glb_img6 = ImageTk.PhotoImage(img6)


        def animation():

            pass       

        def selection() -> Image:

            '''

            This function displays the selected image from the Tkinter window

            to the pygame window.

            '''

            GRAY = (150, 150, 150)
            pygame.init()
            w, h = 640, 640
            screen = pygame.display.set_mode((w, h))
            running = True
            if running == True:

                p1 = multiprocessing.Process(target=eye_Tracking.operate) 
                p1.start()

            img_url = radio_img.get()

            # Downloading selected Image

            response = requests.get(img_url)
            if response.status_code:
                fp = open('image.png', 'wb')
                fp.write(response.content)
                fp.close()

            # Selecting image from the directory

            img_name = 'image.png'
            img = pygame.image.load(img_name)           

            x,y = 200,200
            xv = 5
            yv = -5
            clock = pygame.time.Clock()

            # font type

            x_list = []
            y_list = []
            duration_list = []
            duration_2_list = []

            start_time_2 = pygame.time.get_ticks()
            start_time_3 = time.time()

            writer_2 = pd.ExcelWriter('./game_2.xlsx')

            font = pygame.font.Font('freesansbold.ttf', 32)
            while running:

                position = font.render("Position" +str(x)+','+str(y) , True, (255, 255, 255))
                screen.blit(position, (100, 100))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False
                screen.blit(img,(x,y))
                pygame.display.flip()
                movement = mvmnt.get()        


                if movement == 'V':
                    y += yv
                    x_list.append(x)
                    y_list.append(y)
                    duration = pygame.time.get_ticks() -  start_time_2         
                    duration_rounded = round(duration, 2)                      
                    duration_list.append(duration_rounded)                     

                    duration_2 = time.time() - start_time_3                    
                    duration_2_rounded = round(duration_2, 2)                  
                    duration_2_list.append(duration_2_rounded)                 
                    

                elif movement == 'H':
                    x += xv
                    x_list.append(x)
                    y_list.append(y)
                    duration = pygame.time.get_ticks() -  start_time_2         
                    duration_rounded = round(duration, 2)                      
                    duration_list.append(duration_rounded)                     

                    duration_2 = time.time() - start_time_3                    
                    duration_2_rounded = round(duration_2, 2)                  
                    duration_2_list.append(duration_2_rounded)                 

                    
                else:
                    y += yv
                    x += xv
                    y_list.append(y)
                    x_list.append(x)
                    duration =  pygame.time.get_ticks() -  start_time_2      
                    duration_rounded = round(duration, 2)                    
                    duration_list.append(duration_rounded)                   

                    duration_2 = time.time() - start_time_3                    
                    duration_2_rounded = round(duration_2, 2)                  
                    duration_2_list.append(duration_2_rounded)                 


                if x>490 or x<10:
                    xv *= -1

                if y>490 or y<10:
                    yv *= -1               

                screen.fill(GRAY)               
               
                speed = spd.get()


                if speed == 'High':
                    clock.tick(100)
                    #print(x,y)

                elif speed == 'Medium':
                    clock.tick(50)
                    #print(x,y)

                else:
                    clock.tick(5)
                    #print(x,y)

                    
            game_coor_x_1 = pd.DataFrame(x_list)
            game_coor_y_1 = pd.DataFrame(y_list)
            game_duration_1 = pd.DataFrame(duration_list)       
            game_duration_1_2 = pd.DataFrame(duration_2_list)   

            game_coor_x = game_coor_x_1.iloc[186:]                            
            game_coor_y = game_coor_y_1[186:]                                 
            game_duration = game_duration_1[186:]                             
            game_duration_3 = game_duration_1_2.iloc[186:]    

            game_coor_x.to_excel(writer_2, sheet_name = 'data1', startrow=0, startcol=0, header = True, index = False)
            game_coor_y.to_excel(writer_2, sheet_name = 'data1', startrow=0, startcol=1, header = True, index = False)
            game_duration.to_excel(writer_2, sheet_name = 'data1', startrow=0, startcol=2, header = True, index = False)  
            game_duration_3.to_excel(writer_2, sheet_name = 'data1', startrow=0, startcol=3, header = True, index = False)  
            
            pygame.quit()
            # removing the image
            os.remove(img_name)

            # record number of looking right in game
            game_looking_right = 0 # game looking right
            
            for i in range(len(game_coor_x)):
                # if x_list[i+186] == 495: # kinda working
                counter_game = i*15
                if counter_game < len(game_coor_x): 
                    if x_list[counter_game] >= 425 and x_list[counter_game] <= 495:
                        game_looking_right += 1
                        # print(f"this is game looking right: {game_looking_right}")
                elif counter_game >= len(game_coor_x):
                    if x_list[len(game_coor_x)] >= 425 and x_list[len(game_coor_x)] <= 495:
                        game_looking_right += 1
                        # print(f"this is game looking right: {game_looking_right}")
                        break

            game_looking_right_list = []
            game_looking_right_list.append(game_looking_right)
            game_looking_right_list = pd.DataFrame(game_looking_right_list)
            game_looking_right_list.to_excel(writer_2, sheet_name = 'data1', startrow = 0, startcol = 5, header = True, index = False)

            # record number of looking left in game
            game_looking_left = 0 
            
            for i in range(len(game_coor_x)):
                counter_game = i*15
                if counter_game < len(game_coor_x): 
                    if x_list[counter_game] >= 0 and x_list[counter_game] <= 70:
                        game_looking_left += 1
                        # print(f"this is game looking left: {game_looking_left}")
                elif counter_game >= len(game_coor_x):
                    if x_list[len(game_coor_x)] >= 0 and x_list[len(game_coor_x)] <= 70:
                        game_looking_left += 1
                        # print(f"this is game looking left: {game_looking_left}")
                        break

            # record number of looking center in game
            game_looking_center = 0 
            
            for i in range(len(game_coor_x)):
                counter_game = i*15
                if counter_game < (len(game_coor_x)): 
                    if (x_list[counter_game] >= 165 and x_list[counter_game] <= 235) and (y_list[counter_game]>= 165 and y_list[counter_game] <= 235):
                        game_looking_center += 1
                        # print(f"this is game looking center: {game_looking_center}")
                elif counter_game >= (len(game_coor_x)):
                    if (x_list[len(game_coor_x)] >= 165 and x_list[len(game_coor_x)]<= 235) and (y_list[len(game_coor_x)] >= 165 and y_list[len(game_coor_x)] <= 235):
                        game_looking_center += 1
                        # print(f"this is game looking center: {game_looking_center}")
                        break
            
            # record number of looking up in game
            game_looking_up = 0 
            
            for i in range(len(game_coor_y)):
                counter_game = i*15
                if counter_game < (len(game_coor_y)): 
                    if (y_list[counter_game] >= 425 and y_list[counter_game] <= 495) :
                        game_looking_up += 1
                        # print(f"this is game looking up: {game_looking_up}")
                elif counter_game >= (len(game_coor_y)):
                    if (y_list[len(game_coor_x)] >= 425 and y_list[len(game_coor_x)] <= 495):
                        game_looking_up += 1
                        # print(f"this is game looking up: {game_looking_up}")
                        break

            # record number of looking down in game
            game_looking_down = 0 
            
            for i in range(len(game_coor_y)):
                counter_game = i*15
                if counter_game < (len(game_coor_y)): 
                    if (y_list[counter_game] >= 0 and y_list[counter_game] <= 75) :
                        game_looking_down += 1
                        # print(f"this is game looking down: {game_looking_down}")
                elif counter_game >= (len(game_coor_y)):
                    if (y_list[len(game_coor_x)] >= 0 and y_list[len(game_coor_x)] <= 75):
                        game_looking_down += 1
                        # print(f"this is game looking down: {game_looking_down}")
                        break

            game_looking_right_list = []
            game_looking_left_list = []
            game_looking_center_list = []
            game_looking_up_list = []
            game_looking_down_list = []


            game_looking_right_list.append(game_looking_right)
            game_looking_left_list.append(game_looking_left)
            game_looking_center_list.append(game_looking_center)
            game_looking_up_list.append(game_looking_up)
            game_looking_down_list.append(game_looking_down)

            
            game_looking_right_list = pd.DataFrame(game_looking_right_list)
            game_looking_left_list = pd.DataFrame(game_looking_left_list)
            game_looking_center_list = pd.DataFrame(game_looking_center_list)
            game_looking_up_list = pd.DataFrame(game_looking_up_list)
            game_looking_down_list = pd.DataFrame(game_looking_down_list)


            game_looking_right_list.to_excel(writer_2, sheet_name = 'data1', startrow = 0, startcol = 7, header = True, index = False)
            game_looking_left_list.to_excel(writer_2, sheet_name = 'data1', startrow = 0, startcol = 5, header = True, index = False)
            game_looking_center_list.to_excel(writer_2, sheet_name = 'data1', startrow = 0, startcol = 6, header = True, index = False)
            game_looking_up_list.to_excel(writer_2, sheet_name = 'data1', startrow = 0, startcol = 9, header = True, index = False)
            game_looking_down_list.to_excel(writer_2, sheet_name = 'data1', startrow = 0, startcol = 10, header = True, index = False)


            writer_2.save()        


        #Radio Buttons Character

        radio_img = tkinter.StringVar()
        radio_img.set(None)
        c1 = tkinter.Radiobutton(self.root, text='', image=glb_img1, variable=radio_img,
                value=url1)
        c1.grid(row=2, column=2)

        c2 = tkinter.Radiobutton(self.root, text='', image=glb_img2, variable=radio_img,
                value=url2)
        c2.grid(row=2, column=4)
        
        c3 = tkinter.Radiobutton(self.root, text='', image=glb_img3, variable=radio_img,
                value=url3)
        c3.grid(row=2, column=6)
        
        c4 = tkinter.Radiobutton(self.root, text='', image=glb_img4, variable=radio_img,
               value=url4)
        c4.grid(row=6, column=2)
        
        c5 = tkinter.Radiobutton(self.root, text='', image=glb_img5, variable=radio_img,
               value=url5)
        c5.grid(row=6, column=4)
        
        c6 = tkinter.Radiobutton(self.root, text='', image=glb_img6, variable=radio_img,
                value=url6)
        c6.grid(row=6, column=6)
        
        
        

        #Movement
        mvmnt  = tkinter.StringVar()
        mvmnt.set(None)
        mvmnt1 = tkinter.Radiobutton(self.root, text='Horizontal', variable=mvmnt,
                value='H')
        mvmnt1.grid(row=8, column=2)
        
        mvmnt2 = tkinter.Radiobutton(self.root, text='Veritical', variable=mvmnt,
                value='V')
        mvmnt2.grid(row=8, column=4)    

        mvmnt3 = tkinter.Radiobutton(self.root, text='Free', variable=mvmnt,
                value='F')
        mvmnt3.grid(row=8, column=6)



        #speed

        spd = tkinter.StringVar()
        spd.set(None)
        sp1 = tkinter.Radiobutton(self.root, text='High', variable= spd,
                value='High')
        sp1.grid(row=10, column=2)
        
        sp2 = tkinter.Radiobutton(self.root, text='Medium', variable= spd,
                value='Medium')
        sp2.grid(row=10, column=4)

        sp3 = tkinter.Radiobutton(self.root, text='Low', variable= spd,
                value='Low')
        sp3.grid(row=10, column=6)

        # B1 = Button(self.root, text = ' Run ',bg="#0000FF", fg="#FFFFFF", font=("Times", 16), command=selection)
        B1 = Button(self.root, text = ' Run ',fg= "red", highlightbackground = "white", font=("Times", 16), command=selection)

        B1.grid(row=14, column=2)
        
        root.mainloop()



   # Frame Packing Methords

    def log(self):

        self.username.set('')
        self.password.set('')
        self.regf.pack_forget()
        self.head['text'] = 'Sign In'
        self.logf.pack()



    def reg(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.regf.pack()



    def regp(self):
        self.name.set('')
        self.age.set('')
        self.address.set('')
        self.phoneno.set('')
        self.pdesc.set('')
        self.regpf.pack_forget()
        self.head['text'] = 'Register Patient'
        self.regpf.pack()
    

    def logout(self):
        
        self.d_homef.pack_forget()
        self.username.set('')
        self.password.set('')
        self.regf.pack_forget()
        self.head['text'] = 'Sign In'
        self.logf.pack()

        
    # Draw Widgets

    def widgets(self):
        self.head = Label(self.master, text="Sign In", bg='#343434', fg="#EF2E05", font=("Times", 38))
        self.head.pack()
        self.logf = Frame(self.master, bg='#333333')
        Label(self.logf, text="Username", bg='#343434', fg="#FFFFFF", font=("Arial", 16)).grid(sticky = W, pady=5)
        Entry(self.logf, textvariable = self.username,font = ('Arial',15)).grid(row=0,column=1, pady=5)
        Label(self.logf, text = 'Password: ', bg='#343434', fg="#FFFFFF", font=("Arial", 16)).grid(sticky = W, pady=5)
        Entry(self.logf, textvariable = self.password,font = ('Arial',15),show = '*').grid(row=1,column=1)
        # Button(self.logf, text = ' Login ',bg="#EF2E05", fg="#FFFFFF", font=("Times", 16), command=self.login).grid( pady=5)
        Button(self.logf, text = ' Login ',fg= "blue", highlightbackground = "white", font=("Times", 16), command=self.login).grid( pady=5)
        # Button(self.logf, text = ' Create Account ', bg='#269400', fg="#FFFFFF", font=("Arial", 16), command=self.reg).grid(row=2,column=1, pady=5)
        Button(self.logf, text = ' Create Account ',fg= "blue", highlightbackground = "white", font=("Arial", 16), command=self.reg).grid(row=2,column=1, pady=5)


        self.logf.pack()

        self.regf = Frame(self.master, padx =10,pady = 10, bg='#333333')
        Label(self.regf, text = 'Username: ', bg='#343434', fg="#FFFFFF", font=("Arial", 16),pady=5,padx=5).grid(sticky = W)
        Entry(self.regf, textvariable = self.n_username,font = ('Arial',15)).grid(row=0,column=1)
        Label(self.regf, text = 'Password: ',bg='#343434', fg="#FFFFFF", font=("Arial", 16),pady=5,padx=5).grid(sticky = W)
        Entry(self.regf, textvariable = self.n_password, font = ('Arial',15),show = '*').grid(row=1,column=1)
        # Button(self.regf, text = 'Create Account', bg='#269400', fg="#FFFFFF", font=("Arial", 16),command=self.new_user).grid()
        Button(self.regf, text = 'Create Account',fg= "blue", highlightbackground = "white", font=("Arial", 16),command=self.new_user).grid()
        # Button(self.regf, text = 'Go to Login', bg="#EF2E05", fg="#FFFFFF", font=("Times", 16), padx=5,pady=5,command=self.log).grid(row=2,column=1)
        Button(self.regf, text = 'Go to Login',fg= "red", highlightbackground = "white", font=("Times", 16), padx=5,pady=5,command=self.log).grid(row=2,column=1)



        self.d_homef = Frame(self.master, bg='#333333')
        # Button(self.d_homef, text = 'Register Patient', bg='#269400', fg="#FFFFFF", font=("Arial", 16), width=20,command=self.reg_p).grid(pady=5)
        Button(self.d_homef, text = 'Register Patient',fg= "blue", highlightbackground = "white", font=("Arial", 16), width=20,command=self.reg_p).grid(pady=5)
        # Button(self.d_homef, text = 'View Patient Record', bg='#269400', fg="#FFFFFF", font=("Arial", 16), width=20,command=self.list_p).grid(pady=5)
        Button(self.d_homef, text = 'View Patient Record',fg= "blue", highlightbackground = "white", font=("Arial", 16), width=20,command=self.list_p).grid(pady=5)
        # Button(self.d_homef, text = 'Start Therapy', bg='#269400', fg="#FFFFFF", font=("Arial", 16), width=20,command=self.therapy).grid(pady=5)
        Button(self.d_homef, text = 'Start Therapy',fg= "blue", highlightbackground = "white", font=("Arial", 16), width=20,command=self.therapy).grid(pady=5)
        # Button(self.d_homef, text = 'Logout', bg='#269400', fg="#FFFFFF", font=("Arial", 16), width=20,command=self.reg_p).grid(pady=5)
        # Button(self.d_homef, text = 'Logout',fg= "blue", highlightbackground = "white", font=("Arial", 16), width=20,command=self.reg_p).grid(pady=5)
        Button(self.d_homef, text = 'Logout',fg= "blue", highlightbackground = "white", font=("Arial", 16), width=20,command=self.logout).grid(pady=5)



        self.regpf = Frame(self.master, bg='#333333')

        Label(self.regpf, text = 'Name: ', bg='#343434', fg="#FFFFFF", font=("Arial", 16),pady=5,padx=5).grid(sticky = W)
        Entry(self.regpf, textvariable = self.name,font = ('Arial',15)).grid(row=0,column=1)
        Label(self.regpf, text = 'Age: ',bg='#343434', fg="#FFFFFF", font=("Arial", 16),pady=5,padx=5).grid(sticky = W)
        Entry(self.regpf, textvariable = self.age, font = ('Arial',15)).grid(row=1,column=1)
        Label(self.regpf, text = 'Address: ', bg='#343434', fg="#FFFFFF", font=("Arial", 16),pady=5,padx=5).grid(sticky = W)
        Entry(self.regpf, textvariable = self.address,font = ('Arial',15)).grid(row=2,column=1)
        Label(self.regpf, text = 'Contact Number: ',bg='#343434', fg="#FFFFFF", font=("Arial", 16),pady=5,padx=5).grid(sticky = W)
        Entry(self.regpf, textvariable = self.phoneno, font = ('Arial',15)).grid(row=3,column=1)
        Label(self.regpf, text = 'Problem Description: ', bg='#343434', fg="#FFFFFF", font=("Arial", 16),pady=5,padx=5).grid(sticky = W)
        Entry(self.regpf, textvariable = self.pdesc, font = ('Arial',15)).grid(row=4,column=1)
        Button(self.regpf, text = 'Save', fg= "blue", highlightbackground = "white", font=("Arial", 16),command=self.reg_p_save).grid(row=5)
        # Button(self.regpf, text = 'Save', bg='#269400', fg="#FFFFFF", font=("Arial", 16),command=self.reg_p_save).grid(row=5)
        Button(self.regpf, text = 'Home', fg= "blue", highlightbackground = "white", font=("Arial", 16),command=self.home).grid(row=5, column=2)
        # Button(self.regpf, text = 'Home', bg='#C70039', fg="#FFFFFF", font=("Arial", 16),command=self.home).grid(row=5, column=2)

# This is the eye tracking part
class eye_Tracking:

    def operate():
        
        ESCAPE_KEY = 27
        POINTS_NUM_LANDMARK = 68


        k=1
        sumx=0
        sumy=0
        orn=2 # 7, frame / s

        cap = cv2.VideoCapture(0)
        gaze = GazeTracking()

        detector = dlib.get_frontal_face_detector()
        # predictor = dlib.shape_predictor("./gaze_tracking/trained_models/shape_predictor_68_face_landmarks.dat")
        predictor = dlib.shape_predictor("./gaze_tracking/shape_predictor_68_face_landmarks.dat")


        start_time = time.time()

        eye_x_positions = list()
        eye_y_positions = list()
        time_stamp = list()
        game_start_time = time.time()

        while True:

            # This is the part for the pose estimation, head tracking.

            def get_image_points(img, detector, predictor, POINTS_NUM_LANDMARK):

                def _largest_face(dets):
                    if len(dets) == 1:
                        return 0

                    face_areas = [ (det.right()-det.left())*(det.bottom()-det.top()) for det in dets]

                    largest_area = face_areas[0]
                    largest_index = 0
                    for index in range(1, len(dets)):
                        if face_areas[index] > largest_area :
                            largest_index = index
                            largest_area = face_areas[index]

                    # print("largest_face index is {} in {} faces".format(largest_index, len(dets)))

                    return largest_index
                
                
                def get_image_points_from_landmark_shape(landmark_shape):
                    if landmark_shape.num_parts != POINTS_NUM_LANDMARK:
                        print("ERROR:landmark_shape.num_parts-{}".format(landmark_shape.num_parts))
                        return -1, None
                
                    #2D image points. If you change the image, you need to change vector
                    image_points = np.array([
                                            (landmark_shape.part(30).x, landmark_shape.part(30).y),     # Nose tip
                                            (landmark_shape.part(8).x, landmark_shape.part(8).y),       # Chin
                                            (landmark_shape.part(36).x, landmark_shape.part(36).y),     # Left eye left corner
                                            (landmark_shape.part(45).x, landmark_shape.part(45).y),     # Right eye right corne
                                            (landmark_shape.part(48).x, landmark_shape.part(48).y),     # Left Mouth corner
                                            (landmark_shape.part(54).x, landmark_shape.part(54).y)      # Right mouth corner
                                        ], dtype="double")

                    return 0, image_points
                                    
                dets = detector(img, 1)

                if 0 == len( dets ):
                    print( "ERROR: found no face" )
                    return -1, None
                largest_index = _largest_face(dets)
                face_rectangle = dets[largest_index]

                landmark_shape = predictor(img, face_rectangle)

                return get_image_points_from_landmark_shape(landmark_shape)


            # Get rotation vector and translation vector                    
            def get_pose_estimation(img_size, image_points ):
                # 3D model points.
                model_points = np.array([
                                        (0.0, 0.0, 0.0),             # Nose tip
                                        (0.0, -330.0, -65.0),        # Chin
                                        (-225.0, 170.0, -135.0),     # Left eye left corner
                                        (225.0, 170.0, -135.0),      # Right eye right corne
                                        (-150.0, -150.0, -125.0),    # Left Mouth corner
                                        (150.0, -150.0, -125.0)      # Right mouth corner
                                    
                                    ])
            
                # Camera internals
            
                focal_length = img_size[1]
                center = (img_size[1]/2, img_size[0]/2)
                camera_matrix = np.array(
                                    [[focal_length, 0, center[0]],
                                    [0, focal_length, center[1]],
                                    [0, 0, 1]], dtype = "double"
                                    )
            
                # print("Camera Matrix :{}".format(camera_matrix))
            
                dist_coeffs = np.zeros((4,1)) # Assuming no lens distortion
                (success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE )

                # print("Rotation Vector:\n {}".format(rotation_vector))
                # print("Translation Vector:\n {}".format(translation_vector))
                return success, rotation_vector, translation_vector, camera_matrix, dist_coeffs

            # Convert from rotation vector to Euler angles
            def get_euler_angle(rotation_vector, ret):
        
                # calculate rotation angles
                theta = cv2.norm(rotation_vector, cv2.NORM_L2)
            
                # transformed to quaterniond
                w = math.cos(theta / 2)
                x = math.sin(theta / 2)*rotation_vector[0][0] / theta
                y = math.sin(theta / 2)*rotation_vector[1][0] / theta
                z = math.sin(theta / 2)*rotation_vector[2][0] / theta
            
                ysqr = y * y
                # pitch (y-axis rotation)
                t0 = 2.0 * (w * x + y * z)
                t1 = 1.0 - 2.0 * (x * x + ysqr)
                # print('t0:{}, t1:{}'.format(t0, t1))
                pitch = math.atan2(t0, t1)
                
                # yaw (x-axis rotation)
                t2 = 2.0 * (w * y - z * x)
                if t2 > 1.0:
                    t2 = 1.0
                if t2 < -1.0:
                    t2 = -1.0
                # yaw = math.asin(t2) # original
                yaw = - math.asin(t2) # due to mirroring, make some changes to negative to mirror
                
                # roll (z-axis rotation)
                t3 = 2.0 * (w * z + x * y)
                t4 = 1.0 - 2.0 * (ysqr + z * z)
                roll = math.atan2(t3, t4)
                
                # print('pitch:{}, yaw:{}, roll:{}'.format(pitch, yaw, roll))
                
                # Unit conversion: convert radians to degrees
                Y = int((pitch/math.pi)*180)
                X = int((yaw/math.pi)*180)
                Z = int((roll/math.pi)*180)

                return ret, Y, X, Z

            # Read Image
            ret, im = cap.read()
            im = cv2.flip(im, 1)
            if ret != True:
                print('read frame failed')
                continue
            size = im.shape
                
            if size[0] > 700:
                h = size[0] / 3
                w = size[1] / 3
                im = cv2.resize( im, (int( w ), int( h )), interpolation=cv2.INTER_CUBIC )
                size = im.shape
            
            ret, image_points = get_image_points(im, detector, predictor, POINTS_NUM_LANDMARK)
            if ret != 0:
                print('get_image_points failed')
                continue
                
            ret, rotation_vector, translation_vector, camera_matrix, dist_coeffs = get_pose_estimation(size, image_points)
            if ret != True:
                print('get_pose_estimation failed')
                continue
            used_time = time.time() - start_time
            # print("used_time:{} sec".format(round(used_time, 3)))
                
            ret, pitch, yaw, roll = get_euler_angle(rotation_vector, ret)
         

            yaw_condition = yaw >= -5 and yaw <=5
            pitch_condition_1 = pitch >= 170 and pitch <= 180
            pitch_condition_2 = pitch <= -170 and pitch >= -180
            pitch_condition = pitch_condition_1 or pitch_condition_2

            if yaw_condition == True and pitch_condition == True:
                euler_angle_str = 'Y:{}, X:{}, Z:{}'.format(pitch, yaw, roll)
                print(euler_angle_str)
                cv2.putText( im, "GOOD!", (0, 80), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                cv2.putText( im, euler_angle_str, (0, 120), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2 )

            elif yaw_condition == False and pitch_condition == True:
                print(f"X not in range.")
                euler_angle_str = 'Y:{}, X:{}, Z:{}'.format(pitch, yaw, roll)
                cv2.putText( im, "X not in range", (0, 80), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                cv2.putText( im, euler_angle_str, (0, 120), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2 )

            
            elif yaw_condition == True and pitch_condition == False:
                print(f"Y not in range.")
                euler_angle_str = 'Y:{}, X:{}, Z:{}'.format(pitch, yaw, roll)
                cv2.putText( im, "Y not in range", (0, 80), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                cv2.putText( im, euler_angle_str, (0, 120), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2 )

            else:
                print(f"Nothing is in range")
                euler_angle_str = 'Y:{}, X:{}, Z:{}'.format(pitch, yaw, roll)
                cv2.putText( im, "Nothing is in range.", (0, 80), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                cv2.putText( im, euler_angle_str, (0, 120), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2 )

                
            # Project a 3D point (0, 0, 1000.0) onto the image plane.
            # We use this to draw a line sticking out of the nose
            # translation_vector = cv2.flip(translation_vector, 1)
            (nose_end_point2D, jacobian) = cv2.projectPoints(np.array([(0.0, 0.0, 1000.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)
                
            for p in image_points:
                cv2.circle(im, (int(p[0]), int(p[1])), 3, (0,0,255), -1)
                
                
            p1 = ( int(image_points[0][0]), int(image_points[0][1]))
            p2 = ( int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))
                
            cv2.line(im, p1, p2, (255,0,0), 2)
                
            # Display image
            # cv2.putText( im, str(rotation_vector), (0, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1 )
            # cv2.putText( im, euler_angle_str, (0, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1 )
            cv2.imshow("Head Tracking", im)
            cv2.moveWindow("Head Tracking", 1250, 50) # set the initial position so that it is in the top right placement.

            start_time = time.time()

            # We get a new frame from the webcam
            success, framecv = cap.read()
            framecv = cv2.flip(framecv,1) # part where we do the flipping of the frame
            
            frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            frame_fps = cap.get(cv2.CAP_PROP_FPS)
            # print(f' This is the width: {frame_width} , this is the height: {frame_height}, this is the fps {frame_fps}') 
            # video taken in 30 fps, reso default 1280 x 720 

            # We send this frame to GazeTracking to analyze it
            gaze.refresh(framecv)

            framecv = gaze.annotated_frame()
            text = ""

            if gaze.is_blinking():
                text = "Blinking"
            
            elif gaze.is_right():
                text = "Looking right"
       
            elif gaze.is_left():
                text = "Looking left"
         
            elif gaze.is_center():
                text = "Looking center"

            cv2.putText(framecv, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

            left_pupil = gaze.pupil_left_coords()
            right_pupil = gaze.pupil_right_coords()
            cv2.putText(framecv, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
            cv2.putText(framecv, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

            # cv2.imshow("Demo", framecv)

            resize_main = cv2.resize(framecv.copy(), (640, 360))
            cv2.imshow("Resized Demo", resize_main)
            cv2.moveWindow("Resized Demo", 10, 600)
            
            
            frame_1 = framecv
            roi = frame_1[275:375 , 525:625]
            
            resized1 = cv2.resize(roi, (200,200), interpolation = cv2.INTER_AREA)
            # print(f'This is the shape of resized1: {resized1.shape}')
            
            # The pink diamond thingy in the Eye screen
            cv2.circle(resized1, (190, 127), 1, (155, 155, 255), 4) # 160, 127 # 190 127
            cv2.circle(resized1, (60, 127), 1, (155, 155, 255), 4) # 50, 127 # 60 127
            # cv2.imshow("Parça",resized1)
            
            resized2 = resized1[80:200 , 50:200] # 80:170 , 50:160 for zoom in and zoom out area of the eye
            # cv2.imshow("resized2", resized2)

            resized = cv2.resize(resized2, (440,360), interpolation = cv2.INTER_AREA)
            # cv2.imshow("Eye_before", resized)
            
            rows,cols,_ = resized1.shape
            gray1 = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
            # cv2.imshow("grayscaled", gray1)

            # some sort of smoothing
            eye_blur = cv2.bilateralFilter(gray1, 5, 800, 800) # real time applicatio use d = 5, use high value for sigma above 150 have cartoonish effect
            # eye_blur = cv2.bilateralFilter(gray1,  10, 195,195) # last used
            # cv2.imshow("eye_blur",eye_blur)
            
            img_blur = cv2.Canny(eye_blur, 15,55) # threshold1 smallest used for edge linking, largest threshold uses initial segments of strong edges.
            # img_blur1 = cv2.Canny(eye_blur,10,30) # last used
            # img_blur2 = cv2.Canny(eye_blur,15,70) 
            # cv2.imshow('Canny', img_blur)
                        
            circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 2, 800, param1=500, param2=10, minRadius=50, maxRadius=60) #  0.1, 400, param1=200, param2=10, minRadius=76, maxRadius=84) # 50, 60
            # dp = 2 accumulator half as big width and height 
            # minDist between the center of the circle = 800, need to be really large because we don't want to detect any neighbouring circles as we only have one iris to detect
            # param1 for this as we only can use Hough gradient it is the higher threshold value used in canny maybe change it to 55? Does not affect anything 
            # param2 must be reached in order to form a line just make it small maybe 1, doesn't seem to have any difference

            if circles is not None:
                circles = np.uint16(np.around(circles))
                # print(f'This is circles: {circles}')
                for i in circles[0, :]:
                    # print(i)
                    # print(f' this is i0: {i[0]}, this is i1: {i[1]}, this is i2: {i[2]}')
                    cv2.circle(resized, (i[0], i[1]), i[2], (0, 255, 0), 2) # green outline
                    cv2.circle(resized, (i[0], i[1]), 2, (0, 0, 255), 5) # red dot
                    # print(f"The coordinate of the pupil in the isolated screen: x : {i[0]} y: {i[1]}")

                    if k==orn:
                        k=1
                        sumx=sumx/orn
                        sumx=round(sumx,2)
                        sumy=sumy/orn
                        sumy=round(sumy,2)
                        print("_______\n",sumx,sumy,"\n_______")
                        eye_x_p=round((sumx),2) #sumx-145
                        #eye_y_p=(sumy-62)
                        eye_y_p=round((sumy),2) #sumy-145
                        print(f"The coordinate of the pupil in the isolated screen: x : {eye_x_p} y: {eye_y_p}")
                        
                        run_time = time.time() -  game_start_time 
                        run_time_rounded = round(run_time, 2)
                        # print(f"Run time is :{run_time_rounded} sec")
                        
                        if yaw_condition == True and pitch_condition == True:
                            eye_x_positions.append(eye_x_p)
                            eye_y_positions.append(eye_y_p)
                            time_stamp.append(run_time_rounded)
                        
                    elif k==0:
                        sumx=0
                        sumy=0
                        k=k+1
                        
                    elif k==1:
                        sumx=sumx+i[0]
                        sumy=sumy+i[1]
                        k=k+1
                        
                    else:
                        sumx=sumx+i[0]
                        sumy=sumy+i[1]
                        k=k+1
                    
                    cv2.putText(frame_1, str(i[0]) , (200,30), cv2.FONT_HERSHEY_SIMPLEX,0.5, (155, 255, 0), 2)
                    cv2.putText(frame_1, str(i[1]) , (200,50), cv2.FONT_HERSHEY_SIMPLEX,0.5, (155, 255, 0), 2)
            
            cv2.imshow("Eye", resized)
            cv2.moveWindow("Eye", 50, 50) # set the initial position so that it is in the top left placement.
            # cv2.imshow("Roi", resized1)

            # Ending the eye tracking and head tracking part to save it into an excel file for data processing            
            if cv2.waitKey(1) == 27:
                
                eye_x_positions_1 = pd.DataFrame(eye_x_positions)
                eye_y_positions_1 = pd.DataFrame(eye_y_positions)
                time_stamp_1 = pd.DataFrame(time_stamp)

                writer = pd.ExcelWriter('./Output_5.xlsx')

                time_stamp_1.to_excel(writer, sheet_name='data1', startrow=0, startcol=0, header=True, index=False)
                eye_x_positions_1.to_excel(writer, sheet_name = 'data1', startrow=0, startcol=1, header = True, index = False)
                eye_y_positions_1.to_excel(writer, sheet_name = 'data1', startrow=0, startcol=2, header = True, index = False)

                left_eye_track = 0 # looking left
                
                for i in range(len(eye_x_positions_1)):
                    #print(eye_x_positions_1)
                    # if eye_x_positions[i] >= 140 and eye_x_positions[i] < 210:
                    # if eye_x_positions[i] >= 90 and eye_x_positions[i] < 150:
                    if eye_x_positions[i] >= 90 and eye_x_positions[i] < 210:
                        left_eye_track += 1
                        # print(f"this is left_eye_track: {left_eye_track}")

                left_eye_track_list = []
                left_eye_track_list.append(left_eye_track)
                left_eye_track_list = pd.DataFrame(left_eye_track_list)
                left_eye_track_list.to_excel(writer, sheet_name = 'data1', startrow = 0, startcol = 4, header = True, index = False)
                
                center_eye_track = 0 # looking center

                for i in range(len(eye_x_positions_1)):
                    #print(eye_x_positions_1)
                    # if eye_x_positions[i] >= 210 and eye_x_positions[i] <= 280:
                    if (eye_x_positions[i] >= 210 and eye_x_positions[i] <= 280) and (eye_y_positions[i] >= 110 and eye_y_positions[i] < 200): 
                    #if (eye_x_positions[i] >= 150 and eye_x_positions[i] <= 210) and (eye_y_positions[i] >= 110 and eye_y_positions[i] < 175):
                        center_eye_track += 1
                        # print(f"this is center_eye_track: {center_eye_track}")

                center_eye_track_list = []
                center_eye_track_list.append(center_eye_track)
                center_eye_track_list = pd.DataFrame(center_eye_track_list)
                center_eye_track_list.to_excel(writer, sheet_name = 'data1', startrow = 0, startcol = 5, header = True, index = False)

                right_eye_track = 0 # looking right

                for j in range(len(eye_x_positions_1)):
                    #print(eye_x_positions_1)
                    if eye_x_positions[j] > 280 and eye_x_positions[j] <= 350:
                    # if eye_x_positions[j] > 210 and eye_x_positions[j] <= 300:

                        right_eye_track += 1
                        # print(f"this is right_eye_track: {right_eye_track}")
                
                right_eye_track_list = []
                right_eye_track_list.append(right_eye_track)
                right_eye_track_list = pd.DataFrame(right_eye_track_list)
                right_eye_track_list.to_excel(writer, sheet_name = 'data1', startrow = 0, startcol = 6, header = True, index = False)

                up_eye_track = 0 # looking up
                
                for i in range(len(eye_y_positions_1)):
                    #print(eye_y_positions_1)
                    if eye_y_positions[i] >= 50 and eye_y_positions[i] < 110:
                        up_eye_track += 1
                        # print(f"this is up_eye_track: {up_eye_track}")

                up_eye_track_list = []
                up_eye_track_list.append(up_eye_track)
                up_eye_track_list = pd.DataFrame(up_eye_track_list)
                up_eye_track_list.to_excel(writer, sheet_name = 'data1', startrow = 0, startcol = 8, header = True, index = False)

                down_eye_track = 0 # looking down
                
                for i in range(len(eye_y_positions_1)):
                    #print(eye_y_positions_1)
                    if eye_y_positions[i] >= 200 and eye_y_positions[i] < 250:
                        down_eye_track += 1
                        # print(f"this is down_eye_track: {down_eye_track}")

                down_eye_track_list = []
                down_eye_track_list.append(down_eye_track)
                down_eye_track_list = pd.DataFrame(down_eye_track_list)
                down_eye_track_list.to_excel(writer, sheet_name = 'data1', startrow = 0, startcol = 9, header = True, index = False)

                writer.save()

                break


        # Plotting blue dots
        data_all = list(zip(eye_x_positions,eye_y_positions ))
        print(data_all)

        plt.scatter(eye_x_positions, eye_y_positions, c= 'blue', marker= 'o')
        plt.title("Pupil position in the Eye window", fontweight='bold')
        plt.xlabel("X position", style='italic', fontsize = 10)
        plt.ylabel("Y position", style='italic', fontsize = 10)
        plt.grid('on','both')
        plt.axis([0, 440, 360, 0]) # edit this
        plt.show()

        # Plotting the "heat map"
        # x_axis_labels = [0,10,20,30,40,50,60,70,80,90,100] 
        # y_axis_labels = [0,2.5,5,7.5,10,12.5,15,17.5,20]
        # sns.heatmap(data_all, xticklabels=x_axis_labels, yticklabels=y_axis_labels, cbar=False)
        # plt.xlabel("X position")
        # plt.ylabel("Y position")
        # plt.show()  

        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
       # Create Object
       # and setup window
    with sqlite3.connect('demo.db') as db:
        c = db.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS doctor (username TEXT NOT NULL PRIMARY KEY,password TEXT NOT NULL);')
    c.execute('CREATE TABLE IF NOT EXISTS patient (name TEXT NOT NULL PRIMARY KEY, age TEXT NOT NULL, address TEXT NOT NULL, phoneno TEXT NOT NULL, pdesc TEXT NOT NULL,doctor_name TEXT NOT NULL, FOREIGN KEY(doctor_name) REFERENCES doctor(username));')
    db.commit()
    db.close()

    root = Tk()
    root.title('Login Form')
    root.geometry("440x440+650+250") # width x height; so that the home button can be seen; make it so that it is center to screen
    root.configure(bg='#333333')
    thegame = game(root)
    root.mainloop()