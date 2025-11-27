import gradio as gr
import random

class TreeNode:
    # Nodes used for the visualization tree
    def __init__(self, unsorted_state, sorted_state, step_num, node_type="Leaf"):
        self.unsorted_state = list(unsorted_state) 
        self.sorted_state = list(sorted_state)     
        self.step_num = step_num
        self.node_type = node_type 
        self.left = None
        self.right = None

# Global Counter for Steps 
step_counter = 0

# Merge Logic
def merge(arr, l, m, r):
    # sets the split arrays
    #calculates the right array
    n1 = m - l + 1
    #calculates the left array 
    n2 = r - m
    
    #temp arrays set to the size of the splits 
    L = [0] * n1
    R = [0] * n2
    # loops through array and stores the values
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

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
    #compares the left and right arrays    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSortBuilder(arr, l=None, r=None):
    global step_counter
    # sets the left and right pointers
    if l is None: l = 0
    if r is None: r = len(arr) - 1
    
    # Capture the Unsorted State (Before any sorting happens in this scope)
    unsorted_snapshot = arr[l:r+1]
    
    # Recursive Case
    # exits if there only one element left in the array 
    if l < r:
        # sets the middle 
        m = l + (r - l) // 2
        
        # 1. recursive call for the left split 
        left_node = mergeSortBuilder(arr, l, m)
        
        # 2. recursive call for the right split 
        right_node = mergeSortBuilder(arr, m + 1, r)
        
        # 3. Merge left and right arrays
        merge(arr, l, m, r)
        
        # 4. Creates Node and increments the step
        step_counter += 1
        node = TreeNode(unsorted_snapshot, arr[l:r+1], step_counter, "Merged")
        node.left = left_node
        node.right = right_node
        return node
    else:
        # Base Case 
        step_counter += 1
        return TreeNode(unsorted_snapshot, arr[l:r+1], step_counter, "Leaf")
#Converts the Tree to Html
def tree_to_html(node):
    if node is None:
        return ""
    
    # ----Styles---
    # Blue Box (Divide Phase)
    blue_box_style = """
        background-color: #a0c4ff;
        border: 2px solid #0056b3;
        color: black;
        border-radius: 4px;
        padding: 5px;
        min-width: 40px;
        text-align: center;
        font-family: monospace;
        font-weight: bold;
        margin-bottom: 5px;
        box-shadow: 2px 2px 3px rgba(0,0,0,0.2);
    """
    
    # Yellow Box (Merge Phase)
    yellow_box_style = """
        background-color: #ffd670;
        border: 2px solid #e07a00;
        color: black;
        border-radius: 4px;
        padding: 5px;
        min-width: 40px;
        text-align: center;
        font-family: monospace;
        font-weight: bold;
        margin-top: 5px;
        box-shadow: 2px 2px 3px rgba(0,0,0,0.2);
    """

    # ---UI Generation---
    
    # 1. Top Element: Blue Box (Unsorted State)
    blue_content = f"""
    <div style="{blue_box_style}">
        <div style="font-size: 10px; color: #004085; margin-bottom: 2px;">Step {node.step_num} (Split)</div>
        {node.unsorted_state}
    </div>
    """

    # 2. Bottom Element: Yellow Box (Sorted State)
    yellow_content = f"""
    <div style="{yellow_box_style}">
        <div style="font-size: 10px; color: #856404; margin-bottom: 2px;">Step {node.step_num} (Merge)</div>
        {node.sorted_state}
    </div>
    """

    # 3. Middle Elements: Children and Connectors
    children_html = ""
    blue_connectors = ""
    green_connectors = ""
    
    if node.left or node.right:
        # Recursively generate children
        children_html = f"""
        <div style="display: flex; flex-direction: row; gap: 30px; justify-content: center;">
            <div style="display: flex; flex-direction: column; align-items: center;">
                {tree_to_html(node.left)}
            </div>
            <div style="display: flex; flex-direction: column; align-items: center;">
                {tree_to_html(node.right)}
            </div>
        </div>
        """
        
        # Blue Arrows pointing DOWN (from Blue box to children)
        blue_connectors = f"""
        <div style="display: flex; justify-content: center; width: 100%; height: 20px; position: relative;">
            <div style="position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 2px; height: 100%; background-color: #0056b3;"></div>
            <!-- Diagonal lines would require SVG, simplified to vertical for HTML/CSS robustness -->
        </div>
        """
        
        # Green Arrows pointing DOWN (from Children to Yellow box)
        green_connectors = f"""
        <div style="display: flex; justify-content: center; width: 100%; height: 20px; position: relative;">
            <div style="position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 2px; height: 100%; background-color: #28a745;"></div>
        </div>
        """


    return f"""
    <div style="display: flex; flex-direction: column; align-items: center; margin: 0 5px;">
        {blue_content}
        {blue_connectors}
        {children_html}
        {green_connectors}
        {yellow_content}
    </div>
    """

# --- UI Functions ---
def generate_random_string():
    #Generates a random list and returns it as a string.
    arr = random.sample(range(1, 50), 8) 
    return ", ".join(map(str, arr))

def run_visualization(input_str):
    #Runs the sort and returns the tree HTML.
    global step_counter
    
    try:
        if not input_str.strip():
            return "<div style='padding: 20px; color: red;'>⚠️ Please enter numbers first.</div>"
            
        arr = [int(x.strip()) for x in input_str.split(',')]
        step_counter = 0
        
        # Build Tree
        root = mergeSortBuilder(list(arr))
        
        # Convert to HTML
        html_content = f"""
        <div style="width: 100%; overflow-x: auto; padding: 20px; display: flex; justify-content: center; align-items: flex-start;">
            {tree_to_html(root)}
        </div>
        """
        return html_content
    except ValueError:
        return "<div style='padding: 20px; color: red;'>⚠️ Error: Please enter valid integers separated by commas.</div>"

# --- Gradio App Layout ---
with gr.Blocks(title="Merge Sort Visualizer") as demo:
    gr.Markdown("# Merge Sort Visualizer")
    gr.Markdown("Visualize how Merge Sort splits the array (Blue) and merges it back (Yellow).")
    
    with gr.Row():
        inp = gr.Textbox(label="Input List", placeholder="e.g., 5, 2, 4, 7, 1, 3, 2, 6", scale=2)
        gen_btn = gr.Button("🎲 Generate Random", variant="secondary", scale=1)
        sort_btn = gr.Button("Sort & Visualize", variant="primary", scale=1)
    
    tree_box = gr.HTML(label="Visualization Tree")
    
    gen_btn.click(fn=generate_random_string, inputs=[], outputs=[inp])
    sort_btn.click(fn=run_visualization, inputs=[inp], outputs=[tree_box])

if __name__ == "__main__":
    demo.launch()