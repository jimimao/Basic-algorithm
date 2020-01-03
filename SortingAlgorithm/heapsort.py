class HeapSort:
    """ heap 都是从 1位置开始 A[0] 设置为0，且不使用该位置"""
    def __init__(self,A):
        self.A = [0] + A
        self.heap_size = len(A)
        self.list_size = len(A)

    def _parent(self,i:int):
        return i // 2

    def _lchild(self,i:int):
        return 2*i

    def _rchild(self,i:int):
        return 2*i + 1

    """ 从当前结点开始，维护最大堆的属性"""
    def MAX_Heapify(self,i:int):
        flag = False
        while not flag:
            l = self._lchild(i)
            r = self._rchild(i)
            if l <= self.heap_size and self.A[l] > self.A[i]:
                largest = l
            else:
                largest = i

            if r <=self.heap_size and self.A[r] > self.A[largest]:
                largest = r

            # 最大值是当前根结点本身，最大堆属性未被破坏
            if largest == i:
                flag = True
                break

            # exchange A[largest] and A[i}
            temp = self.A[largest]
            self.A[largest] = self.A[i]
            self.A[i] = temp

            # 递归维护最大堆
            i = largest

        # return A

    """利用MAX_Heapify建堆，从最后一个非叶子结点开始，倒序往上，维护最大堆堆"""
    def build_MAX_Heap(self):
        n = self._parent(self.heap_size)
        for i in range(n,0,-1):
            self.MAX_Heapify(i)


    """插入建堆,也可用于插入结点"""
    def insert_MAX_Heap(self,key):
        self.A.append(key)
        self.heap_size += 1
        i  = self.heap_size
        while i > 1 and self.A[i] > self.A[self._parent(i)]:
            temp = self.A[self._parent(i)]
            self.A[self._parent(i)] = self.A[i]
            self.A[i]  = temp
            i = self._parent(i)
    """堆排序，交换A[1] 和 A[n], 然后维护一次"""
    def MAX_Heap_sort(self):
        while self.heap_size > 1:
            temp = self.A[self.heap_size]
            self.A[self.heap_size] = self.A[1]
            self.A[1] = temp
            self.heap_size -= 1
            self.MAX_Heapify(1)


if __name__ =="__main__":
    A = [3,10,1,4,5]
    a = HeapSort(A)
    a.build_MAX_Heap()
    print(a.A)
    a.insert_MAX_Heap(9)
    a.insert_MAX_Heap(10)
    # a.insert_MAX_Heap(3)
    print(a.A)
    a.MAX_Heap_sort()
    print(a.A)
    print(A)

    import heapq