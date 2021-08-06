import os.path
import re

from pymysql import *
import json


global result1


def connectDB():
    db = connect( host ='127.0.0.1',port=3306,user ='root',password ='lulibo1201',db='django_vue_elementui')
    return db
db = connectDB()


filesDir = 'E:\\卢立波\\基因组\\data\\Gm12878\\negative'
fileNameList = os.listdir(filesDir)

rules = re.compile(r'(.*?)_shuffle.fasta')
cursor = db.cursor()
i=0
for filename in fileNameList:
    print("旧的名字是:\t"+filename)
    print("开始截取！")
    newFilename = re.findall(rules, str(filename))[0]
    print("新名字是:\t" + newFilename)
    #cursor.execute("""INSERT INTO browse(id,factor,cell_line,ucsc,lab)
    #VALUES (i,newFilename, '3','4','5')""")

    keyword1 = "GM12878"
    keyword2 = newFilename
    a = open("E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", "r", encoding='UTF-8')  # 注意此处的转义字符
    count = len(open(r"E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", 'r',
                     encoding='UTF-8').readlines())  # 使用len+readlines读取行数
    k = 0
    while k < count:  # 使用循环遍历所有行，逐行判断，只要有关键字，就存到新文件
        line = a.readline()
        if keyword1  in line and keyword2 in line:  # 此处注意代码缩进
            result = line.split("	")
            #print("结果："+result[4][1])
            j=0
            flag=0
            while j<len(result[5]):
                if(result[5][j]=='l' and result[5][j+1]=='a' and result[5][j+2]=='b'):
                    j=j+4
                    result1=''
                    while result[5][j]!=';':
                        result1=result1+result[5][j]
                        j=j+1
                    flag=1
                    if flag==1:
                        print("!"+result1)
                        break
                j=j+1
            cursor.execute("INSERT INTO browse_information(id,factor,cell_line,ucsc,lab) \
                       VALUES ('%d', '%s',  '%s',  '%s',  '%s')" % \
                           (i, newFilename, 'GM12878', result[3], result1))
            result1=''
            break
        k += 1
    db.commit()
    i=i+1
    print("\n")




filesDir = 'E:\\卢立波\\基因组\\data\\Gm12878\\positive'
fileNameList = os.listdir(filesDir)

rules = re.compile(r'(.*?).fasta')
cursor = db.cursor()
for filename in fileNameList:
    print("旧的名字是:\t"+filename)
    print("开始截取！")
    newFilename = re.findall(rules, str(filename))[0]
    print("新名字是:\t" + newFilename)
    #cursor.execute("""INSERT INTO browse(id,factor,cell_line,ucsc,lab)
    #VALUES (i,newFilename, '3','4','5')""")

    keyword1 = "GM12878"
    keyword2 = newFilename
    a = open("E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", "r", encoding='UTF-8')  # 注意此处的转义字符
    count = len(open(r"E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", 'r',
                     encoding='UTF-8').readlines())  # 使用len+readlines读取行数
    k = 0
    while k < count:  # 使用循环遍历所有行，逐行判断，只要有关键字，就存到新文件
        line = a.readline()
        if keyword1  in line and keyword2 in line:  # 此处注意代码缩进
            result = line.split("	")
            #print("结果："+result[4][1])
            j=0
            flag=0
            while j<len(result[5]):
                if(result[5][j]=='l' and result[5][j+1]=='a' and result[5][j+2]=='b'):
                    j=j+4
                    result1=''
                    while result[5][j]!=';':
                        result1=result1+result[5][j]
                        j=j+1
                    flag=1
                    if flag==1:
                        break
                j=j+1
            cursor.execute("INSERT INTO browse_information(id,factor,cell_line,ucsc,lab) \
                       VALUES ('%d', '%s',  '%s',  '%s',  '%s')" % \
                           (i, newFilename, 'GM12878', result[3], result1))
            result1=''
            break
        k += 1
    db.commit()
    i=i+1
    print("\n")



filesDir = 'E:\\卢立波\\基因组\\data\\H1hesc\\negative'
fileNameList = os.listdir(filesDir)

