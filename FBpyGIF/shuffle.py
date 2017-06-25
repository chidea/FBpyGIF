
def sfcycle(lst, nxt=0):
  from random import shuffle
  while True:
    half=len(lst)//2
    last=lst[-1]
    remain=lst[:-1]
    shuffle(remain)
    lst=remain[:half]+[last]+remain[half:]
    for o in lst:
      yield o
