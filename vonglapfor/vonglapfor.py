def Tong(n):
    s = 0
    for i in range(1,n+1):
        s+=i
    return s
def main():
    n = int(input("Nhập n: "))
    s = Tong(n)
    print("kết quả: ",s)
if __name__ == "__main__":
    main()  
