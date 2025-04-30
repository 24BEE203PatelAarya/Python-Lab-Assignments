#5.Write a program to copy contents of one file to another.
#  While doing so, replace all lowercase characters into uppercase characters

import os

source_file = 'source.txt'  
destination_file = 'destination.txt'  


if os.path.exists(source_file):
    
    with open(source_file, 'r') as src_file:
        content = src_file.read()      
    
    modified_content = content.upper()  
    
    
    with open(destination_file, 'w') as dest_file:
        dest_file.write(modified_content)  
    
    print(f"Contents of '{source_file}' copied to '{destination_file}' with lowercase replaced by uppercase.")
else:
    print(f"Source file '{source_file}' does not exist.")
