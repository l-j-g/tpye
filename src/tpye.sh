#!/bin/bash
if ! [[ -x "$(command -v python)" ]]
then
	echo 'Error:
		This program runs on Python, but it looks like Python is not installed.
		To install Python, check out https://installpython3.com/' >&2
	exit 1
fi
pip3 install -r requirements.txt
python3 tpye.py $1
