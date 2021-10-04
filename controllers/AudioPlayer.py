import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M

class AudioPlayer:
    prefixPath = './songs/'
    song = ''
    player = None

    def __init__(self, song):
        self.song = song

        url = C.QUrl.fromLocalFile(self.song)
        content = M.QMediaContent(url)
        self.player = M.QMediaPlayer()
        self.player.setMedia(content)


    def play(self):
        self.player.play()


    def stop(self):
        self.player.stop()

    def pause(self):
        self.player.pause()
