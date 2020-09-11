def setValue():
    n = int(input("Nhập số lượng phần tử n = "))
    A=[]
    for i in range(n+1):
        A.append(0)

        
    for i in range(1,n+1):
        A[i] = int(input("X="))
    return A,n
def Sum(A,n):
    sum = 0
    for i in range(1,n+1):
        sum += A[i]
    return sum    
def main():

    A,n = setValue()
    print("Tổng: ",Sum(A,n))

if __name__ == "__main__":
    main()
