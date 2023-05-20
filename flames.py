import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase
from kivy.properties import StringProperty
from kivy.animation import Animation
LabelBase.register(name="pacifico",fn_regular="Pacifico.ttf")
LabelBase.register(name="tusj",fn_regular="FFF_Tusj.ttf")

class RoundedTextInput(TextInput):
    pass

class console(BoxLayout):
    name1 = StringProperty('')
    name2 = StringProperty('')
    value=0
    result=StringProperty("")
    def flames(self):
        if(self.name1==self.name2):
            self.result="Enter two [color=#FF0000]DIFFERENT[/color] names"
        elif(self.name1 and self.name2==''):
            self.result="Enter any [color=#FF0000]NAMES[/color]"
        else:
            fname1=list(max(self.name1,self.name2))
            fname2=list(min(self.name1,self.name2))
            for i in fname1:
                if i in fname2:
                    fname1.remove(i)
                    fname2.remove(i)
            print(fname1,fname2)
            self.value=len(fname1)+len(fname2)
            flames=["f","l","a","m","e","s"]
            while len(flames)!=1:
                if self.value>len(flames):
                    index = (self.value) % len(flames)
                    del flames[index]
                else:
                    if len(flames)<self.value:
                        del flames[self.value]
                    else:
                        self.value=self.value%len(flames)
                        del flames[self.value]
            flames1 = flames[0] 
            if flames1 == 'f':
                self.result = f"[color=#FF0000]{self.name1}[/color] and [color=#FF0000]{self.name2}[/color] are good [color=#FF0000]FRIENDS[/color]"
            elif flames1 == 'l':
                self.result = f"[color=#FF0000]{self.name1}[/color] and [color=#FF0000]{self.name2}[/color] are [color=#FF0000]LOVERS[/color]"
            elif flames1 == 'a':
                self.result = f"[color=#FF0000]{self.name1}[/color] and [color=#FF0000]{self.name2}[/color] are [color=#FF0000]AFFECTIONATE people[/color]"
            elif flames1 == 'm':
                self.result = f"[color=#FF0000]{self.name1}[/color] and [color=#FF0000]{self.name2}[/color] are [color=#FF0000]MARRIED[/color]"
            elif flames1 == 'e':
                self.result = f"[color=#FF0000]{self.name1} and [color=#FF0000]{self.name2}[/color] are [color=#FF0000]ENEMIES[/color]"
            elif flames1 == 's':
                self.result = f"[color=#FF0000]{self.name1}[/color] and [color=#FF0000]{self.name2}[/color] are [color=#FF0000]SISTERS[/color]"
            else:
                self.result = ''
    def button_press(self):
        self.name1 = self.ids.first_name.text
        self.name2 = self.ids.second_name.text
        print(self.name1, self.name2)
        print(self.result)
    
        

class flames(App):
    def build(self):
        return console()
    def animateme(self,Label):
        anim=Animation(opacity=0,duration=3)
        anim.start(self)
if __name__ == '__main__':
    flames().run()
