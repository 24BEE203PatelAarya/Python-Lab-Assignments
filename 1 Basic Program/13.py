#13. Convert bytes into KB, MB and GB.

bytes = int(input("Enter bytes: "))  

KB = 1024
MB = KB * 1024
GB = MB * 1024


kb = bytes / KB
mb = bytes / MB
gb = bytes / GB


print(f"{bytes} bytes = {kb} KB")
print(f"{bytes} bytes = {mb} MB")
print(f"{bytes} bytes = {gb} GB")
