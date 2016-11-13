class Median:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def add_element(self, value):
        if len(self.max_heap) == 0 or value <= self.max_heap[0]:
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

        self.build_max_heap()
        self.build_min_heap()

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


a = Median()

for i in [2, 4, 6, 23, -12, -12, 42, 24 , 21, -100]:
    a.add_element(i)

print(a.get_median())
print(a.min_heap)
print(a.max_heap)

