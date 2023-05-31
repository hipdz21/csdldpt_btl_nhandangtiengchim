# csdldpt_btl_nhandangtiengchim
BTL Hệ cơ sở dữ liệu đa phương tiện: Nhận dạng tiếng chim
## Cài thư viện
- Để chạy được chương trình cần cài các thư viện:
  + jsonpickle
  + tkinter
  + pandas
  + sklearn
  + numpy
  + pydub

## Chạy chương trình
- Chạy chương trình: chạy file Home.py
- Chương trình gồm 2 chức năng:
  + Thêm dữ liệu: Chức năng này sẽ thêm dữ liệu vào hệ thống, chọn 1 trong 11 loài chim
  + Nhận dạng tiếng chim: Chức năng này sẽ trích rút đặc trưng âm thanh thành các vector đặc trưng rồi so sánh với các vector trong metadata
- Dữ liệu dùng để dùng cho chức năng thêm, nhận dạng tiếng chim nằm trong folder "data test": bộ dữ liệu này chứa 90 file âm thanh bao gồm 76 file âm thanh loài chim có trong hệ thống, 14 file âm thanh về loài chim không có trong hệ thống
