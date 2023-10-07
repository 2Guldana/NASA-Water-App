from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen 
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder
from kivy.core.window import Window 
from kivymd.uix.list import MDList, OneLineListItem

Window.size = (360, 640)

class MainScreen(MDScreen):
    pass 

class MyApp(MDApp):
    def build(self):
        kv = Builder.load_file('main_screen.kv')
        global sm 
        sm = MDScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))
        return sm


MyApp().run()
