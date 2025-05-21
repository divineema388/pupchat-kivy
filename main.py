from kivy.app import App
from kivy.uix.label import Label

class PupchatApp(App):
    def build(self):
        return Label(text='Welcome to Pupchat!', font_size=40)

if __name__ == '__main__':
    PupchatApp().run()