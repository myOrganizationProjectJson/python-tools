# coding:utf-8
import os

def getfilelist(filepath, tabnum=1):
    simplepath = os.path.split(filepath)[1]
    returnstr = simplepath + "目录<>" + "\n"
    returndirstr = ""
    returnfilestr = ""
    getfileliststr = ""
    dir = ""
    filelist = os.listdir(filepath)
    #print filelist
    #if filelist == "":
    #    print filepath
    for num in range(len(filelist)):
        filename = filelist[num]
        if os.path.isdir(filepath + "/" + filename):
            getfileliststr = getfilelist(filepath + "/" + filename, tabnum + 1)
            dir = os.listdir(filepath + "/" + filename)
            if dir == []:
                print filepath + "/" + filename
                o = open(filepath + "/" + filename+"/.null", "w+")
                o.writelines("")
                o.close()
            #print dir
            # returndirstr += "\t"*tabnum+getfileliststr
            returndirstr += "\t" * tabnum + getfileliststr
            # print getfileliststr ;
          #  print returndirstr ;
            #if getfileliststr == "":
             #   print filename

        else:
            returnfilestr += "\t" * tabnum + filename + "\n"
            #print filename+"dd"
    #else:
         #print filepath
    returnstr += returnfilestr + returndirstr
    return returnstr + "\t" * tabnum + "</>\n"


path = raw_input("please input project path:")
usefulpath = path.replace('\\', '/')
if usefulpath.endswith("/"):
    usefulpath = usefulpath[:-1]
if not os.path.exists(usefulpath):
    print "path error!"
elif not os.path.isdir(usefulpath):
    print "path is not a dir!"
else:
    filelist = os.listdir(usefulpath)
    o = open("root.xml", "w+")
    o.writelines(getfilelist(usefulpath))
    o.close()
    print "please check root.xml"