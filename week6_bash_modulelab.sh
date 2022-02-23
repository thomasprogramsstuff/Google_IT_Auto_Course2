#cd data
#cat list.txt
#ls
#grep 'jane' ../data/list.txt
#grep ' jane ' ../data/list.txt
#grep " jane " ../data/list.txt | cut -d ' ' -f 1
#grep " jane " ../data/list.txt | cut -d ' ' -f 2
#grep " jane " ../data/list.txt | cut -d ' ' -f 3
#grep " jane " ../data/list.txt | cut -d ' ' -f 1-3
#grep " jane " ../data/list.txt | cut -d ' ' -f 1,3
#test EXPRESSION
#if test -e ~/data/jane_profile_07272018.doc; then echo "File exists"; else echo "File doesn't exist"; fi
#> test.txt ###creates file test.txt
#echo "I am appending text to this test file" >> test.txt
#cat test.txt
#for i in 1 2 3; do echo $i; done
#cd ~/scripts
#nano findJane.sh
##!/bin/bash
#> oldFiles.txt

####findJane.sh
#!/bin/bash
> oldFiles.txt
files=$(grep " jane " ../data/list.txt | cut -d' ' -f3)
for f in $files; do
  if [ -e $HOME$f ]; then
    echo $HOME$f >> oldFiles.txt;
  fi
done
#

#chmod +x findJane.sh
#./findJane.sh
#cat oldFiles.txt
#nano changeJane.py

###changeJane.py
#!/usr/bin/env python3
import sys
import subprocess

f = open(sys.argv[1], "r")
for line in f.readlines():
  old_name = line.strip()
  new_name = old_name.replace("jane", "jdoe")
  subprocess.run(["mv", old_name, new_name])
f.close()

#chmod +x changeJane.py
#./changeJane.py oldFiles.txt
#cd ~/data
#ls
