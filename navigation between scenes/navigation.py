import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

#login
class MainWindow(Screen):
    pass
#stranka
class SecondWindow(Screen):
    pass
#transition
class WindowManager(ScreenManager):
    pass



kv = Builder.load_file("my.kv") #otevře i když se class nejmenuje MyApp (bez app)

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()