from kivy.config import Config
Config.set('graphics','width','1000')
Config.set('graphics','height','600')
Config.set('graphics','borderless','1')
Config.set('graphics','resizable','0')
Config.set('input','mouse','mouse,multitouch_on_demand')
from kivy.uix.behaviors import ButtonBehavior
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.properties import ObjectProperty,NumericProperty,StringProperty,BooleanProperty
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import csv



class ImageButton(ButtonBehavior,Image):
    angle=NumericProperty(0)
    pass


class CheckBox(CheckBox):
    pass

class TextInput(TextInput):
    pass

class Label(Label):

    pass

class Frame(FloatLayout):

    def set_pos(self,posx,posy):
        return (Window.width*posx,Window.height*posy)

    def set_status(self,value,state):
        if not state:
            for i in range(len(self.children)):

                if i!=13:
                    self.children[i].disabled=True
        else:
            self.children[14].color = (0.1, 0.5, 0.95, 1)
            for i in range(len(self.children)):
                self.children[i].disabled = False

    def connect(self,state):
        print("düğmeye basıldı")

    def init(self,get_x,get_y,size_x,size_y):

    # Set Frame Object


        # Create Frame Objects
        # Connect Button
        self.add_widget(ImageButton(),0)
        # Port label
        self.add_widget(Label(), 1)
        # Port inputbox
        self.add_widget(TextInput(), 2)
        # IP adress label
        self.add_widget(Label(), 3)
        # IP adress ınput box
        self.add_widget(TextInput(),4)
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
        self.add_widget(CheckBox(),10)
        #OPC option label
        self.add_widget(Label(),11)
        #OPC option button
        self.add_widget(CheckBox(), 12)
        # Frame enable
        self.add_widget(CheckBox(), 13)
        #Frame Label
        self.add_widget(Label(),14)
        # Frame Picture
        self.add_widget(Image(),15)

        # Disable all the buttons until check box press

        for i in range(len(self.children)):
            if i != 13:
                self.children[i].disabled=True

        size_h=0.1,0.1
        # Set Frame Picture
        self.children[15].allow_stretch=True
        self.children[15].keep_ratio=False
        self.children[15].size_hint=self.parent.size_hint
        self.children[15].pos= self.set_pos(get_x,get_y)
        self.children[15].source="picture_lib/frame.png"

        # Set Frame Label

        self.children[14].halign = 'left'
        self.children[14].valign = 'middle'
        self.children[14].color = (0.2, 0.2, 0.2, 1)

        self.children[14].font_size=9*(size_x*4.5)
        self.children[14].italic=True
        self.children[14].bold=True
        self.children[14].text = 'Protokol'
        self.children[14].size_hint=size_h
        self.children[14].pos = self.set_pos(get_x+0.04,get_y+size_y-0.01)



        # Set CheckBox for enable/disabel frame

        self.children[13].size_hint=size_h
        self.children[13].pos=self.set_pos(get_x+0.1,get_y+size_y-0.01)
        self.children[13].bind(active=self.set_status)


        # Set OptionBox for OPC
        self.children[12].size_hint=0.6,0.1
        self.children[12].pos=self.set_pos(get_x+size_x*(-0.2),get_y+size_y*0.7)
        self.children[12].group='protokol'
    
        # Set Option Label for OPC

        self.children[11].halign = 'left'
        self.children[11].valign = 'middle'
        self.children[11].color = (1, 1, 1, 1)
        self.children[11].font_size = 8 * (size_x * 4.5)
        self.children[11].italic = False
        self.children[11].text = 'OPC-UA Protokolü'
        self.children[11].size_hint = size_h
        self.children[11].pos = self.set_pos(get_x + size_x*0.23, get_y + size_y * 0.7)

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

        self.children[4].size_hint=0.27,0.15
        self.children[4].pos=self.set_pos(get_x + size_x * 0.55, get_y + size_y * 0.64)
        self.children[4].multiline=False
        self.children[4].padding_y=3,1
    
        # IP Address Label

        self.children[3].halign = 'left'
        self.children[3].valign = 'middle'
        self.children[3].color = (1, 1, 1, 1)
        self.children[3].font_size = 7 * (size_x * 4.5)
        self.children[3].italic = False
        self.children[3].underline=True
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
        self.children[0].keep_ratio=False
        self.children[0].allow_stretch=True
        self.children[0].size_hint=size_x*0.878,size_y*1.13
        self.children[0].pos=self.set_pos(get_x + size_x * 0.55, get_y + size_y * 0.22)
        self.children[0].source="picture_lib/connect.png"
        self.children[0].bind(on_release= self.connect)

pass

