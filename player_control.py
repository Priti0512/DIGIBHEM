import tkinter as tk
from ttkthemes import themed_tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
from mutagen.mp3 import MP3
import os
import time
import pygame

class MediaPlayer:
    def __init__(self,window):

        style = ttk.Style()
        style.theme_use("breeze")

        background = "grey"
        style.configure("TScale",background = background)

        self.root = window
        self.root.configure(bg="black")
        self.music_image = Image.open('images/6063588.jpg')
        self.music_image = self.music_image.resize((430,315),Image.Resampling.LANCZOS)
        self.music_image = ImageTk.PhotoImage(self.music_image)

        self.repeat_icon = Image.open('images/repeat.png')
        self.repeat_icon = self.repeat_icon.resize((40, 40), Image.Resampling.LANCZOS)
        self.repeat_icon = ImageTk.PhotoImage(self.repeat_icon)

        self.repeat1_icon = Image.open('images/repeat1.png')
        self.repeat1_icon = self.repeat1_icon.resize((40, 40), Image.Resampling.LANCZOS)
        self.repeat1_icon = ImageTk.PhotoImage(self.repeat1_icon)

        self.play_icon = Image.open('images/play.png')
        self.play_icon = self.play_icon.resize((60, 60), Image.Resampling.LANCZOS)
        self.play_icon = ImageTk.PhotoImage(self.play_icon)

        self.pause_icon = Image.open('images/pause.png')
        self.pause_icon = self.pause_icon.resize((60, 60), Image.Resampling.LANCZOS)
        self.pause_icon = ImageTk.PhotoImage(self.pause_icon)

        self.next_icon = Image.open('images/next.png')
        self.next_icon = self.next_icon.resize((55, 55), Image.Resampling.LANCZOS)
        self.next_icon = ImageTk.PhotoImage(self.next_icon)

        self.previous_icon = Image.open('images/previous.png')
        self.previous_icon = self.previous_icon.resize((55, 55), Image.Resampling.LANCZOS)
        self.previous_icon = ImageTk.PhotoImage(self.previous_icon)

        self.stop_icon = Image.open('images/stop.png')
        self.stop_icon = self.stop_icon.resize((60, 60), Image.Resampling.LANCZOS)
        self.stop_icon = ImageTk.PhotoImage(self.stop_icon)

        self.speaker_icon = Image.open('images/speaker.png')
        self.speaker_icon = self.speaker_icon.resize((35, 35), Image.Resampling.LANCZOS)
        self.speaker_icon = ImageTk.PhotoImage(self.speaker_icon)

        self.mute_icon = Image.open('images/mute.png')
        self.mute_icon = self.mute_icon.resize((40, 40), Image.Resampling.LANCZOS)
        self.mute_icon = ImageTk.PhotoImage(self.mute_icon)

        self.delete_icon = Image.open('images/delete.png')
        self.delete_icon = self.delete_icon.resize((30, 30), Image.Resampling.LANCZOS)
        self.delete_icon = ImageTk.PhotoImage(self.delete_icon)

        self.delete_all_icon = Image.open('images/delete.png')
        self.delete_all_icon = self.delete_all_icon.resize((30, 30), Image.Resampling.LANCZOS)
        self.delete_all_icon = ImageTk.PhotoImage(self.delete_all_icon)

        self.add_song_icon = Image.open('images/song.png')
        self.add_song_icon = self.add_song_icon.resize((25, 25), Image.Resampling.LANCZOS)
        self.add_song_icon = ImageTk.PhotoImage(self.add_song_icon)

        self.add_multiple_song_icon = Image.open('images/song2.png')
        self.add_multiple_song_icon = self.add_multiple_song_icon.resize((25, 25), Image.Resampling.LANCZOS)
        self.add_multiple_song_icon = ImageTk.PhotoImage(self.add_multiple_song_icon)

        self.shuffle = Image.open('images/shuffle.png')
        self.shuffle = self.shuffle.resize((40, 40), Image.Resampling.LANCZOS)
        self.shuffle = ImageTk.PhotoImage(self.shuffle)

        self.auto_play_icon = Image.open('images/auto_play.png')
        self.auto_play_icon = self.auto_play_icon.resize((40, 50), Image.Resampling.LANCZOS)
        self.auto_play_icon = ImageTk.PhotoImage(self.auto_play_icon)

        self.auto_play_not_icon = Image.open('images/auto_play_not.png')
        self.auto_play_not_icon = self.auto_play_not_icon.resize((40, 40), Image.Resampling.LANCZOS)
        self.auto_play_not_icon = ImageTk.PhotoImage(self.auto_play_not_icon)

        self.song_photo = tk.Label(self.root,text="",image=self.music_image,bd=0)
        self.song_photo.place(x =80,y=78)

        self.heading = tk.Label(self.root,bg="black",text="Music Player",font="lucida 40 bold",fg="#F4B81A")
        self.heading.place(x=0,y=2,relwidth=1)

        tk.Label(self.root,text="",background=background,height=7,width=120).place(x=5,y=400)

        self.song_list = tk.Listbox(self.root,width=30, height=18, bg ="black",fg = "blue",relief="flat" ,selectbackground="grey")
        self.song_list.place(x = 520, y = 60)
        self.time_elapsed_label = tk.Label(self.root,text ="00:00", fg = "black",background= background,activebackground = background,padx = 5)
        self.time_elapsed_label.place(x = 10, y = 400)
        self.music_duration_label = tk.Label(self.root,text="00:00",fg ="black", background = background, activebackground = background,padx = 5)
        self.music_duration_label.place(x = 450, y = 400)

        self.progress_scale = ttk.Scale(self.root,orient="horizontal",style='TScale',from_= 0,length = 380,command=self.progress_scale_moved,cursor="hand2")
        self.progress_scale.place(x = 65,y = 400)

        self.play_button = tk.Button(self.root,image=self.play_icon,command = self.check_play_pause,cursor="hand2",bd = 0,background=background,activebackground=background)
        self.play_button.place(x = 165, y=425)

        self.next_button = tk.Button(self.root, image=self.next_icon, command=self.next_song, cursor="hand2", bd=0,
                                     background=background, activebackground=background)
        self.next_button.place(x=305, y=426)

        self.previous_button = tk.Button(self.root, image=self.previous_icon, command=self.previous_song, cursor="hand2", bd=0,
                                     background=background, activebackground=background)
        self.previous_button.place(x=95, y=426)

        self.stop_button = tk.Button(self.root, image=self.stop_icon, command=self.stop_song, cursor="hand2", bd=0,
                                     background=background, activebackground=background)
        self.stop_button.place(x=236, y=425)

        self.shuffle_button = tk.Button(self.root, image=self.shuffle, command=self.shuffle_song, cursor="hand2", bd=0,
                                     background=background, activebackground=background)
        self.shuffle_button.place(x=10, y=425)

        self.speaker_button = tk.Button(self.root, image=self.speaker_icon, command="command", cursor="hand2", bd=0,
                                     background=background, activebackground=background)
        self.speaker_button.place(x=375, y=430)

        self.repeat_button = tk.Button(self.root, image=self.repeat_icon, command=self.repeat_song, cursor="hand2", bd=0,
                                     background=background, activebackground=background)
        self.repeat_button.place(x=10, y=470)
        self.auto_play_button = tk.Button(self.root, image=self.auto_play_not_icon, command=self.auto_play_song,
                                          cursor='hand2', bd=0,
                                          background=background, activebackground=background)
        self.auto_play_button.place(x=420, y=453)

        self.vol_scale = ttk.Scale(self.root,from_=0,to=100,orient="horizontal",command=self.change_volume,cursor="hand2")
        self.vol_scale.place(x=420,y=425)

        self.status = tk.Label(self.root,text="Playing...........Song: 0 of 0",fg="black",anchor="w",background=background,font="lucida 9 bold", bd = 5, relief="ridge")
        self.status.place(x=5,y=520,relwidth=1)

        self.menu = tk.Menu(self.root)
        self.root.configure(menu=self.menu)

        m1 =tk.Menu(self.menu,background="grey",tearoff=False,bd=0,activebackground="black")
        self.menu.add_cascade(label="Action",menu=m1)

        m1.add_command(label="Add Song",command = self.add_songs,image=self.add_song_icon,compound="left")

        m2 = tk.Menu(self.menu, background="grey", tearoff=False, bd=0, activebackground="black")
        self.menu.add_cascade(label="Delete", menu=m2)

        m2.add_command(label="Delete Selected", command=lambda: self.delete_song('selected'), image=self.delete_icon,
                       compound="left")
        m2.add_command(label="Delete All", command=lambda: self.delete_song('all'), image=self.delete_all_icon,
                       compound="left")

        self.directory_list = []
        self.pause  = False
        self.repeat_conditions = False
        self.autoplay = False

        self.songs_to_play=[]

    def add_songs(self):
        songs = filedialog.askopenfilenames(title="Select Music Folder", filetypes=(('mp3 files', '*.mp3'),))
        for song in songs:
            song_name = os.path.basename(song)
            directory_path = song.replace(song_name, "")
            self.directory_list.append({'path': directory_path, 'song': song_name})
            self.song_list.insert('end', song_name)

        self.song_list.select_set('0')
        def check_play_pause(self):

        if self.song_list.size()>=1:

          self.songs_to_play.append(self.song_list.get('active'))

          length = len(self.songs_to_play)
          if len(self.songs_to_play)==1:
              self.play_song()

          elif self.songs_to_play[length-1]!=self.songs_to_play[length-2]:
             self.root.after_cancel(self.updater)
             self.play_song()
          else:
             self.pause_unpause()

    def pause_unpause(self):
        if not self.pause:
            self.root.after_cancel(self.updater)
            self.play_button.config(image = self.play_icon)
            self.pause = True

            self.status.config(text=f"Paused :{self.song_list.get('active')} {self.song_list.index('active')+1} of {self.song_list.size()}")
            pygame.mixer.music.pause()

        else:
            self.pause = False
            self.play_button.config(image=self.pause_icon)


            self.status.config(text=
                f"Paying :{self.song_list.get('active')} {self.song_list.index('active')+1} of {self.song_list.size()}")
            pygame.mixer.music.unpause()
            self.scale_update()


    

        def play_song(self):
        self.progress_scale['value'] = 0
        self.time_elapsed_label['text'] ="00:00"

        song_name = self.song_list.get('active')
        self.status.config(text=f"Playing : {song_name} song : {self.song_list.index('active')} of "
                           f"{self.song_list.size()}")
        directory_path = None
        for dictio in self.directory_list:
            if dictio['song'] == song_name:
                directory_path = dictio['path']

        song_with_path = f'{directory_path}/{song_name}'
        music_data = MP3(song_with_path)
        self.music_length = int(music_data.info.length)
        self.music_duration_label['text'] = time.strftime('%M:%S',time.gmtime(self.music_length))

        self.progress_scale['to'] = self.music_length
        self.play_button.config(image=self.pause_icon)
        pygame.mixer.music.load(song_with_path)
        pygame.mixer.music.play()
        self.scale_update()
          def progress_scale_moved(self,x):
        self.root.after_cancel(self.updater)
        scale_at=self.progress_scale.get()
        song_name=self.song_list.get('active')
        directory_path=None
        for dictio in self.directory_list:
            if dictio['song'] == song_name:
                directory_path=dictio['path']
        pygame.mixer.music.load(f"{directory_path}/{song_name}")
        pygame.mixer.music.play(0,scale_at)
        self.scale_update()

    def scale_update(self):
        if self.progress_scale['value']<self.music_length:
            self.progress_scale['value'] +=1
            self.time_elapsed_label['text'] = time.strftime('%M:%S',time.gmtime(self.progress_scale.get()))

            self.updater = self.root.after(1000,self.scale_update)
        elif self.repeat_conditions:
            self.play_song()
        elif self.autoplay:
            self.next_song()
        else:
            self.progress_scale['value'] = 0
            self.time_elapsed_label['text'] ="00:00"
            self.play_button.config(image=self.play_icon)
            self.songs_to_play = []
          def next_song(self):
        if self.song_list.size() >= 1:
          self.root.after_cancel(self.updater)
          song_index = self.song_list.index('active')
          self.song_list.select_clear('active')

          list_length = self.song_list.size()

          if list_length-1 == song_index:
              self.song_list.selection_set(0)
              self.song_list.activate(0)
              self.check_play_pause()
          else:
              self.song_list.selection_set(song_index+1)
              self.song_list.activate(song_index+1)
              self.check_play_pause()

    def change_volume(self,event=None):
        self.v = self.vol_scale.get()
        pygame.mixer.music.set_volume(self.v/100)

    def previous_song(self):
        if self.song_list.size() >= 1:
          self.root.after_cancel(self.updater)
          song_index = self.song_list.index('active')
          self.song_list.select_clear('active')

          list_length = self.song_list.size()

          if song_index == 0:
              self.song_list.selection_set(list_length-1)
              self.song_list.activate(list_length-1)
              self.check_play_pause()
          else:
              self.song_list.selection_set(song_index-1)
              self.song_list.activate(song_index-1)
              self.check_play_pause()




  
    if __name__ == '__main__':
    window = themed_tk.ThemedTk()
    pygame.init()
    window.title("Music Player")
    window.wm_iconbitmap('images/music.ico')

    window.maxsize(width=950,height=550)
    window.minsize(width=740,height=550)

    x= MediaPlayer(window)
    window.mainloop()
