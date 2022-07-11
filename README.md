<!-- Intro -->
# **FACE_LOCKER**
> **Lucas Arroyo Blanco**  
> 
> _PatoOsoPatoso_  

&nbsp;

<!-- Index -->
# Table of contents
## &nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;)&nbsp;&nbsp;[Description](#description)
## &nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;)&nbsp;&nbsp;[Requeriments](#requeriments)
## &nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;)&nbsp;&nbsp;[Modifications to be used](#modifications-to-be-used)  

&nbsp;  
&nbsp; 

<!-- Description -->
## **Description**

A face identification software with the ability to take samples of different users from multiple angles and train with that dataset.

* [main.py](main.py) to start the face identification
* [take_samples.py](take_samples.py) to take samples of users from different angles
* [train.py](train.py) to train a model from  the dataset created using [take_samples.py](take_samples.py)

&nbsp;

<!-- Requeriments -->
## **Requeriments**

### _Mandatory_
* OpenCV for python
* A camera plugged into the computer

### _Optional_
* NVIDIA graphics card
* CUDA
* CudNN library
* CMake

The optional requirements improve a lot the performance of the training and of the actual execution of the program.

&nbsp;  

<!-- Modifications -->
## **Modifications to be used**

If you have more than one camera and want to use an other than the default one you have to modify this in order to select that one:  
```python
cap = cv2.VideoCapture(0) # Change the '0' to the device number listed by opencv
```

If you are unable to make the optional requirements I advise you to change a parameter in 2 scripts.
* In both [train.py](train.py) and [main.py](main.py):
  ```python
  boxes = face_recognition.face_locations(rgb, model="cnn")
  ```
  to
  ```python
  boxes = face_recognition.face_locations(rgb, model="hog")
  ```

&nbsp;  
&nbsp;

<!-- Bye bye -->
<img src="https://static.wikia.nocookie.net/horadeaventura/images/c/c2/CaracolRJS.png/revision/latest?cb=20140518032802&path-prefix=es" alt="drawing" style="width:100px;"/>**_bye bye_**