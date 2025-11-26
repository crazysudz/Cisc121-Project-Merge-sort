import gradio as gr

def merge(arr, l, m, r):
    n1 = m - l + 1
    # calculates the size of the left array 
    n2 = r - m
    # calculates the size of the right array
    L = [0] * n1
    R = [0] * n2
    # temp arrays size of the left and right splits 

    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]
    # loops through array and stores the values for the left and right

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # comparing the left and right arrays and places them into arr
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    # copys L and R back into the main arr[k]

def mergeSort(arr, l=None, r=None):
    # Calculate l and r on first call 
    if l is None:
        l = 0
    if r is None:
        r = len(arr) - 1
    if l < r:
        # if this statement is false that means that there is only one element in the recursive call 
        m = l + (r - l) // 2
        # sets the middle of the array
        mergeSort(arr, l, m)
        # sorts the left half
        mergeSort(arr, m + 1, r)
        # sorts the right half 
        merge(arr, l, m, r)
        # merges the two arrays

def sort_input(text):
    """Parse comma-separated integers, sort them in-place with mergeSort and return a string."""
    if not text:
        return ""
    try:
        arr = [int(x.strip()) for x in text.split(",") if x.strip() != ""]
    except ValueError:
        return "Input must be comma-separated integers"
    mergeSort(arr)
    return ", ".join(str(x) for x in arr)

demo = gr.Interface(
    fn=sort_input,
    inputs=gr.Textbox(label="Input Array (comma separated)"),
    outputs=gr.Textbox(label="Sorted Array")
)
demo.launch()

