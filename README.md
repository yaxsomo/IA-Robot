# IA-Robot

## Environment installation
The conda environement management is used. You can install it with this installation procedure or you can do the same with the original Python3 CLI.

- `conda create -n ia-robot python=3.9`
- `conda activate ia-robot`
- `pip3 install -r requirements.txt`

The files `yolov.weights` and `yolov3.cfg` are used to define the network (they are located in `src/cnf`).

We use the tiny version of the layer, it's based on a 200 ish layers.

You can download it from this link : https://pjreddie.com/darknet/yolo/ 

## Getting started

`python3 { x }`

## Caution

The current implementation is working but we have performance issue.

It's using CPU so there is no computational acceleration and the current network is having trouble for working under a Raspberry-PI computer.
