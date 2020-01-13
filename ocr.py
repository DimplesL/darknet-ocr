# -*- coding: UTF-8 -*-
from time import time
from config import scale, maxScale, TEXT_LINE_SCORE
from server.convert import base64_cv2
from server.ocr import text_ocr


def do_ocr(img, config=None, debug=False,
           ifadjustDegree=True, detectAngle=True):
    data = text_ocr(img, scale, maxScale, TEXT_LINE_SCORE)
    return data


def ocr(image, debug=False):
    """工作证识别"""
    image = base64_cv2(image)
    time_take = time()
    res = do_ocr(image, debug=debug)
    return {
        'data': res,
        'waste_time': time() - time_take,
    }


if __name__ == '__main__':
    from fireRest import API, app
    API(ocr)
    app.run(port=20921, host='0.0.0.0', debug=True)
