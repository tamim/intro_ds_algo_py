def bubble_sort(L):
    n = len(L)
    for i in range(0, n):
        swapped = False
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                swapped = True
        if not swapped:
            break

if __name__ == "__main__":
    L = [6, 1, 4, 9, 2]
    print("Before sort:", L)
    bubble_sort(L)
    print("After sort:", L)

