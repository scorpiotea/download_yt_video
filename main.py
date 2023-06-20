import os
import sys
from pytube import YouTube

args = sys.argv

#function to get data from text file
def GetFileData():
    modifiedLink = []
    file = open(fileName, 'r')
    read = file.readlines()
    file.close()

    for link in read:
        if link[-1] == '\n':
            modifiedLink.append(link[:-1])
        else:
            modifiedLink.append(link)
    print(modifiedLink)
    Download(modifiedLink)

#function to download youtube video
def Download(videoLink):
    for link in videoLink:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download()
        except:
            print('An error has occurred')
        print('Download is completed successfully')

#checking if provided arguments are files
if os.path.isfile(args[1]):
    fileName = args[1]
    GetFileData()
else:
    args = args[1:]
    Download(args)


