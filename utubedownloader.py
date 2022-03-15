from cProfile import label
from itertools import count
import json
from struct import pack
from tkinter import*
from pyyoutube import Api
from pytube import YouTube
from threading import Thread
from tkinter import messagebox
  
root = Tk()
root.geometry('400x400')
Label(root,text="Youtube video downloader",font="italic 15 bold").pack(pady = 10)
Label(root,text="Enter playlist url--",font = "italic 10").pack(pady = 10)
playlistID = Entry(root,width=60)
playlistID.pack(pady = 5)
dowload_start=Button(root,text="download start")
dowload_start.pack(pady=10)
root.mainloop()

def threading():
 t1 = Thread(target=download_videos)
 t1.start()

def download_videos():
    api = Api(api_key = 'Enter api key')

    if YouTube in playlistID.get():
        playlist_id = playlistID.get()[len("https://www.youtube.com/playlist?list="):]

    else:
        playlist_id = playlistID.get()
playlist_item_by_id = api.get_playlist_items(
     playlist_id = playlist_id,count = None , return_json = True
 )
for index, videoid in enumerate(playlist_item_by_id['items']):
  
        link = f"https://www.youtube.com/watch?v={videoid['contentDetails']['videoId']}"
  
        yt_obj = YouTube(link)
  
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
  
        # download the highest quality video
        filters.get_highest_resolution().download()
  
        print(f"Downloaded:- {link}")
  
messagebox.showinfo("Success", "Video Successfully downloaded")


