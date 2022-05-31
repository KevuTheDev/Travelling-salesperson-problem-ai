def binary_search(p_arr, p_x):
    return binary_search_aux(p_arr, 0, len(p_arr) - 1, p_x)


def binary_search_aux(p_arr, p_low, p_high, p_x):
    # Check base case
    if p_high >= p_low:

        mid = (p_high + p_low) // 2

        # If element is present at the middle itself
        if p_arr[mid] == p_x:
            p_arr.insert(mid, p_x)
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif p_arr[mid] > p_x:
            return binary_search_aux(p_arr, p_low, mid - 1, p_x)

        # Else the element can only be present in right subarray
        else:
            return binary_search_aux(p_arr, mid + 1, p_high, p_x)

    else:
        # Element is not present in the array
        p_arr.insert(p_low, p_x)
        return -1


# Test array
arr = []
x = 11

# Function call
result = binary_search(arr, x)
print(arr)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")