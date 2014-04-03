A = [[1.0,2.0,3.0],
     [4.0,5.0,6.0],
     [7.0,8.0,9.0]]
I = [[1.0,0.0,0.0],
     [0.0,1.0,0.0],
     [0.0,0.0,1.0]]
def matrixPrint(m,name):
    print("matrix %s" %name)
    for line in m:
        print(line)
matrixPrint(A,"A")
matrixPrint(I,"I")
def matrixAdd(a,b):
    r=[]
    for i in range(len(a)):
        line = []
        for j in range(len(a[i])):
            line.append(a[i][j]+b[i][j])
        r.append(line)
    return r
    
matrixPrint(matrixAdd(A,I),"A+B")
def matrixScale(a,f):
    r=[]
    for i in range(len(a)):
        line = []
        for j in range(len(a[i])):
            line.append(a[i][j]*f)
        r.append(line)
    return r
    
matrixPrint(matrixScale(A,10),"Scale")
def matrixTranspose(M):
    R = []
    for i in range(len(M[0])):
        line = []
        for j in range(len(M)):
            line.append(M[j][i])
            
        R.append(line)
    return R
matrixPrint(matrixTranspose(A),"transpose")
def matrixSubtract(x,y):
    A = matrixScale(x,-1)
    B = matrixAdd(A,y)
    return B
matrixPrint(matrixSubtract(I,A),"Subtract")
def matrixRotate(M):
    R = []
    for i in range(len(M[0])):
        line = []
        for j in range(len(M)):
            line.append(M[j][len(M[0])-i-1])
            
            
        R.append(line)
    return R
matrixPrint(matrixRotate(A),"rotate")    

def matrixflip(M):
    R = []
    for i in range(len(M[0])):
        line = []
        for j in range(len(M)):
            line.append(M[i][len(M)-j-1])
            
            
        R.append(line)
    return R
matrixPrint(matrixflip(A),"flip") 
def matrixRotate180(M):
    R = []
    for i in range(len(M[0])):
        line = []
        for j in range(len(M)):
            line.append(M[len(M)-i-1][len(M)-j-1])
            
            
        R.append(line)
    return R
matrixPrint(matrixRotate180(A),"rotate180")
def matrixDemo(w,h):
    R = []
    a = 0.0
    for i in range(h):
        line = []
        for j in range(w):
            line.append(a)
            a = a + 1 
        R.append(line)
    return R
matrixPrint(matrixDemo(5,3),"matrixDemo")