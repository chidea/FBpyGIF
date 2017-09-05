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
 - [x] Upload on PyPi to let it be installable with `pip install`.
   - [x] Make installation script
 - [x] Proper animtation time delay on every frames
 - [x] Standard argument style launcher
 - [x] Checking Python version
 - [ ] Add more options to program
   - [x] Shuffling
   - [ ] Picture frame
   - [x] Custom clearing
 - [ ] Layer support
 - [ ] Background loading of next animation file to reduce loading delay between them
 - [ ] Optimize with setting screen to RGB mode by sending mailbox message (RGB_to_BGR function will be unused)
 - [ ] Bugfix with wrong ioctl command. `dmesg` shows `bcm2708_fb soc:fb: Unknown ioctl 0x5401`
 - [ ] Wiki documentation about ioctl and mmap with pure Python.

### Tested on
 - Latest Raspbian on Raspberry pi 2 B+
 - Archlinux (No, not with the ARM version on RPi, but the one on a vagrant VM)
 - Ubuntu Mate Xenial on Odroid C2

### How to install
 - prerequisite for pillow (for fresh raspbian)
```
  sudo apt install libjpeg8-dev libfreetype6-dev libwebp-dev -y
```
 - option1: use pip
```
  sudo apt install python3-pip
  sudo pip3 install fbpygif
```
 - option2: use git and setup.py
```
  sudo apt install git
  git clone https://github.com/chidea/FBpyGIF
  cd FBpyGIF
  sudo python3 setup.py install
```

### How to use
These three are identical.
```
sudo FBpyGIF [directory or file list...]
sudo python3 -m FBpyGIF.main [...]
sudo python3 -m FBpyGIF [...]
```
 - `FBpyGIF --help` to see all commands.
 - Library and script is written for Python >= 3.
 - Writing directly to frame buffer driver needs superuser priviledge.
 - `FBpyGIF -ct` will put you into color test mode. (Aware of hypnotising screen ;) )
 - Utility
   - `python3 -m FBpyGIF.util size_cat ~/pictures` will categorize pictures based on its sizes and move into folders horizontal, vertical, square under the directory you run it.
