import os

def removeCommentsFromFile(inputFile):

  targetFile = open("test2.py", "w")
  nameOfInputFile = inputFile
  commentIdentifier = "#"
  file = open(inputFile, "r+")

  for line in file:
    commentSection = line.find(commentIdentifier)
    if commentSection >= 0:
      line = line[:commentSection]

    targetFile.write(line + "\n")

  file.close()
  targetFile.close()

  os.remove(inputFile)
  os.renames("test2.py", nameOfInputFile)


removeCommentsFromFile("secondTestCodeComments.py")

