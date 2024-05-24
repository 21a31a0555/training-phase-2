
def isLeafNode(root):
    if root.left == None and root.right == None:
        return True 
    return False
    
def collectLeftView(root, result):
    if root == None:
        return 
    while root != None and isLeafNode(root)== False:
        result.append(root.data)
        if root.left != None:
            root = root.left 
        else:
            root = root.right
     
def collectLeafNodes(root, result):
    if root == None:
        return 
    elif isLeafNode(root):
        result.append(root.data)
        return 
    collectLeafNodes(root.left, result)
    collectLeafNodes(root.right, result)
    
    
    
def collectRightViewInReverseFashion(root, result):
    if root == None:
        return 
    temp = []
    while root != None and isLeafNode(root)== False:
        temp.append(root.data)
        if root.right != None:
            root = root.right 
        else:
            root = root.left
    temp = temp[::-1]
    for ele in temp:
        result.append(temp)

def findBoundaryTraversal(root):
    if root == None:
        return []
    result = []
    result.append(root.data)
    
    collectLeftView(root.left, result)
    collectLeafNodes(root, result)
    collectRightViewInReverseFashion(root.right, result)
    return result






















def findLeftView(root):
    if root == None:
        return []
    result = []
    Q = [root]
      
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            curr = Q.pop(0)
            if i == 0:
                result.append(curr.data)
            if curr.left != None:
                Q.append(curr.left)
                
            if curr.right != None:
                Q.append(curr.right)
    return result
    
def findRightView(root):
    if root == None:
        return []
    result = []
    Q = [root]
    
    while Q:
        n = len(Q)
        for i in range(n):
            curr = Q.pop(0)
            if i == n - 1:
                result.append(curr.data)
            if curr.left != None:
                Q.append(curr.left)
                
            if curr.right != None:
                Q.append(curr.right)
    return result
    
def topViewHelper(root, store, hd, level):
    if root == None:
        return 
    
    if hd not in store or store[hd][0] > level:
        store[hd] = [level, root.data]
        
    topViewHelper(root.left, store, hd - 1, level + 1)
    topViewHelper(root.right, store, hd + 1, level + 1)
  
def findTopView(root):
    result = []
    if root == None:
        return result
    
    store = {}
    topViewHelper(root, store, 0, 0)
    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
    return result
    
def bottomViewHelper(root, store, hd, level):
    if root == None:
        return 
    
    if hd not in store or store[hd][0] <= level:
        store[hd] = [level, root.data]
        
    bottomViewHelper(root.left, store, hd - 1, level + 1)
    bottomViewHelper(root.right, store, hd + 1, level + 1)
  
def findBottomView(root):
    result = []
    if root == None:
        return result
    
    store = {}
    bottomViewHelper(root, store, 0, 0)
    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
    return result
    
    o1=node(30)
o2=node(40)
o3=node(50)
o4=node(60)
o5=node(70)
o6=node(80)
o7=node(90)
o8=node(100)
o9=node(110)
o10=node(-50)
o1.lref=o2
o1.rref=o3
o2.lref=o4
o2.rref=o5
o3.lref=o6
o3.rref=o7
o4.lref=o8
o4.rref=o9
o5.lref=o10
root=o1
inordertraversal(root)
print()
preordertraversal(root)
print()
postordertraversal(root)
print()
levelordertraversal(root)
print()
zigzagLevelOrder(root)
print()
findleftview(root)
print()
findrightview(root)
print()
findTopView(root)
print()
findBottomView(root)
    
    
