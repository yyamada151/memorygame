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
from kivy.clock import Clock

opened = [0,0]
score = [10]

numcards = 12
cleared = [0 for i in range(numcards+1)]


class Card(BoxLayout):

    rank = NumericProperty(0)
    state = 0
    display = StringProperty('-')

    def update(self):

        #Already taken
        if cleared[self.rank]==2:
            return
        #Two different cards currently opened
        elif opened[0]==2 and self.state==0:
            return
        #This card and another different-ranked card are opened
        elif opened[0]==2 and self.state==1:
            self.state = 0
            self.display = "-"
            opened[1] -= 1
            cleared[self.rank] -= 1
            #Both cards closed
            if opened[1]==0:
                opened[0]=0
        #This card is closed right now
        elif self.state==0:
            self.state = 1
            cleared[self.rank] += 1
            opened[0] += 1
            opened[1] += 1
            self.display = str(self.rank)
            if cleared[self.rank]==2:
                opened[0] = opened[1] = 0
            elif opened[0]==2:
                score[0] -= 1

        #This card is the only card opened
        else:
            return

class MemoryGame(BoxLayout):

    numcards = numcards
    scoredisp = NumericProperty(10)

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

    def updatescore(self,dt):
        self.scoredisp = score[0]


class MemoryGameApp(App):
    def build(self):
        game = MemoryGame()
        game.initialize()
        Clock.schedule_interval(game.updatescore,1.0/60.0)
        return game


if __name__ == '__main__':
    MemoryGameApp().run()
