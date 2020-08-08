#import card

#priority queue fit to this application

class Node: #card can be said to be a value for now, but later implement for a card object
  def __init__(self, card):
    self.card = card
    self.left = None
    self.right = None
    self.height = 1


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
  
    #insert a new element into tree
  def insert(self, root, key):
    #insert node into place based on value (like a normal binary search tree)
    if root is None:
      return Node(key)
    elif key < root.card:
      root.left = self.insert(root.left, key)
    else:
      root.right = self.insert(root.right, key)
      
    #update heights of all nodes after this insertion is done
    root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
    
    #find the balance of the tree based off of the newly updated heights
    balance = self.getBalance(root)
    
    #left left case
    if balance > 1 and key < root.left.card: 
      return self.rightRotate(root) 
  
    # right right case 
    if balance < -1 and key > root.right.card: 
      return self.leftRotate(root) 
  
    # left right 
    if balance > 1 and key > root.left.card: 
      root.left = self.leftRotate(root.left) 
      return self.rightRotate(root) 
  
    #right left 
    if balance < -1 and key < root.right.card: 
      root.right = self.rightRotate(root.right) 
      return self.leftRotate(root) 
  
    return root 
      
      
    
     
   
       
  def preOrder(self, root):
         if root is None:
           return
         print("{0}".format(root.card), end="")
         self.preOrder(root.left)
         self.preOrder(root.right)
         
myTree = AVL_Tree() 
root = None
  
root = myTree.insert(root, 10) 
root = myTree.insert(root, 20) 
root = myTree.insert(root, 30) 
root = myTree.insert(root, 40) 
root = myTree.insert(root, 50) 
root = myTree.insert(root, 25) 
myTree.preOrder(root)