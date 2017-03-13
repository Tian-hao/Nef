#!/usr/bin/env python
def main():
  infile = open('../analysis2/entropy.txt')
  aacount = 0
  entdict = {}
  for line in infile:
    line = line.rstrip().rsplit()
    if line[1] == '-': continue
    aacount += 1
    entdict[aacount] = [line[1],line[2]]
  infile.close()

  fitfile = open('../analysis2/fitness_residue.txt')
  header = fitfile.readline().rstrip().rsplit('\t')
  resdict = {}
  for line in fitfile:
    line = line.rstrip().rsplit('\t')
    pos  = int(line[0])
    res  = float(line[3])-float(line[4])
    resdict[pos] = str(res)
  fitfile.close()

  outfile = open('../analysis2/cor_ent_res.txt','w')
  outfile.write('Pos\tAA\tEntropy\tResistance\n')
  for pos in entdict:
    if pos > 82: continue
    outfile.write(str(pos)+'\t'+entdict[pos][0]+'\t'+entdict[pos][1]+'\t'+resdict[pos]+'\n')
  outfile.close()

if __name__ == '__main__':
  main()
