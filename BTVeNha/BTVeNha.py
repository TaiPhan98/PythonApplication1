def setValue():
    n = int(input("Nhập số lượng phần tử n = "))
    A=[]
    for i in range(n):
        A.append(0)
    for i in range(n):
        A[i] = int(input("X="))
    return A,n
# --------------------
def viewArray(A,n):
    print("SHOW ARRAY: ")
    for i in range(n):
        print(A[i],end="\t")
    print(end="\n")
# ----------------------
def MaxValue(A,n):
    max = A[0]
    for i in range(1,n-1):
        if A[i] > max:
            max = A[i]
    return max        
# -----------------------
def Sum(A,n):
    sum = 0
    for i in range(n):
        sum += A[i]
    return sum 
# -----------------------

# Xóa phần tử tại vị trí k
def deleteByIndex(A,n):
    # Xóa phần tử thứ k
    print("Nhập vị trí thứ k cần xóa")
    index  = int(input("Nhập vị trí cần xóa: "))
    if index < 0 or index > n:
        print("Vị trí không hợp lệ!")
    else:
        A.pop(index)
        print("Mảng sau kho xóa")
        viewArray(A,n)
def main():
    A,n = setValue()
    viewArray(A,n)
    print("Phần tử lớn nhất trong mảng X= ",MaxValue(A,n),end="\n")
    print("Tổng các số có trong mảng: ",Sum(A,n),end="\n")
    # Sắp xếp mảng tăng dần
    A.sort()
    print("Mảng tăng dần: ")
    viewArray(A,n)

    # Sắp xếp mảng giảm dần
    A.sort(reverse=True)
    print("Mảng giảm dần: ")
    viewArray(A,n)

    # Thêm phần tử vào vị trí K
    # k = int(input("Nhập vị trí cần chèn:"))
    # value = int(input("Nhập giá trị cần chèn:"))
    # A.insert(k,value)
    # print("Danh sách mảng sau khi thêm phần tử vào trị trí ", k)
    # viewArray(A,n+1)

    # Xóa phần tử thứ k
    deleteByIndex(A,n-1)
if __name__ == "__main__":
    main()