
from vpython import *
from time import *
import random


from CardFileNames import *

class Card:
    def __init__(self, cardFileName, x, y, playerNumber, backShown):
        self.fileName = cardFileName
        self.BackShowing = backShown
        invisibleJoker = True

        if(cardFileName == 'CardTextures/black_joker.png' or cardFileName == 'CardTextures/red_joker.png'):
            invisibleJoker = False 

        if playerNumber==1:
            if self.BackShowing == 1:
                self.face = box(texture=back, pos=vector(x,y,1.1), length=2.5, height=3.5, width=.01, visible = invisibleJoker)
            else: 
                self.face = box(texture=self.fileName, pos=vector(x,y,1.1), length=2.5, height=3.5, width=.01, visible = invisibleJoker)
        elif playerNumber == 2:
            if self.BackShowing == 1:
                self.face = box(texture={'file':back, 'turn':2}, pos=vector(x,y,1.1), length=2.5, height=3.5, width=.01, visible = invisibleJoker)
            else:
                self.face = box(texture={'file':self.fileName, 'turn':2}, pos=vector(x,y,1.1), length=2.5, height=3.5, width=.01, visible = invisibleJoker)                
        elif playerNumber == 3:
            if self.BackShowing == 1:
                self.face = box(texture={'file':back, 'turn':1}, pos=vector(x,y,1.1), length=3.5, height=2.5, width=.01, visible = invisibleJoker)
            else:
                self.face = box(texture={'file':self.fileName, 'turn':1}, pos=vector(x,y,1.1), length=3.5, height=2.5, width=.01, visible = invisibleJoker)                
        elif playerNumber == 4:
            if self.BackShowing == 1:
                self.face = box(texture={'file':back, 'turn':3}, pos=vector(x,y,1.1), length=3.5, height=2.5, width=.01, visible = invisibleJoker)
            else:
                self.face = box(texture={'file':self.fileName, 'turn':3}, pos=vector(x,y,1.1), length=3.5, height=2.5, width=.01, visible = invisibleJoker)

    def Position(self, x, y):
        self.xPos = x
        self.yPos = y
        self.face.pos = vec(x, y, 1.1)

    def GetFileName(self):
        return self.fileName
              
    def FlipCard(self):

        while self.face.pos.z < 4: 
            rate(60)
            self.face.pos.z = self.face.pos.z + ((4-1.1)/15)

        spin = pi/10
        spinCount = 0

        while spinCount < 10:
            rate(60)

            if self.face.pos.y >= 10.25:
                self.face.rotate(axis=vec(0, 1, 0), angle=spin)
                spinCount = spinCount + 1
                if spinCount==5:
                    if self.BackShowing == 0:
                        self.face.texture = back
                        self.BackShowing = 1 
                    else:
                        self.face.texture=self.fileName
                        self.BackShowing = 0 

            else:
                self.face.rotate(axis=vec(1, 0, 0), angle=spin)
                spinCount = spinCount + 1
                if spinCount==5:
                    if self.BackShowing == 0:
                        if self.face.pos.x > 10.5:
                            self.face.texture = {'file':back, 'turn':3}
                        else:
                            self.face.texture = {'file':back, 'turn':1}
                        self.BackShowing = 1 
                    else:
                        if self.face.pos.x > 10.5:
                            self.face.texture = {'file':self.fileName, 'turn':3}
                        else:
                            self.face.texture = {'file':self.fileName, 'turn':1}
                        self.BackShowing = 0 

        while self.face.pos.z > 1.1: 
            rate(60)
            self.face.pos.z = self.face.pos.z - ((4-1.1)/15)


        

