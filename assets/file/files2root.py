#将所有下级文件夹的文件移动到根目录下
#增加随机六位数防止文件重命名
#生成移动记录
import os,random,shutil
def rename_root(name):
    #将文件夹改名，避免最后的文件名重复
    if(path_dict.get(name)==None):
        path_dict[name] = random.randrange(100000,1000000)
    return name+'('+str(path_dict[name])+')'

def walkFile(root_path):
    for root, dirs, files in os.walk(root_path):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            if root != root_path:
                try:
                    old_path = os.path.join(root, f)
                    new_path = root_path+'\\'+rename_root(root.split('\\')[-1])+f
                    #print(old_path+"   "+new_path)
                    shutil.move(old_path,new_path)
                    with open('trans_log.txt','a+') as f:
                        f.write(old_path+' -> '+new_path+'\n')
                except Exception as e:
                    pass


        # # 遍历所有的文件夹
        # for d in dirs:
        #     print(os.path.join(root, d))
if __name__ == '__main__':
    root_path = os.path.split(os.path.realpath(__file__))[0]
    #print(root_path)
    path_dict = {}
    walkFile(root_path)