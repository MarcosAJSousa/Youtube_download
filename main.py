from fileinput import filename
from tkinter import filedialog
from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import os
from pytube import YouTube
from tqdm import tqdm

def autorizacao():
    home.stackedWidget.setCurrentWidget(home.page_2)
    home.formato.setCurrentIndex(-1)
    home.formato.setPlaceholderText(" Selecione:")
    home.url.setText('')

def download():
    try:         
        url = home.url.text()
        video = YouTube(url)
        
        if home.formato.currentText() == " MP3 (Áudio)":
            home.stackedWidget.setCurrentWidget(home.page_4)
            path_place = filedialog.askdirectory()
            video = video.streams.filter(only_audio=True).first()
            out_file = video.download(output_path=path_place)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            home.stackedWidget.setCurrentWidget(home.page_3)
        
        elif home.formato.currentText() == " MP4 (Vídeo)":
            home.stackedWidget.setCurrentWidget(home.page_4)      
            path_place = filedialog.askdirectory()
            video = video.streams.get_highest_resolution()
            video.download(output_path=path_place)
            home.stackedWidget.setCurrentWidget(home.page_3)
        else:
            pass

    except:
        QMessageBox.warning(home, ' Youtube Downloads', '                                Operação inválida!  \n \n  Verifique se os campos estão preenchidos corretamente      ')
        home.stackedWidget.setCurrentWidget(home.page_2)
        pass

app=QtWidgets.QApplication([])
# Janela Principal
home=uic.loadUi('home.ui')
home.stackedWidget.setCurrentWidget(home.page)

#button Download
home.button_concordo.clicked.connect(autorizacao)
home.button_download.clicked.connect(download)
home.button_novo.clicked.connect(autorizacao)
#home.pushButton.clicked.connect(dowload_video)
#QMessageBox.warning(home, '- Atenção -', 'Atenção, os direitos autorais devem ser respeitados')   

home.show()
app.exec()