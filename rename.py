import os
import shutil
from guessit import guessit

MUSICDB = os.environ['HOME'] + '/Music'

def find(folder):
    for song in os.listdir(folder):
        songInfo = guessit(song)
        try:
            renameFile(folder + '/' + song, folder + '/' + songInfo['episode_title'] + '-' + songInfo['title'] + '.mp3')
        except:
            try:
                renameFile(folder + '/' + song, folder + '/' + songInfo['alternative_title'] + '-' + songInfo['title'] + '.mp3')
            except:
                renameFile(folder + '/' + song, folder + '/' + songInfo['title'] + '.mp3')

def renameFile(oldfile, newFile):
    shutil.move(oldfile, newFile)

find(MUSICDB)
