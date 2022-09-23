#-*- coding: utf-8 -*-

from kivy.app import App

from kivy.config import Config
Config.set("graphics", "height", 640)
Config.set("graphics", "width", 480)

from kivy.uix.widget import Widget

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

resource_add_path("C:\Windows\Fonts")
LabelBase.register(DEFAULT_FONT, "UDDIGIKYOKASHON-R.TTC")

from kivy.properties import StringProperty


class Calculator(Widget):
    
    text = StringProperty()

    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.text = "0"
        self.type = 0
        self.call = None


    def change_display(self, number):

        if self.text == "0":

            self.text = number

        elif self.type != 0:

            self.text = number

        else:

            self.text += number

    
    def point(self, number1):

        if "." in self.text:
            pass

        else:
            
            self.text += number1


    def press_number(self, a):
        
        self.change_display(a.text)


    def number_plus(self):

        self.type = 1

        self.call = float(self.ids.hyouji.text)

        self.text = "0"
        

    def number_minus(self):

        self.type = 2

        self.call = float(self.ids.hyouji.text)

        self.text = "0"


    def number_multiplication(self):

        self.type = 3

        self.call = float(self.ids.hyouji.text)

        self.text = "0"
        

    def number_division(self):

        self.type = 4

        self.call = float(self.ids.hyouji.text)

        self.text = "0"


    def number_equal(self):

        if self.type == 1:

            self.a = float(self.call) + float(self.text)

            self.text = str(self.a)

            self.call = None


        elif self.type == 2:

            self.a = float(self.call) - float(self.text)

            self.text = str(self.a)

            self.call = None
 

        elif self.type == 3:

            self.a = float(self.call) * float(self.text)

            self.text = str(self.a)

            self.call = None


        elif self.type == 4:

            self.a = float(self.call) / float(self.text)

            self.text = str(self.a)

            self.call = None



    def number_clear(self):

        self.text = "0"

        self.type = 0

        self.call = None



class DenntakuApp(App):

    def __init__(self, **kwargs):
        super(DenntakuApp, self).__init__(**kwargs)
        self.title = '電卓'


if __name__=="__main__":

    DenntakuApp().run()