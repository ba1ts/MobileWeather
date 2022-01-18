from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

class SpinnerApp(App):
    def build(self):
        fl = FloatLayout()
        self.spinner = Spinner(text='Города', values =('Челябинск','Москва','Санкт-Петербург','Якутск'), size_hint = (0.3,0.2),pos_hint={'center_x': 0.5,'center_y':0.5})
        self.label = Label(text='Температура',size_hint=(0.3,0.2),pos_hint={'center_x': 0.5,'center_y': 0.8})
        self.labels = Label(text='Скорость ветра', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.9})
        self.textinput = TextInput(size_hint=(0.3, 0.2),pos_hint={'center_x': 0.5, 'center_y': 0.2})
        self.btn = Button(text='Поиск', on_press = self.click,size_hint=(0.2, 0.1),pos_hint={'center_x': 0.5, 'center_y': 0.05})
        self.spinner.bind(text=self.on_selected_spinner)
        fl.add_widget(self.spinner)
        fl.add_widget(self.label)
        fl.add_widget(self.labels)
        fl.add_widget(self.textinput)
        fl.add_widget(self.btn)
        self.owm = OWM('71579b940908f2fe19ab16742ab07157')
        self.mgr = self.owm.weather_manager()
        return fl

    def click(self, spinner):
        town = self.textinput.text
        try:
            observation = self.mgr.weather_at_place(town)
            w = observation.weather
            temp = w.temperature('celsius')["temp"]
            if int(temp) <= -25:
                self.label.text = 'Температура: ' + (str(round(temp)) + ' 🥶')
            if int(temp) >= 25:
                self.label.text = 'Температура: ' + (str(round(temp)) + ' 🥵')
            if int(temp) < 25 and int(temp) > -25:
                self.label.text = 'Температура: ' + (str(round(temp)) + ' 🙂')
            veter = w.wind()["speed"]
            if int(veter) >= 0 and int(veter) <= 3.99999999999:
                self.labels.text = (str(veter) + 'м/с ࿓')
            if int(veter) >= 4 and int(veter) <= 6:
                self.labels.text = (str(veter) + 'м/с ༄')
            if int(veter) >= 6.0000000000001:
                self.labels.text = (str(veter) + 'м/с 💨')
        except:
            self.labels.text = 'Error!'
            self.label.text = 'Error!'
        self.textinput.text = ''


    def on_selected_spinner(self, spinner, text):
        self.label.text = text
        town = text
        observation = self.mgr.weather_at_place(town)
        w = observation.weather
        temp = w.temperature('celsius')["temp"]
        if int(temp) <= -25:
            self.label.text = 'Температура: ' + (str(round(temp)) + ' 🥶')
        if int(temp) >= 25:
            self.label.text = 'Температура: ' + (str(round(temp)) + ' 🥵')
        if int(temp) < 25 and int(temp) > -25:
            self.label.text = 'Температура: ' + (str(round(temp)) + ' 🙂')
        veter = w.wind()["speed"]
        if int(veter) >= 0 and int(veter) <= 3.99999999999:
            self.labels.text = (str(veter) + 'м/с ࿓')
        if int(veter) >= 4 and int(veter) <= 6:
            self.labels.text = (str(veter) + 'м/с ༄')
        if int(veter) >= 6.0000000000001:
            self.labels.text = (str(veter) + 'м/с 💨')
if __name__ == "__main__":
    SpinnerApp().run()
