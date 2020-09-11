def Tong(n):
    s = 0
    i=1
    while i<=n:
        s+=i
        i+=1
    return s
def main():
    n = int(input("Nhập n: "))
    s = Tong(n)
    print("kết quả: ",s)
if __name__ == "__main__":
    main()
