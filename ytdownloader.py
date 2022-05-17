from pytube import YouTube
from tqdm import tqdm

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)

format = input("Choose the format you want to download in (A for audio only / V for video only / Enter for normal video):")
if format == '':
    #Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()
elif format == "A" or format == "a":
    ys = yt.streams.get_audio_only()
elif format == "V" or format == "b":
    ys = yt.streams.filter(only_video=True).get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")