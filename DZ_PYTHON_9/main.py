from turtle import title
from pytube import YouTube




def download_video(url):
    yt = YouTube(url) 
    title = yt.title
    print("Загрузка " + title)
    yt.streams.filter(progressive = True, file_extension= 'mp4').order_by('resolution').desc().first().download('C:/Users/Zheka/Desktop')
    print('Загруженно! '+ title)
    return title


