import gradio as gr

class TreeNode:
    # Nodes used for the visualization tree
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

def mergeSortBuilder(arr, l=None, r=None):
    # Calculate l and r on first call 
    if l is None:
        l = 0
    if r is None:
        r = len(arr) - 1
    
    if l < r:
        # if this statement is false that means that there is only one element in the recursive call 
        m = l + (r - l) // 2
        # sets the middle of the array
        
        left_node = mergeSortBuilder(arr, l, m)
        # sorts the left half
        
        right_node = mergeSortBuilder(arr, m + 1, r)
        # sorts the right half 
        
        merge(arr, l, m, r)
        # merges the two arrays
        
        node = TreeNode(arr[l:r+1])
        node.left = left_node
        node.right = right_node
        return node
    else:
        return TreeNode(arr[l:r+1])

# --- HTML Generator ---
def tree_to_html(node):
    if node is None:
        return ""
    
    # Box styling
    node_html = f"""
    <div style="
        border: 2px solid #333; 
        padding: 8px; 
        margin: 5px; 
        background-color: white; 
        border-radius: 4px;
        text-align: center;
        font-family: monospace;
        font-weight: bold;
    ">
        {node.current_state}
    </div>
    """
    
    children_html = ""
    # Recursively generate HTML for children side-by-side
    if node.left or node.right:
        children_html = f"""
        <div style="display: flex; gap: 20px; justify-content: center; margin-top: 10px;">
            <div style="display: flex; flex-direction: column; align-items: center;">
                {tree_to_html(node.left)}
            </div>
            <div style="display: flex; flex-direction: column; align-items: center;">
                {tree_to_html(node.right)}
            </div>
        </div>
        """
    
    # Vertical layout: Parent on top, Children below
    return f"""
    <div style="display: flex; flex-direction: column; align-items: center;">
        {node_html}
        {children_html}
    </div>
    """

# --- Driver Function ---
def visualize_html(text):
    if not text:
        return ""
    try:
        arr = [int(x.strip()) for x in text.split(",") if x.strip() != ""]
        root = mergeSortBuilder(arr)
        
        # Wrap the whole tree in a scrollable container
        return f"""
        <div style="width: 100%; overflow-x: auto; padding: 20px; display: flex; justify-content: center;">
            {tree_to_html(root)}
        </div>
        """
    except Exception as e:
        return f"<div style='color:red'>Error: {str(e)}</div>"

# --- Gradio UI ---
demo = gr.Interface(
    fn=visualize_html,
    inputs=gr.Textbox(label="Input Array (comma separated)", value="5, 1, 4, 2, 8"),
    outputs=gr.HTML(label="Visualization"),
    title="Merge Sort - Stage 3 (HTML Visualization)",
    description="In this stage, we have replaced the debug text with a recursive HTML visualization using Flexbox."
)
demo.launch()