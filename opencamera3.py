from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.core.image import Image
from functools import partial
from kivy.logger import Logger
import logging

from classify_object import Classifier

Logger.setLevel(logging.TRACE)

trainImgPaths = "/pyimagesearch/dataset/images"
maskImgPaths = None

class TestCameraBox(BoxLayout):

    def classify(self, event):
        self.classifier.classify(None)
        print("Classify")

    def capture(self, event):
        if (self.camera.play):
            self.camera.play = False
            img = Image(self.camera.texture)
            img.save("capture.png")
            self.captureButton.text="Take another"
            self.classifyButton.disabled=False

        else:
            self.camera.play = True
            self.captureButton.text="Capture"
            self.classifyButton.disabled = True
            
        
    def __init__(self, **kwargs):
        super(TestCameraBox, self).__init__(**kwargs)
        #Create the classifier and train the model.
        self.classifier = Classifier(trainImgPaths, maskImgPaths)
        self.classifier.train()
        #Start the camera
        self.camera = Camera(resolution=(640, 480))
        self.camera.play = True;

        #Define buttons and bind to handlers
        self.captureButton = Button(text="Capture")
        self.captureButton.bind(on_press=self.capture)
        self.captureButton.size_hint_y = None
        self.captureButton.height='48dp'
        self.classifyButton = Button(text="Classify")
        self.classifyButton.bind(on_press=self.classify)
        self.classifyButton.size_hint_y = None
        self.classifyButton.height='48dp'
        self.classifyButton.disabled=True

        #Add widgets to layouts
        self.orientation='vertical'
        self.buttonLayout = BoxLayout(orientation='horizontal')        
        self.buttonLayout.add_widget(self.captureButton)
        self.buttonLayout.add_widget(self.classifyButton)
        self.add_widget(self.camera)
        self.add_widget(self.buttonLayout)
        

class TestCameraApp(App):
    def build(self):
        return TestCameraBox()
    
if __name__ == "__main__":
    TestCameraApp().run()
