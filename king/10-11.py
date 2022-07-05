# 고정 위치에 배치 
from tkinter import * 

## 전역 변수 선언 부분 ##
btnList = [None] * 9
fnameList = ["honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif", "nougat.gif", "oreo.gif", "pie.gif"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

## 메인 코드 부분 ##
window = Tk()
window.geometry("210x210")

for i in range(0, 9):
    photoList[i] = PhotoImage(file = "gif/" + fnameList[i])
    btnList[i] = Button(window, image = photoList[i], text = "alice") # 위에 줄의 photoList에 있는 PhotoImage를 가져다가 image 속성에 담는 것.
    
for i in range(0, 3): # for문이 두번 돌기 때문에 2차원 배열.
    for k in range(0, 3):
        btnList[num].place(x = xPos, y = yPos)
        print(xPos, yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70
        
window.mainloop()