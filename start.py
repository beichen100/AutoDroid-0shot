# helper file of droidbot
# it parses command arguments and send the options to droidbot
import argparse
from droidbot import input_manager
from droidbot import input_policy
from droidbot import env_manager
from droidbot import DroidBot
from droidbot.droidmaster import DroidMaster


def parse_args():
    """
    parse command line input
    generate options including host name, port number
    """
    parser = argparse.ArgumentParser(description="Start DroidBot to test an Android app.",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-d", action="store", dest="device_serial", required=False,
                        help="The serial number of target device (use `adb devices` to find)")
    parser.add_argument("-a", action="store", dest="apk_path", required=True,
                        help="The file path to target APK")
    parser.add_argument("-o", action="store", dest="output_dir",
                        help="directory of output")
    parser.add_argument("-task", action="store", dest="task", default="mingle around",
                        help="the task to execute, in natural language")

    parser.add_argument("-script", action="store", dest="script_path",
                        help="Use a script to customize input for certain states.")
    parser.add_argument("-count", action="store", dest="count", default=input_manager.DEFAULT_EVENT_COUNT, type=int,
                        help="Number of events to generate in total. Default: %d" % input_manager.DEFAULT_EVENT_COUNT)
    parser.add_argument("-interval", action="store", dest="interval", default=input_manager.DEFAULT_EVENT_INTERVAL,
                        type=int,
                        help="Interval in seconds between each two events. Default: %d" % input_manager.DEFAULT_EVENT_INTERVAL)
    parser.add_argument("-timeout", action="store", dest="timeout", default=input_manager.DEFAULT_TIMEOUT, type=int,
                        help="Timeout in seconds, -1 means unlimited. Default: %d" % input_manager.DEFAULT_TIMEOUT)
    parser.add_argument("-debug", action="store_true", dest="debug_mode",
                        help="Run in debug mode (dump debug messages).")
    parser.add_argument("-keep_app", action="store_true", dest="keep_app",
                        help="Keep the app on the device after testing.")
    parser.add_argument("-keep_env", action="store_true", dest="keep_env",
                        help="Keep the test environment (eg. minicap and accessibility service) after testing.")
    parser.add_argument("-grant_perm", action="store_true", dest="grant_perm",
                        help="Grant all permissions while installing. Useful for Android 6.0+.")
    parser.add_argument("-is_emulator", action="store_true", dest="is_emulator",
                        help="Declare the target device to be an emulator, which would be treated specially by DroidBot.")
    parser.add_argument("-accessibility_auto", action="store_true", dest="enable_accessibility_hard",
                        help="Enable the accessibility service automatically even though it might require device restart\n(can be useful for Android API level < 23).")
    parser.add_argument("-ignore_ad", action="store_true", dest="ignore_ad",
                        help="Ignore Ad views by checking resource_id.")
    options = parser.parse_args()
    # print options
    return options


def main():
    """
    the main function
    it starts a droidbot according to the arguments given in cmd line
    """
    opts = parse_args()
    import os
    if not os.path.exists(opts.apk_path):
        print("APK does not exist.")
        return

    droidbot = DroidBot(
        app_path=opts.apk_path,
        device_serial=opts.device_serial,
        ## task 命令行写死
        ## task=opts.task,
        task = "你是一个有丰富经验的 Android APP 测试工程师，现在我想在一个交友聊天 APP 里完成如下测试任务：第一步，进入 APP 首页后如果界面上弹出需要更新的弹窗，我希望点击弹窗上不更新的按钮；第二步，我想进入 APP 里用户个人信息的展示界面，所以需要点击类似'我的'这种含义的 view，或者其他一些可能会进入用户个人信息展示或设置页面的 view；第三步，我想进入 APP 用户个人信息的具体编辑界面，一般是在上一步点击'我的'view 后进入的个人信息展示界面上点击类似含义是用户名的 view，或者是点击含义是图片的 image view，然后进入到 APP 用户个人信息的具体编辑界面；第四步，我想在 APP 里完成更改用户头像的动作，也就是在个人信息编辑界面更改用户头像时从手机系统相册里选取任意一张图片上传作为新的用户头像，这需要先点击含义是'更改头像'或者'上传头像'的 view，而且很多时候点击一个 image view 就可以，注意，点击的这个 view 后 app 会出现两个类似含义是'拍照'和'从相册选取'的 view。第五步，点击'从相册选取'的 view，接着从手机系统相册里选取任意一张图片上传作为新的用户头像，有时候需要先选中某张照片，需要点击类似check_view的选中框。为了让你更好的理解，我随机选取了一个任意 APP 来完成上面的任务，并以这个 APP 为例子，请你模仿我下面的步骤来测试其他与这个 APP 不同的任意 APP：step1：click view with text '我的';step2: click view with text 'vhnvfgfy ID: 13011803570';step3: click view with text '头像';step4: click view with text '从相册选择'; step4: click view with text 'Pictures'; step5: click view '拍摄于 2023 年 10 月 28 日 下午 6:51:53 的照片'; step6: click view with text '完成'; step7: click view with text '保存';",
        is_emulator=opts.is_emulator,
        output_dir=opts.output_dir,
        env_policy=env_manager.POLICY_NONE,
        policy_name=input_manager.POLICY_TASK,
        script_path=opts.script_path,
        event_interval=opts.interval,
        timeout=opts.timeout,
        event_count=opts.count,
        debug_mode=opts.debug_mode,
        keep_app=opts.keep_app,
        keep_env=opts.keep_env,
        grant_perm=opts.grant_perm,
        enable_accessibility_hard=opts.enable_accessibility_hard,
        ignore_ad=opts.ignore_ad)
    droidbot.start()


if __name__ == "__main__":
    main()
