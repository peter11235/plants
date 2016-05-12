import kivy

kivy.require('1.9.1')

from kivy.app import App
from kivy.app import runTouchApp
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.core.camera import CameraBase
from kivy.core.image import Image

kv = '''
TestCameraRoot:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: True
    Button:
        text:'Capture'
        on_press: print("AHH")
        size_hint_y: None
        height: '48dp'
'''

class TestCameraRoot(BoxLayout):
    def saveImg(tex, event):
        img = Image(tex)
        #img.save("capture.png")
        print("Would have captured")

class TestCameraApp(App):
    def build(self):
        return Builder.load_string(kv)
    
TestCameraApp().run()
