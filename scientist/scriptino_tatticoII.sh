#!/bin/bash

while read p; do 
	sed -i 's+https://guide2research.com/u+scientist+g' scientist.txt
done <scientist.txt
