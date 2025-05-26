#!/bin/bash
#SBATCH -p i64m512u
#SBATCH -J ZTtttKkbp
#SBATCH --nodes=1
#SBATCH --ntasks=30
#SBATCH -o job.%j.out
#SBATCH -e job.%j.err

loc='#self-defined'

python ${loc}top.py

for ((i=1;i<=30;i=i+1))
do
	{
	sed 's/y=1/'y=${i}'/g' ${loc}gro.py > ${loc}gro${i}.py

	python ${loc}gro${i}.py

	grompp_mpi -f ${loc}minim.mdp -c ${loc}${i}.gro -p ${loc}1.top -o ${loc}em${i}.tpr -maxwarn 600
	mdrun_mpi -v -deffnm em${i}

	grompp_mpi -f ${loc}  CHrTFModel.mdp -c ${loc}em${i}.gro -p ${loc}1.top -o ${loc}${i}.tpr -maxwarn 600
	mdrun_mpi -s ${loc}${i}.tpr -x ${loc}${i}.xtc -g ${loc}md${i}.log -plumed ${loc}at13.dat
	echo 0 | trjconv_mpi -s ${loc}${i}.tpr -f ${loc}${i}.xtc -o ${loc}${i}.pdb

	sed 's/fn=1/'fn=${i}'/g' ${loc}platforms.py > ${loc}plat${i}.py
	python ${loc}plat${i}.py
	
	sed 's/fn=1/'fn=${i}'/g' ${loc}distance.py > ${loc}dis${i}.py
	python ${loc}dis${i}.py
	} &
done

wait
