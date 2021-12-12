# pacote para edição de vídeo
from moviepy.editor import *
import numpy as np
from scipy.io import wavfile
import os
from operator import itemgetter
from itertools import groupby, count
from datetime import datetime

class EdicaoVideo:
    """Sets video file main characteristics"""
    def __init__(self, videoPath, resourcesPath):
        self.x = 0
        self.y = 0
        self.resourcesPath = resourcesPath #Sets the path we want to save our video
        print('Resources path: ' + self.resourcesPath)
        self.path = videoPath #The path of the video we want to edit
        print('Video path: '+self.path)
        self.clip = VideoFileClip(self.path) # array que representa vídeo

    """Audio processing stage"""
    def extract_audio_features(self):
        #Extracts audio from video
        self.clip.audio.write_audiofile(self.resourcesPath+"edicao.wav",codec='pcm_s16le') #codec = codifica áudio em .wav 16bits
        #Extracts audio array
        self.fs_wav, self.data_wav = wavfile.read(self.resourcesPath+"edicao.wav")  #.wav ~= 44kHz, 'sample frequency' e 'sample data'
        #Data normalization
        self.data_wav_norm = self.data_wav / (2**15)
        print('DONE - extract_audio_features - 20% concluído')
        return self.data_wav_norm

    """Fixed size segmentation"""
    def size_segmentation(self):
        self.extract_audio_features()
        signal_len = len(self.data_wav_norm) #Array's length
        segment_size_t = 1 #Segments' size
        segment_size = segment_size_t * self.fs_wav  #Segments' size in samples unit
        segments = np.array([self.data_wav_norm[x:x + segment_size] for x in #Breaking signal
                     np.arange(0, signal_len, segment_size)])
        print('DONE - size_segmentation - 40% concluído')
        return segments

    """Segments' mean energy calculation"""
    def mean_energy_calculation(self):
        segments = self.size_segmentation()
        #Calculates segments' energy
        self.energies = [(s**2).sum() / len(s) for s in segments]
        #Calculates threshold
        self.thres = 2.1 * np.median(self.energies)
        #Create rule to separate snippets with value over the threshold
        index_of_segments_to_keep = (np.where(self.energies > self.thres)[0])
        #Separates snippets with value over the threshold
        aux = index_of_segments_to_keep
        segments2 = segments[aux]
        #Concatenates all segments inside segments 2 in one array
        self.new_signal = np.concatenate(segments2)
        self.x = [s for s in range(len(self.energies))]
        self.y = np.ones(len(self.energies)) * self.thres
        print('DONE - mean_energy_calculation - 60% concluído')
        return aux

    """Identifies biggest consecutive subsequence of positive integers inside array"""
    def subseq_max(self):
        aux = self.mean_energy_calculation()
        array_aux = aux.tolist()
        cuts = [] #Tuple that indentify cuts points based on audio reference

        """Identify subsequences"""
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
            return seq

        #Extracts all subsequences that will be converted into videos
        c = subMax(array_aux)
        while c:
            cuts.append(c)
            c = subMax(array_aux)
        #Sorts array
        cuts = sorted(cuts, key=itemgetter(0))
        print('DONE - subseq_max - 80% concluído')
        return cuts

    """Video editing method"""
    def edita_video(self):
        cuts = self.subseq_max()
        contA = 0 #Counts how many videos were generated
        clip_array = []
        #Creates base files
        clip0 = self.clip.subclip(cuts[0][0]-10,cuts[0][len(cuts[0])-1])
        clip1 = self.clip.subclip(cuts[1][0]-10,cuts[1][len(cuts[1])-1])
        #Concatenating both clips
        final = concatenate_videoclips([clip0, clip1])
        final.write_videofile(self.resourcesPath+"corte_{0}.mp4".format(contA))

        #Cuts video based on indexes of the previous stages
        contA = 0
        for i in range(2 , len(cuts)):
            clip_base = VideoFileClip(self.resourcesPath+"corte_{0}.mp4".format(contA))
            clip_corte = self.clip.subclip(cuts[i][0]-10,cuts[i][len(cuts[i])-1])
            final = concatenate_videoclips([clip_base, clip_corte])
            contA+=1
            final.write_videofile(self.resourcesPath+"corte_{0}.mp4".format(contA))
            self.clip_base = 0
            os.remove(self.resourcesPath+"corte_{0}.mp4".format(contA-1))
        os.remove(self.resourcesPath+"edicao.wav")
        print('DONE - edita_video - 100% concluído')
        return contA

    def return_x_y(self):
        return self.x, self.y, self.energies
