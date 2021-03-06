
import re


def linktest_main(text, in_link, not_in_link, char_at_loc):
    #tests if all strings in in_link are contained in text and all str in not
    for s in in_link:
        if s not in text: return False
    for s in not_in_link:
        if s in text: return False
    for s in char_at_loc:
        if text[s[1]] != s[0]: return False
    return True
    
def linktest_gen(in_link, not_in_link, char_at_loc):
    return lambda x: linktest_main(x, in_link, not_in_link, char_at_loc)
    
# def link_extract_gen(in_link, not_in_link):
#     return lambda x:  extract_urls(text)
#     linktest_main(x, in_link, not_in_link)

def extract_urls(text):
    # regex for extrating urls for html sourse code
    url_re='<a href="?\'?([^"\'>]*)'
    urls=re.findall(url_re,text)
    return urls

link_fn_twig=linktest_gen(["https://twigserial.wordpress.com/20"],
                        ['#','?','"','feed'],
                        [r"/",-1])
                        
link_fn_esr=linktest_gen(["https://twigserial.wordpress.com/20"],
                        ['#','?','"','feed'],
                        [r"/",-1])
                        

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

# def link_fn_twig(text):
#     links=extract_urls(text)
#     vaild_links=[x for x in links if linktest_twig(x)==1]
#     return vaild_links
    
# def link_fn_esr(text):
#     links=extract_urls(text)
#     vaild_links=[x for x in links if linktest_esr(x)==1]
#     return vaild_links