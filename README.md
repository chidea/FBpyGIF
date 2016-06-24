# FBpyGIF
Pure Python implemented Memory-mapped Frame Buffer mainly for GIF animation on Raspberry pi

## Description
#### Problem domain
  Recent Raspberry pi and similar single-board computers which needs efficient way to show image usually uses [fbi](https://www.kraxel.org/blog/linux/fbida/).
  This pack of C libraries and programs are able to show GIF image properly thorugh direct frame buffer, but in lack of function to play GIF animation files.
#### Features
So I decided to make almost pure Python implemented library that is utilizing frame buffer and memory mapping.
The only a thing about 'pure' with this library is that it uses PIL library that is default installed python libarary on official Raspbian to convert image formats into raw BGR(A) and is also providing ways to use imagemagick as decompressor.
#### Note
There are many documents online how to mmap frame buffer with C, but none of similar are with Python, which also has mmap library by default. Actually there aren't so many examples about Python mmap library either. Hope this code helps you to understand how to ioctl and mmap not only frame buffers but also general Linux drivers with pure Python. 

### To-do
 - [ ] Upload on PyPi to let it be installable with `pip install`.
   - [ ] Make installation script
 - [x] Proper animtation time delay on every frames
 - [ ] Optimize with setting screen to RGB mode by sending mailbox message (RGB_to_BGR function will be unused)
 - [ ] Bugfix with wrong ioctl command. `dmesg` shows `bcm2708_fb soc:fb: Unknown ioctl 0x5401`
 - [ ] Wiki documentation about ioctl and mmap with pure Python.

### Tested on
 - Latest Raspbian on Raspberry pi 2 B+
 - Archlinux (No, not with the ARM version on RPi, but the one on a vagrant VM)

### How to use
```
sudo python3 fb.py test.gif
```
 - Script is written for <= Python 3.
 - Writing directly to frame buffer driver needs superuser priviledge.
