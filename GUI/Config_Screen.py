
from Main import *
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from kivy.core.window import Window

class AppScreen(FloatLayout):
    app=ObjectProperty(None)

class Configuration_Window(AppScreen):
    def __init__(self, app):  # init the object, receiving the MainApp instance
        super(Configuration_Window, self).__init__()
        self.app = app  # get the MainApp reference
        self.init()
        self.ids.back.init()
        self.ids.back.children[0].text=''

    def set_pos(self,posx,posy):
        return (Window.width*posx,Window.height*posy)


    def set_color(self,status):
        if status==True:
            return (1, 1, 1, 1)
        else:
            return (0.5, 0.5, 0.5, 1)


    def init(self):



        self.ids.exit_button.angle = 0
        self.ids.exit_button.pos = self.set_pos(.96,0.94)
        self.ids.exit_button.size_hint = (0.025, 0.042)


        # Frame1 ayarları
        frame_x=0.01
        frame_y=0.65
        ratio= 1.5 # Ratio değerini değiştirmek frame ölçülerini bozacaktır
        size_x=0.45
        size_y=size_x/ratio

        self.ids.Frame1.pos=self.set_pos(frame_x,frame_y)
        self.ids.Frame1.size_hint = size_x,size_y
        self.ids.Frame1.init(frame_x,frame_y,size_x,size_y)
        self.ids.Frame1.children[14].text = 'Protokol1'

        # Frame2 ayarları
        frame_x = 0.50
        frame_y = 0.65
        ratio = 1.5  # Ratio değerini değiştirmek frame ölçülerini bozacaktır
        size_x = 0.45
        size_y = size_x / ratio

        self.ids.Frame2.pos = self.set_pos(frame_x, frame_y)
        self.ids.Frame2.size_hint = size_x, size_y
        self.ids.Frame2.init(frame_x, frame_y, size_x, size_y)
        self.ids.Frame2.children[14].text = 'Protokol2'

        # Frame3 ayarları
        frame_x = 0.01
        frame_y = 0.25
        ratio = 1.5  # Ratio değerini değiştirmek frame ölçülerini bozacaktır
        size_x = 0.45
        size_y = size_x / ratio

        self.ids.Frame3.pos = self.set_pos(frame_x, frame_y)
        self.ids.Frame3.size_hint = size_x, size_y
        self.ids.Frame3.init(frame_x, frame_y, size_x, size_y)
        self.ids.Frame3.children[14].text = 'Protokol3'

        # Frame4 ayarları
        frame_x = 0.5
        frame_y = 0.25
        ratio = 1.5  # Ratio değerini değiştirmek frame ölçülerini bozacaktır
        size_x = 0.45
        size_y = size_x / ratio

        self.ids.Frame4.pos = self.set_pos(frame_x, frame_y)
        self.ids.Frame4.size_hint = size_x, size_y
        self.ids.Frame4.init(frame_x, frame_y, size_x, size_y)
        self.ids.Frame4.children[14].text = 'Protokol4'


        #Konfigrasyon düğmeleri

        self.ids.config_panel.init()


    def open_window(self,i):

        if i==0:
            self.init()
            self.app.open_screen('menu')
        elif i==1:
            self.init()
            self.app.open_screen('password')



    def x_app(self, *args):
        self.ids.exit_button.angle = 0
        App.get_running_app().stop()

    def close_app(self):
        animation = Animation(angle=360, duration=0.2)
        animation.start(self.ids.exit_button)
        animation.bind(on_complete=self.x_app)

    def connect_device(self):
        print("Cihaza Bağlanıldı")



