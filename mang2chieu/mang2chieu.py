A = []
B = []
m = 2
n = 2 
def Init(A,m,n):
    for i in range(m+1):
        A.append([])
        for j in range(n + 1):
            A[i].append(0)
 #----------------------------------------
def CreateMatrix(A,m,n,c):
    for i in range(1,m+1):
        for j in range(1 ,n+1):
            x =  int(input("%c[%d][%d]="%(c,i,j)))
            A[i][j] = x
#---------------------------------------------
def ViewMatrix(A,m,n):
    for i in range(1,m+1):
        for j in range(1,n+1):
            print("%d" %A[i][j] , end="\t")
        print()
#-------------------------------------------------
def summatrix(A,B,m,n):
    C = []
    Init(C,m,n)
    for i in range(1,m+1):
        for j in range(1 ,n+1):
             C[i][j] = A[i][j] + B[i][j]
    return C
#-------------------------------------------------
def main():
    Init(A,m,n)
    print("tao ma tran A", end="\n")
    CreateMatrix(A,m,n,"A")
    print("xem ma tran A", end="\n")
    ViewMatrix(A,m,n)
    Init(B,m,n)
    print("tao ma tran B", end="\n")
    CreateMatrix(B,m,n,"B")
    print("xem ma tran B", end="\n")
    ViewMatrix(B,m,n)
    C = summatrix(A,B,m,n)
    print("xem ma tran C :", end='\n')
    ViewMatrix(C,m,n)
if __name__ == "__main__":
    main()