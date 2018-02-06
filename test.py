'''
Author: Steven P Sanderson II, MPH

This script with take a file with a given name from the current working
directory so it is important that the file being written to exists in said
directory.

The file being written to must have a single number in it, I suggest using 0 (zero)

The script will prompt for a number, you can enter any number, negative or positive
they should be integers

The script will add the old number and the new number together and write that out
as a new value.

Version     Date         Comment
0.1         2018-02-05   Initial script creation

0.2         2018-02-06   Added IF...ELSE statement incase there is nothing
                         in the file.
                         Added file close statements
                         Changed name of script

0.3         2018-02-07   Make check to see if file exists, if not then create and add value
                         
'''
import os.path

try:
    with open('write_to_file.txt','r+') as f:
        num_lines = sum(1 for line in open('write_to_file.txt','r'))
        if not (num_lines >= 1):
                new_val = int(input("Enter number: "))
                f.seek(0)
                f.write(str(new_val))
                f.close()
        else:
                old_val = int(f.read())
                value_inc = int(input("Enter number: "))
                value_new = str(old_val + value_inc)
                print("The new value is {}".format(value_new))
                f.seek(0)
                f.write(str(old_val + value_inc))
                f.close()
except FileNotFoundError:
    f = open('write_to_file.txt','w')
    with open('write_to_file.txt','r+') as f:
        new_val = int(input("Enter number: "))
        print("The file '{}' did not exist so it was created and {} was written to it".format('write_to_file.txt', new_val))
        f.seek(0)
        f.write(str(new_val))
        f.close()
