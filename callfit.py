#!/usr/bin/env python
import os

def main():
  os.system('cut -f1,2,4,6- ../batch2/MF10_readcount.txt > ../batch2/Nef10_readcount.txt')
  os.system('cut -f1,2,4,6- ../batch2/MF11_readcount.txt > ../batch2/Nef11_readcount.txt')
  infile1 = open('../batch1/mF10.txt')
  infile2 = open('../batch2/Nef10_readcount.txt')
  outfile = open('../data/Nef10_readcount.txt','w')
  freqdict = {}
  liblist,freqdict = read_freq(infile1,freqdict)
  liblist,freqdict = read_freq(infile2,freqdict)
  write_freq(outfile,freqdict,liblist)
  infile1.close()
  infile2.close()
  outfile.close()
  fitfile = open('../data/Nef10_fitness.txt','w')
  write_fit(fitfile,freqdict,liblist)
  fitfile.close()

  infile1 = open('../batch1/mF11.txt')
  infile2 = open('../batch2/Nef11_readcount.txt')
  outfile = open('../data/Nef11_readcount.txt','w')
  freqdict = {}
  liblist,freqdict = read_freq(infile1,freqdict)
  liblist,freqdict = read_freq(infile2,freqdict)
  write_freq(outfile,freqdict,liblist)
  infile1.close()
  infile2.close()
  outfile.close()
  fitfile = open('../data/Nef11_fitness.txt','w')
  write_fit(fitfile,freqdict,liblist)
  fitfile.close()

def write_fit(outfile,freqdict,liblist):
  plasmid_libs = ['P62','P7']
  for lib in liblist:
    if lib in plasmid_libs:
      ref_lib = lib
      break
  outfile.write('Pos\tGenotype\tNef')
  for lib in liblist:
    if lib != ref_lib:
      outfile.write('\t'+lib)
  outfile.write('\n')
  for geno in freqdict:
    if freqdict[geno][ref_lib+'_depth'] < 100000: continue
    ref_freq = float(freqdict[geno][ref_lib])/freqdict[geno][ref_lib+'_depth']
    if ref_freq < 10**-5: continue
    pos = geno[1:-1]
    outfile.write(pos+'\t'+geno+'\t'+freqdict[geno]['nef'])
    for lib in liblist:
      if lib == ref_lib: continue
      if freqdict[geno][lib+'_depth'] == 0: freq = 0
      else: freq = float(freqdict[geno][lib])/freqdict[geno][lib+'_depth']
      fit = freq/ref_freq
      outfile.write('\t'+str(fit))
    outfile.write('\n')

def write_freq(outfile,freqdict,liblist):
  outfile.write('Pos\tGenotypes\tNef')
  for lib in liblist:
    outfile.write('\t'+lib+'\t'+lib+'_WT\t'+lib+'_depth')
  outfile.write('\n')
  for geno in freqdict:
    pos = geno[1:-1]
    outfile.write(pos+'\t'+geno+'\t'+freqdict[geno]['nef'])
    for lib in liblist:
      outfile.write('\t'+str(freqdict[geno][lib])+'\t'+str(freqdict[geno][lib+'_WT'])+'\t'+str(freqdict[geno][lib+'_depth']))
    outfile.write('\n') 
  
def read_freq(infile,freqdict):
  header = infile.readline().rstrip().rsplit('\t')
  liblist = header[3::3]
  for line in infile:
    line = line.rstrip().rsplit('\t')
    geno = line[1]
    if geno not in freqdict: freqdict[geno] = {}
    freqdict[geno]['nef'] = line[2]
    for i,read in enumerate(line[3::3]):
      lib = liblist[i]
      if lib not in freqdict[geno]: 
        freqdict[geno][lib] = 0
	freqdict[geno][lib+'_WT'] = 0
	freqdict[geno][lib+'_depth'] = 0
      freqdict[geno][lib] += int(read)
      freqdict[geno][lib+'_WT'] += int(line[3*i+4])
      freqdict[geno][lib+'_depth'] += int(line[3*i+5])
  return liblist,freqdict   

if __name__=='__main__':
  main()
