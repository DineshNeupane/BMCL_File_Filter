import os
list_of_files = os.listdir('C:\\Users\\Dinesh\\Desktop\\Old')
new_file_path = 'C:\\Users\\Dinesh\\Desktop\\New\\latest.txt'
new_file = open(new_file_path, 'a')
for x in range(1, 366):
    file_name='bmcl'+str(x).zfill(3)
    for each_file in list_of_files:
        if each_file.startswith(file_name):
            path='C:\\Users\\Dinesh\\Desktop\\Old\\'+each_file;
            with open(path, 'r') as f:
                lines = f.readlines()
                for x in range(0, 1440, 60):
                    new_file.write(lines[x])
                new_file.write("\n")
