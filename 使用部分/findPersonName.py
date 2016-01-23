#!/usr/bin/env python2
# -*- coding: utf-8 -
# You need to register your App first, and enter you API key/secret.
# 您需要先注册一个App，并将得到的API key和API secret写在这里。
API_KEY = 'adfcb141240655a7f1df49972c38ffe3'
API_SECRET = 'jDfByUXW5cm2HH6_6pRooDQe37t63r4t'

# Import system libraries and define helper functions
# 导入系统库并定义辅助函数
import time
import cv2
import cv2.cv as cv
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


def repeat():
        x= cv2.imread('1.jpg')
        cv2.imshow('image',x)
        #x = cv2.resize(np.asarray(cv.GetMat(frame))[y:y+h,x:x+w],(282,282), interpolation=cv2.INTER_LINEAR)


api = API(API_KEY, API_SECRET)
#cv.NamedWindow("W1",cv.CV_WINDOW_NORMAL)
#cv.ResizeWindow("W1", 600, 600)
#cv2.destroyAllWindows()
while True:
    cv2.namedWindow("the window")
    x= cv2.imread('1.jpg')
    cv2.imshow('image',x)
    k = cv2.waitKey(0)
   # result = api.recognition.recognize(img = File(r'findface.jpe'), group_name = 'test')
   # print_result('Recognize result:123123', result)
   # print '=' * 60
   # print 'The person with highest confidence:', \
   #     result['face'][0]['candidate'][0]['person_name']