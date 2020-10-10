from sort import BubbleSort, InsertionSort

def main():
    array = [11, 2, 5, 4, 10, 9]
    bubble_array = BubbleSort.arrange_ascendingly(array=array)
    insertion_array = InsertionSort.arrange_ascendingly(array=array)
    print(f"Original array: {array}")
    print(f"Sorted using Bubble Sort: {bubble_array}")
    print(f"Sorted using Insertion Sort: {insertion_array}")

if __name__ == "__main__":
    main()