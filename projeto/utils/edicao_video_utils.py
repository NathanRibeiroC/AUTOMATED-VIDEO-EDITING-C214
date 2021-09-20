# pacote para edição de vídeo
from moviepy.editor import *
# arraynp
import numpy as np
from numpy.core.records import array
# arquivo .wav
from scipy.io import wavfile
# plot
import matplotlib.pyplot as plt
#remove file
import os
#ordenação de lista
from operator import itemgetter
#identificação de subsequencias
from itertools import groupby, count
#notificações
from .logging_utils import logConfig

# adicionar package ao sys.path
import sys
from pathlib import Path 
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Additionally remove the current file's directory from sys.path
try:
    sys.path.remove(str(parent))
except ValueError: # Already removed
    pass

class EdicaoVideo:

    def __init__(self, videoPath, resourcesPath):     
        """Características principais do arquivo de vídeo""" 
        self.resourcesPath = resourcesPath
        self.path = videoPath # caminho do vídeo
        self.clip = VideoFileClip(self.path) # array que representa vídeo


    def extract_audio_features(self):
        """Etapa de processamento do áudio do vídeo"""
        # extração do áudio do vídeo
        self.clip.audio.write_audiofile(self.resourcesPath+"edicao.wav",codec='pcm_s16le') #codec = codifica áudio em .wav 16bits
        # extraindo array de áudio
        self.fs_wav, data_wav = wavfile.read(self.resourcesPath+"edicao.wav")  #.wav ~= 44kHz, 'sample frequency' e 'sample data'
        #normalização
        #divide por 2^15 que geralmente é a resolução de cada bit por amostra
        self.data_wav_norm = data_wav / (2**15)
        return self.data_wav_norm
    
    def size_segmentation(self):
        """Segmentação de tamanho fixo do áudio"""
        self.extract_audio_features()
        signal_len = len(self.data_wav_norm) #comprimento do array
        segment_size_t = 1 # tamanho de segmento em segundos
        segment_size = segment_size_t * self.fs_wav  # tamanho do segmento em amostras
        #quebrando o sinal em 56 páginas de 2 colunas(sinal stereo) e com 48000linhas (amostras)
        self.segments = np.array([self.data_wav_norm[x:x + segment_size] for x in
                     np.arange(0, signal_len, segment_size)])

    def calculo_energia_media(self):
        """Cálculo da energia média dos segmentos do áudio"""
        self.size_segmentation()
        energies = [(s**2).sum() / len(s) for s in self.segments]
        # sem normalização haveria integer overflow aqui
        thres = 2.1 * np.median(energies)
        index_of_segments_to_keep = (np.where(energies > thres)[0])
        self.aux = index_of_segments_to_keep
        #segmentos com energia maior do que o limiar
        segments2 = self.segments[self.aux]
        #concatena segmentos dos sinais divididos, com valor de energia > limiar
        self.new_signal = np.concatenate(segments2)
        #vetores para plot (SE NECESSÁRIO NO FUTURO)
        x = [s for s in range(len(energies))]
        y = np.ones(len(energies)) * thres
    
    def subseq_max(self):
        """Código base de como identificar maior subsequência consecutiva de inteiros positivos dentro de array"""
        self.calculo_energia_media()
        array_aux = self.aux.tolist()
        self.cuts = [] # tuplas que identificam pontos de corte nos vídeos

        def subMax(array):
            c = count()
            val = max((list(g) for _, g in groupby(array, lambda x: x-next(c))), key=len)
            index_inicio = array.index(val[0])
            index_final = array.index(val[len(val)-1])
            seq = []
            if(index_inicio==0 and index_final==0):
                return 0
            else:
                for i in range(index_inicio,index_final+1):
                    seq.append(array[i])
                for i in range((index_final-index_inicio)+1):
                    array.pop(index_inicio)
            #cuts.append((index_final,index_final))
            return seq

        #extraio todas as subsequências que virarão vídeos
        c = subMax(array_aux)
        while c:
            self.cuts.append(c)
            c = subMax(array_aux)
        #ordena vetor
        self.cuts = sorted(self.cuts, key=itemgetter(0))

    def edita_video(self):
        self.subseq_max()
        """Edição de vídeo feita ao final de todas as etapas de processamento de áudio"""
        contA = 0 #quantos vídeos foram gerados
        clip_array = []
        #criacao arquivo base
        clip0 = self.clip.subclip(self.cuts[0][0]-10,self.cuts[0][len(self.cuts[0])-1])
        clip1 = self.clip.subclip(self.cuts[1][0]-10,self.cuts[1][len(self.cuts[1])-1])
        # concatinating both the clips
        final = concatenate_videoclips([clip0, clip1])
        final.write_videofile(self.resourcesPath+"corte_{0}.mp4".format(contA))

        contA = 0
        for i in range(2 , len(self.cuts)):
            clip_base = VideoFileClip(self.resourcesPath+"corte_{0}.mp4".format(contA))
            clip_corte = self.clip.subclip(self.cuts[i][0]-10,self.cuts[i][len(self.cuts[i])-1])
            final = concatenate_videoclips([clip_base, clip_corte])
            contA+=1
            final.write_videofile(self.resourcesPath+"corte_{0}.mp4".format(contA))
            clip_base = 0 # desalocar memória do processo, p/ conseguir excluir o arquivo de corte
            os.remove(self.resourcesPath+"corte_{0}.mp4".format(contA-1))
        os.remove(self.resourcesPath+"edicao.wav")



        