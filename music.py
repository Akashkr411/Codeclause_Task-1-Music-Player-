# Importing Required Modules & libraries
from tkinter import *
import pygame
from pygame import mixer
import os


class MusicPlayer:

  # Defining Constructor
  def __init__(self,root):
    self.root = root
    # Title of the window
    self.root.title("Music Player")
    # Window Geometry
    self.root.geometry("1000x200+200+200")
   
    pygame.init()
   
    pygame.mixer.init()
    # Declaring track Variable
    self.track = StringVar()

    # Declaring Status Variable
    self.status = StringVar()

    # Creating Track Frame for Song label & status label
    trackframe = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="blue",fg="white",bd=5,relief=GROOVE)
    trackframe.place(x=0,y=0,width=600,height=100)
    
    # Inserting Song Track Label
    songtrack = Label(trackframe,textvariable=self.track,width=25,font=("times new roman",17,"bold"),bg="black",fg="white").grid(row=0,column=0,padx=20,pady=15)

    # Inserting Status Label
    trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",17,"bold"),bg="black",fg="white").grid(row=0,column=1,padx=20,pady=15)

    buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="black",fg="white",bd=5,relief=GROOVE)
    buttonframe.place(x=0,y=100,width=600,height=100)

    # Inserting Play Button
    playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=0,padx=20,pady=15)
    
    playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=1,padx=20,pady=15)

    # Inserting Unpause Button
    playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=2,padx=20,pady=15)
    
    # Inserting Stop Button
    playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=3,padx=20,pady=15)
    
    # Creating Playlist Frame
    songsframe = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="blue",fg="white",bd=5,relief=GROOVE)
    songsframe.place(x=600,y=0,width=400,height=200)

    # Inserting scrollbar
    scrol_y = Scrollbar(songsframe,orient=VERTICAL)

    self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)

    # Applying Scrollbar to listbox
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=BOTH)

    # Changing Directory for fetching Songs
    os.chdir("E:\\codeclash\\task 1\\Music Collection")

    # Fetching Songs
    songtracks = os.listdir()

    # Inserting Songs into Playlist
    for track in songtracks:
      self.playlist.insert(END,track)

  # Defining Play Song Function
  def playsong(self):
    # Displaying Selected Song title
    self.track.set(self.playlist.get(ACTIVE))

    # Displaying Status
    self.status.set("-Playing")
    
    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    
    pygame.mixer.music.play(1)

  def stopsong(self):
    # Displaying Status
    self.status.set("-Stopped")
    pygame.mixer.music.stop()

  def pausesong(self):
    # Displaying Status
    self.status.set("-Paused")
    
    pygame.mixer.music.pause()

  def unpausesong(self):
    # Displaying Status
    self.status.set("-Playing")
    pygame.mixer.music.unpause()


# Creating TK Container
root = Tk()

MusicPlayer(root)
# Root Window Looping
root.mainloop()