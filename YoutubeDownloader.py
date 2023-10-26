from pytube import YouTube
from moviepy.editor import *

def download_as_mp3(audio_stream, save_path):
    audio_file_path = audio_stream.download(save_path)
    audio_clip = AudioFileClip(audio_file_path)
    audio_clip.write_audiofile(audio_file_path.replace(".webm", ".mp3").replace(".mp4", ".mp3"))
    audio_clip.close()
    os.remove(audio_file_path)

def download_as_mp4(video_stream, save_path):
    video_stream.download(save_path)

try:
    yt = YouTube(input("Enter link: "))
except:
    print("Connection Error")
    exit()

format_choice = input("Which format do you want to download? (mp4/mp3): ").strip().lower()

if format_choice == 'mp3':
    audio_stream = yt.streams.filter(only_audio=True).first()
    if audio_stream:
        try:
            download_as_mp3(audio_stream, '/Users/sarjhana/Documents/')
        except:
            print("Some Error!")
    else:
        print("Audio stream not found!")
elif format_choice == 'mp4':
    video_stream = yt.streams.filter(file_extension='mp4').first()
    if video_stream:
        try:
            download_as_mp4(video_stream, '/Users/sarjhana/Documents/')
        except:
            print("Some Error!")
    else:
        print("MP4 stream not found!")
else:
    print("Invalid choice!")

print('Task Completed!')
