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
    # waitKey()中的参数为int， 代表 毫秒
    # key得到的返回值为ASCII码，键码标请自寻搜索
    

推荐使用：

    if cv2.waitKey(0) == ord('a'):
        do sth...

例子：
    
    key = cv2.waitKey(0) 
    if key == ord("a"):
        #cv2.destroyAllWindows()
        cv2.imwrite(r"img/ikun_0.jpg", img)

* 图片保存


    cv2.imwrite(imgPath/Name, img)




