import kivy

kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.core.camera import Camera
from kivy.core.image import Image

kv = '''
<TestCameraApp>:
    BoxLayout:
        orientation: 'vertical'
        Camera:
            id: camera
            resolution: (640, 480)
            play: True
        Button:
            text: 'Capture'
            on_press: app.saveImg(self)    
            size_hint_y: None
            height: '48dp'
'''

class TestCameraApp(App):
    def build(self):
        return Builder.load_string(kv)

    def saveImg(self):
        img = Image(self.camera.texture)
        img.save("capture.png")


if __name__ == '__main__':
    TestCameraApp().run()
