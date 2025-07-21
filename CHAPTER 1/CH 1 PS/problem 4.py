import os


directory_path = "/"


contents = os.listdir(directory_path)


print("Contents of the directory:")
for item in contents:
    print(item)

