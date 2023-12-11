from tkinter import *
from PIL import ImageTk, Image
import bonggoQuery
import psutil
import os
import  datetime
import webbrowser
import subprocess

class HoleBody: 

    def groupedBoxes(self, x1,y1, con):
        self.social_media_frame =Frame(self.canvas1)
        self.social_media_frame.pack()
        self.social_media_frame.place(x = x1, y= y1)
        Label(self.social_media_frame, text=con, fg="blue", font ="lucida 10").pack()


        self.image4 = Image.open(".\\src\\shadow_bg.png")
        self.resize_image4 = self.image4.resize((200, 200))
 
        self.img4 = ImageTk.PhotoImage(self.resize_image4)
       
        self.social_media_canvas = Canvas( self.social_media_frame, width = 200,
                     height = 200)
  
        self.social_media_canvas.pack(fill = "both", expand = True)
   
        self.social_media_canvas.create_image( 0, 0, image = self.img4, 
                     anchor = "nw")
        self.social_media_canvas.image = self.img4





    def dateAndTime(self):
        self.data = str(datetime.datetime.now())
        self.data1 = self.data.split(" ")
        self.time = self.data1[1]
        self.date = self.data1[0]
        return (f"Time {self.time}\n DSate{self.date}")

    def Battery(self):
        self.battery = psutil.sensors_battery()
        self.percentage= self.battery.percent
        self.stauts =self.battery.power_plugged

        if self.stauts==False:
            self.data = "unplaged"
            return self.data
        else:
            self.data="plugged"
            return self.data

    def convertTime(self, seconds):
        self.minutes, self.seconds = divmod(seconds, 60)
        self.hours, self.minutes = divmod(self.minutes, 60)
        return "%d:%02d:%02d" % (self.hours, self.minutes, self.seconds)


    def submit(self):
        self.data = str(self.serachInput.get())
        self.result = bonggoQuery.Query.normal_query.speaking(self.data)
       
    def facebook(self):
        webbrowser.open("https://www.facebook.com/")
    def Instagram(self):
        webbrowser.open("https://www.instagram.com/")
    def gitHub(self):
        webbrowser.open("https://github.com/")

    def LinkedIn(self):
        webbrowser.open("https://www.linkedin.com/feed/")

    def browser(self):
        python_file = 'Browser.py'

        try:
            subprocess.run(['python', python_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {python_file}: {e}")

    
    def claculator(self):
        python_file = 'calculator.py'

        try:
            subprocess.run(['python', python_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {python_file}: {e}")
    
    def textEditor(self):
        python_file = 'texteditor.py'

        try:
            subprocess.run(['python', python_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {python_file}: {e}")

    def FileManager(self):
        python_file = 'filemanager.py'

        try:
            subprocess.run(['python', python_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {python_file}: {e}")

    def Clock(self):
        python_file = 'clock.py'

        try:
            subprocess.run(['python', python_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {python_file}: {e}")
        
    def Music(self):
        python_file = 'mediaPlayer.py'

        try:
            subprocess.run(['python', python_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {python_file}: {e}")

    def searchBar(self):
        self.serachInput = StringVar()
        self.f = Frame(self.canvas1, bg="black")
        self.f.pack()
        self.f.place(x =2, y=675)
      
        Entry(self.f, width=50, textvariable=self.serachInput).pack(anchor="nw",padx=15)

        self.image1 = Image.open(".\\src\\search.png")
        self.resize_image1 = self.image1.resize((20 ,20))
    
        self.img1 = ImageTk.PhotoImage(self.resize_image1)

        Button(self.canvas1, text="click", image=self.img1, command=self.submit).place(x =335, y = 670)
        self.battery1 = psutil.sensors_battery()
        Label(self.canvas1, text=f" Remaining Time :: {self.convertTime(self.battery1.secsleft)}\nStatus:: {self.Battery()}", bg="black", fg ="white").place(y=660, x =800)

        Label(self.canvas1, text=f"{self.dateAndTime()}").place(y =660, x= 980)

        
        self.groupedBoxes( 50,90, "Social Media")
        self.groupedBoxes( 50,380, "Day to day Use")
        #
        # Social Media Group

        # GITHUB
        # **********************************************************
        self.image2 = Image.open(".\\src\\gb.png")
        self.resize_image2 = self.image2.resize((50 ,50))
    
        self.img2 = ImageTk.PhotoImage(self.resize_image2)

        Button(self.canvas1, image=self.img2, command= self.gitHub).place(x =80, y= 135)
        # ********************************************************

        # FACEBOOK
        # **********************************************************
        self.image3 = Image.open(".\\src\\fb.png")
        self.resize_image3 = self.image3.resize((50 ,50))
    
        self.img3 = ImageTk.PhotoImage(self.resize_image3)

        Button(self.canvas1, image=self.img3, command= self.facebook).place(x =155, y= 135)
        # ***********************************************************


        #
        # LINKEDIN
        # **********************************************************
        self.image4 = Image.open(".\\src\\ln.png")
        self.resize_image4 = self.image4.resize((50 ,50))
    
        self.img4 = ImageTk.PhotoImage(self.resize_image4)

        Button(self.canvas1, image=self.img4,  command= self.LinkedIn).place(x =80, y= 220)
        # ***********************************************************

         # INSTAGRAM
        # **********************************************************
        self.image5 = Image.open(".\\src\\insta.png")
        self.resize_image5 = self.image5.resize((50 ,50))
    
        self.img5 = ImageTk.PhotoImage(self.resize_image5)

        Button(self.canvas1, image=self.img5, command=self.Instagram).place(x =155, y= 220)
        
        # ***********************************************************
        # ============================================================



        # DAILY UZSE GROUP
        # ===============================================================
        # ------------------Browser--------------------------------------
        self.image6 = Image.open(".\\src\\you.png")
        self.resize_image6 = self.image6.resize((50 ,50))
    
        self.img6 = ImageTk.PhotoImage(self.resize_image6)

        Button(self.canvas1, image=self.img6, command= self.browser).place(x =60, y= 430)
        

        # ---------------------------------------------------------------

        # --------------------------- CALCULATOR -------------------------------------
        self.image7 = Image.open(".\\src\\news.png")
        self.resize_image7 = self.image7.resize((50 ,50))
    
        self.img7 = ImageTk.PhotoImage(self.resize_image7)

        self.b = Button(self.canvas1, image=self.img7, command= self.claculator)
        self.b.place(x =125, y= 430)
        self.b.image = self.img7
        

        # ------------------------------------------------------------------------


        # --------------------------- TEXT EDITOR --------------------------------------
        self.image8 = Image.open(".\\src\\weather.png")
        self.resize_image8 = self.image8.resize((50 ,50))
    
        self.img8 = ImageTk.PhotoImage(self.resize_image8)

        Button(self.canvas1, image=self.img8, command= self.textEditor).place(x =185, y= 430)
        

        # ------------------------------------------------------------------------
    
         # --------------------------- Music --------------------------------------
        self.image9 = Image.open(".\\src\\vs.png")
        self.resize_image9 = self.image9.resize((50 ,50))
    
        self.img9 = ImageTk.PhotoImage(self.resize_image9)

        Button(self.canvas1, image=self.img9, command= self.Music).place(x =60, y= 500)
        

        # ------------------------------------------------------------------------
        # --------------------------- file manager--------------------------------------
        self.image10 = Image.open(".\\src\\disk.png")
        self.resize_image10 = self.image10.resize((50 ,50))
    
        self.img10 = ImageTk.PhotoImage(self.resize_image10)

        Button(self.canvas1, image=self.img10, command= self.FileManager).place(x =125, y= 500)
        11
        # ------------------------------------------------------------------------
        # --------------------------- CLOCK--------------------------------------
        self.image11 = Image.open(".\\src\\clock.png")
        self.resize_image11 = self.image11.resize((50 ,50))
    
        self.img11 = ImageTk.PhotoImage(self.resize_image11)

        Button(self.canvas1, image=self.img11, command= self.Clock ).place(x =185, y= 500)
        

        # ------------------------------------------------------------------------

    def git_profile(self):
        webbrowser.open("https://github.com/SudipBera083")
    
    def linkedin_profile(self):
        webbrowser.open("https://www.linkedin.com/in/sudipbera083/")

    def instagram_profile(self):
        webbrowser.open("https://www.instagram.com/itzz_bonggo_hriday/")
    
    def facebook_profile(self):
        webbrowser.open("https://www.facebook.com/sudipberasrijitananda")
       

    def __init__(self):
        self.root =Tk()
        self.root.title("Secure Environment")
        self.root.configure(bg="black")
        self.root.geometry("1100x700")
        self.root.maxsize(1100,700)
        self.root.minsize(1100,700)


# creating the background canvas
# ======================================================

        self.image = Image.open(".\\src\\bg.jpg")
 
    # Resize the image using resize() method
        self.resize_image = self.image.resize((1100, 700))
    
        self.img = ImageTk.PhotoImage(self.resize_image)

    # Create Canvas
        self.canvas1 = Canvas( self.root, width = 400,
                 height = 400)
  
        self.canvas1.pack(fill = "both", expand = True)
  
    # Display image
        self.canvas1.create_image( 0, 0, image = self.img, 
                     anchor = "nw")
  
    # Add Text
    # canvas1.create_text( 200, 250, text = "Welcome")
        Label(self.canvas1,text="Welcome to Secure Environment", font="lucida 20", bg="black", fg ="white").place(y=35, x =410)
        self.searchBar()
        # Label(self.canvas1, text =  self.Battery()).pack()
        self.Battery()

    # ------------------------  profile----------------------------
        # self.profile_Frame = Frame(self.canvas1)
        # self.profile_Frame.place(x =850, y= 50)

        Label(self.canvas1, text=":: About Developer ::", bg="black", fg ="white", font="lucida 13 bold").place(x =875, y =60)
        
        self.image_profile = Image.open(".\\src\\d.png")
        self.resize_image_profile = self.image_profile.resize((200, 480))
    
        self.img_profile = ImageTk.PhotoImage(self.resize_image_profile)

        self.canvas2 = Canvas( self.canvas1, width = 200,
                 height = 480)
  
        self.canvas2.pack(fill = "both", expand = True)
        self.canvas2.place(x =860, y=100)
  
        self.canvas2.create_image( 0, 0, image = self.img_profile, 
                     anchor = "nw")

        self.image_profile_pic = Image.open(".\\src\\fm.png")
        self.resize_image_profile_pic = self.image_profile_pic.resize((162, 162))
    
        self.img_profile_pic = ImageTk.PhotoImage(self.resize_image_profile_pic)

        self.canvas23 = Canvas( self.canvas1, width = 162,
                 height = 162)
  
        self.canvas23.pack(fill = "both", expand = True)
        self.canvas23.place(x =877, y=160)
  
        self.canvas23.create_image( 0, 0, image = self.img_profile_pic, 
                     anchor = "nw")

        Label(self.canvas1, text=":: Social Media ::", font="lucida 10", fg="#C6322B", bg ="#FFFFFF").place(x =877, y = 335)

        # **********************************************************
        
        self.image_git_prf = Image.open(".\\src\\gb.png")
        self.resize_image_git_prf = self.image_git_prf.resize((20 ,20))
    
        self.img_git_prf = ImageTk.PhotoImage(self.resize_image_git_prf)
        Button(self.canvas1, image=self.img_git_prf, command=self. git_profile).place(x=877, y = 370)


        self.image_linkedIn_prf = Image.open(".\\src\\ln.png")
        self.resize_image_linkedIn_prf = self.image_linkedIn_prf.resize((20 ,20))
    
        self.img_linkedIn_prf = ImageTk.PhotoImage(self.resize_image_linkedIn_prf)
        Button(self.canvas1, image=self.img_linkedIn_prf, command=self.linkedin_profile).place(x=920, y = 370)

        self.image_instagram_prf = Image.open(".\\src\\insta.png")
        self.resize_image_instagram_prf = self.image_instagram_prf.resize((20 ,20))
    
        self.img_instagram_prf = ImageTk.PhotoImage(self.resize_image_instagram_prf)
        Button(self.canvas1, image=self.img_instagram_prf, command=self.instagram_profile).place(x=960, y = 370)

        self.image_facebook_prf = Image.open(".\\src\\fb.png")
        self.resize_image_facebook_prf = self.image_facebook_prf.resize((20 ,20))
    
        self.img_facebook_prf = ImageTk.PhotoImage(self.resize_image_facebook_prf)
        Button(self.canvas1, image=self.img_facebook_prf, command=self.facebook_profile).place(x=1000, y = 370)

        Label(self.canvas1, text=":: About ::", font="lucida 10", fg="#C6322B", bg ="#FFFFFF").place(x =877, y = 410)

        para = """Student of UEM, Kolkata.\n\nPython || Django\n******************\nReact ||  DataBase\n********************
                """

        Label(self.canvas1, text=para, font="lucida 9", fg="black", bg ="#FFFFFF").place(x =877, y = 435)



    # ===============================================================
    
# =====================================================
        self. root.mainloop()

    

    

       
if __name__ =='__main__':
    HoleBody()
  
