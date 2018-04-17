from Main import *
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from kivy.core.window import Window
import csv
class AppScreen(FloatLayout):
    app=ObjectProperty(None)

class Password_Window(AppScreen):
        def __init__(self, app):  # init the object, receiving the MainApp instance
            super(Password_Window, self).__init__()
            self.app = app  # get the MainApp reference
            self.init()
            self.ids.back.init()
            self.ids.back.children[0].text =''


        def set_pos(self, posx, posy):
            return (Window.width * posx, Window.height * posy)

        def set_color(self, status):
            if status == True:
                return (1, 1, 1, 1)
            else:
                return (0.5, 0.5, 0.5, 1)

        def init(self):

            self.ids.exit_button.angle = 0
            self.ids.exit_button.pos = self.set_pos(.96, 0.94)
            self.ids.exit_button.size_hint = (0.025, 0.042)

            # #
            # self.ids.password_panel.init()
            # # Konfigrasyon düğmeleri

            self.ids.config_panel_1.init()






        def open_window(self, i):

            if i == 0:
                self.init()
                self.app.open_screen('menu')
            elif i == 1:
                 self.read_parameters()

        def create_user(self):
            with open('Data/password.dtf', 'w') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')

        def read_parameters(self):
            with open('Data/parameters.dtf', 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    self.ids.back.children[0].pos = self.set_pos(0.3, -0.005)
                    self.ids.back.children[0].text= ' Bu bölüme girebilmeniz için <admin> olmanız gerekmektedir. Kullanıcı:  '+ row['Parametre']



        def x_app(self, *args):
            self.ids.exit_button.angle = 0
            App.get_running_app().stop()

        def close_app(self):
            animation = Animation(angle=360, duration=0.2)
            animation.start(self.ids.exit_button)
            animation.bind(on_complete=self.x_app)

        def connect_device(self):
            print("Cihaza Bağlanıldı")

      








