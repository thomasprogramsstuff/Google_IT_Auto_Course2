#cat syslog.log
#grep ticky syslog.log
#grep "ERROR" syslog.log
#grep "ERROR Tried to add information to closed ticket" syslog.log

#python3 ###opens python shell
#import re
#line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
#re.search(r"ticky: INFO: ([\w ]*) ", line)
#line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
#re.search(r"ticky: ERROR: ([\w ]*) ", line)

#fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
#sorted(fruit.items())

#import operator
#sorted(fruit.items(), key=operator.itemgetter(0))
#sorted(fruit.items(), key=operator.itemgetter(1))
#sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)

#exit() ###exit python shell

#nano user_emails.csv

Full Name, Email Address
Blossom Gill, blossom@abc.edu
Hayes Delgado, nonummy@utnisia.com
Petra Jones, ac@abc.edu
Oleg Noel, noel@liberomauris.ca
Ahmed Miller, ahmed.miller@nequenonquam.co.uk
Macaulay Douglas, mdouglas@abc.edu
Aurora Grant, enim.non@abc.edu
Madison Mcintosh, mcintosh@nisiaenean.net
Montana Powell, montanap@semmagna.org
Rogan Robinson, rr.robinson@abc.edu
Simon Rivera, sri@abc.edu
Benedict Pacheco, bpacheco@abc.edu
Maisie Hendrix, mai.hendrix@abc.edu
Xaviera Gould, xlg@utnisia.net
Oren Rollins, oren@semmagna.com
Flavia Santiago, flavia@utnisia.net
Jackson Owens, jackowens@abc.edu
Britanni Humphrey, britanni@ut.net
Kirk Nixon, kirknixon@abc.edu
Bree Campbell, breee@utnisia.net

#sudo chmod +x csv_to_html.py
#sudo chmod  o+w /var/www/html 
#./csv_to_html.py user_emails.csv /var/www/html/user_emails.html  ####<html-filename> replaced html-filename with user_emails.html
#ls /var/www/html

#### http://35.232.189.189/user_emails.html ####shows file in browser

###trial 1. Not good..
#nano ticky_check.py

#!/usr/bin/env python3
import re
import sys
import csv
import operator
import os

dict_error = {}
dict_per_user = {}
user_count = []

###Opens file; returns data
def open_file(log_file):
  with open(log_file, "r") as file:
    data = file.readlines()
  return data
###Analyzes to see if it is INFO or ERROR and seperates
def create_data(data_input):
  for data_i in data_input:
    patern_error = re.search(r"ticky: ERROR ([\w ]*)", line)
    pattern_user = re.search(r" \(([\w\. ]*)\)", line)
    if pattern_error != None: #Checks that not empty
      if pattern_error.group(1) not in dict_error.keys():
        dict_errors[pattern_error.group(1)]=1
      else:
        dict_errors[pattern_errors.group(1)]+=1
    if pattern_user != None: #Checks that not empty
      if pattern_user.group(1) not in dict_per_user.keys():
        dict_per_user[pattern_user.group(1)]={}
        dict_per_user[pattern_user.group(1)]['INFO']=0
        dict_per_user[pattern_user.group(1)]['ERROR']=0
        if pattern_error != None:
          dict_per_user[pattern_user.group(1)]['ERROR']=1
        else:
          dict_per_user[pattern_user.group(1)]['INFO']=1
      else:
        if pattern_error != None:
          dict_per_user[pattern_user.group(1)]['ERROR']+=1
        else:
          dict_per_user[pattern_user.group(1)]['INFO']+=1
  ### Filter and create file
  error_list = sorted(dict_error.items(), key=operator.itemgetter(1), reverse=True)
  error_list.insert(0, ('Error', 'Count'))
  per_user_list = sorted(dict_per_user.items(), key=operator.itemgetter(0))
  per_user_list.insert(0, ('Username', {'INFO', 'ERROR'}))
  with open("error_message.csv", "w") as file1:
    writer = csv.writer(file1)
    for key, value in error_list:
      writer.writerow([key, value])
  with open("user_statistics.csv", "w") as file2:
    writer = csv.writer(file2)
    for a, key in per_user_list:
      if a != "Username":
        for b, key_ind in key.items():
          if len(user_count) == 2:
            user_count.clear()
          user_count.append(key_ind)
        writer.writerow([a, user_count[0], user_count[1]])
def main():
  log_file = sys.argv[1]
  data_input = open_file(log_file)
  create_data(data_input)

if __name__ == "__main__":
  main()

                          
                          
                          
