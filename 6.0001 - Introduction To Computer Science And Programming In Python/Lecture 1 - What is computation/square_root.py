from random import *


def psg_merde( start, square ):
  test = start * start
  while ( test - square ) > 0.01 or ( test - square ) < -0.01:
    start = ( start + ( square / start ) ) / 2
    print( 'Trying ' + str( start ) + '...' )
    test = start * start
  return start

def main():
  find = randint(1, 100)
  start = randint(1, 100)
  print( 'Find square root of ' + str( find * find ) + ' start guessing with ' + str( start ) + '...' )
  returned = psg_merde( start, find * find )
  print( 'Found ' + str( returned ) + '.' )


if __name__ == "__main__":
    main()
