import os
import subprocess

def make_webm(videofile):
    subprocess.call(['ffmpeg', '-i', videofile, '-b', '1500k', '-vcodec', 'libvpx', 
        '-acodec', 'libvorbis', '-f', 'webm', '-ar', '44100', '-ab', '64k',
        '-y', videofile+".webm"])

