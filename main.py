from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer


class APPPP(App):
    def build(self):
        video = VideoPlayer(source='Historia_de_la_ciencia.mp4')
        return video


if __name__ == '__main__':
    APPPP().run()