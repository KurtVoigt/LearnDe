import card

#priority queue fit to the needs of this application

class Node: #card can be said to be a value for now, but later implement for a card object
  def __init__(self, card):
    self.cardObject = card
    self.left = None
    self.right = None
    self.height = 1
  def getCardWeight(self):
    return self.cardObject.weight
    


class AVL_Tree():
  #height getter for purposes of calculating balance of tree
  def getHeight(self, root):
    if root is None:
      return 0
    return root.height

  #calculates balance of AVL tree to determine rotations
  def getBalance(self, root):
    if root is None:
      return 0
    return self.getHeight(root.left) - self.getHeight(root.right)

  def leftRotate(self, root):
     rightNode = root.right
     newRightNode = rightNode.left
     
     rightNode.left = root
     root.right = newRightNode
     
     #update heights
     root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
     
     rightNode.height = 1 + max(self.getHeight(rightNode.left), self.getHeight(rightNode.right))
     return rightNode   
     
  def rightRotate(self, root):
    leftNode = root.left
    newLeftNode = leftNode.right
       
    leftNode.right = root
    root.left = newLeftNode
       
    root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
    leftNode.height = 1 + max(self.getHeight(leftNode.left), self.getHeight(leftNode.right))
    return leftNode
  
    #insert a new card into tree
  def insert(self, root, newCard):
    #insert node into place based on value (like a normal binary search tree)
    if root is None:
      return Node(newCard)
    elif newCard.weight < root.cardObject.weight:
      root.left = self.insert(root.left, newCard)
    else:
      root.right = self.insert(root.right, newCard)
      
    #update heights of all nodes after this insertion is done
    root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
    
    #find the balance of the tree based off of the newly updated heights
    balance = self.getBalance(root)
    
    #left left case
    if balance > 1 and newCard.weight < root.left.cardObject.weight: 
      return self.rightRotate(root) 
  
    # right right case 
    if balance < -1 and newCard.weight > root.right.cardObject.weight: 
      return self.leftRotate(root) 
  
    # left right 
    if balance > 1 and newCard.weight > root.left.cardObject.weight: 
      root.left = self.leftRotate(root.left) 
      return self.rightRotate(root) 
  
    #right left 
    if balance < -1 and newCard.weight < root.right.cardObject.weight: 
      root.right = self.rightRotate(root.right) 
      return self.leftRotate(root) 
  
    return root 
      
      
  #finds minimum element in tree (in order to display it)  
  def findMin(self, root):
    if root is None:
      return
    if root.left is None:
      return root.cardObject.weight
    return self.findMin(root.left)
   
       
  def preOrder(self, root):
    if root is None:
      return
    
    
    self.preOrder(root.left)
    
    self.preOrder(root.right)
    print(root.getCardWeight())



#myTree = AVL_Tree() 
#root = None
#testNode = card.Card("name","word", "translation", "sentence", 0.5)
#print(testNode.cardObject.weight)
#print(testNode.card.name)
#testNode = Node(testCard)
#root = myTree.insert(root, card.Card("name","word", "translation", "sentence", 30))
#root = myTree.insert(root, card.Card("name","word", "translation", "sentence", 10))
#root = myTree.insert(root,  card.Card("name","word", "translation", "sentence", 60))
#root = myTree.insert(root, card.Card("name","word", "translation", "sentence", 50))
#root = myTree.insert(root, card.Card("name","word", "translation", "sentence", 65))
#root = myTree.insert(root,  card.Card("name","word", "translation", "sentence", 55))
#print(myTree.findMin(root)) 
#myTree.preOrder(root)