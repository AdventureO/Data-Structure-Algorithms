class Median:
    def __init__(self, array):
        self.max_heap = array[:len(array)//2]
        self.min_heap = array[len(array)//2:]

    def add_element(self, value):
        if value <= self.max_heap[0]:
            self.max_heap.append(value)
            self.build_max_heap()

        else:
            self.min_heap.append(value)
            self.build_min_heap()

        self._equal()

    def _equal(self):
        if (len(self.min_heap) - len(self.max_heap)) >= 2:
            min = self.min_heap[0]
            self.min_heap[0] = self.min_heap[len(self.min_heap) - 1]
            self.min_heap = self.min_heap[:len(self.min_heap) - 1]
            self.min_heapify(1)
            self.max_heap.append(min)
            self.max_heapify(len(self.max_heap) - 1)


        elif (len(self.max_heap) - len(self.min_heap)) >= 2:
            max = self.max_heap[0]
            self.max_heap[0] = self.max_heap[len(self.max_heap) - 1]
            self.max_heap = self.max_heap[:len(self.max_heap) - 1]

            self.max_heapify(1)
            self.min_heap.append(max)
            self.min_heapify(len(self.min_heap) - 1)


    def get_median(self):
        if len(self.max_heap) == len(self.min_heap) and len(self.max_heap) != 0:
            return (self.max_heap[0], self.min_heap[0])

        elif len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]

        elif len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0]


    def get_maxheap_elements(self):
        return self.max_heap

    def get_minheap_elements(self):
        return self.min_heap

    def max_heapify(self, i):
        while(1):
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < len(self.max_heap) and self.max_heap[left] > self.max_heap[largest]:
                largest = left
            if right < len(self.max_heap) and self.max_heap[right] > self.max_heap[largest]:
                largest = right
            if largest == i:
                break

            self.max_heap[i], self.max_heap[largest] = self.max_heap[largest], self.max_heap[i]
            i = largest

    def build_max_heap(self):
        for i in range(len(self.max_heap) // 2, -1, -1):
            self.max_heapify(i)

    def min_heapify(self, i):
        while(1):
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < len(self.min_heap) and self.min_heap[left] < self.min_heap[smallest]:
                smallest = left
            if right < len(self.min_heap) and self.min_heap[right] < self.min_heap[smallest]:
                smallest = right
            if smallest == i:
                break

            self.min_heap[i], self.min_heap[smallest] = self.min_heap[smallest], self.min_heap[i]
            i = smallest

    def build_min_heap(self):
        for i in range(len(self.min_heap) // 2, -1, -1):
            self.min_heapify(i)

a = Median([0,1,2,3,4,5,6,7,8,9,10])
a.add_element(1)
a.add_element(2)
a.add_element(3)
a.add_element(4)
a.add_element(5)
a.add_element(6)
a.add_element(7)
a.add_element(8)
a.add_element(9)
a.add_element(10)

a.build_max_heap()
print(a.max_heap)
a.build_min_heap()
print(a.min_heap)
print(a.get_median())