import random


# Bubble sort array
def bubbleSort(A):
    # get array length
    n = len(A)

    # traverse through every element in array
    for i in range(n):
        swap_occurred = False

        # traverse through n-i-1 elements
        for j in range(n-i-1):

            # if previous is greater than next, swap them
            if A[j] > A[j+1]:
                holder = A[j]
                A[j] = A[j+1]
                A[j+1] = holder
                swap_occurred = True
        if swap_occurred == False:
            break
    return A

if __name__ == '__main__':
    # Define unsorted array and print
    N = 100000
    A = random.sample(range(-2147483647, 2147483647), N)
    print("Unsorted Array: ", A)
    print("Sorted Array: ", bubbleSort(A))
