#num_to_text.py

#works for numbers 1-999. Does not put any spaces in the output

def main(n):

  outputlist=''

  if n > 999 or n < 1:
    print("ERROR: ONLY WORKS FOR NUMBERS 1-999!")

  elif n > 99:
    hundreds=int(str(n)[0])

    if hundreds==1:
      outputlist+=("one")
    elif hundreds==2:
      outputlist+=("two")
    elif hundreds==3:
      outputlist+=("three")
    elif hundreds==4:
      outputlist+=("four")
    elif hundreds==5:
      outputlist+=("five")
    elif hundreds==6:
      outputlist+=("six")
    elif hundreds==7:
      outputlist+=("seven")
    elif hundreds==8:
      outputlist+=("eight")
    elif hundreds==9:
      outputlist+=("nine")

    outputlist+=("hundred")

    tens_ones=int(str(n)[-2:])
    if tens_ones != 0:
      outputlist+=("and")

  if n<1000 and n > 0:

    tens_ones=int(str(n)[-2:])
    if tens_ones > 19:
      tens=int(str(n)[-2])

      if tens==2:
        outputlist+=("twenty")
      elif tens==3:
        outputlist+=("thirty")
      elif tens==4:
        outputlist+=("forty")
      elif tens==5:
        outputlist+=("fifty")
      elif tens==6:
        outputlist+=("sixty")
      elif tens==7:
        outputlist+=("seventy")
      elif tens==8:
        outputlist+=("eighty")
      elif tens==9:
        outputlist+=("ninety")

      ones=int(str(n)[-1])
      if ones==1:
        outputlist+=("one")
      elif ones==2:
        outputlist+=("two")
      elif ones==3:
        outputlist+=("three")
      elif ones==4:
        outputlist+=("four")
      elif ones==5:
        outputlist+=("five")
      elif ones==6:
        outputlist+=("six")
      elif ones==7:
        outputlist+=("seven")
      elif ones==8:
        outputlist+=("eight")
      elif ones==9:
        outputlist+=("nine")

    elif tens_ones < 10:
          
      if tens_ones==1:
        outputlist+=("one")
      elif tens_ones==2:
        outputlist+=("two")
      elif tens_ones==3:
        outputlist+=("three")
      elif tens_ones==4:
        outputlist+=("four")
      elif tens_ones==5:
        outputlist+=("five")
      elif tens_ones==6:
        outputlist+=("six")
      elif tens_ones==7:
        outputlist+=("seven")
      elif tens_ones==8:
        outputlist+=("eight")
      elif tens_ones==9:
        outputlist+=("nine")

    else:
      if tens_ones==10:
        outputlist+=("ten")
      elif tens_ones==11:
        outputlist+=("eleven")
      elif tens_ones==12:
        outputlist+=("twelve")
      elif tens_ones==13:
        outputlist+=("thirteen")
      elif tens_ones==14:
        outputlist+=("fourteen")
      elif tens_ones==15:
        outputlist+=("fifteen")
      elif tens_ones==16:
        outputlist+=("sixteen")
      elif tens_ones==17:
        outputlist+=("seventeen")
      elif tens_ones==18:
        outputlist+=("eighteen")
      elif tens_ones==19:
        outputlist+=("nineteen")


  return outputlist
