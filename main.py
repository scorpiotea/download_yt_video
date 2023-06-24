import os
import sys
from pytube import YouTube

args = sys.argv

#function to get data from text file
def get_file_data(arg):
    modified_line = []
    file = open(arg, 'r')
    read = file.readlines()
    file.close()

    for line in read:
        if line[-1] == '\n':
            modified_line.append(line[:-1])
        else:
            modified_line.append(line)
    
    for link in modified_line:
        download(link)

#function to download youtube video
def download(link):
        youtube_object = YouTube(link)
        youtube_object = youtube_object.streams.get_highest_resolution()
        try:
            youtube_object.download()
        except:
            print('An error has occurred')
        print('Download is completed successfully')

#function to check if provided arguments are files
def check_arguments():
    if len(args) > 1 : 
        for arg in args[1:]:
            if os.path.isfile(arg):
                get_file_data(arg)
            else:
                download(arg)
    else:
        print('No arguments provided')
        exit()

check_arguments()
