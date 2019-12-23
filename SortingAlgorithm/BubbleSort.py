class BubbleSort():
    def __init__(self,listA:list):
        self.listA = listA

    def BubbleSort(self):
        n = len(self.listA)
        for i in range(0,n):
            for j in range(n-1,i,-1):
                if self.listA[j] < self.listA[j-1]:
                    key = self.listA[j]
                    self.listA[j] = self.listA[j-1]
                    self.listA[j-1] = key
        return self.listA

if __name__ == "__main__":
    import os
    print(os.path.abspath(__file__))
    a = BubbleSort(listA= [4,32,46,7,2,3,-5,3,-10,4,4,52,53,32,3])
    print(a.listA)
    out = a.BubbleSort()
    print(out)