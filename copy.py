import os
src_path=r'D:\123\1'
target_path=r'D:\123\2'

def copy(src,target):
    if os.path.isdir(src) and os.path.isdir(target):
        filelist=os.listdir(src)
        for file in filelist:
             path=os.path.join(src,file)
             if os.path.isdir(path):         #判断是否为文件夹
                 target1=os.path.join(target,file)
                 os.mkdir(target1)    #在目标文件下在创建一个文件夹

                 copy(path,target1)
             else:
                 with open(path, 'rb') as rstream:
                     container = rstream.read()
                     path1 = os.path.join(target, file)
                     with open(path1, 'wb') as wstream:
                         wstream.write(container)
        else:
            print('复制完毕!')
copy(src_path, target_path)
