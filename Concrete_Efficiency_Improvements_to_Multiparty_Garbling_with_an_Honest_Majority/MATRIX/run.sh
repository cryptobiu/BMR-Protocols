#!/usr/bin/env bash

#!/usr/bin/env bash

# read the arguments without party id

argc=$#
argv=($@)
values=""

for (( j=1; j<argc; j++ )); do
    values+=`echo ${argv[j]}`
    values+=' '
done

# read parties file
parties=()
while IFS= read -r line || [[ -n "${line}" ]]; do
    # cut = split('=)
    l=`echo ${line} | cut -d'=' -f2`
    parties+=(${l})
done < ../parties.conf

for each in "${parties[@]}"
do
  echo "$each"
done

printf "%s\n" "${parties[@]}" > parties

idx=${1}
#addr=${parties[0]}
#
cd ../
#./innerproduct_test -r ${idx} -a ${addr} ${values}

./BMRPassive ${idx} ${values}