import kivy

kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.graphics.texture import Texture
import kivy.core.image

tex = None
img = None
kv = '''
BoxLayout:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Capture'
        on_press: tex = camera.texture; img = Image(tex); img.save('last_photo.png')
        size_hint_y: None
        height: '48dp'
'''

class TestCamera(App):
    def build(self):
        return Builder.load_string(kv)

TestCamera().run()
