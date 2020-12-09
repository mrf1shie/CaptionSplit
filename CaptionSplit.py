# This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys

while(True):
    fName = input("Enter Input Filename: ")
    try:
        f = open(fName, "r", encoding='utf8',errors= 'ignore')
    except FileNotFoundError: 
        print ("File not found, enter valid file name")
    else:
        break
try:
    fileText = f.read()
except Exception as e:
    print(e)
    print("Could not read file, press enter to exit")
    f.close()
    input()
    sys.exit()

f.close()

try:
    words = fileText.split()
except:
    print("Could not split text, press enter to exit")
    input()
    sys.exit()

 
print (words)

while(True):
    fName = input("Enter Output Filename: ")

    try:
        f = open(fName, "x")
    
    except FileExistsError:
        print("File exists, to overwrite type Y, else type anything else and re-enter file name")
        if (input()=="Y" or input()=='y'):
            f = open(fName,"w")
            break
    except:
        print("Unknown Error, Check you have permission to write the files")
    else:
        break

i = 0
j = 0
for word in words:
    i+=len(word)+1
    if (i>41):
        i = len(word)
        f.write("\n")
        if j == 0:
            j = 1
        else:
            j = 0
            f.write("\n")
        f.write(word)
        f.write(" ")
    elif j == 1 and i>28 and (word[-1]=="." or word[-1]=="!" or word[-1]=="?"):
        i = 0
        j = 0
        f.write(word)
        f.write("\n\n")
    else:
        f.write(word)
        f.write(" ")
f.close()

print ("Finished converting, press enter to quit")
input()