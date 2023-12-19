import os 
import numpy as np
import matplotlib.pyplot as plt

## code to write xyz file for all the geo opt iterations
main=os.getcwd()

structures = os.listdir(main)
print(structures)
structures=[i for i in structures if i.split('.')[-1] != 'py' and i.split('.')[-1] != 'ipynb' and 
i.split('.')[-1] != 'slurm' and 
i.split('.')[-1] != 'ipynb_checkpoints' and 
i.split('.')[-1] != 'inp']
print(structures)

for i in structures:
    print(i)
    # if i=='Ini_pbed3-dhfsvp':
    for root, dirs, files in os.walk(i, topdown=False):
        print("root",root)
        for name in files:
            if name.endswith('output.out'):
                print(name)
                input_file=f'{main}/{root}/output.out'
                output_file=f'{main}/{root}/Allcoords.xyz'
                final_file=f'{main}/{root}/final.xyz'

                infile=open(input_file)
                outfile=open(output_file,'w+')
                finalfile=open(final_file,'w+')
                atm=[]
                frame=[]
                found_cart=0
                found_dash=0
                count_atm=0

                for line in infile:

                    if found_dash==1 and len(line.split())==0:        
                        found_dash=0
                        found_cart=0
                        frame.append(atm)
                        atm=[]

                    if found_dash==1:
                        atm.append([line.split()[0],line.split()[1],line.split()[2],line.split()[3]])

                    if found_cart==1:
                        found_dash=1

                    if len(line.split())==3:
                        if line.split()[0]=='CARTESIAN' and line.split()[1]=='COORDINATES' and line.split()[2]=='(ANGSTROEM)':
                            found_cart=1
                for i in range(len(frame)):
                    fr_i=frame[i]
                    outfile.write(f'{len(fr_i)}'+'\n')
                    outfile.write('\n')
                    for j in range(len(fr_i)):
                        outfile.write(str(fr_i[j][0])+' '+str(fr_i[j][1])+' '+ str(fr_i[j][2])+' '+str(fr_i[j][3])+'\n')
                    if i==len(frame)-1:
                        fr_i=frame[i]
                        finalfile.write(f'{len(fr_i)}'+'\n')
                        finalfile.write('\n')
                        for j in range(len(fr_i)):
                            finalfile.write(str(fr_i[j][0])+' '+str(fr_i[j][1])+' '+ str(fr_i[j][2])+' '+str(fr_i[j][3])+'\n')

                    

                outfile.close()
                finalfile.close()









