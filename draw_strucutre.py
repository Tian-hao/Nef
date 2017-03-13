#!/usr/bin/env python
import os

def main():
  infile = open('../analysis2/fitness_residue.txt')
  header = infile.readline().rstrip().rsplit('\t')
  liblist = header[1:]
  fitdict = {}
  for line in infile:
    line = line.rstrip().rsplit('\t')
    pos  = line[0]
    fitdict[pos] = {}
    for i in range(1,5):
     fitdict[pos][header[i]] = float(line[i])
  infile.close()

  resdict = {}
  for pos in fitdict:
    resdict[pos] = fitdict[pos]['KF11']-fitdict[pos]['KF11No']
  for lib in liblist:
    pf = open('fit_'+lib+'.pml','w')
    pf.write('set_color br11= [0.647 , 0.000 , 0.149]\n')
    pf.write('set_color br10= [0.843 , 0.188 , 0.153]\n')
    pf.write('set_color br9 = [0.957 , 0.427 , 0.263]\n')
    pf.write('set_color br8 = [0.992 , 0.682 , 0.380]\n')
    pf.write('set_color br7 = [0.996 , 0.878 , 0.565]\n')
    pf.write('set_color br6 = [1.000 , 1.000 , 0.749]\n')
    pf.write('set_color br5 = [0.878 , 0.953 , 0.973]\n')
    pf.write('set_color br4 = [0.671 , 0.851 , 0.914]\n')
    pf.write('set_color br3 = [0.455 , 0.678 , 0.820]\n')
    pf.write('set_color br2 = [0.271 , 0.459 , 0.706]\n')
    pf.write('set_color br1 = [0.192 , 0.212 , 0.584]\n')
    pf.write('load ../analysis2/Nef_Swiss.pdb, 4EN2\n')
    pf.write('create B, resi 83-206\n')
    pf.write('create N, resi 1-82\n')
    pf.write('bg_color white\n')
    pf.write('hide everything\n')
    pf.write('show surface, B\n')
    pf.write('color grey, B\n')
    pf.write('show sphere, N\n')
    for pos in fitdict:
      pf.write('select P'+pos+', object N and resi '+pos+'\n')
    for pos in fitdict:
      fit = fitdict[pos][lib]
      #fit = resdict[pos]
      norm_fit = (fit+0.8)/(0.6+0.8) * 11
      col = int(round(norm_fit))
      if col < 1: col = 1
      pf.write('color br'+str(col)+', P'+pos+'\n')
    pf.write('zoom complete=1\n')
    pf.write('png ../figures/'+lib+'_fit.png\n')
    pf.close()
    os.system('pymol -c fit_'+lib+'.pml')


if __name__ == '__main__':
  main()
