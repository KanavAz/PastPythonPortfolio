#Kanav Azad
#11/05/2023
#Purpose: using files to produce a program

def frequency(lines):
  data = {}

  punctuation = ("''", "!", "()" "-", "[]", "{}", ";", ":", ".", "/", "?", "%", "&", "*", "_", "\"")
  
  for line in lines:
    
    for c in punctuation:
      line = line.replace(c, " ")

    words = line.split()

    for word in words:
      lim = word.lower()

      if lim in data:
        data[lim] += 1
        
      else:
        data[lim] = 1

  return data


def display(data):

  for key, value in sorted(data.items()):
    print(key + ": " + str(value))

def main():

  chooseFile = input("Enter which file you would like to process - writing.txt, major.txt, or alternative.txt: ")
  chooseFile = chooseFile.lower()
  
  try:
    with open(chooseFile) as file:
      lines = file.readlines()
  except FileNotFoundError:
    print("File not found.")
    quit()

  data = frequency(lines)
  print("\n")
  display(data)

main()