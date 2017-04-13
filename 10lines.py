#转载自:作者：赖勇浩（http://blog.csdn.net/lanphaday）
import sys
from PIL import Image
img=Image.open(sys.argv[1]).convert('YCbCr')
weight,height=img.size
data=img.getdata()
cnt=0
for index,ycbcr in enumerate(data):
    #print(index,ybrbc)
    y,cb,cr=ycbcr
    if 86<=cb<=127 and 130<=cr<=168:
        cnt+=1
print('%s%s不健康图片'%(sys.argv[1],'是' if cnt>weight*height*0.3 else '不是'))

