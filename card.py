#Class for a "Card" in learnDe, a card is formed from four strings and a weight It is stored in a deck file format 
#change program to suit name
class Card:
#  name = ""
 # word = ""
#  participle = ""
#  translation = ""
#  sentence = ""
#  weight = 0.0 #default, but should never be below 0
  
  def __init__(self, name, word, translation, sentence, weight):
    self.name = name
    self.word = word
    self.translation = translation
    self.weight = weight
    self.sentence = sentence

#updates weight of each card  
  def updateWeight(self, assess):
    if assess == "great":
      self.weight = self.weight + 0.4
    elif assess == "good":
      self.weight = self.weight + 0.2
    elif assess == "neutral":
      self.weight = self.weight - .1
    elif assess == "bad":
      self.weight = self.weight - .2
    elif assess == "terrible":
      self.weight = self.weight - .4
    else:
      print("error on updateWeight")
    
    if self.weight > 1:
      self.weight = 1.0
    if self.weight < -1.0:
      self.weight = -1 

  def displayCard(self):
    print(self.word)   
    
    check = True
    while check:
      print(">", end ="")
      answer = input()
      if answer == self.translation:
        print("How do you feel about the word? (great, good, neutral, bad, terrible)")
        print(">", end = "")
        answer = input()
        self.updateWeight(answer)
        break
      else:
        print("wrong, try again")

  

#new = Card("one", "two", "three", 1.0)
#new.displayCard()
