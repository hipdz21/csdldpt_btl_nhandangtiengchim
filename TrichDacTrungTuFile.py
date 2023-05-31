import TrichRutDacTrung as ft
import os
from Class import Feature
import LuuTruDacTrung as luu

# Đường dẫn đến thư mục chứa các file
folder_path = 'data'

# Lấy tất cả các file trong thư mục
files = os.listdir(folder_path)

listFeatures = []
demf = 0

for file in files:
    demf += 1
    loai = "Hoạ mi"
    if(demf <= 40):
        loai = "Bồ câu"
    elif(demf <= 120):
        loai = "Chào mào"
    elif(demf <= 160):
        loai = "Chìa vôi"
    elif(demf <= 215):
        loai = "Chích choè"
    elif(demf <= 240):
        loai = "Bìm bịp"
    elif(demf <= 280):
        loai = "Cuốc"
    elif(demf <= 310):
        loai = "Sáo"
    elif(demf <= 385):
        loai = "Sẻ"
    elif(demf <= 405):
        loai = "Cu gáy"
    elif(demf <= 420):
        loai = "Cú"
    features = ft.features(os.path.join(folder_path, file))
    for feature in features:
        feature = Feature(link=os.path.join(folder_path, file), lable=loai, feature=feature)
        listFeatures.append(feature)


Clusters = luu.ClusterUseKmeans(listFeatures)
# Luu vào file json
luu.save(Clusters)