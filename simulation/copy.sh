loc=''  #self-defined

mkdir -p 60 200 400 600 800 940

for i in 60 200 400 600 800 940
do
    cp -f ${loc}minim.mdp ${loc}at13.dat ${loc}good016.pdb ${loc}gro.py ${loc}  CHrTFModel.mdp ${loc}platforms.py ${loc}top.py ${loc}distance.py ${loc}test.sh ${loc}${i}/

	sed -i 's/kbp/'${i}'/g' ${loc}${i}/test.sh
	sed -i 's/kbp/'${i}'/g' ${loc}${i}/distance.py
	sed -i 's/kbp/'${i}'/g' ${loc}${i}/platforms.py

	if [ $i -eq 12 ]; then
	    a=165   
	    b=169
	    let gStart=$a+100
	    let gEnd=$b+100
	    let dStart=$a-1
	    let dEnd=$b-1
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/gro.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/gro.py
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/top.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/top.py
	    sed -i 's/145/'${dStart}'/g' ${loc}${i}/distance.py
	    sed -i 's/185/'${dEnd}'/g' ${loc}${i}/distance.py
	    
	elif [ $i -eq 18 ]; then
	    a=164
	    b=170
	    let gStart=$a+100
	    let gEnd=$b+100
	    let dStart=$a-1
	    let dEnd=$b-1
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/gro.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/gro.py
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/top.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/top.py
	    sed -i 's/145/'${dStart}'/g' ${loc}${i}/distance.py
	    sed -i 's/185/'${dEnd}'/g' ${loc}${i}/distance.py
	
	elif [ $i -eq 24 ]; then
	    a=163
	    b=171
	    let gStart=$a+100
	    let gEnd=$b+100
	    let dStart=$a-1
	    let dEnd=$b-1
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/gro.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/gro.py
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/top.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/top.py
	    sed -i 's/145/'${dStart}'/g' ${loc}${i}/distance.py
	    sed -i 's/185/'${dEnd}'/g' ${loc}${i}/distance.py

	elif [ $i -eq 30 ]; then
	    a=162
	    b=172
	    let gStart=$a+100
	    let gEnd=$b+100
	    let dStart=$a-1
	    let dEnd=$b-1
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/gro.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/gro.py
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/top.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/top.py
	    sed -i 's/145/'${dStart}'/g' ${loc}${i}/distance.py
	    sed -i 's/185/'${dEnd}'/g' ${loc}${i}/distance.py
	    
	elif [ $i -eq 45 ]; then
	    a=159
	    b=175
	    let gStart=$a+100
	    let gEnd=$b+100
	    let dStart=$a-1
	    let dEnd=$b-1
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/gro.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/gro.py
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/top.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/top.py
	    sed -i 's/145/'${dStart}'/g' ${loc}${i}/distance.py
	    sed -i 's/185/'${dEnd}'/g' ${loc}${i}/distance.py
	
	elif [ $i -eq 60 ]; then
	    a=157
	    b=177
	    let gStart=$a+100
	    let gEnd=$b+100
	    let dStart=$a-1
	    let dEnd=$b-1
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/gro.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/gro.py
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/top.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/top.py
	    sed -i 's/145/'${dStart}'/g' ${loc}${i}/distance.py
	    sed -i 's/185/'${dEnd}'/g' ${loc}${i}/distance.py

	elif [ $i -eq 90 ]; then
	    a=152
	    b=182
	    let gStart=$a+100
	    let gEnd=$b+100
	    let dStart=$a-1
	    let dEnd=$b-1
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/gro.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/gro.py
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/top.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/top.py
	    sed -i 's/145/'${dStart}'/g' ${loc}${i}/distance.py
	    sed -i 's/185/'${dEnd}'/g' ${loc}${i}/distance.py
	
	elif [ $i -eq 200 ]; then
	    a=134
	    b=200
	    let gStart=$a+100
	    let gEnd=$b+100
	    let dStart=$a-1
	    let dEnd=$b-1
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/gro.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/gro.py
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/top.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/top.py
	    sed -i 's/145/'${dStart}'/g' ${loc}${i}/distance.py
	    sed -i 's/185/'${dEnd}'/g' ${loc}${i}/distance.py

	elif [ $i -eq 400 ]; then
	    a=100
	    b=234
	    let gStart=$a+100
	    let gEnd=$b+100
	    let dStart=$a-1
	    let dEnd=$b-1
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/gro.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/gro.py
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/top.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/top.py
	    sed -i 's/145/'${dStart}'/g' ${loc}${i}/distance.py
	    sed -i 's/185/'${dEnd}'/g' ${loc}${i}/distance.py
	
	elif [ $i -eq 600 ]; then
	    a=67
	    b=267
	    let gStart=$a+100
	    let gEnd=$b+100
	    let dStart=$a-1
	    let dEnd=$b-1
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/gro.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/gro.py
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/top.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/top.py
	    sed -i 's/145/'${dStart}'/g' ${loc}${i}/distance.py
	    sed -i 's/185/'${dEnd}'/g' ${loc}${i}/distance.py
	    
	elif [ $i -eq 800 ]; then
	    a=34
	    b=300
	    let gStart=$a+100
	    let gEnd=$b+100
	    let dStart=$a-1
	    let dEnd=$b-1
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/gro.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/gro.py
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/top.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/top.py
	    sed -i 's/145/'${dStart}'/g' ${loc}${i}/distance.py
	    sed -i 's/185/'${dEnd}'/g' ${loc}${i}/distance.py
	
	elif [ $i -eq 910 ]; then
	    a=15
	    b=319
	    let gStart=$a+100
	    let gEnd=$b+100
	    let dStart=$a-1
	    let dEnd=$b-1
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/gro.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/gro.py
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/top.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/top.py
	    sed -i 's/145/'${dStart}'/g' ${loc}${i}/distance.py
	    sed -i 's/185/'${dEnd}'/g' ${loc}${i}/distance.py
	    
	elif [ $i -eq 940 ]; then
	    a=10
	    b=324
	    let gStart=$a+100
	    let gEnd=$b+100
	    let dStart=$a-1
	    let dEnd=$b-1
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/gro.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/gro.py
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/top.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/top.py
	    sed -i 's/145/'${dStart}'/g' ${loc}${i}/distance.py
	    sed -i 's/185/'${dEnd}'/g' ${loc}${i}/distance.py
	
	elif [ $i -eq 955 ]; then
	    a=8
	    b=326
	    let gStart=$a+100
	    let gEnd=$b+100
	    let dStart=$a-1
	    let dEnd=$b-1
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/gro.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/gro.py
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/top.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/top.py
	    sed -i 's/145/'${dStart}'/g' ${loc}${i}/distance.py
	    sed -i 's/185/'${dEnd}'/g' ${loc}${i}/distance.py
	    
	elif [ $i -eq 970 ]; then
	    a=5
	    b=329
	    let gStart=$a+100
	    let gEnd=$b+100
	    let dStart=$a-1
	    let dEnd=$b-1
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/gro.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/gro.py
	    sed -i 's/246/'${gStart}'/g' ${loc}${i}/top.py
	    sed -i 's/286/'${gEnd}'/g' ${loc}${i}/top.py
	    sed -i 's/145/'${dStart}'/g' ${loc}${i}/distance.py
	    sed -i 's/185/'${dEnd}'/g' ${loc}${i}/distance.py
	fi
	
	
	cd ${i} 
	sbatch test.sh 
	cd ..

done

