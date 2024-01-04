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

实际上是因为，kk 直播里'我的'这种控件没有 clickable 的属性，它属于 navigateBar view，但是是 onTouch 事件，droidbot 无法找到这种属性，这一点没解决的话就测不了 kk 直播

![20231212174551](https://raw.githubusercontent.com/beichen100/image_host/master/img/20231212174551.png)

最后解决了，发现'我的'这种控件虽然自己和祖宗都没有 clickable，但是祖宗有 longclickable，添加了动作就完事了，但是不知道对其他 APP 合不合理

droidbot -a c:\Users\Administrator\Desktop\YogaNow_1.4.10.apk -keep_app -keep_env -grant_perm -ignore_ad -o c:\Users\Administrator\Desktop\out -task "你是一个有丰富经验的 Android APP 测试工程师，现在我想在一个交友聊天 APP 里完成如下测试任务：第一步，进入 APP 首页后如果界面上弹出需要更新的弹窗，我希望点击弹窗上不更新的按钮；第二步，我想进入 APP 里用户个人信息的展示界面，所以需要点击类似'我的'这种含义的 view，或者其他一些可能会进入用户个人信息展示或设置页面的 view；第三步，我想进入 APP 用户个人信息的具体编辑界面，一般是在上一步点击'我的'view 后进入的个人信息展示界面上点击类似含义是用户名的 view，或者是点击含义是图片的 image view，然后进入到 APP 用户个人信息的具体编辑界面；第四步，我想在 APP 里完成更改用户头像的动作，也就是在个人信息编辑界面更改用户头像时从手机系统相册里选取任意一张图片上传作为新的用户头像，这需要先点击含义是'更改头像'或者'上传头像'的 view，而且很多时候点击一个 image view 就可以，注意，点击的这个 view 后 app 会出现两个类似含义是'拍照'和'从相册选取'的 view。第五步，点击'从相册选取'的 view，接着从手机系统相册里选取任意一张图片上传作为新的用户头像。"

通过以上 prompt 能进入好型 app 里选取头像的页面，但 gpt 无法选取相册图片(有一次又完成了全流程).

![20231210212045](https://raw.githubusercontent.com/beichen100/image_host/master/img/20231210212045.png)

同时效果不稳定，同一个 prompt 有时候不能复现进入的功能

目前 droidbot 显示 view 的时候只能显示出带 text 的 view，但是很多需要点击的 view，如上传头像的 view 没有 text，也就点不到，后续是不是能够加入 resource_id 来显示 view

droidbot -a c:\Users\Administrator\Desktop\aicare.net.cn.goodtype_v1.8.3_2265.com.apk -keep_app -keep_env -grant_perm -ignore_ad -o c:\Users\Administrator\Desktop\out\aicare.net.cn.goodtype_v1.8.3_2265.com -task "你是一个有丰富经验的 Android APP 测试工程师，现在我想在一个交友聊天 APP 里完成如下测试任务：第一步，进入 APP 首页后如果界面上弹出需要更新的弹窗，我希望点击弹窗上不更新的按钮；第二步，我想进入 APP 里用户个人信息的展示界面，所以需要点击类似'我的'这种含义的 view，或者其他一些可能会进入用户个人信息展示或设置页面的 view；第三步，我想进入 APP 用户个人信息的具体编辑界面，一般是在上一步点击'我的'view 后进入的个人信息展示界面上点击类似含义是用户名的 view，或者是点击含义是图片的 image view，然后进入到 APP 用户个人信息的具体编辑界面；第四步，我想在 APP 里完成更改用户头像的动作，也就是在个人信息编辑界面更改用户头像时从手机系统相册里选取任意一张图片上传作为新的用户头像，这需要先点击含义是'更改头像'或者'上传头像'的 view，而且很多时候点击一个 image view 就可以，注意，点击的这个 view 后 app 会出现两个类似含义是'拍照'和'从相册选取'的 view。第五步，点击'从相册选取'的 view，接着从手机系统相册里选取任意一张图片上传作为新的用户头像。为了让你更好的理解，我随机选取了一个任意 APP 来完成上面的任务，并以这个 APP 为例子，请你模仿我下面的步骤来测试其他与这个 APP 不同的任意 APP：step1：click view with text '我的';step2: click view with text 'vhnvfgfy ID: 13011803570';step3: click view with text '头像';step4: click view with text '从相册选择'; step4: click view with text 'Pictures'; step5: click view '拍摄于 2023 年 10 月 28 日 下午 6:51:53 的照片'; step6: click view with text '完成'; step7: click view with text '保存';"

更换 gpt4 后效果变好了，一次调用大概 1500 token，花费 0.04 刀

针对好型 app,使用上述 prompt，顺利完成任务，耗时 5min，11 次回答，10000 token

添加 view 的 resurce-id 和 class 信息给 gpt 后，gpt3.5 的表现还是不稳定，但是 gpt4 效果比较好，YogaNow 和 xiaoyibang 都能顺利到达更换头像那一步

但是在系统相册那选取照片还是有困难，有的 APP 不进入原生的照片界面，自己实现，prompt 还得优化

gpt4 3w token 1 刀

加其他非 头像功能的，只要是 upload 的

        task = "你是一个有丰富经验的 Android APP 测试工程师，现在我想在一个交友聊天 APP 里完成如下测试任务：第一步，进入 APP 后请同意隐私政策，并且如果界面上弹出需要更新的弹窗，我希望点击弹窗上不更新的按钮；第二步，如果APP提示需要登录或者注册，那你就先完成登录或者注册.进入登录界面后，如果有类似同意服务协议或者隐私政策含义的checkbox，你同意就行。完成后使用手机号登录，输入手机号然后点击获取验证码，输完验证码后点击登录就行;第三步，我想进入 APP 里用户个人信息的展示界面，所以需要点击类似'我的'这种含义的 view，或者其他一些可能会进入用户个人信息展示或设置页面的 view；第四步，我想进入 APP 用户个人信息的具体编辑界面，一般是在上一步点击'我的'view 后进入的个人信息展示界面上点击类似含义是用户名的 view，或者是点击含义是图片的 image view，然后进入到 APP 用户个人信息的具体编辑界面；第五步，我想在 APP 里完成更改用户头像的动作，也就是在个人信息编辑界面更改用户头像时从手机系统相册里选取任意一张图片上传作为新的用户头像，这需要先点击含义是'更改头像'或者'上传头像'的 view，而且很多时候点击一个 image view 就可以，注意，点击的这个 view 后 app 会出现两个类似含义是'拍照'和'从相册选取'的 view。第六步，点击'从相册选取'的 view，接着从手机系统相册里选取任意一张图片上传作为新的用户头像，有时候需要先选中某张照片，需要点击类似check_view的选中框。为了让你更好的理解，我随机选取了一个任意 APP 来完成上面的任务，并以这个 APP 为例子，请你模仿我下面的步骤来测试其他与这个 APP 不同的任意 APP：step1：click view with text '我的';step2: click view with text 'vhnvfgfy ID: 13011803570';step3: click view with text '头像';step4: click view with text '从相册选择'; step4: click view with text 'Pictures'; step5: click view '拍摄于 2023 年 10 月 28 日 下午 6:51:53 的照片'; step6: click view with text '完成'; step7: click view with text '保存';",
