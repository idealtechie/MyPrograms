class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def fheight(self,temp):
        if(self.root==None):
            print("Empty")
            return 0
        else:
            leftHeight=0
            rightHeight=0
            if(temp.left!=None):
                leftHeight=self.fheight(temp.left)
            if(temp.right!=None):
                rightHeight=self.fheight(temp.right)
            if (leftHeight>rightHeight):
                maximum=leftHeight
            else:
                maximum=rightHeight
            return(maximum+1)
bt=BinaryTree()
bt.root=Node(1)
bt.root.left=Node(2)
bt.root.right=Node(3)
bt.root.left.left=Node(4)
bt.root.left.right=Node(5)

print("Maximum Height : "+str(bt.fheight(bt.root)))
