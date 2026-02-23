# 📊 Sorting Algorithms Benchmark in Python

Dự án này thực hiện đo lường và so sánh hiệu năng thực tế của các thuật toán sắp xếp kinh điển (Quick Sort, Heap Sort, Merge Sort) so với hàm sắp xếp tối ưu của thư viện NumPy (`numpy.sort`). 

Thực nghiệm được tiến hành trên 10 tập dữ liệu khác nhau (số nguyên, số thực, đã sắp xếp, ngẫu nhiên), mỗi tập gồm **1.000.000 phần tử**.

## 💻 Cấu hình phần cứng thử nghiệm
- **Thiết bị:** Laptop Acer Nitro V 15 (ANV15-51)
- **CPU:** Tối ưu cho các tác vụ tính toán đa luồng và đơn luồng.
- **RAM:** Cung cấp băng thông lớn cho việc cấp phát bộ nhớ mảng.

## 📂 Cấu trúc thư mục
- `data.py`: Code tự động sinh 10 tập dữ liệu (mỗi tập 1 triệu phần tử).
- `main_sort.py`: Code chính chứa các thuật toán sắp xếp và tiến hành đo lường thời gian.
- `ket_qua_sap_xep.csv`: File bảng tính lưu trữ số liệu thời gian chạy thực tế.
- `bieu_do_thoi_gian.png`: Biểu đồ trực quan hóa kết quả so sánh.

## 🛠️ Hướng dẫn Cài đặt và Chạy thử nghiệm

**Bước 1: Cài đặt thư viện yêu cầu**
Dự án sử dụng Python 3. Bạn cần cài đặt các thư viện hỗ trợ bằng lệnh sau:
```bash
pip install numpy pandas matplotlib
