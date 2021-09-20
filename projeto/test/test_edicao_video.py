import unittest
from unittest import mock
from moviepy.editor import *
import os
import numpy as np
from utils.edicao_video_utils import EdicaoVideo

# python -m unittest discover
class extract_audio_feature_test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dirname=os.path.dirname #pega diretório atual
        # diretorio do arquivo video teste
        self.resourcesPath = os.path.join(self.dirname(self.dirname(__file__)))+"\\test\\resources\\video_t.mp4"          
    
    def test_extract_audio_features(self):
        ev = EdicaoVideo(self.videoTestPath,self.resourcesPath)
        self.assertEqual(str(type(ev.extract_audio_features())),"<class 'numpy.ndarray'>")
    
    def test_50(self):
        self.assertEqual(50, 50,'ver se 50 == 50')