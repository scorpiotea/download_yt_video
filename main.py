import os
import sys
from pytube import YouTube

args = sys.argv

#function to get data from text file
def GetFileData(arg):
    modifiedLine = []
    file = open(arg, 'r')
    read = file.readlines()
    file.close()

    for line in read:
        if line[-1] == '\n':
            modifiedLine.append(line[:-1])
        else:
            modifiedLine.append(line)
    
    for link in modifiedLine:
        Download(link)

#function to download youtube video
def Download(link):
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download()
        except:
            print('An error has occurred')
        print('Download is completed successfully')

#function to check if provided arguments are files
def CheckArgs():
    for arg in args[1:]:
        if os.path.isfile(arg):
            GetFileData(arg)
        else:
            Download(arg)

CheckArgs()
