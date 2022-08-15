#pip install pytube
from pytube import YouTube

print("byFat1h")
link = input("indirmek istediğiniz Youtube Video linkini giriniz:  ")
yt = YouTube(link)

print("Başlık: ",yt.title)
print("Görüntüleme: ",yt.views)
print("Video Uzunluğu: ",yt.length)
print("Video Değerlendirmesi: ",yt.rating)

ys = yt.streams.get_highest_resolution()

print("İndiriliyor...")
ys.download()
print("İndirme Tamamlandı!!")
print("byFat1h")
