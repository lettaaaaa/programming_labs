class ElementK:
    def __init__(self, numbers, k):
        self.numbers = numbers
        self.k = k
        self.array_not_sorted = self.numbers.copy()
        self.bubble_sort(self.numbers)
        self.element_k = self.numbers[k - 1]
        self.pos_k = self.array_not_sorted.index(self.element_k)

    def bubble_sort(self, nums):

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        n = len(nums)
        swapped = True

        x = -1
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n - x):
                if nums[i - 1] < nums[i]:
                    swap(i - 1, i)
                    swapped = True


"""if __name__ == "__main__":

    numbers = list(map(int, input("enter an array of numbers ").split()))
    k = int(input("enter k "))

    if len(numbers) < k:
        print("the array must be longer k")
    else:
        Laba = ElementK(numbers, k)
        print(Laba.element_k)
        print(Laba.pos_k)"""
