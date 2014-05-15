'''
Application from a .kv
======================

The root application is created from the corresponding .kv. Check the test.kv
file to see what will be the root widget.
'''

import kivy
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.app import App

kivy.require('1.0.7')


class ColorView(ModalView):

    bcolour = ListProperty([0.5,0.5,0.5,0.5])

class MainView(BoxLayout):

    def showcolor(self,inputColor):
        myColorView = ColorView(bcolour=inputColor)
        myColorView.open()


class CrFeedbackApp(App):

    def build(self):
        return MainView()

if __name__ == '__main__':
    CrFeedbackApp().run()