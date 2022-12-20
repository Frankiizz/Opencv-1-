本章内容: cv2 图片读取，展示， 保存
-----------

环境: 
---

* python 3.9.7

* Opencv

-----------
Opencv安装:
--

终端


    pip install opencv-python

or

* Pycharm 安装

----
图片读取：


    img = cv2.imread(path)

图片展示：

    cv2.imshow(img)

额外的：
* 展示窗停留


    cv2.waitKey(0)

* 展示窗关闭


    key = cv2.waitKey(0) & 0xFF
    if key == 27:
        cv2.destroyAllWindows()

推荐使用：

    if cv2.waitKey(33) == ord('a'):
        do sth...

* 图片保存


    cv2.imwrite(imgPath/Name, img)




