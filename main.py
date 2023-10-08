from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen 
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder
from kivy.core.window import Window 
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRectangleFlatButton 
from kivy.clock import Clock
Window.size = (360, 640)
class button_for_menu(MDRectangleFlatButton):
    font_name = '/usr/share/fonts/TTF/Dongle-Regular.ttf'
    font_size = '40sp'
    text_color = '#FFFFFF'
    line_color = [1, 1, 1, 1]
class MyScreens(MDScreenManager):
    pass
class splashScreen(MDScreen):
    pass 
class Markakol(MDScreen):
    pass 
class Alakol(MDScreen):
    pass
class Huron(MDScreen):
    pass
class Irtysh(MDScreen):
    pass
class MainScreen(MDScreen):
    def open_menu(self):
        self.ids.button1.text = 'Choose location:                  '
        menu_items=[
            {'viewclass': 'button_for_menu', 
             "text": 'Kazakhstan',
             'on_release':lambda: self.loading(1),
             'id':'first'
             },
            {'viewclass': 'button_for_menu', 
             "text": 'U.S.A.',
             'on_release': lambda: self.loading(2),
             },

        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.button1,
            items=menu_items,
            width_mult=4,
            elevation=0,
            background_color = '#B1BCF5', 
            opening_time=.5,
            max_height=224,
            position='center',
        )

        self.menu.open()
    def loading(self, num):
        self.menu.dismiss()
        sm.current = 'splashScreen'
        if num == 1: 
            Clock.schedule_once(self.change_kz, 1)
        elif num == 2: 
            Clock.schedule_once(self.change_en, 2)
        elif num == 3: 
            Clock.schedule_once(self.change_fr, 2)
    def change_kz(self, dt):
        sm.current = 'kz'
    def change_en(self, dt):
        sm.current = 'en'
    def change_fr(self, dt):
        sm.current = 'fr'  
class KZ(MDScreen):
    pass
class EN(MDScreen):
    pass

class MyApp(MDApp):
    country = ''
    def build(self):
        kv = Builder.load_file('main_screen.kv')
        global sm 
        sm = MDScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(splashScreen(name='splashScreen'))
        sm.add_widget(KZ(name='kz'))
        sm.add_widget(EN(name='en'))
        sm.add_widget(Markakol(name='markakol'))
        sm.add_widget(Alakol(name='alakol'))
        sm.add_widget(Huron(name='huron'))
        sm.add_widget(Irtysh(name='irtysh'))
        self.menu_items = ['Item1', 'Item2', 'Item3']
        return sm


MyApp().run()
