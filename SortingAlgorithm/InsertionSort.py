class InsertionSort():
    """ 从小到大 直接插入排序
    1. 空间O(1)
    2. 时间最差 O(n**2)，最好O(n)
    3. 排序是稳定排序
    """
    def __init__(self,listA:list):
        self.listA = listA
    def InsertionSort(self):
        n = len(self.listA)
        for j in range(1,n):
            key = self.listA[j]
            i = j-1
            while i >=0 and key < self.listA[i]:
                self.listA[i+1] = self.listA[i]
                i -= 1
            # 此时 key >= lsitA[i]
            self.listA[i+1] = key
        return self.listA

if __name__ == "__main__":
    import os
    print(os.path.abspath(__file__))
    a = InsertionSort(listA= [4,32,46,7,2,3,-5,3,-10,4,4,52,53,32,3])
    print(a.listA)
    out = a.InsertionSort()
    print(out)

