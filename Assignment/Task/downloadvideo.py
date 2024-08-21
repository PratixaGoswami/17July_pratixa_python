
import yt_dlp

def download_video(url, path='.'):
    ydl_opts = {
        'outtmpl': f'{path}/%(title)s.%(ext)s',
        'format': 'best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
download_video('https://www.youtube.com/watch?v=iUjOd7zpdsc', 'D:/Store')

