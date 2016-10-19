#! /bin/bash


pre_comm=`tail -n 1 ~/.bash_history`

for((i=1;i<10;i))
do
	out=''
	c=0
	comm=`tail -n 1 ~/.bash_history`
	if [ "$pre_comm" == "$comm" ];then
		pre_comm=$comm
	else
		pre_comm=$comm
		for ch in $pre_comm
		do
			if [ "$c" -eq 0 ];then
				out=$ch
				c=1
			else
				out=${out}"_"${ch}
			fi
		done
		echo -e ${out}"\c"
	fi
done

