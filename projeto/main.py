from utils.edicao_video_utils import EdicaoVideo
import os


# top level main
if __name__ == '__main__':
    # padrão
    dirname=os.path.dirname #pega diretório atual
    resourcesPath = os.path.join(dirname(dirname(__file__)))+'\\projeto\\utils\\resources\\'    # parent do diretório atual + folder recources
    # quem passa esse path é a interface do usuário
    ev = EdicaoVideo("C:\\Users\\Nathan Ribeiro\\Desktop\\Nacional-URU 2 x 6 River Plate _ Melhores Momentos _ Libertadores 17_12_2020.mp4",
    resourcesPath)
    ev.edita_video()


'''
#main test
if __name__ == '__main__':
    dirname=os.path.dirname #pega diretório atual
    videoTestPath = os.path.join(dirname(dirname(__file__)))+"\\projeto\\tests\\resources\\video_t.mp4"
    ev = EdicaoVideo(videoTestPath)
    print(type(ev.extract_audio_features()))    
    if(str(type(ev.extract_audio_features()))=="<class 'numpy.ndarray'>"):
        print('true')
'''
    