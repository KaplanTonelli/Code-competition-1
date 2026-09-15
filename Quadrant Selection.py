"""
Code for the Quadrant Selection code problem
Kaplan Tonelli - September 2026
"""

def main() -> None:

  # input
  x:int=int(input(""))
  y:int=int(input(""))

  # processing
  if x>0 and y>0:
    print("1")
  elif x>0 and y<0:
    print("4")
  elif x<0 and y>0:
    print("2")
  elif x<0 and y<0:
    print("3")
  
  # output


if __name__ == "__main__":
  main()
    
