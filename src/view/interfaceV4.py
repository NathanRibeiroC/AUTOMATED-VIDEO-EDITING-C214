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

x = 10
y = 10
e = 10

"""Class that implements the thread called when editing video, to avoid freezing UI"""
class EditThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    """Thread class initializator"""
    def __init__(self,filename,resourcesPath):
        QThread.__init__(self)
        self.f = filename #Filename we want to edit path
        self.r = resourcesPath #Folder we want to save our edited file

    """Run method gets called when we start the thread"""
    def run(self):
        global x
        global y
        global e
        ev = EdicaoVideo(self.f, self.r)
        self.progress.emit(25) #Updates progress bar
        ev.edita_video() #Calls video editing method
        self.progress.emit(100) #Updates progress bar
        x, y, e = ev.return_x_y()
        self.finished.emit() #Finished video editing thread

"""Class that defines matplot lib layout"""
class MplWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

"""Class that defines UI elements and it's methods"""
class Ui_MainWindow(object):
    """Method that is responsible for seting up UI's elements"""
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

        #Set default path to save our edited video
        dirname = os.path.dirname
        self.resourcesPath = os.path.join(dirname(dirname(__file__))) + '\\resources\\'  # parent do diretório atual + folder recources
        self.label_3.setText('Salvar em: ' + str(self.resourcesPath))
        self.status_label.setText('Nenhum arquivo importado')

        #Toolbar configuration
        self.toolbar = NavigationToolbar(self.widget.canvas, self.centralwidget)
        self.horizontalLayout_ApplyStyle.addWidget(self.toolbar)

        #Unable edit button
        self.editarPushButton.setEnabled(False)

        #Action triggered when clicking on "Import video" option on "Options"
        self.actionImport_Video.triggered.connect(self.get_video_file_path)
        #Action triggered when clicking on "Definir diretório destino" option on "Options"
        self.actionDefinir_diret_rio_destino.triggered.connect(self.set_video_edited_path)

        #Action triggered when clicking on Edit button, if it is enabled
        self.editarPushButton.clicked.connect(self.edit_video)

        #Set progress bar default configuration
        self.progressBar.setValue(0)
        self.progressBar.hide()

    """Method that calls video editing"""
    def edit_video(self):
        self.edit_thread = EditThread(self.filename,self.resourcesPath)  #Instantiate thread object
        self.status_label.setStyleSheet('color: yellow') #Sets status label to yellow
        self.status_label.setText('Edição em andamento') #Changes status label text content
        self.editarPushButton.setEnabled(False) #Unables edit button
        self.editarPushButton.setText('Editando ...') #Changes status label text content
        self.edit_thread.progress.connect(self.update_progressbar) #Configures thread to pass emit method value as update_progressbar parameter
        self.edit_thread.start()  #Starts the thread
        self.edit_thread.finished.connect(self.reset) #When finishes thread calls reset method

    def plot_audio(self):
        global x
        global y
        global e
        self.widget.canvas.axes.clear()
        self.widget.canvas.axes.plot(x, y, label='Áudio do Vídeo')
        self.widget.canvas.axes.plot(x, e, label='Limiar')
        self.widget.canvas.draw()

    """Method that resets UI's informations after video editing"""
    def reset(self):
        self.progressBar.hide() #Hide progressbar
        self.label.setText('Opções --> Importar Vídeo --> Editar') #Resets description on UI
        self.status_label.setStyleSheet('color: blue') #Resets description on UI
        self.status_label.setText('Edição Concluída') #Resets description on UI
        self.editarPushButton.setText('Editar') #Changes text on edit button
        self.edit_thread.quit() #Quit from thread
        self.edit_thread.deleteLater() #Delete thread
        self.plot_audio()

    """Method that updates progress bar"""
    def update_progressbar(self,value):
        self.progressBar.show() #Shows progress bar
        self.progressBar.setValue(value) #Sets progress bar value

    """Method that opens OS' modal to catch the path you want to save your edited video"""
    def get_video_file_path(self):
        aux = str(QFileDialog.getOpenFileName()[0]).replace("/","\\")
        if(aux!=''):
            self.filename = aux
            self.editarPushButton.setEnabled(True)
            self.label.setText('File: ' + str(self.filename))
            self.status_label.setStyleSheet('color: green')
            self.status_label.setText('Pronto para edição')
        else:
            pass

    """Method that sets the path we want to save our edited video"""
    def set_video_edited_path(self):
        aux = str(QFileDialog.getExistingDirectory()+'/').replace("/","\\")
        if(aux!=''):
            self.resourcesPath = aux
            self.label_3.setText('Salvar em: ' + self.resourcesPath)
        else:
            pass

    """Method used during UI's execution"""
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
