# Su dung tkinter tao giao dien ---> 
from tkinter.ttk import *
from tkinter import *
from tkinter import filedialog
import TrichRutDacTrung as ft
import jsonpickle as json
import shutil
import TinhDoTuongDong
import os
import Class
import LuuTruDacTrung

# Mở file JSON và đọc nội dung của file
with open('metadata/data.json', 'r') as file:
    json_data = file.read()

# Chuyển đổi nội dung file JSON thành đối tượng Python
clusters = json.loads(json_data)

def nhanDang():
    global win
    file = filedialog.askopenfilename(filetypes = (("Audio files","*.wav"),("all files","*.*")))
    label = ["Bồ câu", "Chào mào", "Chìa vôi", "Chích choè", "Bìm bịp", "Cuốc", "Sáo", "Sẻ", "Cu gáy", "Cú", "Hoạ mi"]
    if file:
        features = ft.features(file=file)
        doTD = TinhDoTuongDong.SimilarityCalculation(clusters=clusters, features=features)
        doTDMax = 0
        indx = 0
        meg = ''
        for d in range(len(doTD)):
            meg += (label[d]) + ": " + str(round(float(float(doTD[d])*100), 2)) + "%               \n"
            if doTD[d] > doTDMax:
                doTDMax = doTD[d]
                indx = d
        lbl1 = Label(win, text=meg, font=("Arial Bold", 14), anchor="sw", wraplength=400)
        lbl1.place(x=350, y=100)
        lab = '=> Loài chim được xác định: '
        if(doTDMax >= 0.5):
            lab += label[indx]
        else:
            lab += "Không xác định"
        lab += '                          '
        lbl2 = Label(win, text=lab, font=("Arial Bold", 14))
        lbl2.place(x=350, y=400)

def nhanAddData():
    global win1
    def addData(clusters):
        global win1
        file = filedialog.askopenfilename(filetypes = (("Audio files","*.wav"),("all files","*.*")))
        loai = combo.get()
        try:
            if file:
                lbl1 = Label(win1, text="Đang lưu dữ liệu!", font=("Arial Bold", 13))
                lbl1.place(x=300, y=10)
                dst_folder = 'data'
                fileName = os.path.basename(file)
                shutil.move(file, dst_folder)
                linkFile = os.path.join(dst_folder, fileName)
                features = ft.features(linkFile)
                for feature in features:
                    vectorFeature = Class.Feature(link=os.path.join(dst_folder, fileName), lable=loai, feature=feature)
                    clusters = LuuTruDacTrung.AddToCluster(feature=vectorFeature, clusters=clusters)
                LuuTruDacTrung.save(clusters)
                lbl1 = Label(win1, text="Lưu dữ liệu thành công!                                                    ", font=("Arial Bold", 13), fg="green")
                lbl1.place(x=300, y=10)
        except RuntimeError:
            print("Loi! Khong luu duoc Dac trung")
            lbl1 = Label(win1, text="Lỗi! Không thể lưu được dữ liệu. Vui lòng thử lại", font=("Arial Bold", 13), fg="red")
            lbl1.place(x=50, y=10)

    win1 = Toplevel(window)
    win1.title("THÊM DỮ LIỆU")
    win1.geometry('800x600')
    #Thêm label có nội dung Hello, font chữ
    lbl = Label(win1, text="Loài chim", font=("Arial Bold", 16))
    #Xác định vị trí của label
    lbl.place(x=200, y=100)
    combo = Combobox(win1, width=20, height=2)
    combo.place(x=350, y=100)
    combo['value'] = ("Bồ câu", "Chào mào", "Chìa vôi", "Chích choè", "Bìm bịp", "Cuốc", "Sáo", "Sẻ", "Cu gáy", "Cú", "Hoạ mi")
    combo.current(0)
    butAdd = Button(win1, text='Chọn tệp âm thanh', width=20, height=2, command=lambda: addData(clusters))
    butAdd.place(x=340, y=200)
    win1.mainloop()

    
def nhanNhanDang():
    global win
    win = Toplevel(window)
    win.title("NHẬN DẠNG ÂM THANH TIẾNG CHIM")
    win.geometry('800x600')
    butAdd = Button(win, text='Chọn tệp âm thanh', width=20, height=2, command=nhanDang)
    butAdd.place(x=100, y=200)
    win.mainloop()


window = Tk()
window.title("HỆ THỐNG NHẬN DẠNG ÂM THANH TIẾNG CHIM")
window.geometry('800x600')
but1 = Button(window, text='Thêm dữ liệu', command=nhanAddData, width=20, height=2)
but1.place(x=340, y=200)
but2 = Button(window, text='Nhận dạng âm thanh', command=nhanNhanDang, width=20, height=2)
but2.place(x=340, y=300)
window.mainloop()

