from Main import *
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from functools import partial
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager,Screen
import datetime
from kivy.clock import Clock


class Background(FloatLayout):
    def update_time(self,dt):
        self.children[1].text = str(datetime.datetime.now().strftime('%Y-%m-%d'))
        self.children[2].text = str(datetime.datetime.now().strftime('%H:%M:%S'))
    def set_pos(self, posx, posy):
        return (Window.width * posx, Window.height * posy)
    def init(self):
        self.add_widget(Image(), 3)
        for i in range(4):
            self.add_widget(Label(),i)
            self.children[i].halign = 'left'
            self.children[i].valign = 'middle'
            self.children[i].color = (0.8, 0.8, 0.8, 1)
            self.children[i].font_size = 12
            self.children[i].size_hint = 0.05, 0.05





        self.children[4].allow_stretch = True
        self.children[4].keep_ratio = False
        self.children[4].size_hint = self.parent.size_hint
        self.children[4].pos = self.set_pos(0,0)
        self.children[4].source= "picture_lib/Background.png"


        self.children[0].color = (0.8, 0.8, 0.1, 1)
        self.children[0].text = 'Endüstri 4.0 Uygulama Yazılım Projesi v1.0'
        self.children[0].pos=self.set_pos(0.25,-0.005)
        self.children[0].font_size = 14
        Clock.schedule_interval(self.update_time,1)
        self.children[1].pos=self.set_pos(0.92,0.005)
        self.children[2].pos = self.set_pos(0.92, -0.008)
        self.children[1].font_size = 10
        self.children[2].font_size = 10
        self.children[3].pos=self.set_pos(0.03,-0.005)
        self.children[3].text='Durum'
        self.children[3].font_size = 16
        self.children[3].bold=True


class ImageButton(ButtonBehavior, Image):
    angle = NumericProperty(0)
    pass


class CheckBox(CheckBox):
    pass


class TextInput(TextInput):
    pass


class Label(Label):
    pass


class ConfigPanel(FloatLayout):
    def set_pos(self, posx, posy):
        return (Window.width * posx, Window.height * posy)

    def edit_parameter(self, i, state):

        self.parent.open_window(i)

    def init(self):
        button_count = 6
        for i in range(button_count):
            self.add_widget(ImageButton(), i)
            self.children[i].keep_ratio = False
            self.children[i].allow_stretch = True
            self.children[i].size_hint = 1 / (2*button_count), 0.05
            self.children[i].pos = self.set_pos((1 / button_count) * 0.5*i, 0.05)
            self.children[i].source = "picture_lib/config_button" + str(i) + ".png"
            self.children[i].id='Button_'+str(i)
            self.children[i].bind(on_release=partial(self.edit_parameter, i))

    pass


