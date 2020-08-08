#Deck class, a vector of cards with other functionallity reading from and writing to memory
import card
import os
class Deck:
  deck = [] #vector of cards
  weight = 0.0
  deckName = ""

  def __init__(self, filename): #creating a deck from file
    try:
      fhand = open(filename, 'r')
    except:
      print("Deck does not exist")
      
    unworked = fhand.readlines()
    
    at_counter = 0
    perc_counter = 0
    #builds card vector from disk
    for i in range(len(unworked)-1):
      if unworked[i][0:len(unworked[i])-1] == "end":
        break
      if unworked[i][0] == "@":
        at_counter = at_counter+1
        continue
      if unworked[i][0] == "%":
        perc_counter = perc_counter+1
      if at_counter == 2 and perc_counter == 1: #inside the data portion of .deck
        
        if unworked[i][0:4] == "Card": #make a new card with the data
          new = card.Card(unworked[i][5:len(unworked[i])-1],unworked[i+1][7:len(unworked[i+1])-1], unworked[i+2][14:len(unworked[i+2])-1], unworked[i+3][11:len(unworked[i+3])-1], float(unworked[i+4][9:len(unworked[i+4])-1]))
          self.deck.append(new)
      if perc_counter == 2:
        self.weight = float(unworked[i+1][0:len(unworked[i+1])-1])
    self.deckName = filename    
    fhand.close()
          



  #writeWeight, updates the weight of a deck file from a vector cards
  #python deletes all content of a file when opening for writing, so will make a temp file, 
  #copy needed contents and then rewrite the cards figure out hw to pass list into method
  def writeWeight(self):
    try:
      fhand = open(self.deckName, 'r') #not working because no reference to self in parameter lol wtf hjow that work watch youtube dude
    except:
      print("Error on writing the weight")
    unworked = fhand.readlines()
    fhand.close()
    try:
      fhandTemp = open("gieh9h3rf9hdv9dshdfsdqwer", 'w')#temp file
    except:
      print("Error on writing the weight 2")
    #copy comments
    at_counter = 0
    for i in range(len(unworked)-1):
      if at_counter == 2:
        break
      if unworked[i][0] == "@":
        fhandTemp.write(unworked[i])
        at_counter = at_counter + 1
        continue
      fhandTemp.write(unworked[i])
    #write cards
    fhandTemp.write("%\n")
    for i in range(len(self.deck)):
      fhandTemp.write("Card " + self.deck[i].name + "\n")
      fhandTemp.write("word = " + self.deck[i].word + "\n")
      fhandTemp.write("translation = " + self.deck[i].translation + "\n")
      fhandTemp.write("sentence = " + self.deck[i].sentence + "\n")
      fhandTemp.write("weight = " + str(self.deck[i].weight) + "\n")
    fhandTemp.write("%\n")
    fhandTemp.write(str(self.weight))
    fhandTemp.write("\n")
    fhandTemp.close()
    os.remove(self.deckName)
    os.rename("gieh9h3rf9hdv9dshdfsdqwer", self.deckName)





#obj = Deck("example.deck")
#print(obj.weight)
#print(obj.deck[1].word)
#length = len(obj.deck)
#print(length)

#j = 0
#while j < 2:
 # print(obj.deck[j].word)
  #j = j+1
  
  
