# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import*
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as FigureCanvas)
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from ..utils.edicao_video_utils import EdicaoVideo

'''
# Step 1: Create a worker class
class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self,filename,resourcesPath):
        EdicaoVideo(filename, resourcesPath).edita_video()
        #self.progress.emit(i + 1)
        self.finished.emit()
'''
class CloneThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')
    finished = pyqtSignal()

    def __init__(self,filename,resourcesPath):
        QThread.__init__(self)
        self.f = filename
        self.r = resourcesPath

    # run method gets called when we start the thread
    def run(self):
        EdicaoVideo(self.f, self.r).edita_video()
        # git clone done, now inform the main thread with the output
        self.finished.emit()

class MplWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(749, 584)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = MplWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 240, 521, 301))
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 210, 521, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_ApplyStyle = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_ApplyStyle.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_ApplyStyle.setObjectName("horizontalLayout_ApplyStyle")
        self.editarPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.editarPushButton.setGeometry(QtCore.QRect(10, 10, 221, 71))
        self.editarPushButton.setObjectName("editarPushButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 90, 251, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 400, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 50, 200, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 80, 400, 16))
        self.label_3.setObjectName("label_3")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(320, 50, 141, 16))
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 749, 21))
        self.menubar.setObjectName("menubar")
        self.menuOp_es = QtWidgets.QMenu(self.menubar)
        self.menuOp_es.setObjectName("menuOp_es")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport_Video = QtWidgets.QAction(MainWindow)
        self.actionImport_Video.setObjectName("actionImport_Video")
        self.actionDefinir_diret_rio_destino = QtWidgets.QAction(MainWindow)
        self.actionDefinir_diret_rio_destino.setObjectName("actionDefinir_diret_rio_destino")
        self.menuOp_es.addAction(self.actionImport_Video)
        self.menuOp_es.addAction(self.actionDefinir_diret_rio_destino)
        self.menubar.addAction(self.menuOp_es.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # set caminho padrão para salvar o vídeo editado
        dirname = os.path.dirname
        self.resourcesPath = os.path.join(dirname(dirname(__file__))) + '\\resources\\'  # parent do diretório atual + folder recources
        self.label_3.setText('Salvar em: ' + str(self.resourcesPath))
        self.label_2.setText('Status: Nenhum arquivo importado')

        # configuração toolbar
        self.toolbar = NavigationToolbar(self.widget.canvas, self.centralwidget)
        self.horizontalLayout_ApplyStyle.addWidget(self.toolbar)

        # desabilita botão
        self.editarPushButton.setEnabled(False)

        # menubar import video
        self.actionImport_Video.triggered.connect(self.get_video_file_path)
        # menubar set lugar para salvar o vídeo pós edição
        self.actionDefinir_diret_rio_destino.triggered.connect(self.set_video_edited_path)

        # push button editar
        self.editarPushButton.clicked.connect(self.git_clone)

    '''
    def edit_video(self):
        EdicaoVideo(self.filename, self.resourcesPath).edita_video()
    '''
    '''
    def edit_video(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run(self.filename,self.resourcesPath))
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect()
        # Step 6: Start the thread
        self.thread.start()

        # Final resets
        #self.longRunningBtn.setEnabled(False)
        #self.thread.finished.connect(
            #lambda: self.longRunningBtn.setEnabled(True)
        #    pass
        #)
        #self.thread.finished.connect(
            #lambda: self.stepLabel.setText("Long-Running Step: 0")
        #    pass
        #)
    '''

    def git_clone(self):
        # defining thread
        self.git_thread = CloneThread(self.filename,self.resourcesPath)  # This is the thread object
        self.git_thread.start()  # Finally starts the thread

    def get_video_file_path(self):
        aux = str(QFileDialog.getOpenFileName()[0]).replace("/","\\")
        if(aux!=''):
            self.filename = aux
            self.editarPushButton.setEnabled(True)
            self.label.setText('File: ' + str(self.filename))
            self.label_2.setText('Status: Arquivo importado')
        else:
            pass


    def set_video_edited_path(self):
        aux = str(QFileDialog.getExistingDirectory()).replace("/","\\")
        if(aux!=''):
            self.resourcesPath = aux
            self.label_3.setText('Salvar em: ' + self.resourcesPath)
        else:
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PROJETO C213"))
        self.editarPushButton.setText(_translate("MainWindow", "Editar"))
        self.label.setText(_translate("MainWindow", "Opções --> Importar Vídeo --> Editar"))
        self.label_2.setText(_translate("MainWindow", "Status:"))
        self.label_3.setText(_translate("MainWindow", "Salvar em:"))
        self.menuOp_es.setTitle(_translate("MainWindow", "Opções"))
        self.actionImport_Video.setText(_translate("MainWindow", "Import Video"))
        self.actionDefinir_diret_rio_destino.setText(_translate("MainWindow", "Definir diretório destino"))


