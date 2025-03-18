from pytube import YouTube

import yt_dlp

link = input("Enter a link to download: ")
ydl_opts = {
    'format': 'best',
    'outtmpl': 'video_download.mp4',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    print("downloading...")
    ydl.download([link])
    print("finished downloading.")
