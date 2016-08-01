from argparse import ArgumentParser

argp = ArgumentParser(description='Utilities for GIF animation display')
cat = argp.add_subparsers(help='Utility tools')
par_cat = cat.add_parser('size_cat', help='Categorize files based on its sizes and move into 3 folders : horizontal, vertical, square')
par_cat.add_argument('cat_paths', nargs='+', type=str, help='Paths to files or folders that contains images')
args = argp.parse_args()

trgdirs = HOR, VER, SQR = 'horizontal', 'vertical', 'square'

if __name__ == '__main__':
  if 'cat_paths' in args:
    print('image size categorization')
    rstcnt = {}
    from os.path import exists, isdir
    from os import mkdir
    for t in trgdirs:
      if not isdir(t):mkdir(t)
      rstcnt[t] = 0
    from path import rrec_list_dir, move_file
    from PIL import Image
    for p in rrec_list_dir(args.cat_paths):
      w,h = Image.open(p).size
      t = HOR if w>h else VER if w<h else SQR
      move_file(p, t)
      rstcnt[t] += 1
    for t in trgdirs:
      print(rstcnt[t], 'files have moved into', t)
    exit()
  argp.print_help()
