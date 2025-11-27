import gradio as gr

# stores the state of the array at every step.
class TreeNode:
    def __init__(self, current_state):
        self.current_state = list(current_state)
        self.left = None
        self.right = None

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

#Builds and returns a Tree structure.
def mergeSortBuilder(arr, l=None, r=None):
    if l is None:
        l = 0
    if r is None:
        r = len(arr) - 1
    
    if l < r:
        m = l + (r - l) // 2
        
        # Recurse to build children nodes first
        left_node = mergeSortBuilder(arr, l, m)
        right_node = mergeSortBuilder(arr, m + 1, r)
        
        # Perform the merge 
        merge(arr, l, m, r)
        
        # Saves the merged state
        node = TreeNode(arr[l:r+1])
        node.left = left_node
        node.right = right_node
        return node
    else:
        # Base case: single element left
        return TreeNode(arr[l:r+1])

def debug_tree_structure(text):
    if not text:
        return ""
    try:
        arr = [int(x.strip()) for x in text.split(",") if x.strip() != ""]
        
        # Build the tree
        root = mergeSortBuilder(arr)
        
        # Simple debug output to verify the object structure
        return f" Tree Constructed Successfully {root.current_state}\nLeft Child: {root.left.current_state}\nRight Child: {root.right.current_state}"
    except Exception as e:
        return f"Error: {str(e)}"

# --- Gradio UI ---
demo = gr.Interface(
    fn=debug_tree_structure,
    inputs=gr.Textbox(label="Input Array (comma separated)", value="5, 1, 4, 2, 8"),
    outputs=gr.Textbox(label="Debug Output"),
    title="Merge Sort",
    description="visuallize the merge sort with nodes and branching trees."
)
demo.launch()