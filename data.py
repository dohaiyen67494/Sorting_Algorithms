import numpy as np
import os

def generate_data():
    N = 1000000
    output_folder = "dataset_sorting"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    dataset_info = []

    # Dãy số thực - tăng dần
    d1 = np.sort(np.random.uniform(-10000.0, 10000.0, N))
    path1 = f"{output_folder}/01_float_asc.txt"
    np.savetxt(path1, d1, fmt='%.4f')
    dataset_info.append(("Dãy 1 (Float, Tăng)", path1, "float"))

    # Dãy số thực - giảm dần
    d2 = np.sort(np.random.uniform(-10000.0, 10000.0, N))[::-1]
    path2 = f"{output_folder}/02_float_desc.txt"
    np.savetxt(path2, d2, fmt='%.4f')
    dataset_info.append(("Dãy 2 (Float, Giảm)", path2, "float"))

    # Dãy số thực - random
    for i in range (3, 6):
        d_random = np.random.uniform(-10000.0, 10000.0, N)
        path = f"{output_folder}/{i:02d}_float_random.txt"
        np.savetxt(path, d_random, fmt='%.4f')
        dataset_info.append((f"Dãy {i} (Float, Random)", path, "float"))
    
    # Dãy số nguyên
    for i in range(6, 11):
        d_int = np.random.randint(-100000, 100000, N) 
        path = f"{output_folder}/{i:02d}_int_random.txt"
        np.savetxt(path, d_int, fmt='%d')
        dataset_info.append((f"Dãy {i} (Int, Random)", path, "int"))
    
    return dataset_info

if __name__ == "__main__":
    generate_data()