
from calendar import c
import os, subprocess

directory = "."

for filename in os.listdir(directory):
   if filename.lower().endswith(".heic"):
      print('Converting %s...' % os.path.join(directory, filename))
      subprocess.run(["magick", "%s" % filename, "%s" % (filename[0:-5] + '.jpg')])
      # inputFile = filename
      # outputFile = filename[0:-5] + '.jpg'
      # os.system('cmd /k "magick %s %s"'%(inputFile, outputFile))
      # os.system('cmd /k "echo %s"' %filename )
      continue