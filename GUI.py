from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.image import Image
from IPE_Box_Improved1 import IPE_box
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.factory import Factory 
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang import Builder

import os
import numpy as np

        # 1 2 3 4
        # 2 1 3 4
        # 3 3 1 2
        # 4 4 2 1
class ScreenManagement(ScreenManager):
    EW = StringProperty('')

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(True)

def matrix(txt):
    return [item.split() for item in txt.split('\n')]

class Root(Screen):
    draw = False
    hist = False
    loading = ObjectProperty(False)
    text_input = TextInput()
    InputMatrix = 0
    EW = 0

    def on_enter(self):
        text = self.text_input.text
        # print(text)
        mat = matrix(text) 
        mat = np.array(mat,dtype=float)
        # print(mat)
        Root.InputMatrix = mat

        

    def dismiss_popup(self):
        self._popup.dismiss()
        
            
    def on_checkbox_active(draw,hist):
        if draw:
            # print("The checkbox is active because value1={}".format(draw))
            Root.draw = draw
        if hist:
            # print("The checkbox is active because value2={}".format(hist))
            Root.hist = hist

    def load(self):
        draw = Root.draw
        hist = Root.hist
        m=6
        ScreenManagement.EW = str(IPE_box(Root.InputMatrix,m,True,True))
        
class ScreenTwo(Screen):
    EW = Root.EW

class ScreenThree(Screen):
    pass

        
    # def show_load(self):
    #     content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
    #     self._popup = Popup(title="Load file", content=content,
    #                         size_hint=(0.9, 0.9))
    #     self._popup.open()
        

      


class Editor(App):
    pass



if __name__ == '__main__':
    Editor().run()
    
