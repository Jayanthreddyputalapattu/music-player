
def unmute():
    root.unmuteButton.grid_remove()
    root.muteButton.grid()
    mixer.music.set_volume(currentvolume)
    ProgressbarVolume.configure(value=100)
    ProgressbarVolumeLabel.configure(text='100%')
    mixer.music.set_volume(100)

def mutemusic():
    global currentvolume
    root.muteButton.grid_remove()
    root.unmuteButton.grid()
    currentvolume = mixer.music.get_volume()
    mixer.music.set_volume(0)
    ProgressbarVolumeLabel.configure(text="0%")
    ProgressbarVolume.configure(value=0)
def resumemusic():
    root.PauseButton.grid()
    root.ResumeButton.grid_remove()
    root.audioStatusLabel.configure(text='')
    mixer.music.unpause()
    root.audioStatusLabel.configure(text='Playing...')

    
    

def volumeup():
    vol = mixer.music.get_volume()
    if(vol>=vol*100):
        mixer.music.set_volume(vol+0.1)
    else:
        mixer.music.set_volume(vol+0.05)
    ProgressbarVolumeLabel.configure(text="{}%".format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100

def volumedown():
    vol = mixer.music.get_volume()
    if(vol>=vol*100):
        mixer.music.set_volume(vol-0.1)
    else:
        mixer.music.set_volume(vol-0.05)
    ProgressbarVolumeLabel.configure(text="{}%".format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100
def stopmusic():
    mixer.music.stop()
    root.audioStatusLabel.configure(text="Stopped....")

def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    root.audioStatusLabel.configure(text='Paused.......')
def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    mixer.music.play()
    ProgressbarMusic.grid()
    ProgressbarMusicLabel.grid()
    ProgressbarEndTimeMusicLabel.grid()
    ProgressbarStartTimeMusicLabel.grid()
    mixer.music.set_volume(0.4)
    ProgressbarVolume['value'] = 40
    ProgressbarVolumeLabel['text'] = '40%'
    root.audioStatusLabel.configure(text='Playing...')

    Song = MP3(ad)
    totalsonglength = int(Song.info.length)
    ProgressbarMusic['maximum'] = totalsonglength
    ProgressbarEndTimeMusicLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))
    def Progressbarmusictick():
        CurrentSonglength = mixer.music.get_pos()//1000
        ProgressbarMusic['value'] = CurrentSonglength
        ProgressbarStartTimeMusicLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSonglength))))
        ProgressbarMusic.after(2,Progressbarmusictick)
    Progressbarmusictick()
def musicurl():
    try:
       dd = filedialog.askopenfilename(initialdir='/home/panchajanyam/Desktop/audio',
                                      title="Select Audio File",
                                      filetypes=(("MP3",'*.mp3'),("WAV","*.wav")))
    except:
        dd = filedialog.askopenfilename(title="Select Audio File",
                                      filetypes=(("MP3",'*.mp3'),("WAV","*.wav")))
    audiotrack.set(dd)
