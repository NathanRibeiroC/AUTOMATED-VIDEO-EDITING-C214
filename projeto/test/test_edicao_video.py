import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock
from moviepy.editor import *
import os
import numpy as np
from utils.edicao_video_utils import EdicaoVideo, EdVideoMetaData
from scipy.io import wavfile

# python -m unittest discover
class extract_audio_feature_test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dirname=os.path.dirname #pega diretório atual
        # diretorio do arquivo video teste
        self.testResourcesPath = os.path.join(self.dirname(self.dirname(__file__)))+"\\test\\resources\\"    
        self.videoTestResourcesPath = os.path.join(self.dirname(self.dirname(__file__)))+"\\test\\resources\\video_t.mp4"       
    
    # verifico se chamou a função anterior
    def test_size_segmentation_mock(self):
        ev = EdicaoVideo(self.videoTestResourcesPath,self.testResourcesPath)
        ev.extract_audio_features = MagicMock()
        ev.data_wav_norm = [[0,1,1],[0,0,0]]
        ev.fs_wav = 4800
        ev.size_segmentation()
        ev.extract_audio_features.assert_called_once_with()
    '''
    def test_calculo_energia_media_mock(self):
        ev = EdicaoVideo(self.videoTestResourcesPath,self.testResourcesPath)
        ev.extract_audio_features = MagicMock()
        ev.size_segmentation = MagicMock()
        ev.conta_media = MagicMock(return_value=[[1,2,3,4,5],[1,2,3,4,5]])
        ev.calculo_energia_media()
        ev.extract_audio_features.assert_called_once_with()
        ev.size_segmentation.assert_called_once_with()       
    '''
    # verifico retorno da função é 1
    def test_size_segmentation_return(self):
        ev = EdicaoVideo(self.videoTestResourcesPath,self.testResourcesPath)
        ev.extract_audio_features = MagicMock()
        ev.data_wav_norm = [1]
        ev.fs_wav = 4800
        ev.size_segmentation()
        self.assertEqual(ev.segments,1)

    def test_get_time(self):
        evmt = EdVideoMetaData()
        self.assertEqual(str(type(evmt.getTime())),"<class 'datetime.time'>")

    def test_get_date(self):
        evmt = EdVideoMetaData()
        self.assertEqual(str(type(evmt.getDate())),"<class 'datetime.date'>")
