import TinhDoTuongDong
import TrichRutDacTrung as ft
import jsonpickle as json
import os
import pandas as pd

# Doc file am thanh test
# Đường dẫn đến thư mục chứa các file
folder_path = 'data test'

# Mở file JSON và đọc nội dung của file
with open('metadata/data.json', 'r') as file:
    json_data = file.read()

# Chuyển đổi nội dung file JSON thành đối tượng Python
clusters = json.loads(json_data)

# Lấy tất cả các file trong thư mục
files = os.listdir(folder_path)
demf = 0
kq = []
label = ["Bồ câu", "Chào mào", "Chìa vôi", "Chích choè", "Bìm bịp", "Cuốc", "Sáo", "Sẻ", "Cu gáy", "Cú", "Hoạ mi", "Không xác định"]
for file in files:
    demf += 1
    loai = "Không xác định"
    if(demf <= 8):
        loai = "Bồ câu"
    elif(demf <= 20):
        loai = "Chào mào"
    elif(demf <= 25):
        loai = "Chìa vôi"
    elif(demf <= 32):
        loai = "Chích choè"
    elif(demf <= 38):
        loai = "Bìm bịp"
    elif(demf <= 45):
        loai = "Cuốc"
    elif(demf <= 52):
        loai = "Sáo"
    elif(demf <= 60):
        loai = "Sẻ"
    elif(demf <= 62):
        loai = "Cu gáy"
    elif(demf <= 65):
        loai = "Cú"
    elif(demf <= 76):
        loai = "Hoạ mi"
    features = ft.features(os.path.join(folder_path, file))
    similarity = TinhDoTuongDong.SimilarityCalculation(clusters=clusters, features=features)
    maxS = 0
    ind = 0
    for i in range(len(similarity)):
        if(similarity[i] > maxS):
            maxS = similarity[i]
            ind = i
    labelC = label[11]
    if(maxS >= 0.5):
        labelC = label[ind]
    kq.append([labelC, loai])

# Xuat ket qua test ra file
df = pd.DataFrame(kq, columns=["Nhãn dự đoán", "Nhãn"])
df.to_csv('metadata/ketQuaTest.csv', index=False, encoding="utf-8")

# In do chinh xac
c = 0
for k in kq:
    if(k[0] == k[1]):
        c += 1
print("Độ chính xác: " , (c/len(kq) * 100) , "%")