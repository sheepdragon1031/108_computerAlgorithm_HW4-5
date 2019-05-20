URL = '測試資料.txt'
text = []
tempTxt = ['', 0, 0]


def printknapSack(W, wt, val, na, n): 
    K = [[0 for w in range(W + 1)] 
            for i in range(n + 1)] 
              
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i - 1] <= w: 
                K[i][w] = max(val[i - 1]  
                  + K[i - 1][w - wt[i - 1]], 
                               K[i - 1][w]) 
            else: 
                K[i][w] = K[i - 1][w] 
  
    # 結果
    res = K[n][W] 
    tempTxt[2] = res  
    
    w = W 
    first = True
    for i in range(n, 0, -1): 
        if res <= 0: 
            break
       

        if res == K[i - 1][w]: 
            continue
        else: 
  
            # 此項目包括在內。 
            if first:
                first = False
                tempTxt[0] = na[i - 1]
                tempTxt[1] = wt[i - 1]
            else:
                tempTxt[0] = str(tempTxt[0]) + ", " + str(na[i - 1]) 
                tempTxt[1] += wt[i - 1]
            # 由於包含此重量
            # 扣除其價值
            res = res - val[i - 1] 
            w = w - wt[i - 1] 

   


txt = []
with open(URL,'r') as fp:
    txt = fp.readlines()
    text.append(txt)
Loadable = txt[0].split(', ')
Numbering = txt[1].split(', ')
weight = txt[2].split(', ')
value = txt[3].split(', ')
Loadable[-1] = Loadable[-1].split('\n')[0]
Numbering[-1] = Numbering[-1].split('\n')[0]
weight[-1] = weight[-1].split('\n')[0]
value[-1] = value[-1].split('\n')[0]

val = []
wt = []
na = []
for i in value:
    val.append(int(i))
for i in weight:
    wt.append(int(i))
for i in Numbering:
    na.append(int(i))

W = int(Loadable[0])
n = len(val) 
      
printknapSack(W, wt, val, na, n) 
  
Txt = "取" + tempTxt[0] + "，重量:" + str(tempTxt[1]) + "，價值:" + str(tempTxt[2])        
f = open(URL,mode='w')
for line in text:
    f.writelines(line)
f.write('\n')
f.write(Txt)
f.close()
