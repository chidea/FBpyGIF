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

def rrec_list_dir(path, rec=True):
  l = []
  for p in path:
    l += rec_list_dir(p)
  return l

def move_file(fpath, trgdir):
  from os import rename
  from os.path import join, basename
  rename(fpath, join(trgdir, basename(fpath)))