class Left_Menu(FloatLayout,ButtonBehavior):

    def set_pos(self, posx, posy):
        return (Window.width * posx, Window.height * posy)

    def init(self,screen_name):
        if str(screen_name) == 'MainMenu':
            for i in range(6):
                    self.add_widget(ImageButton(), i)


            for i in range(len(self.children)):
                 if i<5:
                     self.children[i].id="btn"+str(i)
                     self.children[i].size_hint=0.8,0.07
                     self.children[i].allow_stretch=True
                     self.children[i].keep_ratio=False
                     self.children[i].pos=self.set_pos(-0.8,0.8 - i*0.08)
                     self.children[i].source='picture_lib/button'+str(i+1)+'.png'
                 elif i==5: #Bu düğme her zaman son düğmedir ve ayar ekranına gider
                     self.children[i].id = "btn" + str(i)
                     self.children[i].size_hint = 0.8, 0.07
                     self.children[i].allow_stretch = True
                     self.children[i].keep_ratio = False
                     self.children[i].pos = self.set_pos(-0.8, 0.2)
                     self.children[i].source = 'picture_lib/button' + str(i + 1) + '.png'








        self.pos=self.set_pos(-0.17,-0.05)
        self.keep_ratio=False
        self.allow_stretch=True
        self.size_hint=0.2,1.05
        self.status=False


        self.ids.left_menu.pos = self.pos
        self.ids.left_menu.keep_ratio = False
        self.ids.left_menu.allow_stretch = True
        self.ids.left_menu.size_hint = (1,1)
        self.ids.left_menu.status = False


        self.ids.menu_button.pos=self.set_pos(0.001,0.91)
        self.ids.menu_button.keep_ratio=False
        self.ids.menu_button.allow_stretch=True
        self.ids.menu_button.size_hint=(0.13,0.045)
        self.ids.menu_button.angle=0




  















    pass


class OpenDialog(Popup):
    kullanici=StringProperty()
    passw=StringProperty()
    error=StringProperty()
    check=BooleanProperty()



    def __init__(self,parent,app,*args):
        super(OpenDialog,self).__init__(*args)
        self.parent = parent
        self.bind(kullanici=self.parent.setter('user'))
        self.bind(passw=self.parent.setter('passw'))
        self.bind(check=self.parent.setter('check'))
        self.app = app  # get the MainApp reference
        self.init()
    def init(self):
        self.title='Yetkili Girişi'
        self.ids.t1.text='Kullanıcı Adı: '
        self.ids.input.hint_text='Kullanıcı adınızı girin...'
        self.ids.input.font_size=13
        self.ids.t2.text="Şifre: "
        self.ids.input2.font_size = 13
        self.ids.input2.hint_text='Şifrenizi girin...'
    def on_error(self,inst,text):
        if text:
            self.lb_error.size_hint_y=None
            self.size_hint = self.size_hint

        else:
            self.lb_error.size_hint_y = None
            self.lb_error.height=0
            self.size_hint = self.size_hint



    def enter(self):
        if not self.text or not self.text2 :
            self.error="Hatalı veya eksik giriş!!"
        else:
            self.kullanici = str(self.text)
            self.passw = str(self.text2)

            if MainMenu.Read_Password(self,self.kullanici,self.passw)!=True:
                self.error = "Hatalı veya eksik giriş!!"

            else:
                self.check=True
                self.dismiss()


    def cancel(self):
        self.check=False
        self.dismiss()


class AppScreen(FloatLayout):
    app=ObjectProperty(None)


