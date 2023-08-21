#Import required Libraries
from tkinter import *
from pytube import YouTube

# Create Display Window
root= Tk()
root.resizable(0,0)
root.geometry('500x450')
root.configure(bg='red')
root.title('Youtube Downloader')

# Label which displays text on the GUI
Label(root,text='Youtube Video Downloader\n Enter Link to download video below...',font='arial 15 bold',bg='red',fg='black').pack()

# Background Image to be displayed on created GUI
photo=PhotoImage(file="Youtube.png")
lbl=Label(image=photo).pack()

# Variable to store user entered link
link=StringVar()

# Create an entry field which accepts link from user
enter_link=Entry(root,width=70,textvariable=link).place(x=50,y=100)

# Function to download the user entered link
def downloader():
    # Getting the user entered link and assinigng it to YouTube class ini pytube
    url=YouTube(str(link.get()))
     # Returns the first element in list of video formats(320 px)
    video=url.streams.first()
    # The download starts here
    video.download()
    # To acknowledge user that the video has downloaded after it's completion
    Label(root,text='Dowloaded').place(x=215,y=390)

# Button to start the downloading the video of provided url
Button(root,text='Download Here',command=downloader,fg='white',bg='black').place(x=200,y=360)

# To start the interface and display the properties in it
mainloop()