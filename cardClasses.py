import random
class Card(object):
    '''Card stores both the card's value and face (a string or Boolean variable to indicate whether the card is facing up or down). '''
    def __init__(self, value, face):
        self._value = value
        self._face = face
    def getValue(self):
        return self._value
    def getFace(self):
        return self._face
    def changeFace(self, face1):
        self._face = face1


class Deck(object):
    '''Deck contains the cards needed for the game.'''
    def __init__(self, list_max):
        #Game.__init__(self, rows, columns)
        self._cards = []
        self._list_max = list_max
        for j in range(2):
            for i in range(self._list_max):
                self._cards.append(Card(i+1,False))
    def deal(self):
        if len(self) == 0:
            return None
        else:
            return self._cards.pop(0)
    def shuffle(self):
        random.shuffle(self._cards)
    def __len__(self):
        '''a method that returns number of cards left in the deck'''
        return len(self._cards)


class Game(Deck):
    '''an extension of Deck class'''
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._2dList = [None] * rows
        for i in range(self._rows):
            self._2dList[i] = [0] * self._columns
        maxnumbers = int((self._columns * self._rows)/2)
        Deck.__init__(self, maxnumbers)
    '''Game simulates playing a single game and represents the interaction between the user and the other classes.'''
    def play(self):
        '''interact with user and other classes'''
        self.populatedBoard()
        self.displayBoard()
        while self.isGameOver() == False:
            firstCard = input("Enter coordinates for first card ")
            secondCard = input("Enter coordinates for second card ")
            if firstCard == secondCard:
                print("Choose different coordinates for each of them")
                continue
            firstCard_list = list(map(int, firstCard.split(" ")))
            secondCard_list = list(map(int, secondCard.split(" ")))
            firstCard_value = self._2dList[firstCard_list[0]-1][firstCard_list[1]-1]
            secondCard_value = self._2dList[secondCard_list[0]-1][secondCard_list[1]-1]
            if firstCard_value.getValue() == secondCard_value.getValue():
                #change the face to be true and then display
                self._2dList[firstCard_list[0]-1][firstCard_list[1]-1].changeFace(True)
                self._2dList[secondCard_list[0]-1][secondCard_list[1]-1].changeFace(True)
                self.displayBoard()
            else:
                print("Not an identical pair. Found " + str(firstCard_value.getValue()) +  " at [ " + str(firstCard_list[0]) + " , " + str(firstCard_list[1]) + " ] and " + str(secondCard_value.getValue()) +" at [ " + str(secondCard_list[0]) + " , " + str(secondCard_list[1]) + " ]")

    def isGameOver(self):
        '''check if the game is over'''
        trueorFalse = True
        for i in range(self._rows):
            for j in range(self._columns):
                if self._2dList[i][j].getFace() == False:
                    trueorFalse =  False
        return trueorFalse

    def displayBoard(self):
        '''display the numbers or * '''
        displayList = [None] * self._rows
        for i in range(self._rows):
            displayList[i] = [0] * self._columns

        for i in range(self._rows):
            for j in range(self._columns):
                if self._2dList[i][j].getFace():
                    displayList[i][j] = self._2dList[i][j].getValue()
                else:
                    displayList[i][j] = "*"
        for i in range(self._rows):
            wordtopr = ""
            for j in range(self._columns):
                wordtopr += (" " + str(displayList[i][j]))
            print(wordtopr)


    def populatedBoard(self):
        '''this will be called at the start'''
        Deck.shuffle(self)
        for i in range(self._rows):
            for j in range(self._columns):
                c = Deck.deal(self)
                self._2dList[i][j] = c

    def getRows(self):
        return self._rows

    def getColumns(self):
        return self._columns


def main():
    while True:
        # Force user to enter valid value for number of rows
        while True:
            rows = input("Enter number of rows ")
            if rows.isdigit() and ( 1 <= int(rows) <= 9):
                rows = int(rows)
                break
            else:
                print ("    ***Number of rows must be between 1 and 9! Try again.***")
                # Adding *** and indenting error message makes it easier for the user to see

        # Force user to enter valid value for number of columns
        while True:
            columns = input("Enter number of columns ")
            if columns.isdigit() and ( 1 <= int(columns) <= 9):
                columns = int(columns)
                break
            else:
                print ("    ***Number of columns must be between 1 and 9! Try again.***")

        if rows * columns % 2 == 0:
            break
        else:
            print ("    ***The value of rows X columns must be even. Try again.***")

    game = Game(rows, columns)
    game.play()

if __name__ == "__main__":
    main()