from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from chat import ChatScreen
from kivy.graphics import RoundedRectangle
from kivy.graphics import Color

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)  # make the background transparent
        self.bind(size=self._update_rect, pos=self._update_rect)
        self.radius = 20  # set the corner radius

    def _update_rect(self, instance, value):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.3, 0.3, 0.3, 1)  # set the background color
            RoundedRectangle(pos=self.pos, size=self.size, radius=[self.radius])

class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        ip_box = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.add_widget(ip_box)

        ip_label = Label(text='IP Address:', size_hint=(0.3, 1))
        ip_box.add_widget(ip_label)

        self.ip_input = TextInput(multiline=False, size_hint=(0.7, 1))
        ip_box.add_widget(self.ip_input)

        port_box = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.add_widget(port_box)

        port_label = Label(text='Port:', size_hint=(0.3, 1))
        port_box.add_widget(port_label)

        self.port_input = TextInput(multiline=False, size_hint=(0.7, 1))
        port_box.add_widget(self.port_input)

        connect_box = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        self.add_widget(connect_box)

        connect_box.add_widget(Label(size_hint=(0.3, 1)))  # add a spacer widget

        self.connect_button = RoundedButton(text='Connect', size_hint=(0.4, 1), pos_hint={'center_x': 0.5})
        self.connect_button.bind(on_press=self.connect_to_chat)
        connect_box.add_widget(self.connect_button)

        connect_box.add_widget(Label(size_hint=(0.3, 1)))  # add another spacer widget
    def connect_to_chat(self, *args):
        ip_address = self.ip_input.text
        port = self.port_input.text
        # do something with the ip_address and port, e.g. connect to a chat server
        print(f'Connecting to chat server: {ip_address}:{port}')
        chat_screen = ChatScreen()
        chat_screen.ip_address = ip_address
        chat_screen.port = port
        self.parent.add_widget(chat_screen)
        self.parent.remove_widget(self)

class MyApp(App):
    def build(self):
        return HomeScreen()

if __name__ == '__main__':
    MyApp().run()