class Frame(FloatLayout):

    def set_pos(self, posx, posy):
        return (Window.width * posx, Window.height * posy)

    def set_status(self, value, state):
        if not state:
            for i in range(len(self.children)):

                if i != 13:
                    self.children[i].disabled = True
        else:
            self.children[14].color = (0.1, 0.5, 0.95, 1)
            for i in range(len(self.children)):
                self.children[i].disabled = False

    def connect(self, state):
        print("düğmeye basıldı")

    def init(self, get_x, get_y, size_x, size_y):

        # Set Frame Object

        # Create Frame Objects
        # Connect Button
        self.add_widget(ImageButton(), 0)
        # Port label
        self.add_widget(Label(), 1)
        # Port inputbox
        self.add_widget(TextInput(), 2)
        # IP adress label
        self.add_widget(Label(), 3)
        # IP adress ınput box
        self.add_widget(TextInput(), 4)
        # Profibus option label
        self.add_widget(Label(), 5)
        # Profibus option button
        self.add_widget(CheckBox(), 6)
        # MOD-BUS option label
        self.add_widget(Label(), 7)
        # MOD-BUS option button
        self.add_widget(CheckBox(), 8)
        # TCP option label
        self.add_widget(Label(), 9)
        # TCP option button
        self.add_widget(CheckBox(), 10)
        # OPC option label
        self.add_widget(Label(), 11)
        # OPC option button
        self.add_widget(CheckBox(), 12)
        # Frame enable
        self.add_widget(CheckBox(), 13)
        # Frame Label
        self.add_widget(Label(), 14)
        # Frame Picture
        self.add_widget(Image(), 15)

        # Disable all the buttons until check box press

        for i in range(len(self.children)):
            if i != 13:
                self.children[i].disabled = True

        size_h = 0.1, 0.1
        # Set Frame Picture
        self.children[15].allow_stretch = True
        self.children[15].keep_ratio = False
        self.children[15].size_hint = self.parent.size_hint
        self.children[15].pos = self.set_pos(get_x, get_y)
        self.children[15].source = "picture_lib/frame.png"

        # Set Frame Label

        self.children[14].halign = 'left'
        self.children[14].valign = 'middle'
        self.children[14].color = (0.2, 0.2, 0.2, 1)

        self.children[14].font_size = 9 * (size_x * 4.5)
        self.children[14].italic = True
        self.children[14].bold = True
        self.children[14].text = 'Protokol'
        self.children[14].size_hint = size_h
        self.children[14].pos = self.set_pos(get_x + 0.04, get_y + size_y - 0.01)

        # Set CheckBox for enable/disabel frame

        self.children[13].size_hint = size_h
        self.children[13].pos = self.set_pos(get_x + 0.1, get_y + size_y - 0.01)
        self.children[13].bind(active=self.set_status)

        # Set OptionBox for OPC
        self.children[12].size_hint = 0.6, 0.1
        self.children[12].pos = self.set_pos(get_x + size_x * (-0.2), get_y + size_y * 0.7)
        self.children[12].group = 'protokol'

        # Set Option Label for OPC

        self.children[11].halign = 'left'
        self.children[11].valign = 'middle'
        self.children[11].color = (1, 1, 1, 1)
        self.children[11].font_size = 8 * (size_x * 4.5)
        self.children[11].italic = False
        self.children[11].text = 'OPC-UA Protokolü'
        self.children[11].size_hint = size_h
        self.children[11].pos = self.set_pos(get_x + size_x * 0.23, get_y + size_y * 0.7)

        # Set OptionBox for TCP
        self.children[10].size_hint = 0.6, 0.1
        self.children[10].pos = self.set_pos(get_x + size_x * (-0.2), get_y + size_y * 0.55)
        self.children[10].group = 'protokol'

        # Set Option Label for TCP

        self.children[9].halign = 'left'
        self.children[9].valign = 'middle'
        self.children[9].color = (1, 1, 1, 1)
        self.children[9].font_size = 8 * (size_x * 4.5)
        self.children[9].italic = False
        self.children[9].text = 'TCP-IP Protokolü'
        self.children[9].size_hint = size_h
        self.children[9].pos = self.set_pos(get_x + size_x * 0.22, get_y + size_y * 0.55)

        # Set OptionBox for Mod-Bus
        self.children[8].size_hint = 0.6, 0.1
        self.children[8].pos = self.set_pos(get_x + size_x * (-0.2), get_y + size_y * 0.4)
        self.children[8].group = 'protokol'

        # Set Option Label for Mod-Bus

        self.children[7].halign = 'left'
        self.children[7].valign = 'middle'
        self.children[7].color = (1, 1, 1, 1)
        self.children[7].font_size = 8 * (size_x * 4.5)
        self.children[7].italic = False
        self.children[7].text = 'MOD-BUS Protokolü'
        self.children[7].size_hint = size_h
        self.children[7].pos = self.set_pos(get_x + size_x * 0.24, get_y + size_y * 0.4)

        # Set OptionBox for Mod-Bus
        self.children[6].size_hint = 0.6, 0.1
        self.children[6].pos = self.set_pos(get_x + size_x * (-0.2), get_y + size_y * 0.25)
        self.children[6].group = 'protokol'

        # Set Option Label for Mod-Bus

        self.children[5].halign = 'left'
        self.children[5].valign = 'middle'
        self.children[5].color = (1, 1, 1, 1)
        self.children[5].font_size = 8 * (size_x * 4.5)
        self.children[5].italic = False
        self.children[5].text = 'PROFI-BUS Protokolü'
        self.children[5].size_hint = size_h
        self.children[5].pos = self.set_pos(get_x + size_x * 0.25, get_y + size_y * 0.25)

        # IP Address Input Box

        self.children[4].size_hint = 0.27, 0.15
        self.children[4].pos = self.set_pos(get_x + size_x * 0.55, get_y + size_y * 0.64)
        self.children[4].multiline = False
        self.children[4].padding_y = 3, 1

        # IP Address Label

        self.children[3].halign = 'left'
        self.children[3].valign = 'middle'
        self.children[3].color = (1, 1, 1, 1)
        self.children[3].font_size = 7 * (size_x * 4.5)
        self.children[3].italic = False
        self.children[3].underline = True
        self.children[3].text = ' IP Adresi'
        self.children[3].size_hint = size_h
        self.children[3].pos = self.set_pos(get_x + size_x * 0.57, get_y + size_y * 0.82)

        # Port Input Box

        self.children[2].size_hint = 0.1, 0.15
        self.children[2].pos = self.set_pos(get_x + size_x * 0.85, get_y + size_y * 0.64)
        self.children[2].multiline = False
        self.children[2].padding_y = 3, 1

        # Port Label

        self.children[1].halign = 'left'
        self.children[1].valign = 'middle'
        self.children[1].color = (1, 1, 1, 1)
        self.children[1].font_size = 7 * (size_x * 4.5)
        self.children[1].italic = False
        self.children[1].underline = True
        self.children[1].text = ' Port'
        self.children[1].size_hint = size_h
        self.children[1].pos = self.set_pos(get_x + size_x * 0.835, get_y + size_y * 0.82)

        # Connect Button
        self.children[0].keep_ratio = False
        self.children[0].allow_stretch = True
        self.children[0].size_hint = size_x * 0.878, size_y * 1.13
        self.children[0].pos = self.set_pos(get_x + size_x * 0.55, get_y + size_y * 0.22)
        self.children[0].source = "picture_lib/connect.png"
        self.children[0].bind(on_release=self.connect)


