# coding:utf-8
from PIL import Image

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import SGD
from keras.utils import np_utils
from keras.models import load_model
from keras import backend as K

#from chainer import Link, Chain, ChainList
#import chainer.functions as F
#import chainer.links as L

import numpy as np


class Model:
    """
    Modelを管理するクラス
    """
    def __init__(self):
        self.model = None

    def model_train(self):
        # 好きな学習器をだれかここに書いて
        self.model.save("保存するpathを指定")

    # モデルの読み込み
    def read_model(self, model_path):
        self.model = load_model(model_path)

    def otaku_predict(self, image_data):
        result = model.predict(image_data)
        if result == 0:  # オタクの場合
            return True
        return False

def otaku_classifier(file_name):
    # 画像の読み込み
    image = Image.open(file_name)
    model = Model()
    # モデルの読み込みを実行
    model.read_model("モデルへのpath")


    """この辺で画像の前処理をする"""
    

    # 前処理後の画像を引数にpredictを呼び出し
    return model.otaku_predict(image)
    

    
