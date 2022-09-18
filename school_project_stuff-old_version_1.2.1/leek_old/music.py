from pygame import mixer
import rich
import threading

music_path = "F:\Music\Soundtracks\Witcher_3"
mixer.init()
mixer.music.load(music_path)
progress = rich.pro

def playing_music():
    mixer.music.play()

t1 = threading.Thread