rules = re.compile(r'(.*?)_shuffle.fasta')
cursor = db.cursor()
for filename in fileNameList:
    print("旧的名字是:\t"+filename)
    print("开始截取！")
    newFilename = re.findall(rules, str(filename))[0]
    print("新名字是:\t" + newFilename)
    #cursor.execute("""INSERT INTO browse(id,factor,cell_line,ucsc,lab)
    #VALUES (i,newFilename, '3','4','5')""")

    keyword1 = "H1hesc"
    keyword2 = newFilename
    a = open("E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", "r", encoding='UTF-8')  # 注意此处的转义字符
    count = len(open(r"E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", 'r',
                     encoding='UTF-8').readlines())  # 使用len+readlines读取行数
    k = 0
    while k < count:  # 使用循环遍历所有行，逐行判断，只要有关键字，就存到新文件
        line = a.readline()
        if keyword1  in line and keyword2 in line:  # 此处注意代码缩进
            result = line.split("	")
            #print("结果："+result[4][1])
            j=0
            flag=0
            while j<len(result[5]):
                if(result[5][j]=='l' and result[5][j+1]=='a' and result[5][j+2]=='b'):
                    j=j+4
                    result1=''
                    while result[5][j]!=';':
                        result1=result1+result[5][j]
                        j=j+1
                    flag=1
                    if flag==1:
                        print("!"+result1)
                        break
                j=j+1
            cursor.execute("INSERT INTO browse_information(id,factor,cell_line,ucsc,lab) \
                       VALUES ('%d', '%s',  '%s',  '%s',  '%s')" % \
                           (i, newFilename, 'H1hesc', result[3], result1))
            result1=''
            break
        k += 1
    db.commit()
    i=i+1
    print("\n")

filesDir = 'E:\\卢立波\\基因组\\data\\H1hesc\\positive'
fileNameList = os.listdir(filesDir)

rules = re.compile(r'(.*?).fasta')
cursor = db.cursor()
for filename in fileNameList:
    print("旧的名字是:\t"+filename)
    print("开始截取！")
    newFilename = re.findall(rules, str(filename))[0]
    print("新名字是:\t" + newFilename)
    #cursor.execute("""INSERT INTO browse(id,factor,cell_line,ucsc,lab)
    #VALUES (i,newFilename, '3','4','5')""")

    keyword1 = "H1hesc"
    keyword2 = newFilename
    a = open("E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", "r", encoding='UTF-8')  # 注意此处的转义字符
    count = len(open(r"E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", 'r',
                     encoding='UTF-8').readlines())  # 使用len+readlines读取行数
    k = 0
    while k < count:  # 使用循环遍历所有行，逐行判断，只要有关键字，就存到新文件
        line = a.readline()
        if keyword1  in line and keyword2 in line:  # 此处注意代码缩进
            result = line.split("	")
            #print("结果："+result[4][1])
            j=0
            flag=0
            while j<len(result[5]):
                if(result[5][j]=='l' and result[5][j+1]=='a' and result[5][j+2]=='b'):
                    j=j+4
                    result1=''
                    while result[5][j]!=';':
                        result1=result1+result[5][j]
                        j=j+1
                    flag=1
                    if flag==1:
                        print("!"+result1)
                        break
                j=j+1
            cursor.execute("INSERT INTO browse_information(id,factor,cell_line,ucsc,lab) \
                       VALUES ('%d', '%s',  '%s',  '%s',  '%s')" % \
                           (i, newFilename, 'H1hesc', result[3], result1))
            result1=''
            break
        k += 1
    db.commit()
    i=i+1
    print("\n")

filesDir = 'E:\\卢立波\\基因组\\data\\Helas3\\negative'
fileNameList = os.listdir(filesDir)

rules = re.compile(r'(.*?)_shuffle.fasta')
cursor = db.cursor()
for filename in fileNameList:
    print("旧的名字是:\t"+filename)
    print("开始截取！")
    newFilename = re.findall(rules, str(filename))[0]
    print("新名字是:\t" + newFilename)
    #cursor.execute("""INSERT INTO browse(id,factor,cell_line,ucsc,lab)
    #VALUES (i,newFilename, '3','4','5')""")

    keyword1 = "Helas3"
    keyword2 = newFilename
    a = open("E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", "r", encoding='UTF-8')  # 注意此处的转义字符
    count = len(open(r"E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", 'r',
                     encoding='UTF-8').readlines())  # 使用len+readlines读取行数
    k = 0
    while k < count:  # 使用循环遍历所有行，逐行判断，只要有关键字，就存到新文件
        line = a.readline()
        if keyword1  in line and keyword2 in line:  # 此处注意代码缩进
            result = line.split("	")
            #print("结果："+result[4][1])
            j=0
            flag=0
            while j<len(result[5]):
                if(result[5][j]=='l' and result[5][j+1]=='a' and result[5][j+2]=='b'):
                    j=j+4
                    result1=''
                    while result[5][j]!=';':
                        result1=result1+result[5][j]
                        j=j+1
                    flag=1
                    if flag==1:
                        print("!"+result1)
                        break
                j=j+1
            cursor.execute("INSERT INTO browse_information(id,factor,cell_line,ucsc,lab) \
                       VALUES ('%d', '%s',  '%s',  '%s',  '%s')" % \
                           (i, newFilename, 'Helas3', result[3], result1))
            result1=''
            break
        k += 1
    db.commit()
    i=i+1
    print("\n")

