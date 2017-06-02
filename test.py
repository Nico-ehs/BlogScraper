import os


# def save_file(filename,text,path):
#     m_dir=os.getcwd()
#     os.chdir(m_dir+path)
#     f_out=open(filename, "w", encoding='utf-8')
#     f_out.write(text)
#     f_out.close
#     os.chdir(m_dir)
#     return True


# def load_file(filename,path):
#     m_dir=os.getcwd()
#     os.chdir(m_dir+path)
#     f_in=open(filename, "r", encoding='utf-8').read()
#     os.chdir(m_dir)
#     return f_in
    
    
# def get_sitelist():
# saves to sielis.txr th s
#     m_dir=os.getcwd()
#     os.chdir(m_dir+'/site data')
#     sitelist=os.listdir(os.getcwd())
#     os.chdir(m_dir)
#     return sitelist
    
# def posts_test(site):
#     m_dir=os.getcwd()
#     os.chdir(m_dir+'/site data/'+sitename)
#     posts=load_file("",posts.txt)
    
    
# def name_test(sitename):
#     m_dir=os.getcwd()
#     # os.chdir(m_dir+'/site data/'+sitename)
#     comments=eval(load_file("comments.txt",'/site data/'+sitename))
#     names=list(map((lambda x: x[3]),comments))
#     for x in names[:100]:
#         print(x)
#     return 1
    
# def post_test(sitename):
#     m_dir=os.getcwd()
#     # os.chdir(m_dir+'/site data/'+sitename)
#     posts=eval(load_file("posts.txt",'/site data/'+sitename))
#     names=list(map((lambda x: x[2]),posts))
#     for x in names:
#         print(x)
#     return 1
        
# name_test("twig")
# post_test("ESR")


def multi_selection(text,start,end):
    r1=text.split(start)
    r1=r1[1:]
    r=[]
    for x in range(len(r1)):
        r=r+[r1[x].split(end)[0]]
    return r
    
def selection(text,start,end):
    r=''
    r1=text.split(start,1)
    if len(r1)==2:
        r=r1[1].split(end)[0]
    else:
        r=""
    return r





def remove_tags(text):
    for x in range(len(text)):
        if text[x]=='>' or text[x]=='<':
            if text[x]=='>':
                t=0
            if text[x]=='<':
                t=1
            break
    r=""""""
    t=0
    for x in range(len(text)):
        if text[x]=='>' or text[x]=='<':
            if text[x]=='>':
                t=0
            if text[x]=='<':
                t=1
        else:
            if t==0:
                r=r+text[x]
    return r

    

def test1():
    return 1

print(test1)
