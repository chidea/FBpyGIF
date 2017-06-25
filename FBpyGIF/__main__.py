
def main(argv=None):
  print('main called with', argv)
  if argv is None:
    from sys import argv
    argv= argv[1:]
    print('main argv revision with', argv)
  from .main import main as m
  exit(m(argv))
main()
