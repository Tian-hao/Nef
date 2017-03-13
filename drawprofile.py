#!/usr/bin/env python
from math import log
def main():
  infile = open('../analysis2/fitness.txt')
  outfile = open('../analysis2/fitness_residue.txt','w')
  header = infile.readline().rstrip().rsplit('\t')
  outfile.write(header[0]+'\t'+'\t'.join(header[3:])+'\n')
  fitdict = {}
  for line in infile:
    line = line.rstrip().rsplit('\t')
    if int(line[0]) > 9030: continue
    pos = line[2][1:-1]
    if line[2][-1] == '_': continue
    if line[2][0] == line[2][-1]: continue
    if pos not in fitdict:
      fitdict[pos] = {}
      for lib in header[3:]:
        fitdict[pos][lib] = []
    for i,fit in enumerate(line[3:]):
      fit = log(float(fit),10)
      fitdict[pos][header[3:][i]].append(fit)
  for pos in fitdict:
    outfile.write(pos)
    for lib in header[3:]:
      fit = str(sum(fitdict[pos][lib])/len(fitdict[pos][lib]))
      outfile.write('\t'+fit)
    outfile.write('\n')
  infile.close()
  outfile.close()

if __name__ == '__main__':
  main()
