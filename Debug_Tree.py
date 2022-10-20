# Build a Tree
## 
"""
    Ques : Why does this code go in an infinite loop?
    
    Ans : list(Childrem) set outside __init__ belong to the class.
    They're shared by all instances which means for every node defined the
    value of children list will be same i.e.,
    
    node11.children = ['1', '1.1', '1.2', '1.3', '1.4', '1.5', '2', '2.1', '2.2', '2.3', '2.4', '2.5']
    
    node21.children = ['1', '1.1', '1.2', '1.3', '1.4', '1.5', '2', '2.1', '2.2', '2.3', '2.4', '2.5']

    so, we see here every instance node created will have same variable children(same value)
    due to which in the recursive printer no Base cases is there to handle recursion break.

    Generally in the recursive method of printing Nodes of a Tree the base cases is handled by leaf_nodes(only in acyclic Tree)
    as leaf nodes has no children but in this program each node has same amount of childrens causing the TREE to cylic in nature.

    This is why infinite loop or say never ending recuraion is happening.

    Soltion to the problem:
        Now we know Variables created inside __init__ (and all other method functions)
        and prefaced with self. belong to the object instance.
        so, in this program we can define children variable inside the init methods like:
        self.children = []
        This is will avoid the recursion problem as each node will have their child node mention in the self.children list not all nodes children
        like before.

        When printer function will run it will search for base_cases to end recursion loop which will end by empty children list of leaf_nodes.
        
        Note : I have made the corrections.


"""

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

        self.children = [] #Correction made here only.
        
        if parent is not None:
            parent.children.append(self)
    def __str__(self):
        return self.name

def printer(root, level=0):
    print(" "*level + "|-", root.name)
    for node in root.children:
        printer(node, level+1)
if __name__ == "__main__":
    root = Node("Root")
    node1 = Node("1",root)
    node11 = Node("1.1", node1)
    node12 = Node("1.2", node1)
    node13 = Node("1.3", node1)
    node14 = Node("1.4", node1)
    node15 = Node("1.5", node1)
    node2 = Node("2",root)
    node21 = Node("2.1", node2)
    node22 = Node("2.2", node2)
    node23 = Node("2.3", node2)
    node24 = Node("2.4", node2)
    node25 = Node("2.5", node2)
    
    print('After correction the print Trees node are:')
    printer(root)


# Thank you,
# Jayant Sharma,
# 9654751995