class Game:
    def __init__(self):
        self.players=int(0)
        self.suit='None'
        self.Player1 = Player(1)
        self.Player2 = Player(2)
        self.Player3 = Player(3)
        self.Player4 = Player(4)

    def SetPlayers(self, evt):
        if scene.mouse.pos._x > -0.85 and scene.mouse.pos._x < 0.85:
            if scene.mouse.pos._y > -5.4 and scene.mouse.pos._y < -4.5:
                self.players = int(2)
            elif scene.mouse.pos._y > -6.6 and scene.mouse.pos._y < -5.7:
                self.players = int(3)
            elif scene.mouse.pos._y > -7.8 and scene.mouse.pos._y < -6.9:
                self.players = int(4)

    def SetScene(self):
        scene.width = 1200
        scene.height = 850
        scene.userzoom = False
        scene.userspin = False
        scene.autoscale = False

    def SetCardPositions(self, player):
        partySide = 2.9
        partyFront = 6

        numberFront = 10.25
        numberBack = 14.25
        numberSide = 2.9

        if player == self.Player1:
                self.Player1.cardPositionsX.append(0)   # joker
                self.Player1.cardPositionsY.append(0)
                self.Player1.cardPositionsX.append(numberSide*-2)   # ace
                self.Player1.cardPositionsY.append(-numberFront)
                self.Player1.cardPositionsX.append(numberSide*-1)   # 2
                self.Player1.cardPositionsY.append(-numberFront)
                self.Player1.cardPositionsX.append(0)   # 3
                self.Player1.cardPositionsY.append(-numberFront)
                self.Player1.cardPositionsX.append(numberSide)   # 4
                self.Player1.cardPositionsY.append(-numberFront)
                self.Player1.cardPositionsX.append(numberSide*2)   # 5
                self.Player1.cardPositionsY.append(-numberFront)
                self.Player1.cardPositionsX.append(numberSide*-2)   # 6
                self.Player1.cardPositionsY.append(-numberBack)
                self.Player1.cardPositionsX.append(numberSide*-1)   # 7
                self.Player1.cardPositionsY.append(-numberBack)
                self.Player1.cardPositionsX.append(0)   # 8
                self.Player1.cardPositionsY.append(-numberBack)
                self.Player1.cardPositionsX.append(numberSide)   # 9
                self.Player1.cardPositionsY.append(-numberBack)
                self.Player1.cardPositionsX.append(numberSide*2)   # 10
                self.Player1.cardPositionsY.append(-numberBack)
                self.Player1.cardPositionsX.append(-partySide)   # jack
                self.Player1.cardPositionsY.append(-partyFront)
                self.Player1.cardPositionsX.append(0)   # queen
                self.Player1.cardPositionsY.append(-partyFront)
                self.Player1.cardPositionsX.append(partySide)   # king
                self.Player1.cardPositionsY.append(-partyFront)
                
        elif player == self.Player2:
                self.Player2.cardPositionsX.append(0)   # joker
                self.Player2.cardPositionsY.append(0)
                self.Player2.cardPositionsX.append(numberSide*2)   # ace
                self.Player2.cardPositionsY.append(numberFront)
                self.Player2.cardPositionsX.append(numberSide)   # 2
                self.Player2.cardPositionsY.append(numberFront)
                self.Player2.cardPositionsX.append(0)   # 3
                self.Player2.cardPositionsY.append(numberFront)
                self.Player2.cardPositionsX.append(numberSide*-1)   # 4
                self.Player2.cardPositionsY.append(numberFront)
                self.Player2.cardPositionsX.append(numberSide*-2)   # 5
                self.Player2.cardPositionsY.append(numberFront)
                self.Player2.cardPositionsX.append(numberSide*2)   # 6
                self.Player2.cardPositionsY.append(numberBack)
                self.Player2.cardPositionsX.append(numberSide)   # 7
                self.Player2.cardPositionsY.append(numberBack)
                self.Player2.cardPositionsX.append(0)   # 8
                self.Player2.cardPositionsY.append(numberBack)
                self.Player2.cardPositionsX.append(numberSide*-1)   # 9
                self.Player2.cardPositionsY.append(numberBack)
                self.Player2.cardPositionsX.append(numberSide*-2)   # 10
                self.Player2.cardPositionsY.append(numberBack)
                self.Player2.cardPositionsX.append(-partySide)   # jack
                self.Player2.cardPositionsY.append(partyFront)
                self.Player2.cardPositionsX.append(0)   # queen
                self.Player2.cardPositionsY.append(partyFront)
                self.Player2.cardPositionsX.append(partySide)   # king
                self.Player2.cardPositionsY.append(partyFront)

        elif player == self.Player3:
                self.Player3.cardPositionsX.append(0)   # joker
                self.Player3.cardPositionsY.append(0)
                self.Player3.cardPositionsX.append(numberFront)   # ace
                self.Player3.cardPositionsY.append(numberSide*-2)
                self.Player3.cardPositionsX.append(numberFront)   # 2
                self.Player3.cardPositionsY.append(numberSide*-1)
                self.Player3.cardPositionsX.append(numberFront)   # 3
                self.Player3.cardPositionsY.append(0)
                self.Player3.cardPositionsX.append(numberFront)   # 4
                self.Player3.cardPositionsY.append(numberSide*1)
                self.Player3.cardPositionsX.append(numberFront)   # 5
                self.Player3.cardPositionsY.append(numberSide*2)
                self.Player3.cardPositionsX.append(numberBack)   # 6
                self.Player3.cardPositionsY.append(numberSide*-2)
                self.Player3.cardPositionsX.append(numberBack)   # 7
                self.Player3.cardPositionsY.append(numberSide*-1)
                self.Player3.cardPositionsX.append(numberBack)   # 8
                self.Player3.cardPositionsY.append(0)
                self.Player3.cardPositionsX.append(numberBack)   # 9
                self.Player3.cardPositionsY.append(numberSide*1)
                self.Player3.cardPositionsX.append(numberBack)   # 10
                self.Player3.cardPositionsY.append(numberSide*2)
                self.Player3.cardPositionsX.append(partyFront)   # jack
                self.Player3.cardPositionsY.append(-partySide)
                self.Player3.cardPositionsX.append(partyFront)   # queen
                self.Player3.cardPositionsY.append(0)
                self.Player3.cardPositionsX.append(partyFront)   # king
                self.Player3.cardPositionsY.append(partySide)

        elif player == self.Player4:
                self.Player4.cardPositionsX.append(0)   # joker
                self.Player4.cardPositionsY.append(0)
                self.Player4.cardPositionsX.append(-numberFront)   # ace
                self.Player4.cardPositionsY.append(numberSide*2)
                self.Player4.cardPositionsX.append(-numberFront)   # 2
                self.Player4.cardPositionsY.append(numberSide)
                self.Player4.cardPositionsX.append(-numberFront)   # 3
                self.Player4.cardPositionsY.append(0)
                self.Player4.cardPositionsX.append(-numberFront)   # 4
                self.Player4.cardPositionsY.append(numberSide*-1)
                self.Player4.cardPositionsX.append(-numberFront)   # 5
                self.Player4.cardPositionsY.append(numberSide*-2)
                self.Player4.cardPositionsX.append(-numberBack)   # 6
                self.Player4.cardPositionsY.append(numberSide*2)
                self.Player4.cardPositionsX.append(-numberBack)   # 7
                self.Player4.cardPositionsY.append(numberSide)
                self.Player4.cardPositionsX.append(-numberBack)   # 8
                self.Player4.cardPositionsY.append(0)
                self.Player4.cardPositionsX.append(-numberBack)   # 9
                self.Player4.cardPositionsY.append(numberSide*-1)
                self.Player4.cardPositionsX.append(-numberBack)   # 10
                self.Player4.cardPositionsY.append(numberSide*-2)
                self.Player4.cardPositionsX.append(-partyFront)   # jack
                self.Player4.cardPositionsY.append(-partySide)
                self.Player4.cardPositionsX.append(-partyFront)   # queen
                self.Player4.cardPositionsY.append(0)
                self.Player4.cardPositionsX.append(-partyFront)   # king
                self.Player4.cardPositionsY.append(partySide)

    def SetTable(self):

        suitedTitle = label(pos=vec(0, 7, 0), text='SUITED', space=30, height=100, border=None, font='sans', line=False, box= False)

        suitedLogo = box(texture = back, pos=vector(0,.6,10), length=2.5, height=3.5, width=0.01)

        optionsLabel = label(pos=vec(0, -3, 3), text='How many opponents do you want? ', space=30, height=26, border=None, font='sans', line=False, box= False)

        option1 = label(pos=vec(0, -4, 3), text='   1   ', space=30, height=26, border=5, font='sans', line=False)

        option2 = label(pos=vec(0, -5, 3), text='   2   ', space=30, height=26, border=5, font='sans', line=False)

        option3 = label(pos=vec(0, -6, 3), text='   3   ', space=30, height=26, border=5, font='sans', line=False)

        option4 = label(pos=vec(0, -7, 3), text='   4   ', space=30, height=26, border=5, font='sans', line=False, visible=False)

        scene.bind('click', self.SetPlayers)

        while self.players==0:
            pass      

        scene.unbind('click', self.SetPlayers)
            
        optionsLabel.visible = False

        option1.visible = False

        option2.visible = False

        option3.visible = False


        self.SetCardPositions(self.Player1)
        self.SetCardPositions(self.Player2)

        if(self.players>2):
            self.SetCardPositions(self.Player3)
        if(self.players>3):
            self.SetCardPositions(self.Player4)

        optionsLabel.text = 'What suit do you want to play?'

        option1.text = '   Clubs    '

        option2.text = 'Diamonds'

        option3.text = '   Hearts   '

        option4.text = '  Spades  '

        optionsLabel.visible = True

        option1.visible = True

        option2.visible = True

        option3.visible = True

        option4.visible = True

        scene.bind('click', self.Player1.SetSuit)

        while self.Player1.suit == 'None':
            pass

        scene.unbind('click', self.Player1.SetSuit)

        suitedLogo.visible = False

        suitedTitle.visible = False

        optionsLabel.visible = False

        option1.visible = False

        option2.visible = False

        option3.visible = False

        option4.visible = False

        scene.width = 1600

        scene.background = vector(1,1,1)

        scene.camera.pos = vector(14,0,13.5)

        table = box(texture=textures.wood, length= 33, height = 33, width = 2)

        self.Player1.SetCards()

        suitList = ["Clubs", "Diamonds", "Hearts", "Spades"]

        suitList.remove(self.Player1.suit)

        self.Player2.suit = random.choice(suitList)

        self.Player2.SetCards()

        if self.players > 2:
            suitList.remove(self.Player2.suit)
            self.Player3.suit = random.choice(suitList)
            self.Player3.SetCards()

        if self.players > 3:
            suitList.remove(self.Player3.suit)
            self.Player4.suit = suitList[0]
            self.Player4.SetCards()


    def PickCard(self):
        
        clickPos = scene.mouse.pick.pos

        if(scene.mouse.pos.y > 5):
            for card in self.Player2.Hand:
                if clickPos == card.face.pos:
                    card.FlipCard()
                    self.Player1.turn = 1
                    break   

        elif self.players > 2 and scene.mouse.pos.x > 10.5:
            for card in self.Player3.Hand:
                if clickPos == card.face.pos:
                    card.FlipCard()
                    self.Player1.turn = 1
                    break   

        elif self.players > 3 and scene.mouse.pos.x < 0.5:
            for card in self.Player4.Hand:
                if clickPos == card.face.pos:
                    card.FlipCard()
                    self.Player1.turn = 1
                    break   





    def FirstTurn(self):

        scene.userspin = True
        scene.userzoom = True


        self.PickCardLabel = label(pos=vec(-0.5, 0, 0), text='Click on \n a opponent\'s \n flipped card', 
                                   space=30, height=25, border=None, font='sans', line=False, box= False)

        scene.bind('click', self.PickCard)

        while True:
