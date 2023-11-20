![DroidBot-GPT demo](droidbot/resources/dummy_documents/DroidBot-GPT-demo.gif)

# DroidBot-GPT

## About

DroidBot-GPT is a GPT-powered GUI task automator for Android.
It can control an app automatically based on a natural language task description.

It is built upon [DroidBot](https://github.com/honeynet/droidbot) with [ChatGPT](https://chat.openai.com/)-style APIs.

A more advanced version can be found in [AutoDroid](https://github.com/MobileLLM/AutoDroid).

Technical report:

DroidBot-GPT: [Hao Wen, Hongming Wang, Jiaxuan Liu, Yuanchun Li. "DroidBot-GPT: GPT-powered UI Automation for Android"](https://arxiv.org/abs/2304.07061)


## How to install

Make sure you have:

1. `Python` (both 2 and 3 are supported)
2. `Java`
3. `Android SDK`
4. Added `platform_tools` directory in Android SDK to `PATH`

Then clone this repo and install with `pip`:

```shell
git clone https://github.com/honeynet/droidbot.git
cd droidbot/
pip install -e .
```

If successfully installed, you should be able to execute `droidbot -h`.

## How to use

1. Prepare:

    + An app to use. Download the `.apk` file to your host machine.
    + A device or an emulator connected to your host machine via `adb`.

2. Start DroidBot:

    ```
    droidbot -a <path_to_apk> -o output_dir -task <your_task>
    ```
    That's it! The options are mostly the same as [DroidBot](https://github.com/honeynet/droidbot) except for the new `-task` option, where you can specify any task you want DroidBot-GPT to complete. For example,

    - Create a contact named Yuanchun with phone number 1234567.
    - Book a table for 4 people on Saterday.
    - Send a message to OpenAI to open their AI.
    - ...

Note that DroidBot-GPT is currently for research purpose only. It may perform unintended actions. Please use at your own risk.

Enjoy!

