from src.utils.edicao_video_utils import EdicaoVideo
import os
from src.view.interfaceV4 import *


# Calls ui
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


'''
# top level main
if __name__ == '__main__':
    # padrão
    dirname=os.path.dirname #pega diretório atual
    resourcesPath = os.path.join(dirname(dirname(__file__)))+'\\src\\resources\\'    # parent do diretório atual + folder recources
    # quem passa esse path é a interface do usuário
    ev = EdicaoVideo("C:\\Users\\Nathan Ribeiro\\Desktop\\Nacional-URU 2 x 6 River Plate _ Melhores Momentos _ Libertadores 17_12_2020.mp4",
    resourcesPath)
    ev.edita_video()
'''

'''
#main test
if __name__ == '__main__':
    dirname=os.path.dirname #pega diretório atual
    videoMainPath = os.path.join(dirname(dirname(__file__)))+"\\projeto\\test\\resources\\video_t.mp4"
    mainResourcesPath = os.path.join(dirname(dirname(__file__)))+"\\projeto\\utils\\resources\\"
    ev = EdicaoVideo(videoMainPath,mainResourcesPath)
    mt = EdVideoMetaData()
    print(type(mt.getDate()))
'''


    