class MainMenu(AppScreen):
    def __init__(self, app):  # init the object, receiving the MainApp instance
        super(MainMenu, self).__init__()
        self.app = app  # get the MainApp reference
        self.init()

    user = StringProperty()
    passw = StringProperty()
    check= BooleanProperty()
    def set_pos(self, posx, posy):
        return (Window.width * posx, Window.height * posy)

    def init(self):
        self.check=False
        self.ids.exit_button.angle = 0
        self.ids.exit_button.pos = self.set_pos(0.96, 0.94)
        self.ids.exit_button.size_hint = (0.025, 0.042)
        self.ids.menu.init(self.__class__.__name__)

    def menu_buttons(self, *args):
        if (self.ids.menu.ids.left_menu.status == True):
            for i in range (len(self.ids.menu.children)):
                if i<5:

                    anim = Animation(opacity=0.8, duration=0.5)
                    anim &= Animation(pos=self.set_pos(0.005,0.8-i*0.08), duration=0.1+i*0.2)
                    anim.start(self.ids.menu.children[i])
                elif i==5: # Config
                    anim = Animation(opacity=0.8, duration=0.5)
                    anim &= Animation(pos=self.set_pos(0.005, 0.2), duration=0.1 + i * 0.2)
                    anim.start(self.ids.menu.children[i])

        elif (self.ids.menu.ids.left_menu.status == False):
            for i in range(len(self.ids.menu.children)):
                if i < 5:
                    anim = Animation(opacity=0.8, duration=0.5)
                    anim &= Animation(pos=self.set_pos(-0.8, 0.8 - i * 0.08), duration=1 )
                    anim.start(self.ids.menu.children[i])
                elif i==5: # Config
                    anim = Animation(opacity=0.8, duration=0.5)
                    anim &= Animation(pos=self.set_pos(-0.8, 0.2), duration=0.1 + i * 0.2)
                    anim.start(self.ids.menu.children[i])

    def menu_mov(self):



        if (self.ids.menu.ids.left_menu.status == False):

            animate_open = Animation(pos=self.set_pos(0,-0.05), duration=0.3)
            animate_open.start(self.ids.menu.ids.left_menu)
            self.ids.menu.ids.left_menu.status = True
            animate_open.bind(on_complete=self.menu_buttons)
        elif (self.ids.menu.ids.left_menu.status == True):
            animate_close = Animation(pos=self.set_pos(-0.171,-0.05), duration=0.3)
            animate_close.start(self.ids.menu.ids.left_menu)
            self.ids.menu.ids.left_menu.status = False
            self.menu_buttons()
        if self.ids.menu.ids.menu_button.angle == 0:
            animate_mb_open = Animation(pos=self.set_pos(0.171,0.91), angle=90, duration=0.3)
            animate_mb_open.start(self.ids.menu.ids.menu_button)
        elif self.ids.menu.ids.menu_button.angle == 90:
            animate_mb_close = Animation(pos=self.set_pos(0.001,0.91), angle=0, duration=0.3)
            animate_mb_close.start(self.ids.menu.ids.menu_button)


    def Read_Password(self,user,passw):


        self.check=False
        with open('Data/password.dtf', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')

            for satir,sutun in enumerate(reader):
                if satir>=1 :

                   if self.check== False:


                        if str(user)==str(sutun[0]) and str(passw)==str(sutun[1]):

                            self.check=True
                            return True













            #
               # b1= bytearray((sutun[0]),'utf-8')

               # b2=bytearray('test123456789','utf-8')

               #
               # b= bytearray(len(b1))
               #
               # for i in range(len(b1)):
               #     b[i]=b1[i]^b2[i]
               #

               # c = str(b, encoding='utf-8')

               #
               # b1=bytearray(c,'utf-8')

               #
               # b = bytearray(len(b1))
               # for i in range(len(b1)):
               #     b[i] = b1[i] ^ b2[i]
               #
               # c = str(b, encoding='utf-8')



    def openwindow(self,instance):


            print(instance.check)
            if instance.check==True:
                self.init()
                self.app.open_screen('configure')

    def password_check(self):
        # pop up ile yetki sor



        obj = OpenDialog(self,MainMenu)
        obj.bind(on_dismiss=self.openwindow)
        obj.open()







    def x_app(self,*args):
        self.ids.exit_button.angle=0
        App.get_running_app().stop()

    def close_app(self):
        animation=Animation(angle=360,duration=0.2)
        animation.start(self.ids.exit_button)
        animation.bind(on_complete=self.x_app)


    def on_touch_down(self, touch):

        if touch.x<self.ids.menu.ids.left_menu.right and touch.x>self.ids.menu.ids.left_menu.right-30:

            self.menu_mov()
        if self.ids.exit_button.collide_point(touch.x,touch.y):
            self.close_app()
        if self.ids.menu.children[5].collide_point(touch.x,touch.y):
            self.password_check()



class Configuration_Window(AppScreen):
    def __init__(self, app):  # init the object, receiving the MainApp instance
        super(Configuration_Window, self).__init__()
        self.app = app  # get the MainApp reference
        self.init()

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




    def create_user(self):
        with open('Data/password.dtf', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')


    def x_app(self, *args):
        self.ids.exit_button.angle = 0
        App.get_running_app().stop()

    def close_app(self):
        animation = Animation(angle=360, duration=0.2)
        animation.start(self.ids.exit_button)
        animation.bind(on_complete=self.x_app)

    def connect_device(self):
        print("Cihaza Bağlanıldı")











class MainApp(App):
    def build(self):
        print("Main App")
        self.screens = {}  # list of app screens
        self.screens['menu'] = MainMenu(self)  # self the MainApp instance, so others objects can change the screen
        self.screens['configure'] = Configuration_Window(self)
        self.root = FloatLayout()

        self.open_screen('menu') # Burası menu olmalı ama test için online yapıldı
        return self.root

    def open_screen(self,name):
        self.root.clear_widgets()
        self.root.add_widget(self.screens[name])
        #self.screens[name].run()




if __name__ == '__main__':
    MainApp().run()