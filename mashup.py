import os
import sys
import yt_dlp
from pydub import AudioSegment

def download_videos(singer, num_videos):
    os.makedirs("audios", exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': 'audios/%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    search_query = f"ytsearch{num_videos}:{singer} official song"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])


def trim_and_merge(duration, output_file):
    merged = AudioSegment.empty()

    for file in os.listdir("audios"):
        if file.endswith(".mp3"):
            audio_path = os.path.join("audios", file)
            audio = AudioSegment.from_file(audio_path)
            trimmed = audio[:duration * 1000]
            merged += trimmed

    merged.export(output_file, format="mp3")


def main():
    if len(sys.argv) != 5:
        print("Usage: python 102303794.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer = sys.argv[1]

    try:
        num_videos = int(sys.argv[2])
        duration = int(sys.argv[3])
    except ValueError:
        print("Error: NumberOfVideos and AudioDuration must be integers.")
        sys.exit(1)

    output_file = sys.argv[4]

    if num_videos <= 10:
        print("Error: Number of videos must be greater than 10.")
        sys.exit(1)

    if duration <= 20:
        print("Error: Duration must be greater than 20 seconds.")
        sys.exit(1)

    try:
        download_videos(singer, num_videos)
        trim_and_merge(duration, output_file)
        print("Mashup created successfully:", output_file)
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()