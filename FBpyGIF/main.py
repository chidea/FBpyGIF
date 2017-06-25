if __name__ != '__main__' and __name__ != 'FBpyGIF.main':
  print('This script is intended to be a launcher of library. Thus it doesn\'t export any useful functions')
  exit(1)

from sys import version_info
if version_info.major<3 :
  print('This library is not supported on this version of Python iterpreter. \n\
The minimum supported version is Python 3.2')
  exit(1)

def main(argv=None):
  if argv is None:
    from sys import argv as sysargv
    argv = sysargv[1:]
  from .args import args, argp
  args.args = argp.parse_args(argv)
  if not argv:
    argp.print_help()
    exit()
  
  if args.paths:
    # path scan back to the argument
    from .path import rec_list_dir
    paths = []
    for path in args.paths:
      paths += rec_list_dir(path, not args.no_recurse)
    args.paths = paths
    del paths
    
    # precedecing arguments
    if len(args.paths) == 1 and not args.no_loop:
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
  from . import fb
  fb._verbose = args.verbose
  fb.ready_fb(args.bpp, args.fb, _win = args.win)
  if args.clear != -1:
    fb.fill_scr(args.clear >> 16, args.clear >> 8 & 0xFF, args.clear  & 0xFF)
    exit(0)
  if not args.no_clear:
    fb.black_scr()

  from threading import Event, Timer
  e=Event()
  try:
    print('Press Ctrl+C to stop playing')
    if args.color_test:
      print('Color testing mode')
      fb.fill_scr_ani(event=e, delay=1/30)
    else:
      print('files to play:', args.paths)
      from time import sleep
      from imghdr import what
      # it : iterator
      if args.no_loop:
        if args.shuffle:
          from random import shuffle
          it = shuffle(args.paths)
        else:
          it = args.paths
      else:
        if args.shuffle:
          from shuffle import sfcycle
          it = sfcycle(args.paths)
        else:
          from itertools import cycle
          it = cycle(args.paths)
      for path in it:
        if args.verbose: print('playing : '+path)
        if what(path) == 'gif':
          if args.animate_delay : Timer(args.animate_delay , lambda e:e.set(), [e]).start()
          fb.gif_loop(fb.ready_img(path, False), e, args.animate_loop if args.animate_loop else True, args.preview)
          if args.animate_delay :
            e.wait()
            e.clear()
        else: # static images
          fb.show_img(fb.ready_img(path))
          sleep(args.static_delay)
  except KeyboardInterrupt:
    e.set() # stop gif loop
  finally:
    if not args.no_clear:
      fb.black_scr()
    #e.wait() # wait for thread end
main()
