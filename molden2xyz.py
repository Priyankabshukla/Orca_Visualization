import numpy as np
import os


def molden2xyz(inpath,outpath):
    f = open(inpath,'r')
    outfile=open(outpath,'w+')
    found = 0
    pos=[]
    count=0
    big_pos=[]
    for i, lines in enumerate(f):
        if i ==2:
            natoms=int(lines.split()[0])

        if i >=2 and found == 0:
            if len(lines.split())==4:
                pos.append([str(lines.split()[0]),float(lines.split()[1]),float(lines.split()[2]),float(lines.split()[3])])
                count+=1

            if count==natoms:
                big_pos.append(pos)
                count=0
                pos=[]   

            if len(lines.split())==1 and lines.split()[0]=='[GEOCONV]':
                found=1
           
    for i in range(0,len(big_pos)):
        fr_i=big_pos[i]
        outfile.write(str(natoms)+'\n')
        outfile.write('\n')
        for i in range(len(fr_i)):
            outfile.write(str(fr_i[i][0])+' '+ str(fr_i[i][1]) +' ' +str(fr_i[i][2]) + ' ' + str(fr_i[i][3])+'\n')




    outfile.close()   

    
root=os.getcwd()
inpath=root+'/'+'grown_string1_000.xyz'
print(inpath)
outpath=root+'/'+'ase.xyz'

molden2xyz(inpath,outpath)
