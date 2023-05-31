import math
import jsonpickle as json
import TrichRutDacTrung
from Class import Cluster

def SimilarityCalculation(clusters, features):  #features là list các đặc trưng 
    label = ["Bồ câu", "Chào mào", "Chìa vôi", "Chích choè", "Bìm bịp", "Cuốc", "Sáo", "Sẻ", "Cu gáy", "Cú", "Hoạ mi"]
    labelCount = []
    countN = 0
    for i in range(11):
        labelCount.append(0)
    for feature in features:
        dmin = 9999999999999999.9
        tmp = 0
        for c in range(len(clusters)):
            d = euclideanDistance(clusters[c].center, feature)
            if(d < dmin):
                dmin = d
                tmp = c
        count = []
        lb = []
        for i in range(1):
            count.append(9999999999999999.9)
            lb.append("")
        for f in clusters[tmp].features:
            d = euclideanDistance(feature, f.feature)

            # Thêm điều kiện nếu d > ngưỡng thì loại f
            if(d > 5000):
                continue

            for i in range(1):
                if(count[i] > d):
                    count[i] = d
                    lb[i] = f.lable
                    break

        for i in range(1):
            if(lb[i] != ""):
                labelCount[label.index(lb[i])] += 1
                countN += 1
    for i in range(11):
        if(countN != 0):
            labelCount[i] /= countN
    return labelCount
    

def euclideanDistance(feature1, feature2):
    d = 0.0
    for i in range(len(feature1)):
        d += (feature1[i] - feature2[i])**2
    d = math.sqrt(d)
    return d



# # Mở file JSON và đọc nội dung của file
# with open('metadata/data.json', 'r') as file:
#     json_data = file.read()

# # Chuyển đổi nội dung file JSON thành đối tượng Python
# clusters = json.loads(json_data)

# features = TrichRutDacTrung.features("data test/Tieng-bo-cau-430s.wav")
# # print(SimilarityCalculation(clusters=clusters, features=features))
