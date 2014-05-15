'''
Application from a .kv
======================

The root application is created from the corresponding .kv. Check the test.kv
file to see what will be the root widget.
'''

import kivy
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, StringProperty
from kivy.app import App

kivy.require('1.0.7')


class ColorView(ModalView):

    bcolour = ListProperty([0.5,0.5,0.5,1])
    answer_text = StringProperty('')

class MainView(BoxLayout):

    def show_answer(self,inputColor,answer_text='',stealth=False):
        myColorView = ColorView(bcolour=inputColor, answer_text=answer_text)
        myColorView.open()
        if stealth==True:
            #hide the answer underneath a grey colorView-popup
            myColorView = ColorView(bcolour=[0.6,0.6,0.6,1], answer_text="tap to show the answer")
            myColorView.open()

class CrFeedbackApp(App):

    def build(self):
        return MainView()

if __name__ == '__main__':
    CrFeedbackApp().run()