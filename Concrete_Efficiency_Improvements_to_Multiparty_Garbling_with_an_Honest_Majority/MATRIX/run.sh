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

printf "%s\n" "${parties[@]}" > parties

# execute the program
idx=${1}
cd ../
./BMRPassive ${idx} ${values}
