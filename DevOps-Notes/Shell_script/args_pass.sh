#echo "Enter arguments to read"
#var = "abcdH"
cat gradle.properties| grep "version="|cut -d= -f1
#echo "user: $1"
#echo "age: $2"
#echo "City: $3"
#echo All Arguments are: "$*"

# for i in "$@"
# do 
# 	echo argeument are:"$i"
# done
