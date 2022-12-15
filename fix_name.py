import os

root_path = './AI_img/'
file_name = os.listdir(root_path)

for f in file_name:
    new_f = f.split('.')[0]
    new_f = new_f.split('-')
    new_f[2] = new_f[2].replace('(', '').replace(')', '').zfill(3)

    os.rename(root_path+f, root_path+'-'.join(new_f)+'.png')
