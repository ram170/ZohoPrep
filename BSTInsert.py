class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,node):
    if(root):
        if(root.val>node.val):
            if(root.left is None):
                root.left=node
            else:    
                insert(root.left,node)
        else:
            if(root.right is None):
                root.right=node
            else:
                insert(root.right,node)
def inorder(root):
    if(root):
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        
root=node(50)
insert(root,node(30))
insert(root,node(20))
insert(root,node(40))
insert(root,node(70))
insert(root,node(60)) 
insert(root,node(80))
inorder(root)
