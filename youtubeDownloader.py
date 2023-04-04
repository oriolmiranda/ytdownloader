from pytube import YouTube
from sys import argv

# Youtube Downloader - al executar el scrip hem de pasar com a parametre el link del video entre cometes ("link")

outputFolder = './VideosDescarregats' # On volem guardar

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("View: ", yt.views)
print("Size: ", yt.streams.get_highest_resolution().filesize)

yd = yt.streams.get_highest_resolution() # Si volem descarregui maxima resolucio
# yd = yt.streams.get_by_resolution("1080p") # Si volem descarregar una resolucio especifica

# yd = yt.streams.get_audio_only # Descarregar només audio (música)

yd.download(outputFolder)
