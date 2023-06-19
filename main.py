import os
from pytube import YouTube

#create directory
directory = input("Enter the name of the directory you want to create: ")

os.mkdir(directory)

#function to download youtube video
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(directory)
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)

