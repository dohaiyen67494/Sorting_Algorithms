import numpy as np
import pandas as pd
import time
import sys
import matplotlib.pyplot as plt
import random
import glob
import os

sys.setrecursionlimit(10**6)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]

        return quick_sort(less) + equal + quick_sort(greater)
    

def max_heap(arr, n, i):
    biggest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l<n and arr[i] < arr[l]:
        biggest = l
    if r < n and arr[biggest] < arr[r]:
        biggest = r
    if biggest != i:
        arr[i], arr[biggest] = arr[biggest], arr[i]
        max_heap(arr, n, biggest)
def heap_sort(arr):
    n=len(arr)
    for i in range (n//2 - 1, -1, -1):
        max_heap(arr, n, i)
    for i in range (n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heap(arr, i, 0)
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def np_sort(arr):
    return np.sort(arr)

def run_benchmark():
    input_folder = "dataset_sorting"
    
    if not os.path.exists(input_folder):
        print(f"Lỗi: Không tìm thấy thư mục '{input_folder}'. Hãy chạy code tạo dữ liệu trước!")
        return

    file_list = sorted(glob.glob(os.path.join(input_folder, "*.txt")))
    
    if not file_list:
        print("Lỗi: Thư mục rỗng!")
        return

    results = []

    print(f"{'='*80}")
    print(f"{'BẮT ĐẦU CHẠY THỬ NGHIỆM (Benchmark)':^80}")
    print(f"{'='*80}")
    print("Lưu ý: Python thuần chạy rất chậm với 1 triệu phần tử. Vui lòng kiên nhẫn...")

    for filepath in file_list:
        filename = os.path.basename(filepath)
        print(f"\n--> Đang xử lý file: {filename}")

        try:
            original_data = np.loadtxt(filepath)
        except Exception as e:
            print(f"    Lỗi đọc file: {e}")
            continue
        
        row_result = {"Dataset": filename}

        algorithms = [
            ("QuickSort", quick_sort, True),
            ("HeapSort", heap_sort, True),
            ("MergeSort", merge_sort, True),
            ("NumPy Sort", np_sort, False)
        ]

        for alg_name, func, need_list in algorithms:
            print(f"    - Đang chạy {alg_name}...", end="", flush=True)
            
            if need_list:
                data_input = original_data.tolist()
            else:
                data_input = original_data.copy()

            start_time = time.time()
            func(data_input)
            end_time = time.time()
            
            duration_ms = (end_time - start_time) * 1000
            row_result[alg_name] = round(duration_ms, 2)
            print(f" Xong! ({duration_ms:.2f}ms)")

        results.append(row_result)

    df = pd.DataFrame(results)
    
    print("\n" + "="*80)
    print(f"{'KẾT QUẢ THỬ NGHIỆM':^80}")
    print("="*80)
    print(df.to_string(index=False))
    
    df.to_csv("ket_qua_sap_xep.csv", index=False)
    print("\n(Đã lưu bảng kết quả vào file 'ket_qua_sap_xep.csv')")

    df.set_index("Dataset", inplace=True)
    
    ax = df.plot(kind='bar', figsize=(14, 7), width=0.8)
    
    plt.title("So sánh thời gian thực thi các thuật toán sắp xếp (1 triệu phần tử)", fontsize=16)
    plt.ylabel("Thời gian (ms)", fontsize=12)
    plt.xlabel("Bộ dữ liệu", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    plt.savefig("bieu_do_thoi_gian.png")
    print("(Đã lưu biểu đồ vào file 'bieu_do_thoi_gian.png')")
    plt.show()

if __name__ == "__main__":
    run_benchmark()