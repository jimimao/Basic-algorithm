class BubbleSort():
    def __init__(self,listA:list):
        self.listA = listA

    """ 冒泡普通版本"""
    def BubbleSort(self):
        n = len(self.listA)
        for i in range(0,n):
            for j in range(n-1,i,-1):
                if self.listA[j] < self.listA[j-1]:
                    key = self.listA[j]
                    self.listA[j] = self.listA[j-1]
                    self.listA[j-1] = key
        return self.listA

    """ 冒泡++版本： 加入flag，如果当前这趟的比较中，没有发生元素的交换，代表已经全局有序了，直接break循环，返回list"""
    def BubbleSort_enhanced(self):
        flag = True
        n = len(self.listA)
        for i in range(0,n):
            for j in range(n-1,i,-1):
                if self.listA[j] < self.listA[j-1]:
                    key = self.listA[j]
                    self.listA[j] = self.listA[j-1]
                    self.listA[j-1] = key
                    flag = False
            if flag:  # 已经有序了，这一趟比较没有发生交换
                break
            flag = True
        return self.listA

if __name__ == "__main__":
    import os
    print(os.path.abspath(__file__))
    a = BubbleSort(listA= [i for i in range(1,1000)])
    print(a.listA)
    out = a.BubbleSort()
    print(out)