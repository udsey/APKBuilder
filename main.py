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
        webbrowser.open(self.ids.inpt.text)


        '''sourse = self.ids.inpt.text
        if sourse:
            url, title = self.get_youtube_video_url(sourse)
            self.ids.video_player.source = url
            print(title)
            self.ids.lbl.text = title'''

    def get_youtube_video_url(self, youtube_url):
        yt = YouTube(youtube_url)
        title = yt.title
        video_stream = yt.streams.filter(res='720p').first()
        return video_stream.url, title




        #self.ids.video_player.source = url



class MyApp(App):
    def build(self):
        ssl_context = ssl.create_default_context()

        if platform == 'android':
            # On Android, use the default CA certificates bundle included in the Python for Android distribution
            ssl_context.load_default_certs()
        else:
            # On other platforms, use the default system CA certificates
            ssl_context.load_default_certs()

        return MainScreen()





if __name__ == '__main__':
    MyApp().run()

