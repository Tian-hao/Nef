#!/usr/bin/env python
from math import log
def main():
  ddgfile = open('../analysis2/ddg_predictions1.out')
  header = ddgfile.readline()
  ddgdict = {}
  for line in ddgfile:
    line = line.rstrip().rsplit()
    if len(line) < 2: continue
    mut  = line[1]
    mut  = mut[0] + str(int(mut[1:-1])+5) + mut[-1]
    ddg  = float(line[2])
    if mut not in ddgdict:
      ddgdict[mut] = []
    ddgdict[mut].append(ddg)
  ddgfile.close()
  
  fitfile = open('../analysis2/fitness.txt')
  header = fitfile.readline().rstrip().rsplit('\t')
  resdict = {}
  for line in fitfile:
    line = line.rstrip().rsplit('\t')
    mut  = line[2]
    fit1 = float(line[5])
    fit2 = float(line[6])
    if fit1 < 0.001: fit1 = 0.001
    if fit2 < 0.001: fit2 = 0.001
    fit1 = log(fit1,10)
    fit2 = log(fit2,10)
    res  = float(fit1)-float(fit2)
    if mut not in resdict:
      resdict[mut] = []
    resdict[mut].append(res)
  fitfile.close()

  outfile = open('../analysis2/cor_ddg_res.txt','w')
  outfile.write('mut\tddg\tresistance\n')
  for mut in ddgdict:
    ddgdict[mut] = sum(ddgdict[mut])/len(ddgdict[mut])
    resdict[mut] = sum(resdict[mut])/len(resdict[mut])
    outfile.write(mut+'\t'+str(ddgdict[mut])+'\t'+str(resdict[mut])+'\n')
  outfile.close()


if __name__ == '__main__':
  main()
