# DeepFake Detection

### Problem Statement
<p align="justify">
Significant concerns have arisen due to the rapid progress in generating synthetic images and manipulating them. In addition to the benefits it delivers to society in their daily life and business, these synthetic and manipulated images can be used for malicious and such purposes that can prove to be harmful for the society as it may violate security systems, privacy, and social trust. Due to the technological advancements in the deepfake phenomenon, now people can synthesise and manipulate any kind of videos and images using the data available on the internet which may result in a havoc. Several counter-measures have been introduced to detect such images and videos, however, most of them do not deliver accurate results or target at only certain domains and are ineffective when applied to the deepfakes from another domain or new attacks. As a result, this leads to the feelings of distrust in the users or fake information being spread which may cause a situation of panic and harm the peace of the world.
</p>

### Introduction
<p align="justify">
A light weight Django server which detects whether video is deepfaked buffed or not, using our deep learning model.
Our application let user to simply upload videos which returns results in no time! 🚀
</p>
### Idea behind
<p align="justify">
The deep-fake images have a smoother boundary at the region which is faked or artificially synthesised to make the image a deep-fake, often smoother than the natural image. This key-observation can be used to classify an image as fake or natural. If trained on a well-prepared dataset, the system that is this algorithm combined with the unusual eye-blinking and lip-sync patterns would give a better accuracy and would be able to detect more robust deep-fake videos so as to provide exceptional results. Thus, the frequency domain analysis of the image at the single-pixel level would be a preferred solution.
</p>

### Dependencies / Prerequisites 
- Python
- Django
- Numpy  
- Pandas  
- OpenCV
- Matplotlib 
- Seaborn
- Tensorflow 
- Keras  
- Dlib

### Get started
- Install all the libraries using `pip install -r requirements.txt`.
- Run the Django server `python manage.py runserver`.
- Hurray! 🚀

### Screenshots 


### References
- **Paper:** Deep learning based face liveness detection in videos
- **Paper:** DeepFakes: A New Threat to Face Recognition? Assessment and Detection
- **Paper:** Exposing DeepFake Videos By Detecting Eye Blinking
- **Paper:** A two-track algorithm to detect Deep-Fake images
### Contributors
- <a href="#">Gaurav Singh</a>
- <a href="">Shubhangi Agarwal</a>
- <a href="" >Shubham Tak</a>
- <a href="https://www.github.com/lakshyabatman">Lakshya Khera</a>