pass


class Left_Menu(FloatLayout, ButtonBehavior):

    def set_pos(self, posx, posy):
        return (Window.width * posx, Window.height * posy)

    def create_buttons(self, screen_name):
        if str(screen_name) == 'MainMenu':

            for i in range(6):
                self.add_widget(ImageButton(), i)
            for i in range(len(self.children)):
                if i < 5:
                    self.children[i].id = "btn" + str(i)
                    self.children[i].size_hint = 0.8, 0.07
                    self.children[i].allow_stretch = True
                    self.children[i].keep_ratio = False
                    self.children[i].pos = self.set_pos(-0.8, 0.8 - i * 0.08)
                    self.children[i].source = 'picture_lib/button' + str(i + 1) + '.png'
                elif i == 5:  # Bu düğme her zaman son düğmedir ve ayar ekranına gider
                    self.children[i].id = "btn" + str(i)
                    self.children[i].size_hint = 0.8, 0.07
                    self.children[i].allow_stretch = True
                    self.children[i].keep_ratio = False
                    self.children[i].pos = self.set_pos(-0.8, 0.2)
                    self.children[i].source = 'picture_lib/button' + str(i + 1) + '.png'

    def init(self):

        self.pos = self.set_pos(-0.17, 0.0435)
        self.keep_ratio = False
        self.allow_stretch = True
        self.size_hint = 0.2, 0.957
        self.status = False

        self.ids.left_menu.pos = self.pos
        self.ids.left_menu.keep_ratio = False
        self.ids.left_menu.allow_stretch = True
        self.ids.left_menu.size_hint = (1, 1)
        self.ids.left_menu.status = False

        self.ids.menu_button.pos = self.set_pos(0.001, 0.91)
        self.ids.menu_button.keep_ratio = False
        self.ids.menu_button.allow_stretch = True
        self.ids.menu_button.size_hint = (0.13, 0.045)
        self.ids.menu_button.angle = 0

    pass

