
import re


def extract_urls(text):
    # regex for extrating urls for html sourse code
    url_re='<a href="?\'?([^"\'>]*)'
    urls=re.findall(url_re,text)
    return urls

def linktest_twig(link):
    r=1
    linktest=[]
    linktest+=["https://twigserial.wordpress.com/20" in link]
    linktest+=['#' not in link]
    linktest+=['?' not in link]
    linktest+=[link[-1]==r"/"]
    linktest+=['"' not in link]
    linktest+=['feed' not in link]
    for x in linktest:
        if x==False:
            r=0
    return r
    
def linktest_esr(link):
    r=1
    linktest=[]
    linktest+=["http://esr.ibiblio.org/?p=7" in link]
    linktest+=['#' not in link]
    # linktest+=['?' not in link]
    # linktest+=[link[-1]==r"/"]
    # linktest+=['"' not in link]
    # linktest+=['feed' not in link]
    for x in linktest:
        if x==False:
            r=0
    return r

def link_fn_twig(text):
    links=extract_urls(text)
    vaild_links=[x for x in links if linktest_twig(x)==1]
    return vaild_links
    
def link_fn_esr(text):
    links=extract_urls(text)
    vaild_links=[x for x in links if linktest_esr(x)==1]
    return vaild_links