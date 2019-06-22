import os,time


#1.需要备份的文件与目录将被指定在一个列表中，如mac os x或linux下：
source=['/Users/marvinsmac/marvintang/python/backup_test']

#2.备份必须存储在一个主备份目录下：
target_dir = '/Users/marvinsmac/marvintang/python/'

#如果目标目录还不存在，则创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)




#3.备份文件将打包压缩成zip文件
#（第一版）4.zip压缩文件的文件名由当前日期与时间构成
#target = target_dir+os.sep+time.strftime('%Y%m%d%H%M%S')+' .zip'


#(第二版)4.将当前日期做为主备份目录下的子目录名称
today= target_dir+os.sep+time.strftime('%Y%m%d')
#将当前时间做为zip文件的文件名
now=time.strftime('%H%M%S')




#(第二版)zip 文件名称格式
#target=today+os.sep+now+' .zip'


#（第三版）
comment=input('Enter a comment --> ')
if len(comment)==0:
    target=today+os.sep+now+' .zip'
else:
    target=today+os.sep+now+'_'+comment.replace(' ','_')+ '.zip'



#如果目标目录还不存在，则创建
#if not os.path.exists(target_dir):
#    os.mkdir(target_dir)

if not os.path.exists(today):
    os.mkdir(today)    #尝试改成zipfile或tarfile内置的模块来创建归档文件



#5.我们使用zip命令将文件打包成zip格式
zip_command='zip -r {0} {1}'.format(target,' '.join(source))

#运送备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command)==0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

