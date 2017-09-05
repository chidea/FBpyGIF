from argparse import ArgumentParser

argp = ArgumentParser(description='Plays GIF animation or draws images on to the frame buffer.')
argp.add_argument('paths', nargs='*', type=str, help='Paths to the directory to scan or to the file to read. Empty list makes it fall into color test mode.')
argp.add_argument('-ct', '--color-test', action='store_true', help='Beautiful color testing mode')
argp.add_argument('-nc', '--no-clear', action='store_true', help='Do not clear screen with black on startup and exit.')
argp.add_argument('-nl', '--no-loop', action='store_true', help='Make entire playlist not to loop forever.')
argp.add_argument('-nr', '--no-recurse', action='store_true', help='Set to don\'t recurse scan into directories.')
argp.add_argument('-gd', '--global-delay', type=float, help='This time (seconds) applies to entire static/animated images to show for. Animated files will be infinitely looped while this delay. This value will be applied precedece than the \'-sd\' and \'-ad\', \'-al\'.')
argp.add_argument('-sd', '--static-delay', type=float, default=20, help='This time (seconds) applies to only static images to show for.')
argp.add_argument('-al', '--animate-loop', type=int, help='This time (times) applies to only animated images to show for. Animated files will be looped for this count. If it\'s not applied, GIF files will be played for only once of its loop. It precedes \'animate-delay\'.')
argp.add_argument('-ad', '--animate-delay', type=float, help='This time (seconds) applies to only animated images to show for. Animated files will be infinitely looped while this delay. If it\'s not applied, GIF files will be played for only once of its loop.')
argp.add_argument('-pv', '--preview', action='store_true', help='Freeze on first frame while loading next frames to preview before playing')
argp.add_argument('-fb', type=int, default=0, help='Selects frame buffer driver. /dev/fb[-fb] will be used.')
argp.add_argument('-w', '--win', type=str, help='Virtual window setting. Form should be : x1,y1,x2,y2. x2 and y2 can be \'w\' or \'h\' to replaced with framebuffer width and height')
argp.add_argument('-bpp', type=int, default=None, help='Bit per pixels. Most framebuffer drivers uses 24 for 8 bits on each BGR as default. It tries to update the value and fallback to available driver specified value in case of failure. If nothing\'s provided, it uses current framebuffer setting.\n See framebuffer_depth boot config for details on rpi.')
argp.add_argument('-sf', '--shuffle', action='store_true', help='Shuffle the playlist')
argp.add_argument('-vb', '--verbose', action='store_true', help='Show verbose information')
def hex_int(string):
  try:
    v = int('0x'+string, 16)
    if v <= 0xffffff and v >= 0 :
      return v
    else:
      print(string + " is not in a valid range(0 <= x <= ffffff). Replaced with 0(black).")
  except:
    print(string + " is not a valid hex value(ex. 'FF0000' for red). Replaced with 0(black).")
  return 0
argp.add_argument('-c', '--clear', default=-1, type=hex_int, nargs='?', help='Clear the screen with black by default, or give an RGB code to fill with. ex)FF0000 : pure red, BBBBBB : light grey, FF00FF : fuchsia purple.')
args = argp.parse_args()

if args.win: args.win = tuple(args.win.split(','))
if args.clear is None: args.clear = 0
if __name__ == '__main__':
  # argument test code
  print(args)
  argp.print_help()
elif not args.paths and not args.color_test and args.clear == -1:
  argp.print_help()
