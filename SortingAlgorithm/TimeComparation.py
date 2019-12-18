import time
from SortingAlgorithm.InsertionSort import InsertionSort


if __name__ == "__main__":
    listA = [4,32,46,7,2,3,-5,3,-10,4,4,52,53,32,3]

    """ InsertionSort"""
    start = time.time()
    a1 = InsertionSort(listA)
    end = time.time()
    print("InsertionSort time %.5f" % (end-start))