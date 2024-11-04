# Author: Rodolfo 
# Date: November 4
# Script will exploring read/write files

# begin with a file in append parameter
f = open("About_me.txt", "a")
f.close

# we're adding a new line into our about me
f = open("About_me.txt", "a")
f.write("Perfect Night Out would be having drinks with friends and catching up. \n")
f.close()

