import torch
import cv2
import os
from model import File, WModel
torch.hub.load('C:/Users/CecilRiver/.cache/torch/hub/ultralytics_yolov5_master',
               'custom',
               path='C:/GitTest/yolov8-flask-vue-deploy/detection-backend/weights/test.pt',
               source='local')