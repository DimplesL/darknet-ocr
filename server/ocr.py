# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2020年01月13日 星期一 10时45分29秒
from PIL import Image
from dnn.ocr import predict_darknet as ocrModel
from .utils import detect_lines, rotate_cut_img


def text_ocr(img, scale, maxScale, TEXT_LINE_SCORE):
    boxes, scores = detect_lines(img, scale=scale, maxScale=maxScale)
    result = []
    if len(boxes) == 0:
        return result

    im = Image.fromarray(img)
    for i, box in enumerate(boxes):
        if scores[i] < TEXT_LINE_SCORE:
            continue
        tmpImg = rotate_cut_img(im, box, leftAdjust=0.01, rightAdjust=0.01)
        text = ocrModel(tmpImg)
        if len(text) == 0:
            continue
        result.append({'text': text, 'box': [int(x) for x in box],
                       'prob': round(float(scores[i]), 2)})
    result = sorted(result, key=lambda x: sum(x['box'][1::2]))
    return result
