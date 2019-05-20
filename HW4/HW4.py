URL = '測試資料.txt'
text = []

# 樹節點類構建
class TreeNode(object):
    def __init__(self, data):
        self.val = data[0]
        self.priority = data[1]
        self.leftChild = None
        self.rightChild = None
        self.code = ""

# 創建樹節點隊列函數
def creatnodeQ(codes):
    q = []
    for code in codes:
        q.append(TreeNode(code))
    return q
    
# 為隊列添加節點元素，並保證優先度從大到小排列
def addQ(queue, nodeNew):
    if len(queue) == 0:
        return [nodeNew]
    for i in range(len(queue)):
        if queue[i].priority >= nodeNew.priority:
            return queue[:i] + [nodeNew] + queue[i:]
    return queue + [nodeNew]

# 節點隊列類定義
class nodeQeuen(object):

    def __init__(self, code):
        self.que = creatnodeQ(code)
        self.size = len(self.que)

    def addNode(self,node):
        self.que = addQ(self.que, node)
        self.size += 1

    def popNode(self):
        self.size -= 1
        return self.que.pop(0)

# 各個字符在字符串中出現的次數，即計算優先度
def freChar():
    data = {}
    txt = []
    with open(URL,'r') as fp:
        txt = fp.readlines()
        text.append(txt)
    txtOne = txt[0].split(', ')
    txtTwo = txt[1].split(', ')
    txtOne[-1] = txtOne[-1].split('\n')[0]
    txtTwo[-1] = txtTwo[-1].split('\n')[0]
    i = 0
    for name in txtOne:
        data[txtOne[i]] = int(txtTwo[i])
        i = i + 1
    return sorted(data.items(),key=lambda x:x[1])

# 創建哈夫曼樹
def creatHuffmanTree(nodeQ):
    while nodeQ.size != 1:
        node1 = nodeQ.popNode()
        node2 = nodeQ.popNode()
        r = TreeNode([None, node1.priority+node2.priority])
        r.leftChild = node1
        r.rightChild = node2
        nodeQ.addNode(r)
    return nodeQ.popNode()

codeDic1 = {}
codeDic2 = {}
# 由哈夫曼樹得到哈夫曼編碼表
def HuffmanCodeDic(head, x):
    global codeDic, codeList
    if head:
        HuffmanCodeDic(head.leftChild, x+'0')
        head.code += x
        if head.val:
            codeDic2[head.code] = head.val
            codeDic1[head.val] = head.code
        HuffmanCodeDic(head.rightChild, x+'1')

t= nodeQeuen(freChar()) 
tree = creatHuffmanTree(t) 
HuffmanCodeDic(tree, '')

lastTxT = ''
first = True
for index in codeDic1:
    if first:
        first = False
        lastTxT += index + ':' + codeDic1[index]
    else:
        lastTxT += ', ' + index + ':' + codeDic1[index]

f = open(URL,mode='w')
for line in text:
    f.writelines(line)
f.write('\n')
f.write(lastTxT)
f.close()