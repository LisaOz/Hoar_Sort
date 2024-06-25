'''
This is a script for sorting array recursively
using Hoar Sort algorithm.
'''

def hoar_sort(A):
    if len(A) <= 1:  # base case, if an array contains 1 element or is empty
        return A
    barrier = A[0]  # set barrier to the first element

    # divide the array into three parts
    L = []  # left
    M = []  # middle
    R = []  # right
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)

    L = hoar_sort(L)
    R = hoar_sort(R)

    return L + M + R


if __name__ == "__main__":
        arr = [1, 2, 8, 10, 5, 4, 7, 2, 1, 0, 3]
        sorted_array = hoar_sort(arr)
       # print(sorted_array)