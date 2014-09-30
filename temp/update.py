#coding=utf-8
import os
import fileinput
import re
import time

def get_update_file(folderpath):

    filedict = {}
    allfilelist = []
    for i in  os.listdir(folderpath):
        filedict[i] = []
        for j in fileinput.input(folderpath+i):
            text = re.compile(r'/svn.*', re.I).findall(j)
            if text:
                for m in text:
                    filedict[i].append(m.strip())
                    allfilelist.append(m.strip())

    updatefilelist = []
    repeatfilelist = []
    for i in filedict.keys():
        for j in filedict[i]:
            if allfilelist.count(j) > 1:
                repeatfilelist.append((i, j))
    
    updatefilelist=list(set(allfilelist))
    return {'updatefilelist':updatefilelist,'repeatfilelist':repeatfilelist}


def generate_command(updatefilelist, localprojectpath, logfile):
    
    updateable_filelist = []
    unupdateable_filelist = []
    filelsit_after_convert = []
    command = []

    for i in updatefilelist:
        filelsit_after_convert.append\
            (i.replace('/svn/OnlineShopping', localprojectpath))

    for i in filelsit_after_convert:
        if os.path.exists(os.path.dirname(i)):
            updateable_filelist.append(i)
        else:
            unupdateable_filelist.append(i.replace(localprojectpath,'/svn/OnlineShopping'))
    for i in updateable_filelist:
        command.append('svn update "%s" >>"%s"'%(i, logfile))
    
    return {'command':command,'filelist':unupdateable_filelist}


if __name__ == '__main__':

    ftime = str(time.strftime('%y-%m-%d %H-%M-%S'))    
    folderpath = 'C:/Users/svn/Desktop/自动更新/提交单/'     #提交单路径
    localprojectpath = 'C:/Users/svn/Workspaces/MyEclipse 8.6'  #本地项目路径，最后不要橫杠
    repeatfile = '重复%s.txt'%ftime      #重复文件
    logfile = 'C:/Users/svn/Desktop/自动更新/更新日志%s.txt'%ftime         #输出日志
    unupdateablefile = '不可更新%s.txt'%ftime  #不可更新文件
    
    filelist = get_update_file(folderpath)    
    with open(repeatfile, 'w') as repeat:
        for i in filelist['repeatfilelist']:
            repeat.write(str(i)+'\n')
    generate_command_result = generate_command(filelist['updatefilelist'], localprojectpath, logfile)

    
    with open(unupdateablefile, 'w') as unupdate:
        for i in generate_command_result['filelist']:
            unupdate.write(i+'\n')


    for i in generate_command_result['command']:os.system(i)
    os.system('notepad "%s"'%(repeatfile))
    os.system('notepad "%s"'%(unupdateablefile))
    os.system('notepad "%s"'%(logfile))
