from typing import List

class Sort(object):
    @staticmethod
    def arrange_ascendingly(array: List) -> List:
        raise NotImplementedError

class BubbleSort(Sort):
    @staticmethod
    def arrange_ascendingly(array: List) -> List:
        """ 
        Sorts an array in ascending order using bubble sort.

        Parameter
        ---------
        array: List
            The array to sort.

        Returns
        -------
        array: List
            The sorted array.
        """
        array = array[:]
        for _ in range(1, len(array) + 1):
            for index in range(0, len(array) - 1):
                if array[index] > array[index + 1]:
                    (array[index], array[index + 1]) = (array[index + 1], array[index])

        return array

class InsertionSort(Sort):
    @staticmethod
    def arrange_ascendingly(array: List) -> List:
        array = array[:]
        for index in range(0, len(array)):
            comparison_index = index 
            while(comparison_index > 0) and (array[comparison_index - 1] > array[comparison_index]):
                (array[comparison_index]), array[comparison_index - 1] = (array[comparison_index - 1], array[comparison_index])
                comparison_index -= 1
        
        return array       
