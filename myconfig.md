安装在本机时，

1. droidbot 是在 D:\python\python.exe 环境下配置的，python 3.7

2. droidbotgpt 在 D:\Anaconda\python.exe 下配置，python 3.9

   ```shell
    D:\Anaconda\python.exe m pip install e .

   ```

对于 kk 直播，prompt 设置为

![20231210111233](https://raw.githubusercontent.com/beichen100/image_host/master/img/20231210111233.png)

点击不到我的，直接跳到直播页面了

问题出在首页里我的无法被点击，gpt 给出了错误的序号

![20231210111346](https://raw.githubusercontent.com/beichen100/image_host/master/img/20231210111346.png)

这一点没解决的话就测不了 kk 直播

droidbot -a c:\Users\Administrator\Desktop\aicare.net.cn.goodtype_v1.8.3_2265.com.apk -keep_app -keep_env -grant_perm -ignore_ad -o c:\Users\Administrator\Desktop\out -task "你是一个有丰富经验的 Android APP 测试工程师，现在我想在一个交友聊天 APP 里完成如下测试任务：第一步，进入 APP 首页后如果界面上弹出需要更新的弹窗，我希望点击弹窗上不更新的按钮；第二步，我想进入 APP 里用户个人信息的展示界面，所以需要点击类似'我的'这种含义的 view，或者其他一些可能会进入用户个人信息展示或设置页面的 view；第三步，我想进入 APP 用户个人信息的具体编辑界面，一般是在上一步点击'我的'view 后进入的个人信息展示界面上点击类似含义是用户名的 view，或者是点击含义是图片的 image view，然后进入到 APP 用户个人信息的具体编辑界面；第四步，我想在 APP 里完成更改用户头像的动作，也就是在个人信息编辑界面更改用户头像时从手机系统相册里选取任意一张图片上传作为新的用户头像，这需要先点击含义是'更改头像'或者'上传头像'的 view，而且很多时候点击一个 image view 就可以，注意，点击的这个 view 后 app 一定会出现两个类似含义是'拍照'和'从相册选取'的 view，如果点击后没有出现这两个 view，那说明需要重新返回上一步，再进行类似操作。第五步，点击'从相册选取'的 view，接着从手机系统相册里选取任意一张图片上传作为新的用户头像。"

通过以上 prompt 能进入好型 app 里选取头像的页面，但 gpt 无法选取相册图片(有一次又完成了全流程).

![20231210212045](https://raw.githubusercontent.com/beichen100/image_host/master/img/20231210212045.png)

同时效果不稳定，同一个 prompt 有时候不能复现进入的功能

目前 droidbot 显示 view 的时候只能显示出带 text 的 view，但是很多需要点击的 view，如上传头像的 view 没有 text，也就点不到，后续是不是能够加入 resource_id 来显示 view
