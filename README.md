---
title: CISC 121 002 Mergesort Project
emoji: 🚀
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 6.0.1
app_file: app.py
pinned: false
short_description: Python app that visually simulates merge sort algorithm
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# Merge Sort Visualization App

## Project Overview
This project is a Python application designed to visualize the **Merge Sort** algorithm It uses **Gradio** to create an interactive Graphical User Interface (GUI) that allows users to input a list of numbers and see the sorting process step-by-step.

### Project Deliverables
[cite_start]Per the project guidelines, the repository contains the following:

| File | Description |
| :--- | :--- |
| `app.py` | Your main application file |
| `requirements.txt` | List of dependencies (i.e., Python packages, e.g., Gradio) |
| `README.md` | Documentation matching marking criteria |
| `demo_screenshot.png` | To illustrate your app visually |
| **Hugging Face app link** | The deployed version of your app (Linked below) |

---

## Demo
![App Demo](demo_screenshot.png)

---

## Problem Breakdown & Computational Thinking

### Why Merge Sort?
I chose Merge Sort because it creates a unique decision tree that would be intresting to visualize and effectively uses the **divide and conquer** approach Additionally, it maintains a time complexity of $O(n \log n)$ regardless of the dataset, making it efficient[cite: 24].

### The Four Pillars
To implement this project, I applied the four pillars of computational thinking:
* **Decomposition:** I broke the Merge Sort algorithm down into smaller steps: splitting the array recursively (`mergeSort`) and comparing/combining the split arrays (`merge`).
* **Pattern Recognition:** The algorithm relies on a repeating pattern of finding the middle index, dividing the list until one element remains, and then comparing them($L \le R$) .
* **Abstraction:** The visualization focuses on showing the user the state of the array at each step helping them understand excatly what the algorithm is preforming..
* **Algorithm Design:** The flow is designed as: **Input** (User provides a raw list) $\rightarrow$ **Processing** (Recursive Divide & Conquer) $\rightarrow$ **Output** (Sorted List displayed in GUI) and the simple algorithm desgin makes it mopre user friendly which is good for teaching somone the algorithm[cite: 30].

---

## Algorithm Flowchart
The following diagram illustrates the logic implemented in the code:

```mermaid
flowchart TD
    Start([Start]) --> Input[/Input: arr, left, right/]
    Input --> MSStart[mergeSort Function]
    MSStart --> CheckBase{left < right?}
    CheckBase -- No --> ReturnBase[Return - Base Case]
    CheckBase -- Yes --> CalcMid[mid = left + right // 2]
    CalcMid --> RecurseLeft[mergeSort arr, left, mid]
    RecurseLeft -. Recursive Call .-> MSStart
    RecurseLeft --> RecurseRight[mergeSort arr, mid+1, right]
    RecurseRight -. Recursive Call .-> MSStart
    RecurseRight --> MergeCall[Call merge Function]
    MergeCall --> CalcSizes["n1 = mid - left + 1<br/>n2 = right - mid"]
    CalcSizes --> CreateArrays[Create L and R<br/>Copy data from arr]
    CreateArrays --> InitPointers["i = 0, j = 0, k = left"]
    InitPointers --> MainLoop{i < n1 AND<br/>j < n2?}
    MainLoop -- Yes --> Compare{"L <= R?"}
    Compare -- Yes --> TakeLeft["arr = L<br/>i++, k++"]
    Compare -- No --> TakeRight["arr = R<br/>j++, k++"]
    TakeLeft --> MainLoop
    TakeRight --> MainLoop
    MainLoop -- No --> CopyLeft{Remaining<br/>in L?}
    CopyLeft -- Yes --> AddLeft["Copy L to arr<br/>i++, k++"]
    AddLeft --> CopyLeft
    CopyLeft -- No --> CopyRight{Remaining<br/>in R?}
    CopyRight -- Yes --> AddRight["Copy R to arr<br/>j++, k++"]
    AddRight --> CopyRight
    CopyRight -- No --> MergeDone[Return from merge]
    MergeDone --> ReturnBase
    ReturnBase --> Output[/Output: Sorted arr/]
    Output --> End([End])