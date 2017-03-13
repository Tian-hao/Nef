#!/usr/bin/env python
def main():
  infile = open('../analysis2/fitness.txt')
  header = infile.readline()
  outfile = open('../analysis2/mutlist.txt','w')
  for line in infile:
    line = line.rstrip().rsplit('\t')
    if line[2][-1] == '_': continue
    if line[2][0] == line[2][-1]: continue
    pos = int(line[2][1:-1])-5
    if pos > 75: continue
    if pos < 1: continue
    outfile.write('1\n')
    outfile.write(line[2][0]+' '+str(pos)+' '+line[2][-1]+'\n')
  infile.close()
  outfile.close()

if __name__ == '__main__':
  main()
