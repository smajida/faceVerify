# faceVerify
## verify the face 就是简单地识别一个人，判断是不是你这个人，比如在这里我预设的就是判断是不是我。
## 这个项目实现了一个类似Windows Hello的功能
## 首先是利用 open cv＋python ，打开摄像头，定期获得你头部的截图，从而获得你的脸的训练集，你也可以在生成之后手动删掉一些你觉得相似的图片，比如你觉得你脸没有变化的图。
## 之后是利用 opencv ＋ python ＋ face++sdk 来开发类似Windows Hello。类似上一步，这里用到的一个技巧是因为是向网上的api传送数据，于是为了让摄像头拍出来的流畅（类似你的主线程的GUI是流畅的），我才用的技巧是只获得一张脸，然后调用异步函数，通过key来获得最终结果再展示出来。这来保证流程度。。
## ![](https://raw.githubusercontent.com/wwxFromTju/faceVerify/master/image1.png)
## ![](https://raw.githubusercontent.com/wwxFromTju/faceVerify/master/image2.png)
## ![](https://raw.githubusercontent.com/wwxFromTju/faceVerify/master/image3.png)


