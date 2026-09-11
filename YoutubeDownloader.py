import yt_dlp
import os
import imageio_ffmpeg as ffmpeg

# user pyenv

def download_as_mp3(video_url, save_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def download_as_mp4(video_url, save_path):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

video_url = input("Enter link: ").strip()
format_choice = input("Which format do you want to download? (mp4/mp3): ").strip().lower()
save_path = '/Users/sarjhana/Documents/'

if format_choice == 'mp3':
    download_as_mp3(video_url, save_path)
elif format_choice == 'mp4':
    download_as_mp4(video_url, save_path)
else:
    print("Invalid choice!")

print('Task Completed!')
