
def main(argv=None):
  if argv == None:
    from sys import argv
    argv = argv[1:]
  from .main import main as m
  m()
