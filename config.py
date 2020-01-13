#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
config
@author: chineseocr
"""
ocrType = 'chinese'
ocrPath = 'models/ocr/{}/ocr.weights'.format(ocrType)
textPath = 'models/text/text.weights'
darkRoot = 'darknet/libdarknet.so'   # darknet
TEXT_LINE_SCORE = 0.7   # text line prob
# scale, maxScale: 这两个参数会对识别效果影响比较大
# 通常越大越好，该值越大则占用内存或者显存资源越大
# 如果资源不够则会报错
scale = 900             # 可动态修改 no care text.cfg height,width
maxScale = 1800
GPU = True              # gpu for darknet  or cpu for opencv.dnn
anchors = '16,11, 16,16, 16,23, 16,33, 16,48, 16,68, 16,97, 16,139, 16,198, 16,283'
