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
             [43,32,21,15,9,8,7,5,3]*100
             ]
    t1,t2,t3 = [],[],[]
    for listA in listAs:
        """ InsertionSort"""
        a1 = InsertionSort(listA)
        start = time.time()
        a1.InsertionSort()
        end = time.time()
        t1.append(end - start)

        """ BubbleSort"""
        a2 = BubbleSort(listA)
        start = time.time()
        a2.BubbleSort()
        end = time.time()
        t2.append(end - start)

        """SelectionSort"""
        a3 = SelectionSort(listA)
        start = time.time()
        a3.SelectionSort()
        end = time.time()
        t3.append(end - start)

    print("InsertionSort time %.5f , BubbleSort %.5f , SelectionSort %.5f" % (ave(t1),ave(t2),ave(t3)))
