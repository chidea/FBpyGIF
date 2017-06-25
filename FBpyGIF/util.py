from argparse import ArgumentParser

argp = ArgumentParser(description='Utilities for GIF animation display')
cat = argp.add_subparsers(help='Utility tools')
par_cat = cat.add_parser('size_cat', help='Categorize files based on its sizes and move into 3 folders : horizontal, vertical, square')
par_cat.add_argument('cat_paths', nargs='+', type=str, help='Paths to files or folders that contains images')
par_cat.add_argument('-t', '--text', action='store_true', help='Write categorized list into files instead of moving around.')
par_cat.add_argument('-std', action='store_true', help='Write result out to the standard output')
par_cat.add_argument('-ho', '--horizontal', action='store_true', help='Filter out horizontal images only')
par_cat.add_argument('-ve', '--vertical', action='store_true', help='Filter out vertical images only')
par_cat.add_argument('-sq', '--square', action='store_true', help='Filter out square images only')
args = argp.parse_args()

trgdirs = HOR, VER, SQR = 'horizontal', 'vertical', 'square'

if __name__ == '__main__':
  if 'cat_paths' in args:
    #print('image size categorization')
    def on_each_type(do):
      from .path import rrec_list_dir
      from PIL import Image
      for p in rrec_list_dir(args.cat_paths):
        w, h = Image.open(p).size
        t = HOR if w>h else VER if w<h else SQR
        do(p, t)
    is_filter = args.horizontal or args.vertical or args.square
    if args.text or args.std:
      if args.std:
        if is_filter:
          if not args.horizontal : HOR = ''
          if not args.vertical : VER = ''
          if not args.square : SQR = ''
        def std(p, t):
          if t : print(p)
        on_each_type(std)
      else:
        trgdirs = [open(t+'.txt','w') for t in trgdirs]
        HOR, VER, SQR = trgdirs
        if is_filter:
          if not args.horizontal : HOR = None
          if not args.vertical : VER = None
          if not args.square : SQR = None
        def txt(p, t):
          if t : t.write(p+'\n')
        on_each_type(txt)
        for t in trgdirs:
          if t : t.close()
    else:
      rstcnt = {}
      def move_cnt(p, t):
        from .path import move_file
        move_file(p, t)
        rstcnt[t] += 1
      from os.path import isdir
      from os import mkdir
      for t in trgdirs:
        if not isdir(t):mkdir(t)
        rstcnt[t] = 0
      on_each_type(move_cnt)
      for t in trgdirs:
        print(rstcnt[t], 'files have moved into', t)
    exit()
  argp.print_help()
