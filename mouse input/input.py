import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line

class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(1,0,0,0.5, mode='rgba')
            self.Rectangle = Rectangle(pos=(0,0), size=(50,50))


    #btn = ObjectProperty(None)

    def on_touch_down(self, touch):
        print("down", touch)
        self.Rectangle.pos = touch.pos
        #self.btn.opacity = 0.5

    def on_touch_move(self, touch):
        print("move", touch)
        self.Rectangle.pos = touch.pos
    #def on_touch_up(self, touch):
        #print("up", touch)
        #self.btn.opacity = 1

class MyApp(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    MyApp().run()