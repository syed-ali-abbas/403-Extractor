#!/bin/bash
inputURLS_Param0=$1
outputURLS_Param1=$2
		#all urls in this file #403 urls in this file
python3 scrapy.py $inputURLS_Param0 $outputURLS_Param1



#temp=$(cat ~/Desktop/Bash-Script/mandatory_scripts/403-URLS-Extractor/test.txt | wc -l)
#echo "$temp"


file='test.txt'
i=1  

while read line; do  
  
#Reading each line  
cd ~/tools/4-ZERO-3/
echo "____________________________________________________"
echo "$line Testing for URL"
echo "____________________________________________________"
./403-bypass.sh -u $line --exploit 
i=$((i+1)) 

done < $file  

