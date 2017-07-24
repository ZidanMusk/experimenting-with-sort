# Experimenting with SORT
Experimenting with [**sort**](https://github.com/abewley/sort) different classical tracking algorithms for realtime multiple object tracking (MOT).

## Description:
- This is an experiment on [**Oxford Town Centre Dataset**](http://www.robots.ox.ac.uk/~lav/Research/Projects/2009bbenfold_headpose/project.html) to compare between ***kalman filter tracker** (a motion model)* and ***dlib correlation tracker** (an appearance model)* in the domain of realtime tracking of multiple objects (pedestrians) in a video sequence (MOT).
- We used the same data association techniques of [**sort**](https://github.com/abewley/sort).

## Results: 
- Dlib correlation tracker: https://youtu.be/tMuX5TP6uqA
- Kalman tracker: https://youtu.be/SKXk6uB8348
-----------------------------------------------------
### Note:
- The *detector/ground truth* was used only for *~40%* of the time.
- We noticed from the above outputs that *Kalman tracker* is ***more robust in highly occluded scenes.***
- *Kalman tracker* is also about ***10x faster***, and so it is more suitable for realtime MOT.

## Dependencies:
- [`Python 2.7x`](https://www.python.org/download/releases/2.7/)
- [`dlib`](https://pypi.python.org/pypi/dlib)
- [`scikit-learn`](http://scikit-learn.org/stable/)
- [`scikit-image`](http://scikit-image.org/download)
- [`FilterPy`](https://github.com/rlabbe/filterpy)

## Usage:
- To test with dlib tracker *(default is kalman)*:
```
python main.py --dlib
```
- To save frames with tracking output: 
```
python main.py --save
```
- To disable online tracking display:
```
python main.py --NoDisplay
```
