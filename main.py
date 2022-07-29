from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty, OptionProperty
import os 
from copiar import calc


class Screen1(Screen):
    ...

class Chooser_Archive(Screen):
   text_input = ObjectProperty(None) 


class Chooser_Sieve(Screen):
    ...


class Start(ScreenManager):
    ...


class Med_to_Excel(App):
    archive = ObjectProperty(None)
    sieve = ObjectProperty(None)
    label_copy = StringProperty('')
    columnOrRow = None

    def load_archive(self, path, filename):
        self.archive =  open(os.path.join(path, filename[0]))


    def load_sieve(self, path, filename):
        self.sieve = open(os.path.join(path, filename[0]))


    def copy(self):
        self.label_copy = calc(self.archive, self.sieve, self.columnOrRow)
    
    def column_or_row(self, tb):
        self.columnOrRow = tb.state
    
    def clear_label(self):
        self.label_copy = ''


if __name__ == '__main__':
    Med_to_Excel().run()