def createwidthes():
    ##################################################################### Image Register
    global imbrowse,implay,impause,imvolumeup,imvolumedown,imstop,imresume,immute,imunmute
    global audiotrack,ProgressbarVolume,ProgressbarVolumeLabel,ProgressbarMusic,ProgressbarEndTimeMusicLabel,ProgressbarMusicStartTimeLabel,ProgressbarStartTimeMusicLabel,ProgressbarMusicLabel
    implay = PhotoImage(file="play.png")
    impause = PhotoImage(file="pause.png")
    imbrowse = PhotoImage(file='browsing.png')
    imvolumeup = PhotoImage(file="volume-up.png")
    imvolumedown = PhotoImage(file="volume-down.png")
    imstop = PhotoImage(file='stop-button.png')
    imresume = PhotoImage(file='resume.png')
    immute = PhotoImage(file='mute.png')
    imunmute = PhotoImage(file='muted.png')
    ##################################################################### change size of the images
    imbrowse = imbrowse.subsample(2,2)
    implay = implay.subsample(2,2)
    impause = impause.subsample(2,2)
    imvolumeup = imvolumeup.subsample(2,2)
    imvolumedown = imvolumedown.subsample(2,2)
    imstop = imstop.subsample(2,2)
    imresume = imresume.subsample(2,2)
    immute = immute.subsample(2,2)
    imunmute = imunmute.subsample(2,2)
    ##################################################################### Labels
    TrackLabel = Label(root,text='Select Audio Track',background='lightskyblue',font=('arial',15,'italic bold'))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)

    root.audioStatusLabel = Label(root,text='',background='lightskyblue',font=('arial',15,'italic bold'))
    root.audioStatusLabel.grid(row=2,column=1)

    ##################################################################### Entry Box
    TrackLabelEntry = Entry(root,font=('arial',16,'italic bold'),width=35,textvariable=audiotrack)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)

    


    ##################################################################### Buttons
    BrowseButton = Button(root,text='Search',font=('arial',13,'italic bold'),bg='deeppink',width=200,bd=5,activebackground='purple4',image=imbrowse,compound=RIGHT,command=musicurl)
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)

    PlayButton = Button(root,text='Play',font=('arial',13,'italic bold'),bg='green2',width=200,bd=5,activebackground='purple4',image=implay,compound=RIGHT,command=playmusic)
    PlayButton.grid(row=1,column=0,padx=20,pady=20)

    root.PauseButton = Button(root,text='Pause',font=('arial',13,'italic bold'),bg='yellow',width=200,bd=5,activebackground='purple4',image=impause,compound=RIGHT,command=pausemusic)
    root.PauseButton.grid(row=1,column=1,padx=20,pady=20)

    root.ResumeButton = Button(root,text='Resume',font=('arial',13,'italic bold'),bg='yellow',width=200,bd=5,activebackground='purple4',compound=RIGHT,image=imresume,command=resumemusic)
    root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)
    root.ResumeButton.grid_remove()


    root.muteButton = Button(root,text='Mute',font=('arial',13,'italic bold'),bg='yellow',width=100,bd=5,activebackground='purple4',compound=RIGHT,image=immute,command=mutemusic)
    root.muteButton.grid(row=3,column=3)

    root.unmuteButton = Button(root,text='Unmute',font=('arial',13,'italic bold'),bg='yellow',width=100,bd=5,activebackground='purple4',image=imunmute,compound=RIGHT,command=unmute)
    root.unmuteButton.grid(row=3,column=3)
    root.unmuteButton.grid_remove()

    VolumeUpButton = Button(root,text='VolumeUp',font=('arial',13,'italic bold'),bg='blue',width=200,bd=5,activebackground='purple4',image=imvolumeup,compound=RIGHT,command=volumeup)
    VolumeUpButton.grid(row=1,column=2,padx=20,pady=20)


    VolumeDownButton = Button(root,text='VolumeDown',font=('arial',13,'italic bold'),bg='blue',width=200,bd=5,activebackground='purple4',image=imvolumedown,compound=RIGHT,command=volumedown)
    VolumeDownButton.grid(row=2,column=2,padx=20,pady=20)

    StopButton = Button(root,text='Stop',font=('arial',13,'italic bold'),bg='red',width=200,bd=5,activebackground='purple4',image=imstop,compound=RIGHT,command=stopmusic)
    StopButton.grid(row=2,column=0,padx=20,pady=20)
    
    ################################################################### Progressbar Volume
    ProgressbarLabel = Label(root,text='',bg='red')
    ProgressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)



    ProgressbarVolume = Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',
                                   value=100,length=190)
    ProgressbarVolume.grid(row=0,column=0,ipadx=5)


    ProgressbarVolumeLabel = Label(ProgressbarLabel,text='100%',bg='lightblue',width=3)
    ProgressbarVolumeLabel.grid(row=0,column=0)

    ################################################################### Progressbar Music
    ProgressbarMusicLabel = Label(root,text='',bg='red')
    ProgressbarMusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
    ProgressbarMusicLabel.grid_remove()

    ProgressbarStartTimeMusicLabel = Label(ProgressbarMusicLabel,text='0:00:0',bg='red',width=10)
    ProgressbarStartTimeMusicLabel.grid(row=0,column=0)
    ProgressbarStartTimeMusicLabel.grid_remove()
    

    ProgressbarMusic = Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode='determinate',value=0)
    ProgressbarMusic.grid(row=0,column=1,ipadx=370,padx=20,pady=20,ipady=3)
    ProgressbarMusic.grid_remove()

    ProgressbarEndTimeMusicLabel = Label(ProgressbarMusicLabel,text="0:00:0",bg='red')
    ProgressbarEndTimeMusicLabel.grid(row=0,column=2)
    ProgressbarMusicLabel.grid_remove()

    


from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3

root = Tk()
root.geometry('1199x500+200+50')
root.title("Music Player 🎶")
root.resizable(False,False)
root.configure(bg='lightskyblue')
######################################################################################### Global varialbels
audiotrack = StringVar()
currentvolume = 30
totalsonglength = 0
count = 0
text= ''
######################################################################################### Create Slider
ss = 'Developed By Jayanth'
count = 0
text = ''
sliderLabel = Label(root,text=ss,bg='lightskyblue',font=('arial',40,'italic bold'))
sliderLabel.grid(row=3,column=0,padx=2,columnspan=3)
def IntroLabelTRick():
    global count,text
    if(count>=len(ss)):
        count = -1
        text = ''
        sliderLabel.configure(text=text)
    else:
        text = text+ss[count]
        sliderLabel.configure(text=text)
    count += 1
    sliderLabel.after(200,IntroLabelTRick )

IntroLabelTRick()
mixer.init()
createwidthes()
root.mainloop()
