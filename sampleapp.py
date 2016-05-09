import kivy

kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label

class SampleApp(App):
    def build(self):
        return Label(text="Sample Application")

if __name__ == '__main__':
    SampleApp().run()
