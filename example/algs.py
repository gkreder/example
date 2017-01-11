import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(A):
    """
    Describe how you are sorting `x`

    from http://www.geekviewpoint.com/python/sorting/bubblesort
    """
    def swap( A, x, y ):
      tmp = A[x]
      A[x] = A[y]
      A[y] = tmp

    for i in range(len(A)):
        for k in range( len( A ) - 1, i, -1 ):
            if ( A[k] < A[k - 1] ):
                swap( A, k, k - 1 )
 
    return A

def quicksort(arr):
    """
    Describe how you are sorting `x`

    from http://stackoverflow.com/questions/18262306/quicksort-with-python
    """

    if len(arr) == 0:
        return []

    return quicksort([x for x in arr if x < arr[0]]) \
        + [x for x in arr if x == arr[0]] \
        + quicksort([x for x in arr if x > arr[0]])
    
    return arr

