from django.shortcuts import render
from .models import Video
from .forms import VideoForm
import tensorflow as tf
import dlib
import cv2
import os
import sys
import numpy as np
from PIL import Image, ImageChops, ImageEnhance
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from django.core.files import File
sys.path.append('../')
from .predict import predict



def hi(request):
    return render(request, 'play/style.html')
def vid(request):
    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    lastvid = Video.objects.last()
    vid = str(lastvid)
    vid = vid.rsplit("/",1)[1]
    main_video = os.path.abspath(vid)
    resp = {}
    resp[1] = predict(r'''main_video''')
#   count = Video.objects.all().count()
    videofile1 = Video.objects.all()



    context = {'videofile': videofile1,
               'count': resp[1]
               }
    return render(request, 'play/vidsplayer.html', context)