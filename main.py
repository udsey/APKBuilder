from kivy.app import App
from kivy.lang import Builder
from pytube import YouTube
from kivy.uix.screenmanager import  Screen
import ssl
from kivy.utils import platform
from kivy.utils import platform
import webbrowser


Builder.load_file("main.kv")



class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

    def play_video(self):
        #webbrowser.open(self.ids.inpt.text)
        sourse = self.ids.inpt.text
        if sourse:
            url, title = self.get_youtube_video_url(sourse)
            print(11111)
            self.ids.video_player.source = url
            print(title)
            self.ids.lbl.text = title

    def get_youtube_video_url(self, youtube_url):
        ssl._create_default_https_context = ssl._create_unverified_context
        yt = YouTube(youtube_url)
        title = yt.title
        print('New title was load')
        video_stream = yt.streams.filter(res='240p').first()
        print('Stream')
        return video_stream.url, title




        #self.ids.video_player.source = url



class MyApp(App):
    def build(self):

        return MainScreen()





if __name__ == '__main__':
    MyApp().run()

