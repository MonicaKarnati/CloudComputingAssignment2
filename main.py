import os
from collections import Counter
import socket

input_path = 'home/data'
result_path = 'home/output/result.txt'

if os.path.exists(result_path):
  os.remove(result_path)
f = open(result_path, "w")

def read_text_file(file_path):
  with open(file_path, 'r') as f:
    f.read()

def count_words(file_path):
  file = open(file_path, "rt")
  data = file.read()
  words = data.split()
  f.write("Number of words in {} is: {} \n".format(file_path, len(words)))

def total_words():
  total = 0
  for file in os.listdir(input_path):
    if file.endswith(".txt"):
      file_path = f"{input_path}/{file}"
      file = open(file_path, "rt")
      data = file.read()
      total = total + len(data.split())
  f.write('total number of words in both the files is {} \n'.format(total))

def frequency(fname):
  with open(fname) as f:
    return Counter(f.read().lower().split()).most_common(3)

# a.	List name of all the text file at location: /home/data
for file in os.listdir(input_path):
  if file.endswith(".txt"):
    f.write("{}\n".format(file))

#b.	Read the two text files and count total number of words in each text files
for file in os.listdir(input_path):
  if file.endswith(".txt"):
    file_path = f"{input_path}/{file}"
    read_text_file(file_path)
    count_words(file_path)

#c.	Add all the number of words to find the grand total (total number of words in both files)
total_words()

#d.	List the top 3 words with maximum number of counts in IF.txt.  Include the word counts for the top 3 words.
file_path = f"{input_path}/IF.txt"
f.write("Word frequency : {} \n".format(frequency(file_path)))

# e.	Find the IP address of your machine
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
f.write("Your Computer IP Address is: {} \n".format(IPAddr))

# print("[INFO] write complte, file saved to {}".format(result_path))

f.close()

with open(result_path) as f:
  print(f.read())
  f.close()