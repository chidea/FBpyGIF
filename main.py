if __name__ != '__main__':
  print('This script is intended to be a launcher of library. Thus it doesn\'t export any useful functions')
  exit(1)

from sys import version_info
if version_info.major<3 :
  print('This library is not supported on this version of Python iterpreter. \n\
The minimum supported version is Python 3.2')
  exit(1)

from argparse import ArgumentParser

argp = ArgumentParser(description='Plays GIF animation or draws images on to the frame buffer.')
argp.add_argument('paths', nargs='*', type=str, help='Paths to the directory to scan or to the file to read. Empty list makes it fall into color test mode.')
argp.add_argument('-nl', '--no-loop', action='store_true', help='Make entire playlist loop forever.')
argp.add_argument('-nr', '--no-recurse', action='store_true', help='Set to don\'t recurse scan into directories.')
argp.add_argument('-gd', '--global-delay', type=float, help='This time (seconds) applies to entire static/animated images to show for. Animated files will be infinitely looped while this delay. This value will be applied precedece than the \'-sd\' and \'-ad\', \'-al\'.')
argp.add_argument('-sd', '--static-delay', type=float, default=20, help='This time (seconds) applies to only static images to show for.')
argp.add_argument('-al', '--animate-loop', type=int, help='This time (times) applies to only animated images to show for. Animated files will be looped for this count. If it\'s not applied, GIF files will be played for only once of its loop. It precedes \'animate-delay\'.')
argp.add_argument('-ad', '--animate-delay', type=float, help='This time (seconds) applies to only animated images to show for. Animated files will be infinitely looped while this delay. If it\'s not applied, GIF files will be played for only once of its loop.')
argp.add_argument('-fb', type=int, default=0, help='Selects frame buffer driver. /dev/fb[-fb] will be used.')
argp.add_argument('-sf', '--shuffle', action='store_true', help='Shuffle the playlist.')
args = argp.parse_args()

if args.paths:
  
  # path scan back to the argument
  def rec_list_dir(path, rec=True):
    from os.path import isdir, isfile, exists
    from imghdr import what
    rst = []
    if exists(path):
      if isdir(path) and rec:
        from os import listdir
        from os.path import join
        for f in listdir(path):
          rst += rec_list_dir(join(path, f))
      elif isfile(path) and what(path):
        rst += [path]
    return rst

  paths = []
  for path in args.paths:
    paths += rec_list_dir(path, not args.no_recurse)
  args.paths = paths
  del paths
  
  # precedecing arguments
  if len(args) == 1 and not args.no_loop:
    args.animate_delay = args.animate_loop = None
  elif args.global_delay:
    args.animate_delay = args.static_delay = args.global_delay
    args.animate_loop = None
  elif args.animate_loop:
    args.animate_delay = None
  elif args.animate_delay:
    args.animate_loop = None
  else:
    args.animate_loop = 1

# main library loading work
import fb

fb.ready_fb(i=args.fb)
fb.black_scr()

from threading import Event, Timer
e=Event()
try:
  print('Press Ctrl+C to stop playing')
  if not args.paths: # color test mode
    print('Color testing mode')
    fb.fill_scr_ani(event=e, delay=1/30)
  else:
    print('files to play:', args.paths)
    from itertools import cycle
    from time import sleep
    from imghdr import what
    from shuffle import sfcycle
    for path in (args.paths if args.no_loop else cycle(args.paths) if not args.shuffle else sfcycle(args.paths)):
      if what(path) == 'gif':
        if args.animate_delay : Timer(args.animate_delay , lambda e:e.set(), [e]).start()
        fb.gif_loop(fb.ready_img(path), e, args.animate_loop if args.animate_loop else True)
        if args.animate_delay :
          e.wait()
          e.clear()
      else: # static images
        fb.show_img(fb.RGB_to_BGR(fb.ready_img(path).convert('RGB').resize((fb.w,fb.h))))
        sleep(args.static_delay)
except KeyboardInterrupt:
  e.set() # stop gif loop
finally:
  #e.wait() # wait for thread end
  fb.black_scr()
