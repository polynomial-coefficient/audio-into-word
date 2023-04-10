# 音频转文本

## 简介

这个 Python 脚本可以将一个文件夹中的音频文件（.wav 或 .m4a）转换为对应的文本文件（.txt）。

转换过程分为两步：

1. 使用 PaddlePaddle 提供的语音识别模型将音频转换为文本
2. 对文本进行处理（如去除标点符号、繁体转简体等）

## 安装

需要安装以下依赖库：

- paddlepaddle
- paddlespeech
- pytest-runner

如果没有安装 `ffmpeg`，还需要安装该软件以进行音频处理。

可以使用以下命令安装这些依赖库：

```bash
pip install paddlepaddle paddlespeech pytest-runner

# 如果需要安装 ffmpeg
sudo apt install ffmpeg
```

## 使用

1.将要转换的音频文件放入 `input-audio` 文件夹中

2.在终端中进入脚本所在的文件夹

3.运行以下命令：

```bash
python3 conversion.py
```

转换后的文本文件将保存在 `output-text` 文件夹中

## 其他

本脚本使用了 PaddlePaddle 提供的模型.
