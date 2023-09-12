from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.chat_history = BoxLayout(orientation='vertical', size_hint_y=0.95, spacing=5)
        self.add_widget(self.chat_history)

        input_box = BoxLayout(orientation='horizontal', size_hint_y=0.05)
        input_box.pos_hint = {'bottom': 1}
        self.add_widget(input_box)

        self.text_input = TextInput(multiline=False)
        self.text_input.bind(on_text_validate=self.send_message)
        input_box.add_widget(self.text_input)

        self.send_button = Button(text='Send')
        self.send_button.bind(on_press=self.send_message)
        self.send_button.size_hint_x = 0.25
        input_box.add_widget(self.send_button)

    def send_message(self, *args):
        message = self.text_input.text
        # do something with the message, e.g. send it to a server or display it on the screen
        print(f'Sending message: {message}')
        message_label = Label(text=f'[Me]: {message}', halign='left', size_hint_y=None, height=20)
        self.chat_history.add_widget(message_label)
        self.text_input.text = ''

class MyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()
