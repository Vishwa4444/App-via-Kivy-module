import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def __init__(self,**kwargs):     #kwargs is used to add unlimited arguments
        super(childApp,self).__init__()
        self.cols = 2
        self.add_widget(Label(text='Student Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text='Student Marks'))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text='Student Gender'))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.press = Button(text='Click here')
        self.press.bind(on_press = self.click_here)
        self.add_widget(self.press)

    def click_here(self,instance):
        print("Name of student is :"+self.s_name.text)
        print("Marks of student is :"+self.s_marks.text)
        print("Gender of student is :"+self.s_gender.text)
        print("")


class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()

