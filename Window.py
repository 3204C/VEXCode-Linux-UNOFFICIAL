from PySide6 import QtWidgets, QtCore, QtGui, QtWebEngineWidgets, QtMultimediaWidgets, QtMultimedia
import sys, requests

class LoadingWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loading")
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setGeometry(300, 600, 600, 300)
        self.setFixedSize(self.size())
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: #f0f0f0;")

        self.player = QtMultimedia.QMediaPlayer()
        self.player.setSource(QtCore.QUrl.fromLocalFile('VEXCode loading-3000.mp4'))
        self.player.setLoops(-1)

        self.videoWidget = QtMultimediaWidgets.QVideoWidget()
        self.player.setVideoOutput(self.videoWidget)

        self.player.play()

        self.setCentralWidget(self.videoWidget)

        self.move(self.pos() + (QtWidgets.QApplication.primaryScreen().geometry().center() - self.geometry().center()))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VEXCode V5")
        self.resize(QtWidgets.QApplication.primaryScreen().size())
        self.webview = QtWebEngineWidgets.QWebEngineView()
        self.webview.setUrl(QtCore.QUrl("https://codev5.vex.com"))
        self.setCentralWidget(self.webview)
        self.webview.loadFinished.connect(on_load_finished)

def on_load_finished():
    loadingWindow.close()
    window.show()

app = QtWidgets.QApplication(sys.argv)
loadingWindow = LoadingWindow()
window = MainWindow()
loadingWindow.show()
app.exec()