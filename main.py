from pytube import YouTube
import subprocess
import os
import shutil

video_save = './video/'  # Ruta de la carpeta donde se guardan los videos
audio_save = './music/'  # Ruta de la carpeta donde se guardarán los archivos de audio

# Asegurarse de que las carpetas de destino existan
os.makedirs(video_save, exist_ok=True)
os.makedirs(audio_save, exist_ok=True)


def download_video(url):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video_filename = os.path.join(video_save, video.default_filename)  # Ruta completa para guardar el video
    video.download(output_path=video_save)
    return video_filename


def convert_to_audio(video_filename):
    audio_filename = os.path.join(audio_save, os.path.basename(video_filename).replace('.mp4',
                                                                                       '.mp3'))  # Ruta completa para guardar el audio
    subprocess.run(['ffmpeg', '-i', video_filename, audio_filename])
    return audio_filename


def read_and_split_file(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            lines.append(parts)
    return lines


if __name__ == "__main__":
    filename = input("write name file : ")
    separator_lines = read_and_split_file(filename)

    for url_you in separator_lines:
        video_filename = download_video(url_you[0])
        print(f"Video download: {video_filename}")

        audio_filename = convert_to_audio(video_filename)
        print(f"Audio convert: {audio_filename}")

    if os.path.exists(video_save):
        print("Delete folder video successfully!")
        shutil.rmtree(video_save)

    if os.path.exists(audio_save) and os.path.isdir(audio_save):
        contend = os.listdir(audio_save)
        if contend:
            print("========== Contend of the folder music ==========")
            for index, song in enumerate(contend):
                print(f"{index+1} - {song}")
            print("=================================================")
        else:
            print("folder is empty")
    else:
        print("Folder dont exist!")