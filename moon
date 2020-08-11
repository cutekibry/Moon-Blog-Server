#!/usr/bin/bash
case "$1" in
	"build" )
		echo Build
		python3 generate.py ~/文档/cutekibry.github.io-source ~/文档/cutekibry.github.io
	;;

	"serve" )
		echo Serve
		cd ~/文档/cutekibry.github.io && python3 -m http.server
	;;

	"loj" )
		if [ "$2" ]
		then
			echo Create LOJ \#$2
			cd ../cutekibry.github.io-source/tools && python3 newloj.py "$2"
		else
			echo Unknown id
		fi
	;;

	* )
		echo Unrecognized argument
	;;
esac