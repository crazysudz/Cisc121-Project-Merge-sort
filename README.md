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

# Merge Sort Visualizer

**_A Python application for visually interactive algorithm simulation._**  
**_Developed for CISC-121 at Queen's University._**

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/GUI-Gradio-orange?style=for-the-badge&logo=gradio)](https://gradio.app/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Merge%20Sort-blueviolet?style=for-the-badge)](#)

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

I chose **Merge Sort** to implement and visualize. It creates a unique decision tree and effectively demonstrates the **divide and conquer** approach. Additionally, it maintains a time complexity of O(n log n) regardless of the dataset, making it highly efficient.

### The Four Pillars

<details>
<summary><b>1. Decomposition</b></summary>

I broke the Merge Sort algorithm down into distinct smaller steps: the `mergeSort` function (which recursively splits the array) and the `merge` function (which compares and combines the split arrays).

</details>

<details>
<summary><b>2. Pattern Recognition</b></summary>

The algorithm relies on a repeating pattern of finding the middle index, dividing the list until single elements remain, and then comparing elements (L ≤ R) to swap and rebuild the sorted list.

</details>

<details>
<summary><b>3. Abstraction</b></summary>

The visualization abstracts away the low-level memory allocation details. It focuses on showing the user the logical flow: the input, the splitting process, and the final output, discarding unnecessary internal processing details from the visual feed.

</details>

<details>
<summary><b>4. Algorithm Design</b></summary>

The flow is designed as: **Input** (User provides a raw list) → **Processing** (Recursive Divide & Conquer) → **Output** (Sorted List displayed in GUI).

</details>

---

## 📊 Algorithm Flowchart

The following diagram illustrates the logic implemented in the code:

```mermaid
flowchart TD
    Start([Start]) --> Input[/Input: arr, left, right/]
    Input --> MSStart[mergeSort Function]
    MSStart --> CheckBase{left less than right?}
    CheckBase -->|No| ReturnBase[Return - Base Case]
    CheckBase -->|Yes| CalcMid[mid = left + right // 2]
    CalcMid --> RecurseLeft[mergeSort: arr, left, mid]
    RecurseLeft -.Recursive Call.-> MSStart
    RecurseLeft --> RecurseRight[mergeSort: arr, mid+1, right]
    RecurseRight -.Recursive Call.-> MSStart
    RecurseRight --> MergeCall[Call merge Function]
    MergeCall --> CalcSizes[Calculate n1 and n2]
    CalcSizes --> CreateArrays[Create L and R arrays]
    CreateArrays --> InitPointers[Initialize i, j, k]
    InitPointers --> MainLoop{Both arrays have elements?}
    MainLoop -->|Yes| Compare{L[i] ≤ R[j]?}
    Compare -->|Yes| TakeLeft[arr[k] = L[i], increment i and k]
    Compare -->|No| TakeRight[arr[k] = R[j], increment j and k]
    TakeLeft --> MainLoop
    TakeRight --> MainLoop
    MainLoop -->|No| CopyLeft{Elements remaining in L?}
    CopyLeft -->|Yes| AddLeft[Copy L[i] to arr[k]]
    AddLeft --> CopyLeft
    CopyLeft -->|No| CopyRight{Elements remaining in R?}
    CopyRight -->|Yes| AddRight[Copy R[j] to arr[k]]
    AddRight --> CopyRight
    CopyRight -->|No| MergeDone[Return from merge]
    MergeDone --> ReturnBase
    ReturnBase --> Output[/Output: Sorted arr/]
    Output --> End([End])
```

---

## 🎯 Features

- **Interactive Visualization**: Watch the merge sort algorithm step through your data
- **User-Friendly Interface**: Built with Gradio for easy interaction
- **Educational Tool**: Perfect for learning and teaching sorting algorithms

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Gradio**: Web-based GUI framework
- **Hugging Face Spaces**: Deployment platform