from kivy.config import Config
# Config.set('graphics','width','1600') #1000
# Config.set('graphics','height','1000')#600
Config.set('graphics','borderless','1')
Config.set('graphics','resizable','0')
Config.set('graphics','fullscreen','auto')
Config.set('input','mouse','mouse,multitouch_on_demand')

# Internal Libraries
from Widget_Library import *
from Config_Screen import *
from PasswordScreen import *
#


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.popup import Popup

from kivy.properties import ObjectProperty,NumericProperty,StringProperty,BooleanProperty
from kivy.animation import Animation
from kivy.core.window import Window




import csv


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
        self.ids.input.font_size=12
        self.ids.t2.text="Şifre: "
        self.ids.input2.font_size = 12
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
        self.ids.menu.create_buttons('MainMenu')
        self.ids.back.init()

    user = StringProperty()
    passw = StringProperty()
    check= BooleanProperty()
    def set_pos(self, posx, posy):
        return (Window.width * posx, Window.height * posy)

    def init(self):
        self.check=False
        self.ids.exit_button.angle = 0
        self.ids.exit_button.pos = self.set_pos(0.96, 0.94)
        self.ids.exit_button.size_hint = (0.020, 0.035)

        self.ids.menu.init()



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

            animate_open = Animation(pos=self.set_pos(0,0.0435), duration=0.3)
            animate_open.start(self.ids.menu.ids.left_menu)
            self.ids.menu.ids.left_menu.status = True
            animate_open.bind(on_complete=self.menu_buttons)
        elif (self.ids.menu.ids.left_menu.status == True):
            animate_close = Animation(pos=self.set_pos(-0.171,0.0435), duration=0.3)
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


#Klaslar arası bilgi aktarımı
    def write_to_parameter(self,user):

          with open('Data/parameters.dtf', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')

            writer.writerow(['Fonksiyon','Parametre'])
            writer.writerow(['Kullanici',str(user)])



    def openwindow(self,instance):

            if instance.check==True:
                self.write_to_parameter(self.user)
                self.menu_mov()
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









class MainApp(App):
    def build(self):

        self.screens = {}  # list of app screens
        self.screens['menu'] = MainMenu(self)  # self the MainApp instance, so others objects can change the screen
        self.screens['configure'] = Configuration_Window(self)
        self.screens['password']= Password_Window(self)
        self.root = FloatLayout()


        self.open_screen('menu')
        return self.root

    def open_screen(self,name):

        self.root.clear_widgets()
        self.root.add_widget(self.screens[name])
        #self.screens[name].run()




if __name__ == '__main__':
    MainApp().run()