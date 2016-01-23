#-*-coding: utf-8-*-
import cv2.cv as cv
import cv2
import numpy as np
from cv2 import VideoCapture

#--------------------------------------------------------------------
API_KEY = 'adfcb141240655a7f1df49972c38ffe3'
API_SECRET = 'jDfByUXW5cm2HH6_6pRooDQe37t63r4t'

# Import system libraries and define helper functions
# 导入系统库并定义辅助函数
import time
from pprint import pformat
def print_result(hint, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(k): encode(v) for (k, v) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hint
    result = encode(result)
    print '\n'.join(['  ' + i for i in pformat(result, width = 75).split('\n')])

# First import the API class from the SDK
# 首先，导入SDK中的API类
from facepp import API
from facepp import File

api = API(API_KEY, API_SECRET)



#-------------------------------------------------------------------







#cv.NamedWindow("W1", cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow("W1",cv.CV_WINDOW_NORMAL)

cv.ResizeWindow("W1", 600, 600)

    #找到设备对象
capture = cv.CaptureFromCAM(0)


    #检测人脸函数

def repeat(find,one,diff,faceid,sessionid):

    #每次从摄像头获取一张图片
    frame = cv.QueryFrame(capture)

    #获取图片的大小
    image_size = cv.GetSize(frame)
    #print image_size

    greyscale = cv.CreateImage(image_size, 8, 1)#建立一个相同大小的灰度图像

    cv.CvtColor(frame, greyscale, cv.CV_BGR2GRAY)#将获取的彩色图像，转换成灰度图像

    storage = cv.CreateMemStorage(0)#创建一个内存空间，人脸检测是要利用

    cv.EqualizeHist(greyscale, greyscale)#将灰度图像直方图均衡化，貌似可以使灰度图像信息量减少，加快检测速度

    #画图像分割线

   # cv.Line(frame, (210,0),(210,480), (0,255,255),1)
   #  cv.Line(frame, (420,0),(420,480), (0,255,255),1)
   #  cv.Line(frame, (0,160),(640,160), (0,255,255),1)
   #  cv.Line(frame, (0,320),(640,320), (0,255,255),1)
        # detect objects
    cascade = cv.Load('/Applications/MATLAB_R2014b.app/toolbox/vision/visionutilities/classifierdata/cascade/haar/haarcascade_frontalface_alt2.xml')
    #加载Intel公司的训练库

    #检测图片中的人脸，并返回一个包含了人脸信息的对象faces
    faces = cv.HaarDetectObjects(greyscale, cascade, storage, 1.2, 2,
                                 cv.CV_HAAR_DO_CANNY_PRUNING,
                                 (100, 100))

        #获得人脸所在位置的数据
    for (x,y,w,h) , n in faces:
       # print x,y
        cv.Rectangle(frame, (x,y), (x+w,y+h), (0,128,0),2)#在相应位置标识一个矩形 边框属性(0,0,255)红色 20宽度
        print h,w
        if y < 50:
            y = 50
        if x < 50:
            x = 50
        x = cv2.resize(np.asarray(cv.GetMat(frame))[y-50:y+h+50,x-50:x+w+50],(282,282), interpolation=cv2.INTER_LINEAR)
        cv.ShowImage("W1", greyscale)#显示互有边框的图片

        #当视频中没有出现人脸
        if(find == 0 and one ==0):
            cv2.imwrite('findface.jpe',x)
            result = api.detection.detect(img = File(r'findface.jpe'), mode = 'oneface',async = 'true')
            print result['session_id']
            sessionid = result['session_id']
            find = 1

        #当出现人脸,来异步地获取特征
        if(find == 1 and one ==0):
            result = api.info.get_session(session_id = sessionid)
            if(result['status'] == 'INQUEUE'):
                break
            elif(result['status'] == 'SUCC'):
                if(result['result']['face']):
                    one = 1
                    faceid = result['result']['face'][0]['face_id']
                else:
                    find = 0
                    break
            else:
                find = 0
                break
        print one,diff,'zheli'

        #通过特征来比对是否是同一个人
        if(one == 1 and diff ==0):
            print 'kaishi'
            result = api.recognition.verify(person_name = 'wwx',face_id = faceid ,async = 'true')
            print 'end'
            sessionid = result['session_id']
            diff = 1

        #得出结果来判断是一个人
        if(one == 1 and diff == 1):
            result = api.info.get_session(session_id = sessionid)
            if(result['status'] == 'INQUEUE'):
                break
            elif(result['status'] == 'SUCC'):
                 font=cv2.FONT_HERSHEY_SIMPLEX
                 x = cv2.imread('findface.jpe')
                 cv2.putText(x,"is wwx " + str(result['result']['is_same_person']),(100,100), font, 0.5,(0,0,255),2)
                 cv2.imshow('image2',x)
                 find = 0
                 one = 0
                 diff = 0
                 break
            else:
                diff = 0
                find = 0
                one = 0
                break

       # if result['face']:
        #  face_id = result['face'][0]['face_id']
       #   print 'hehehhehe' + face_id

       #   result = api.recognition.verify(person_name = 'wwx',face_id = face_id)


      #    print_result('Recognize result:123123', result)
      #    print '=' * 60
      #    font=cv2.FONT_HERSHEY_SIMPLEX
      #    cv2.putText(x,"is wwx " + str(result['is_same_person']),(100,100), font, 0.5,(0,0,255),2)
       #   cv2.imshow('image2',x)
    cv.ShowImage("W1", frame)
    return (find,one,diff,faceid,sessionid)
#在开始的时候默认值都为0
get = repeat(0,0,0,0,0)
print get
while True:
    get = repeat(get[0],get[1],get[2],get[3],get[4])
    print get
    c = cv.WaitKey(10)
    #ESC键退出程序
    if c == 27:
        #cv2.VideoCapture(0).release()
        cv2.destroyWindow("W1")
        break
    if c == 21:
        break
