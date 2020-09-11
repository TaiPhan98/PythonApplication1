def Nhap():
    print("Tính tổng 2 số \n")
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    return a,b
    # ---------------------------------------------
def Tong(a,b):
    return a+b
    # ---------------------------------------------
def main():
    a,b=Nhap()
    print("Tổng: ",Tong(a,b),end="\n")
if __name__ == "__main__":
    main()