filesDir = 'E:\\卢立波\\基因组\\data\\Helas3\\positive'
fileNameList = os.listdir(filesDir)

rules = re.compile(r'(.*?).fasta')
cursor = db.cursor()
for filename in fileNameList:
    print("旧的名字是:\t"+filename)
    print("开始截取！")
    newFilename = re.findall(rules, str(filename))[0]
    print("新名字是:\t" + newFilename)
    #cursor.execute("""INSERT INTO browse(id,factor,cell_line,ucsc,lab)
    #VALUES (i,newFilename, '3','4','5')""")

    keyword1 = "Helas3"
    keyword2 = newFilename
    a = open("E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", "r", encoding='UTF-8')  # 注意此处的转义字符
    count = len(open(r"E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", 'r',
                     encoding='UTF-8').readlines())  # 使用len+readlines读取行数
    k = 0
    while k < count:  # 使用循环遍历所有行，逐行判断，只要有关键字，就存到新文件
        line = a.readline()
        if keyword1  in line and keyword2 in line:  # 此处注意代码缩进
            result = line.split("	")
            #print("结果："+result[4][1])
            j=0
            flag=0
            while j<len(result[5]):
                if(result[5][j]=='l' and result[5][j+1]=='a' and result[5][j+2]=='b'):
                    j=j+4
                    result1=''
                    while result[5][j]!=';':
                        result1=result1+result[5][j]
                        j=j+1
                    flag=1
                    if flag==1:
                        print("!"+result1)
                        break
                j=j+1
            cursor.execute("INSERT INTO browse_information(id,factor,cell_line,ucsc,lab) \
                       VALUES ('%d', '%s',  '%s',  '%s',  '%s')" % \
                           (i, newFilename, 'Helas3', result[3], result1))
            result1=''
            break
        k += 1
    db.commit()
    i=i+1
    print("\n")

filesDir = 'E:\\卢立波\\基因组\\data\\Hepg2\\negative'
fileNameList = os.listdir(filesDir)

rules = re.compile(r'(.*?)_shuffle.fasta')
cursor = db.cursor()
for filename in fileNameList:
    print("旧的名字是:\t"+filename)
    print("开始截取！")
    newFilename = re.findall(rules, str(filename))[0]
    print("新名字是:\t" + newFilename)
    #cursor.execute("""INSERT INTO browse(id,factor,cell_line,ucsc,lab)
    #VALUES (i,newFilename, '3','4','5')""")

    keyword1 = "Hepg2"
    keyword2 = newFilename
    a = open("E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", "r", encoding='UTF-8')  # 注意此处的转义字符
    count = len(open(r"E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", 'r',
                     encoding='UTF-8').readlines())  # 使用len+readlines读取行数
    k = 0
    while k < count:  # 使用循环遍历所有行，逐行判断，只要有关键字，就存到新文件
        line = a.readline()
        if keyword1  in line and keyword2 in line:  # 此处注意代码缩进
            result = line.split("	")
            #print("结果："+result[4][1])
            j=0
            flag=0
            while j<len(result[5]):
                if(result[5][j]=='l' and result[5][j+1]=='a' and result[5][j+2]=='b'):
                    j=j+4
                    result1=''
                    while result[5][j]!=';':
                        result1=result1+result[5][j]
                        j=j+1
                    flag=1
                    if flag==1:
                        print("!"+result1)
                        break
                j=j+1
            cursor.execute("INSERT INTO browse_information(id,factor,cell_line,ucsc,lab) \
                       VALUES ('%d', '%s',  '%s',  '%s',  '%s')" % \
                           (i, newFilename, 'Hepg2', result[3], result1))
            result1=''
            break
        k += 1
    db.commit()
    i=i+1
    print("\n")

filesDir = 'E:\\卢立波\\基因组\\data\\Hepg2\\positive'
fileNameList = os.listdir(filesDir)

