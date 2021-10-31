from PIL import Image,ImageDraw,ImageFont
import os
def read_draw(txtFilePath):
    readTXT= open(txtFilePath,"r")
    topRange=10
    LeftRange=10
    img1=Image.new("RGB",(1500,1500),(230,120,80))
    eimg1=ImageDraw.Draw(img1)
    f1= ImageFont.truetype(font="arial.ttf",size=25,index=0)
    maxLength=0
    for i in readTXT.readlines():
        if(len(i)>maxLength):
            maxLength=len(i)
        eimg1.text((LeftRange,topRange),i,font=f1,width=5)
        if(topRange+ 25 > img1.size[1]):
            LeftRange+=maxLength*10
            topRange=0
        topRange+=25
    img1.save(os.getcwd()+"\\test.png")
    os.startfile(os.getcwd()+"\\test.png")
read_draw("C:\Users\COMPUTER\AppData\Roaming\VisualStudioCode-Projects\Python\test.txt")
