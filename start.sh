#!/bin/bash
# 
# 
# Author: alex
# Created Time: 2019年03月04日 星期一 15时59分39秒

# /ocr: 项目挂载目录
# /images: 图片根目录，根据项目实际挂载，这个目录必须正确设置，否则会出现路径错误
script="ocr.py"
param="-d"
if [ $# = 1 ]; then
    script=$1
fi

if [ "$script" = "bash" ]; then
    param=
else
    script="python3 $script"
fi

sudo docker rm -f ibbd-ocr
sudo docker run --runtime=nvidia -ti "$param" \
    --name=ibbd-ocr \
    -v "$PWD":/ocr \
    -v "$PWD/test":/images \
    -p 20922:20921 \
    -e PYTHONIOENCODING=utf-8 \
    -w /ocr \
    registry.cn-hangzhou.aliyuncs.com/ibbd/ocr:gpu \
    $script
