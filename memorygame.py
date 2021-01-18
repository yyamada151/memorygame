from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from random import shuffle


arr = [1,2,3,4]

class Card(BoxLayout):

    rank = NumericProperty(0)
    state = 0
    display = StringProperty('-')

    def update(self):
        if self.state==0:
            self.state = 1
            self.display = str(self.rank)
        else:
            self.state = 0
            self.display = '-'


class MemoryGame(BoxLayout):

    numcards = 12

    card1 = ObjectProperty(None)
    card2 = ObjectProperty(None)
    card3 = ObjectProperty(None)
    card4 = ObjectProperty(None)
    card5 = ObjectProperty(None)
    card6 = ObjectProperty(None)
    card7 = ObjectProperty(None)
    card8 = ObjectProperty(None)
    card9 = ObjectProperty(None)
    card10 = ObjectProperty(None)
    card11 = ObjectProperty(None)
    card12 = ObjectProperty(None)



    def initialize(self):
        arr = [(i+2)//2 for i in range(self.numcards)]
        shuffle(arr)
        self.card1.rank = arr[0]
        self.card2.rank = arr[1]
        self.card3.rank = arr[2]
        self.card4.rank = arr[3]
        self.card5.rank = arr[4]
        self.card6.rank = arr[5]
        self.card7.rank = arr[6]
        self.card8.rank = arr[7]
        self.card9.rank = arr[8]
        self.card10.rank = arr[9]
        self.card11.rank = arr[10]
        self.card12.rank = arr[11]

    #card4.rank = 1


class MemoryGameApp(App):
    def build(self):
        game = MemoryGame()
        game.initialize()
        return game


if __name__ == '__main__':
    MemoryGameApp().run()
