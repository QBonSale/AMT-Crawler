"""
Created on Thu Jul 3, 2014

@author: McQB
"""
import re
import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   d = {r'\\n':'',r'\\t':'',r'\\u2013':'-',r'\\u00a0':' ',r'\\u2019':"'",' +':' ',
    r'/mturk/preview\?groupId=':'',
    r'/mturk/notqualified\?hitId=':'',
    r'"/mturk/requestqualification\?qualificationId=([0-9A-Z]*)",':'',
    r'You do not meet this qualification requirement':'',
    r'You meet this qualification requirement':'',
   }

   with open(inputfile) as fin, open(outputfile,'w') as fout:
       for line in fin:
        for key in d:
          line = re.sub(key,d[key],line)
        line = re.sub(r'" *", *','',line)
        line = re.sub(r', *" *"','',line)
        line = re.sub(r'" +','"',line)
        line = re.sub(r'\[ +','[',line)
        fout.write(line)

if __name__ == "__main__":
   main(sys.argv[1:])


