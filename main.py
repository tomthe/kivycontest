
import kivy
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, StringProperty
from kivy.app import App

kivy.require('1.0.7')


class ColorView(ModalView):
    bcolour = ListProperty([0.5,0.5,0.5,1])
    answer_text = StringProperty('')
    font_size = StringProperty('50dp')
    
    
class MainView(BoxLayout):

    def show_answer(self,inputColor,answer_text='',stealth=False,font_size='55dp'):
        myColorView = ColorView(bcolour=inputColor, answer_text=answer_text,font_size=font_size)
        myColorView.open()
        if stealth==True:
            #hide the answer underneath a grey colorView-popup
            myColorView = ColorView(bcolour=[0.6,0.6,0.6,1], answer_text='tap to show the answer',font_size='30dp')
            myColorView.open()

class CrFeedbackApp(App):

    def build(self):
        return MainView()

if __name__ == '__main__':
    CrFeedbackApp().run()