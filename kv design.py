import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyLidl(Widget):
    name = ObjectProperty(None)
    lastName = ObjectProperty(None)
    email = ObjectProperty(None)

    def button(self):
        print("Name: ", self.name.text, " \nLast Name: ", self.lastName.text, " \nEmail: ", self.email.text)
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyLidl()

if __name__ == "__main__":
    MyApp().run()