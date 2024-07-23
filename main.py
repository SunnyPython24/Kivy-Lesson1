from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class InterFace(FloatLayout):


    def showme(self):
        print("test")

class MyformApp(App):
    pass
    #def showme(self):
        #print("test")

MyformApp().run()
