---
title: CISC 121 002 Mergesort Project
emoji: 🏃
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 6.0.1
app_file: app.py
pinned: false
short_description: Python app that visually simulates merge sort algorithm
---

<div align="center">

<h1>Merge Sort Visualizer</h1>

<p>
  <b><i>A Python application for visually interactive algorithm simulation.</i></b>
  <br>
  <b><i>Developed for CISC-121 at Queen's University.</i></b>
</p>

<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=for-the-badge&logo=python" alt="Made with Python"></a>
<a href="https://gradio.app/"><img src="https://img.shields.io/badge/GUI-Gradio-orange?style=for-the-badge&logo=gradio" alt="Gradio"></a>
<a href="#"><img src="https://img.shields.io/badge/Algorithm-Merge%20Sort-blueviolet?style=for-the-badge" alt="Algorithm"></a>

</div>

---

## 🚀 Objective
The goal of this project is to create a Python app that demonstrates the **Merge Sort** algorithm in a visually interactive way using a graphical user interface. This application showcases computational thinking, algorithm design, testing, documentation skills, and knowledge of sorting algorithms.

## 📦 Project Deliverables

| File | Description |
| :--- | :--- |
| `app.py` | The main application file |
| `requirements.txt` | List of dependencies (i.e., Python packages, e.g., Gradio) |
| `README.md` | Documentation matching marking criteria |
| **Hugging Face App** | The deployed version of the app (Linked above) |

---

## 🧠 Computational Thinking & Problem Breakdown

I chose **Merge Sort** to implement and visualize. It creates a unique decision tree and effectively demonstrates the **divide and conquer** approach. Additionally, it maintains a time complexity of $O(n \log n)$ regardless of the dataset, making it highly efficient.

### The Four Pillars

<details>
<summary><b>1. Decomposition</b></summary>
I broke the Merge Sort algorithm down into distinct smaller steps: the <code>mergeSort</code> function (which recursively splits the array) and the <code>merge</code> function (which compares and combines the split arrays).
</details>

<details>
<summary><b>2. Pattern Recognition</b></summary>
The algorithm relies on a repeating pattern of finding the middle index, dividing the list until single elements remain, and then comparing elements ($L \le R$) to swap and rebuild the sorted list.
</details>

<details>
<summary><b>3. Abstraction</b></summary>
The visualization abstracts away the low-level memory allocation details. It focuses on showing the user the logical flow: the input, the splitting process, and the final output, discarding unnecessary internal processing details from the visual feed.
</details>

<details>
<summary><b>4. Algorithm Design</b></summary>
The flow is designed as: <b>Input</b> (User provides a raw list) $\rightarrow$ <b>Processing</b> (Recursive Divide & Conquer) $\rightarrow$ <b>Output</b> (Sorted List displayed in GUI).
</details>

---

## 📊 Algorithm Flowchart

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
    MergeCall --> CalcSizes["n1 = mid - left + 1 <br> n2 = right - mid"]
    CalcSizes --> CreateArrays["Create L and R <br> Copy data from arr"]
    CreateArrays --> InitPointers["i = 0, j = 0, k = left"]
    InitPointers --> MainLoop{i < n1 AND <br> j < n2?}
    MainLoop -- Yes --> Compare{"L <= R?"}
    Compare -- Yes --> TakeLeft["arr = L <br> i++, k++"]
    Compare -- No --> TakeRight["arr = R <br> j++, k++"]
    TakeLeft --> MainLoop
    TakeRight --> MainLoop
    MainLoop -- No --> CopyLeft{Remaining <br> in L?}
    CopyLeft -- Yes --> AddLeft["Copy L to arr <br> i++, k++"]
    AddLeft --> CopyLeft
    CopyLeft -- No --> CopyRight{Remaining <br> in R?}
    CopyRight -- Yes --> AddRight["Copy R to arr <br> j++, k++"]
    AddRight --> CopyRight
    CopyRight -- No --> MergeDone[Return from merge]
    MergeDone --> ReturnBase
    ReturnBase --> Output[/Output: Sorted arr/]
    Output --> End([End])
```