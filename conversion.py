import os  # 导入操作系统模块
import paddle  # 导入 PaddlePaddle
# 导入 PaddleSpeech 的 ASRExecutor 和 TextExecutor 类
from paddlespeech.cli.asr.infer import ASRExecutor
from paddlespeech.cli.text.infer import TextExecutor

input_dir = './input-audio/'  # 输入文件夹路径
output_dir = './output-text/'  # 输出文件夹路径

if not os.path.exists(output_dir):  # 如果输出文件夹不存在
    os.makedirs(output_dir)  # 创建输出文件夹

asr_executor = ASRExecutor()  # 创建 ASRExecutor 类的实例
text_executor = TextExecutor()  # 创建 TextExecutor 类的实例

for filename in os.listdir(input_dir):  # 遍历输入文件夹中的文件
    print("filename: "+filename)

    if filename.endswith('.wav') or filename.endswith('.m4a'):  # 如果文件是 .wav 或 .m4a 文件
        audio_path = os.path.join(input_dir, filename)  # 创建音频文件的完整路径
        name = os.path.splitext(filename)[0]  # 获取文件名（不包括扩展名）
        # 创建输出文件的完整路径（扩展名为 .txt）
        output_path = os.path.join(output_dir, name + '.txt')

        text = asr_executor(audio_file=audio_path,
                            device=paddle.get_device())  # 将音频文件转换为文本
        print("text: "+text)

        result = text_executor(
            text=text, task='punc', model='ernie_linear_p3_wudao', device=paddle.get_device())  # 对文本进行处理

        with open(output_path, 'w', encoding='utf-8') as f:  # 打开输出文件
            f.write(result)  # 将处理后的文本写入输出文件
