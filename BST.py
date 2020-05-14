import random
class Node(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
    def addNode(self,n):
        
        if n.val<self.val:
            if self.left==None:
                self.left=n
            else:
                self.left.addNode(n)
        elif n.val>self.val:
            if self.right==None:
                self.right=n
            else:
                self.right.addNode(n)
    def visit(self,order):
        if(order=='preorder'):
            print(self.val)
        if self.left!=None:
            self.left.visit(order)
        if(order=='inorder'):
            print(self.val)
        if self.right!=None:
            self.right.visit(order)
        if(order=='postorder'):
            print(self.val)
    def search(self,val):
        if(self.val==val):
            return val
        elif(val<self.val and self.left!=None):
            return self.left.search(val)
        elif(val>self.val and self.right!=None):
            return self.right.search(val)
        return None
class Tree(object):
    def __init__(self):
        self.root=None
    def addValue(self,val):
        n = Node(val)
        if self.root == None:
            self.root=n
        else:
            self.root.addNode(n)
    def traverse(self,order='inorder'):
        self.root.visit(order)
    def search(self,val):
        x=self.root.search(val)
        if x is None:
            print('Not found')
        else:
            print(x,'Found')


if __name__=='__main__':
    tree=Tree()
    for i in range(10):
        values=random.randint(0,100)
        tree.addValue(values)
    tree.traverse(order='inorder') #define order here (inorder,preorder or postorder
    #tree.search('Enter number to be searched')