rules = re.compile(r'(.*?).fasta')
cursor = db.cursor()
for filename in fileNameList:
    print("旧的名字是:\t"+filename)
    print("开始截取！")
    newFilename = re.findall(rules, str(filename))[0]
    print("新名字是:\t" + newFilename)
    #cursor.execute("""INSERT INTO browse(id,factor,cell_line,ucsc,lab)
    #VALUES (i,newFilename, '3','4','5')""")

    keyword1 = "Hepg2"
    keyword2 = newFilename
    a = open("E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", "r", encoding='UTF-8')  # 注意此处的转义字符
    count = len(open(r"E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", 'r',
                     encoding='UTF-8').readlines())  # 使用len+readlines读取行数
    k = 0
    while k < count:  # 使用循环遍历所有行，逐行判断，只要有关键字，就存到新文件
        line = a.readline()
        if keyword1  in line and keyword2 in line:  # 此处注意代码缩进
            result = line.split("	")
            #print("结果："+result[4][1])
            j=0
            flag=0
            while j<len(result[5]):
                if(result[5][j]=='l' and result[5][j+1]=='a' and result[5][j+2]=='b'):
                    j=j+4
                    result1=''
                    while result[5][j]!=';':
                        result1=result1+result[5][j]
                        j=j+1
                    flag=1
                    if flag==1:
                        print("!"+result1)
                        break
                j=j+1
            cursor.execute("INSERT INTO browse_information(id,factor,cell_line,ucsc,lab) \
                       VALUES ('%d', '%s',  '%s',  '%s',  '%s')" % \
                           (i, newFilename, 'Hepg2', result[3], result1))
            result1=''
            break
        k += 1
    db.commit()
    i=i+1
    print("\n")


filesDir = 'E:\\卢立波\\基因组\\data\\K562\\negative'
fileNameList = os.listdir(filesDir)

rules = re.compile(r'(.*?)_shuffle.fasta')
cursor = db.cursor()
for filename in fileNameList:
    print("旧的名字是:\t"+filename)
    print("开始截取！")
    newFilename = re.findall(rules, str(filename))[0]
    print("新名字是:\t" + newFilename)
    #cursor.execute("""INSERT INTO browse(id,factor,cell_line,ucsc,lab)
    #VALUES (i,newFilename, '3','4','5')""")

    keyword1 = "K562"
    keyword2 = newFilename
    a = open("E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", "r", encoding='UTF-8')  # 注意此处的转义字符
    count = len(open(r"E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", 'r',
                     encoding='UTF-8').readlines())  # 使用len+readlines读取行数
    k = 0
    while k < count:  # 使用循环遍历所有行，逐行判断，只要有关键字，就存到新文件
        line = a.readline()
        if keyword1  in line and keyword2 in line:  # 此处注意代码缩进
            result = line.split("	")
            #print("结果："+result[4][1])
            j=0
            flag=0
            while j<len(result[5]):
                if(result[5][j]=='l' and result[5][j+1]=='a' and result[5][j+2]=='b'):
                    j=j+4
                    result1=''
                    while result[5][j]!=';':
                        result1=result1+result[5][j]
                        j=j+1
                    flag=1
                    if flag==1:
                        print("!"+result1)
                        break
                j=j+1
            cursor.execute("INSERT INTO browse_information(id,factor,cell_line,ucsc,lab) \
                       VALUES ('%d', '%s',  '%s',  '%s',  '%s')" % \
                           (i, newFilename, 'K562', result[3], result1))
            result1=''
            break
        k += 1
    db.commit()
    i=i+1
    print("\n")

filesDir = 'E:\\卢立波\\基因组\\data\\K562\\positive'
fileNameList = os.listdir(filesDir)

rules = re.compile(r'(.*?).fasta')
cursor = db.cursor()
for filename in fileNameList:
    print("旧的名字是:\t"+filename)
    print("开始截取！")
    newFilename = re.findall(rules, str(filename))[0]
    print("新名字是:\t" + newFilename)
    #cursor.execute("""INSERT INTO browse(id,factor,cell_line,ucsc,lab)
    #VALUES (i,newFilename, '3','4','5')""")

    keyword1 = "K562"
    keyword2 = newFilename
    a = open("E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", "r", encoding='UTF-8')  # 注意此处的转义字符
    count = len(open(r"E:\\卢立波\\基因组\\data\\DESSO-master-whole\\data\\wgEncodeAwgTfbsUniform_hg19_ENCODE.txt", 'r',
                     encoding='UTF-8').readlines())  # 使用len+readlines读取行数
    k = 0
    while k < count:  # 使用循环遍历所有行，逐行判断，只要有关键字，就存到新文件
        line = a.readline()
        if keyword1  in line and keyword2 in line:  # 此处注意代码缩进
            result = line.split("	")
            #print("结果："+result[4][1])
            j=0
            flag=0
            while j<len(result[5]):
                if(result[5][j]=='l' and result[5][j+1]=='a' and result[5][j+2]=='b'):
                    j=j+4
                    result1=''
                    while result[5][j]!=';':
                        result1=result1+result[5][j]
                        j=j+1
                    flag=1
                    if flag==1:
                        print("!"+result1)
                        break
                j=j+1
            cursor.execute("INSERT INTO browse_information(id,factor,cell_line,ucsc,lab) \
                       VALUES ('%d', '%s',  '%s',  '%s',  '%s')" % \
                           (i, newFilename, 'K562', result[3], result1))
            result1=''
            break
        k += 1
    db.commit()
    i=i+1
    print("\n")

db.close()
