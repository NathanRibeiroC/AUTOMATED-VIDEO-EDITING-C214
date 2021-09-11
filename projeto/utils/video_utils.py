# pacote para edição de vídeo
from moviepy.editor import *
# arraynp
import numpy as np
# arquivo .wav
from scipy.io import wavfile
# plot
import matplotlib.pyplot as plt
#remove file
import os
#ordenação de lista
from operator import itemgetter

class EdicaoVideo:

    def __init__(self, videoPath):                
        self.path = videoPath # caminho do vídeo
        self.clip = VideoFileClip(self.videoPath) # array que representa vídeo

    def treat_audio(self):
        # extração do áudio do vídeo
        self.clip.audio.write_audiofile("resources/edicao.wav",codec='pcm_s16le') #codec = codifica áudio em .wav 16bits
        # extraindo array de áudio
        self.fs_wav, self.data_wav = wavfile.read("resources/edicao.wav")  #.wav ~= 44kHz, 'sample frequency' e 'sample data'



        