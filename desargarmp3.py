import youtube_dl #libreria que permite descargar y convertir los videos

#funcion para extrer el audio del video
def extraer_audio():
    print("Bienvenido al programa de extraccion de audio.")
    print("Para comenzar copie el enlace del video de youtube que desee convertir y peguelo en el lugar indicado.")
    enlace_video = input("Ingrese el link o url del video a convertir: ")
    #solicita el enlace de youtube para descargar el video

    data_video = youtube_dl.YoutubeDL().extract_info(url = enlace_video, download = False)
    #se obtiene la data del video del enlace y se configura download en false para que no descargue el video

    archivo_audio = f"{data_video['title']}.mp3"
    #extraccion del audio del enlace del video
    options = {
        #configuracion de las opciones de extraccion del audio
        'format':'bestaudio/best', #formato del audio configurado al mejor
        'keepvideo':False, #keepvideo en false ya que solo se desea obtener el audio
        'outtmpl':archivo_audio, #nombre de la salida del archivo de audio
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([data_video['webpage_url']])

    print("Descarga completada, su archivo: {}".format(archivo_audio), "esta listo, tenga un buen dia")


if __name__ == '__main__':
    extraer_audio()