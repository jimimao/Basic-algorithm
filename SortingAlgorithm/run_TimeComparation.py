import time
from SortingAlgorithm.InsertionSort import InsertionSort
from SortingAlgorithm.BubbleSort import BubbleSort
from SortingAlgorithm.SelectionSort import SelectionSort

def ave(A:list):
    return sum(A) / len(A)

if __name__ == "__main__":
    listAs = [
             [1,2,3,4,5,6,7,8,9]*100,
             [4,32,46,7,2,3,-5,3,-10,4,4,52,53,32,3]*100,
             [43,32,21,15,9,8,7,5,3]*100,
             [i for i in range(1,1000)],
             [i for i in range(1000,0,-1)]
             ]
    t1 , t2= [],[]
    for listA in listAs:
        """ InsertionSort"""
        a = InsertionSort(listA)
        start = time.time()
        a.InsertionSort()
        end = time.time()
        t1.append(end - start)
    print("InsertionSort time %.5f \n"%(ave(t1)))

    t1,t2 = [],[]
    for listA in listAs:
        """ BubbleSort"""
        a = BubbleSort(listA)
        start = time.time()
        a.BubbleSort()
        end = time.time()
        t1.append(end - start)

        """ BubbleSort++"""
        start = time.time()
        a.BubbleSort_enhanced()
        end = time.time()
        t2.append(end-start)
    print("BubbleSort %.5f , BubbleSort++ : %.5f" %(ave(t1),ave(t2)))

    t1, t2 = [], []
    for listA in listAs:
        """SelectionSort"""
        a = SelectionSort(listA)
        start = time.time()
        a.SelectionSort()
        end = time.time()
        t1.append(end - start)

        """SelectionSort ++ """

    print("SelectionSort %.5f " % (ave(t1)))
