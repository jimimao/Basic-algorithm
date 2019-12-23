class SelectionSort():
    def __init__(self,listA:list):
        self.listA = listA

    def SelectionSort(self):
        n = len(self.listA)
        for i in range(n):
            minindex = n-1
            sentry = self.listA[i]
            for j in range(n-1,i-1,-1):
                if self.listA[j] < self.listA[minindex]:
                    minindex = j
            self.listA[i] = self.listA[minindex]
            self.listA[minindex] = sentry
        return self.listA

if __name__ == "__main__":
    import os
    print(os.path.abspath(__file__))
    a = SelectionSort(listA= [4,32,46,7,2,3,-5,3,-10,4,4,52,53,32,3])
    print(a.listA)
    out = a.SelectionSort()
    print(out)