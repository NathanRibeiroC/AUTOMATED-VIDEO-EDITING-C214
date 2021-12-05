import unittest
from unittest.mock import MagicMock
import os
from src.utils.edicao_video_utils import EdicaoVideo
from pathlib import Path
import numpy as np

## python -m unittest discover
class edicao_video_utils_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dirname=os.path.dirname #pega diretório atual
        cls.testResourcesPath = os.path.join(cls.dirname(cls.dirname(cls.dirname(__file__)))) + "\\test\\resources\\"
        cls.videoTestResourcesPath = cls.testResourcesPath + "video_t.mp4"
        cls.ev = EdicaoVideo(cls.videoTestResourcesPath, cls.testResourcesPath)


    def test_aaa(self):
        self.assertTrue(True)

    '''
    def test_type_retorn_extract_audio_feature(self):
        self.assertEqual(str(type(self.ev.extract_audio_features())),"<class 'numpy.ndarray'>")

    def test_extract_audio_feature_cria_wav_file(self):
        self.ev.extract_audio_features()
        my_file = Path(self.testResourcesPath + '/edicao.wav')
        if my_file.is_file():
            self.assertTrue(True)

    def test_type_retorn_size_segmentation(self):
        self.assertEqual(str(type(self.ev.size_segmentation())),"<class 'numpy.ndarray'>")

    def test_return_calcula_energia_media(self):
        self.assertEqual(str(type(self.ev.calculo_energia_media())), "<class 'numpy.ndarray'>")

    def test_type_return_sub_max(self):
        self.ev.calculo_energia_media = MagicMock(return_value = np.array([216, 237, 238, 239, 240, 241, 337, 338, 339, 340, 341, 342, 343, 344, 348, 376, 377, 378, 379, 380, 381, 382, 437, 438, 439, 440, 441, 442, 520, 521, 522, 523, 524, 546, 601, 602, 603, 604, 605, 606, 607, 608, 654, 667, 668, 669, 670, 671, 672, 673, 674, 695, 696, 697, 698, 699, 700, 701, 702, 703]))
        self.assertEqual(str(type(self.ev.subseq_max())), "<class 'list'>")

    def test_called_once_calculo_energia_media(self):
        self.ev.calculo_energia_media = MagicMock(return_value = np.array([216, 237, 238, 239, 240, 241, 337, 338, 339, 340, 341, 342, 343, 344, 348, 376, 377, 378, 379, 380, 381, 382, 437, 438, 439, 440, 441, 442, 520, 521, 522, 523, 524, 546, 601, 602, 603, 604, 605, 606, 607, 608, 654, 667, 668, 669, 670, 671, 672, 673, 674, 695, 696, 697, 698, 699, 700, 701, 702, 703]))
        self.ev.subseq_max()
        self.ev.calculo_energia_media.assert_called_once_with()

    def test_create_file_edita_video(self):
        self.ev.extract_audio_features()
        self.ev.subseq_max = MagicMock(return_value = [[2, 3], [5,6]])
        self.ev.edita_video()
        my_file = Path(self.testResourcesPath + '/corte_0.mp4')
        if my_file.is_file():
            self.assertTrue(True)
        os.remove(self.testResourcesPath + "corte_0.mp4")

    def test_edita_video_loop(self):
        self.ev.extract_audio_features()
        self.ev.subseq_max = MagicMock(return_value = [[2, 3], [5,6],[7,8],[1,5],[1,10]])
        self.ev.edita_video()
        self.assertEqual(self.ev.clip_base,0)
        os.remove(self.testResourcesPath + "corte_3.mp4")

    def test_return_threshold_calculo_energia_media(self):
        ev = EdicaoVideo(self.videoTestResourcesPath, self.testResourcesPath)
        ev.calculo_energia_media()
        self.assertEqual(ev.thres,0.0004068760747267377)
    '''



