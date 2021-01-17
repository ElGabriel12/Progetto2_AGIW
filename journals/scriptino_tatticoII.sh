#!/bin/bash

while read p; do 
	sed -i 's+https://www.guide2research.com/journal+journals+g' journals.txt
done <journals.txt
