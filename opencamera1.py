from kivy.app import App
from kivy.core.camera import Camera
from kivy.graphics import *
from kivy.core.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class TestApp(App):
    
    def build(self):
        print("Building self")

        self.camera = Camera(resolution=(640,480))
        self.camera.play=True
        self.camera.bind(on_texture=self.reloadTexture)

        self.tex = self.camera.texture

        self.canvas = RenderContext()
        self.canvas.add(Rectangle(texure=self.tex))

        self.captureButton = Button(text='Capture')
        self.captureButton.bind(on_press=self.capture)
        self.captureButton.height='48dp'

        layout = BoxLayout(orientation='vertical')
        #layout.add_widget(self.canvas)
        layout.add_widget(self.captureButton)
        
        return layout

    def reloadTexture(self, *largs):
        self.tex = self.camera.texture
        self.canvas.ask_update()

    def capture(self, event):
        print("catpured")
        self.tex = self.camera.texture
        img = Image(texture=self.tex)
        img.save("capture.png")

TestApp().run()
