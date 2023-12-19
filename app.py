from pytube import YouTube

print('Informe abaixo a url do vídeo que deseja fazer o Download')
url = input('')

yt = YouTube(url)

resolucao = yt.streams.get_highest_resolution()

resolucao.download()

print('Download Completo')