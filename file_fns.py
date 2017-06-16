import os

def save_file(filename,text,path):
    # Saves string to location
    m_dir=os.getcwd()
    os.chdir(m_dir+path)
    f_out=open(filename, "w")
    out=text
    f_out.write(out)
    f_out.close
    os.chdir(m_dir)
    return True
    
    

def load_file(filename,path):
    # Loads file as string
    m_dir=os.getcwd()
    os.chdir(m_dir+path)
    f_in=open(filename, "r").read()
    os.chdir(m_dir)
    return f_in



def make_site_dir_1(sitename):
    # checks if directory for site exists and if not creates it
    m_dir=os.getcwd()
    os.chdir(m_dir+'/site data')
    if sitename not in os.listdir(os.getcwd()):
        os.chdir(m_dir+'/site data')
        os.mkdir(sitename)
        os.chdir(m_dir+'/site data/'+sitename)
        os.mkdir("html data")
    os.chdir(m_dir)
    return 1

def save_page(d,filename,sitename):
    # formats filename and saves html page in site directory
    m_dir=os.getcwd()
    os.chdir(m_dir+'/site data/'+sitename+'/html data')
    fn=filename
    fn=fn.replace("/",'')
    fn=fn.replace("\\",'')
    fn=fn.replace(":",'')
    fn=fn.replace("/",'')
    f_out=open(fn+'.html', "w")
    out=str(d)
    f_out.write(out)
    f_out.close
    os.chdir(m_dir)
    return 1
    



def load_page(filename,sitename):
    # loads html page wiht filename
    m_dir=os.getcwd()
    os.chdir(m_dir+'/site data/'+sitename+'/html data')
    f_in=open(filename, "r")
    d_in=f_in.read()
    r=d_in
    os.chdir(m_dir)
    return r




def load_site(sitename):
    # returns the page texts of the site as a list of strings
    m_dir=os.getcwd()
    os.chdir(m_dir+'/'+sitename+'/html data')
    pages=[]
    files=os.listdir(os.getcwd())
    for x in files:
        pages+=[[x,open(x, "r").read()]]        
    os.chdir(m_dir)
    return pages

def get_sitelist():
    # gets list of site folders
    m_dir=os.getcwd()
    os.chdir(m_dir+'/site data')
    sitelist=os.listdir(os.getcwd())
    os.chdir(m_dir)
    save_file('sitelist.txt',str(sitelist),'')
    return True
    
    
def load_pagelist(sitename):
    # loads the lists of files in the html data directory for site
    # m_dir=os.getcwd()
    # os.chdir(m_dir+'/site data/'+sitename+'/html data')
    # return os.listdir(os.getcwd())
    return os.listdir(os.getcwd()+'/site data/'+sitename+'/html data')