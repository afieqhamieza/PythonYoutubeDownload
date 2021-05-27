from __future__ import unicode_literals
import youtube_dl
import os
from pydub import AudioSegment
from pytube import YouTube
import moviepy.editor as mp
# from videoprops import get_audio_properties
from IPython.display import Audio
import subprocess
import ffprobe
from datetime import datetime
import sys

# setting the working directory path
def setpath(path):
     # define save path folder
    os.chdir(path)  # change to the file directory

# extracting the audio segment of the audio input url
def audio_process(audio_url, audiofilename, path):
    # audio_url = 'https://youtu.be/xseXbA2N6D0'
    # audiofilename = 'audio_url'
    # download video
    try:
        print("sks")
        print('TryAudio')
        print(audio_url)
        print(sys.version)
        yt_obj = YouTube(audio_url)
        print(yt_obj, 'Audio')

        filters = yt_obj.streams.filter(only_audio=True).first()
        # download the highest quality video
        filters.download(output_path=path, filename=audiofilename)
        mp4_file = audiofilename + '.mp4'
        mp3_file = audiofilename + '.mp3'
        new_file = mp.AudioFileClip(mp4_file)
        new_file.write_audiofile(mp3_file)
        os.remove(mp4_file)
        print('Video Audio Downloaded Successfully')
        return audio_url, path, audiofilename + '.mp3'
    except Exception as e:
        print(e)


if __name__ == "__main__":
    SAVE_PATH = '/Users/afieqhamieza/Documents/github repo/PythonYoutubeDownload/vid_download'
    setpath(SAVE_PATH)
    print("1")
    audiourl, audiopath, audiosfilename = audio_process(
        'https://youtu.be/xseXbA2N6D0', 'audio_url', SAVE_PATH)
