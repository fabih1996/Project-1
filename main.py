from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Interface(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.label = Label(text='Im a label!', pos_hint={'center_x': 0.5, 'center_y': 0.8}, size_hint=(0.5, 0.1))
        self.add_widget(self.label)

        self.button = Button(text='Cliccami', pos_hint={'center_x': 0.5, 'center_y': 0.1}, size_hint=(0.5, 0.1))
        self.button.bind(on_press=self.change_label,on_release=self.release_label)
        self.add_widget(self.button)

        self.my_text = TextInput(pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(0.5, 0.1))
        self.add_widget(self.my_text)

    def change_label(self, instance):
        self.button.text='Ahia'
    def release_label(self, instance):
        self.button.text='Cliccami'

class MyApp(App):
    def build(self):
        return Interface()
    
if __name__ == '__main__':
    MyApp().run()