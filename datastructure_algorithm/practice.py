def heapSort(SList):
    num=len(SList)
    buildHeap(SList)
    for i in range(len(SList)-1,0,0,-1):
        SWAP(SList,0,i)
        percolateDown(SList,0,i-1)

    return SList