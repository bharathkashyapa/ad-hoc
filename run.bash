#!/bin/bash

#hostname='localhost'                                  # assume existence for now

# File to transfer

read -p "Go into network part? (y/n) " RESP1
if [ "$RESP1" = "y" ]; then
	python test.py
else
	echo "..."
fi
sleep 2
read -p "Do you want to transfer a file? (y/n) " RESP
if [ "$RESP" = "y" ]; then
    echo -n "Enter the path of file to transfer > "       # -n to disable line carriage at the end

	read filename

	# Username in remote account
	#echo -n "Username: "
	#read usrname

	# Password
	#echo -n "Password: "
	#read -s  password               # -s to disable echo
	#echo

	#scp $filename $usrname@$hostname:~

	addUsr='y'

	while test "$addUsr" != ""
	do
		#echo $addUsr
		echo -n "Hostname: "
		read hostname

		echo -n "Username: "	
		read usrname

		scp $filename $usrname@$hostname:~

		echo -n "Add more users? (y to add, Enter to exit): "
		read addUsr
	done
else
  echo "Bye"
fi

	
