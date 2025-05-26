loc='#self-defined'

dir_names=("NTF0" "NTF50" "NTF100" "NTF200" "NTF400" "NTF800")

mkdir -p NewResults

for dir_name in "${dir_names[@]}"
do
    mkdir -p "$loc$dir_name"
done

for dir_name in "${dir_names[@]}"
do
    cp -f ${loc}minim.mdp ${loc}at13.dat ${loc}good016.pdb ${loc}gro.py ${loc}  CHrTFModel.mdp ${loc}platforms.py ${loc}top.py ${loc}distance.py ${loc}copy.sh ${loc}test.sh ${loc}${dir_name}/

    sed -i 's/TFDir/'${dir_name}'/g' ${loc}${dir_name}/copy.sh

    if [ "${dir_name}" = "NTF0" ]; then
        t=0
        IndexBead=$((t + 533))
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/test.sh
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/top.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/gro.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/distance.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/platforms.py
        sed -i 's/ILB/'${IndexBead}'/g' ${loc}${dir_name}/at13.dat

    elif [ "${dir_name}" = "NTF50" ]; then
        t=50
        IndexBead=$((t + 533))
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/test.sh
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/top.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/gro.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/distance.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/platforms.py
        sed -i 's/ILB/'${IndexBead}'/g' ${loc}${dir_name}/at13.dat

    elif [ "${dir_name}" = "NTF100" ]; then
        t=100
        IndexBead=$((t + 533))
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/test.sh
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/top.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/gro.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/distance.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/platforms.py
        sed -i 's/ILB/'${IndexBead}'/g' ${loc}${dir_name}/at13.dat

    elif [ "${dir_name}" = "NTF200" ]; then
        t=200
        IndexBead=$((t + 533))
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/test.sh
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/top.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/gro.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/distance.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/platforms.py
        sed -i 's/ILB/'${IndexBead}'/g' ${loc}${dir_name}/at13.dat

    elif [ "${dir_name}" = "NTF400" ]; then
        t=400
        IndexBead=$((t + 533))
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/test.sh
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/top.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/gro.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/distance.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/platforms.py
        sed -i 's/ILB/'${IndexBead}'/g' ${loc}${dir_name}/at13.dat

    elif [ "${dir_name}" = "NTF800" ]; then
        t=800
        IndexBead=$((t + 533))
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/test.sh
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/top.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/gro.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/distance.py
        sed -i 's/ttt/'${t}'/g' ${loc}${dir_name}/platforms.py
        sed -i 's/ILB/'${IndexBead}'/g' ${loc}${dir_name}/at13.dat

    fi

done