#            print(scene.mouse.pick.pos)
            pass

#        while self.Player1.turn == 0:
#           pass
        
        scene.unbind('click', self.PickCard)

        self.Player1.turn = 0



class Player:
    def __init__(self, playerNumber):
        self.suit = 'None'
        self.cardPositionsX = []    # Filled by the game class for each of the four players
        self.cardPositionsY = []    # Filled by the game class for each of the four players
        self.Hand = []
        self.Number = playerNumber
        self.turn = 0


    def SetSuit(self, evt):            
        if scene.mouse.pos._x > -1.6 and scene.mouse.pos._x < 1.6:
            if scene.mouse.pos._y > -5.4 and scene.mouse.pos._y < -4.5:
                self.suit = 'Clubs'
            elif scene.mouse.pos._y > -6.6 and scene.mouse.pos._y < -5.7:
                self.suit = 'Diamonds'
            elif scene.mouse.pos._y > -7.8 and scene.mouse.pos._y < -6.9:
                self.suit = 'Hearts'
            elif scene.mouse.pos._y > -9.0 and scene.mouse.pos._y < -8.1:
                self.suit = 'Spades'


    def SetCards(self):
        if(self.suit == 'Clubs'):
            self.joker = Card(clubs[0], self.cardPositionsX[0],  self.cardPositionsY[0], self.Number, 1)
            self.ace = Card(clubs[1], self.cardPositionsX[1],  self.cardPositionsY[1], self.Number, 1)
            self.two = Card(clubs[2], self.cardPositionsX[2],  self.cardPositionsY[2], self.Number, 1)
            self.three = Card(clubs[3], self.cardPositionsX[3],  self.cardPositionsY[3], self.Number, 1)
            self.four = Card(clubs[4], self.cardPositionsX[4],  self.cardPositionsY[4], self.Number, 1)
            self.five = Card(clubs[5], self.cardPositionsX[5],  self.cardPositionsY[5], self.Number, 1)
            self.six = Card(clubs[6], self.cardPositionsX[6],  self.cardPositionsY[6], self.Number, 1)
            self.seven = Card(clubs[7], self.cardPositionsX[7],  self.cardPositionsY[7], self.Number, 1)
            self.eight = Card(clubs[8], self.cardPositionsX[8],  self.cardPositionsY[8], self.Number, 1)
            self.nine = Card(clubs[9], self.cardPositionsX[9],  self.cardPositionsY[9], self.Number, 1)
            self.ten = Card(clubs[10], self.cardPositionsX[10],  self.cardPositionsY[10], self.Number, 1)
            self.jack = Card(clubs[11], self.cardPositionsX[11],  self.cardPositionsY[11], self.Number, 0)
            self.queen = Card(clubs[12], self.cardPositionsX[12],  self.cardPositionsY[12], self.Number, 0)
            self.king = Card(clubs[13], self.cardPositionsX[13],  self.cardPositionsY[13], self.Number, 0)

        elif(self.suit == 'Diamonds'):
            self.joker = Card(diamonds[0], self.cardPositionsX[0],  self.cardPositionsY[0], self.Number, 1)
            self.ace = Card(diamonds[1], self.cardPositionsX[1],  self.cardPositionsY[1], self.Number, 1)
            self.two = Card(diamonds[2], self.cardPositionsX[2],  self.cardPositionsY[2], self.Number, 1)
            self.three = Card(diamonds[3], self.cardPositionsX[3],  self.cardPositionsY[3], self.Number, 1)
            self.four = Card(diamonds[4], self.cardPositionsX[4],  self.cardPositionsY[4], self.Number, 1)
            self.five = Card(diamonds[5], self.cardPositionsX[5],  self.cardPositionsY[5], self.Number, 1)
            self.six = Card(diamonds[6], self.cardPositionsX[6],  self.cardPositionsY[6], self.Number, 1)
            self.seven = Card(diamonds[7], self.cardPositionsX[7],  self.cardPositionsY[7], self.Number, 1)
            self.eight = Card(diamonds[8], self.cardPositionsX[8],  self.cardPositionsY[8], self.Number, 1)
            self.nine = Card(diamonds[9], self.cardPositionsX[9],  self.cardPositionsY[9], self.Number, 1)
            self.ten = Card(diamonds[10], self.cardPositionsX[10],  self.cardPositionsY[10], self.Number, 1)
            self.jack = Card(diamonds[11], self.cardPositionsX[11],  self.cardPositionsY[11], self.Number, 0)
            self.queen = Card(diamonds[12], self.cardPositionsX[12],  self.cardPositionsY[12], self.Number, 0)
            self.king = Card(diamonds[13], self.cardPositionsX[13],  self.cardPositionsY[13], self.Number, 0)
            
        elif(self.suit == 'Hearts'):
            self.joker = Card(hearts[0], self.cardPositionsX[0],  self.cardPositionsY[0], self.Number, 1)
            self.ace = Card(hearts[1], self.cardPositionsX[1],  self.cardPositionsY[1], self.Number, 1)
            self.two = Card(hearts[2], self.cardPositionsX[2],  self.cardPositionsY[2], self.Number, 1)
            self.three = Card(hearts[3], self.cardPositionsX[3],  self.cardPositionsY[3], self.Number, 1)
            self.four = Card(hearts[4], self.cardPositionsX[4],  self.cardPositionsY[4], self.Number, 1)
            self.five = Card(hearts[5], self.cardPositionsX[5],  self.cardPositionsY[5], self.Number, 1)
            self.six = Card(hearts[6], self.cardPositionsX[6],  self.cardPositionsY[6], self.Number, 1)
            self.seven = Card(hearts[7], self.cardPositionsX[7],  self.cardPositionsY[7], self.Number, 1)
            self.eight = Card(hearts[8], self.cardPositionsX[8],  self.cardPositionsY[8], self.Number, 1)
            self.nine = Card(hearts[9], self.cardPositionsX[9],  self.cardPositionsY[9], self.Number, 1)
            self.ten = Card(hearts[10], self.cardPositionsX[10],  self.cardPositionsY[10], self.Number, 1)
            self.jack = Card(hearts[11], self.cardPositionsX[11],  self.cardPositionsY[11], self.Number, 0)
            self.queen = Card(hearts[12], self.cardPositionsX[12],  self.cardPositionsY[12], self.Number, 0)
            self.king = Card(hearts[13], self.cardPositionsX[13],  self.cardPositionsY[13], self.Number, 0)

        elif(self.suit == 'Spades'):
            self.joker = Card(spades[0], self.cardPositionsX[0],  self.cardPositionsY[0], self.Number, 1)
            self.ace = Card(spades[1], self.cardPositionsX[1],  self.cardPositionsY[1], self.Number, 1)
            self.two = Card(spades[2], self.cardPositionsX[2],  self.cardPositionsY[2], self.Number, 1)
            self.three = Card(spades[3], self.cardPositionsX[3],  self.cardPositionsY[3], self.Number, 1)
            self.four = Card(spades[4], self.cardPositionsX[4],  self.cardPositionsY[4], self.Number, 1)
            self.five = Card(spades[5], self.cardPositionsX[5],  self.cardPositionsY[5], self.Number, 1)
            self.six = Card(spades[6], self.cardPositionsX[6],  self.cardPositionsY[6], self.Number, 1)
            self.seven = Card(spades[7], self.cardPositionsX[7],  self.cardPositionsY[7], self.Number, 1)
            self.eight = Card(spades[8], self.cardPositionsX[8],  self.cardPositionsY[8], self.Number, 1)
            self.nine = Card(spades[9], self.cardPositionsX[9],  self.cardPositionsY[9], self.Number, 1)
            self.ten = Card(spades[10], self.cardPositionsX[10],  self.cardPositionsY[10], self.Number, 1)
            self.jack = Card(spades[11], self.cardPositionsX[11],  self.cardPositionsY[11], self.Number, 0)
            self.queen = Card(spades[12], self.cardPositionsX[12],  self.cardPositionsY[12], self.Number, 0)
            self.king = Card(spades[13], self.cardPositionsX[13],  self.cardPositionsY[13], self.Number, 0)

        self.Hand = [self.joker, self.ace, self.two, self.three, self.four, self.five, 
                     self.six, self.seven, self.eight, self.nine, self.ten, self.jack, 
                     self.queen, self.king]        
    

scene.lights=[]
scene.ambient = vector(1,1,1)

newGame = Game()

newGame.SetScene()

newGame.SetTable()

newGame.FirstTurn()

#scene.autoscale = True
#scene.forward = -100

# REMOVE    
#scene.userspin = True
#scene.userzoom = True


while True:
    pass

