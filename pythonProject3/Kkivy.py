import kivy
#kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwards):
        super(MyGrid, self).__init__(**kwards)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.sumbit = Button(text="Submit", font_size=40)
        self.sumbit.bind(on_press = self.pressed)
        self.add_widget(self.sumbit)

    def pressed(self, instance):
        #print("pressed")
        name = self.name.text
        lastName = self.lastName.text
        email = self.email.text

        print("Name: ", name, " \nLast Name: ", lastName, " \nEmail: ", email)
        
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        #return Label(text="Hello World")
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()