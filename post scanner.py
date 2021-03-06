# -*- coding: utf-8 -*-
import requests
# url_re=r"""(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))"""
import re
import ast
from operator import itemgetter
import time
import os
import linktest
import file_fns

def extract_urls(text):
    # regex for extrating urls for html sourse code
    url_re='<a href="?\'?([^"\'>]*)'
    urls=re.findall(url_re,text)
    return urls
    
def remove_multiple(list_in):
    r=[]
    for x in list_in:
        if x not in r:
            r.append(x)
    return r

class site_data():
    def __init__(self, sitename, site_url, link_extractor):
        # initlizes class with the passed in sitename and link_extractor. Sets fisrt
        # unscanned page at site_url
        self.sitename=sitename
        self.pages=[]
        self.pagelist=[]
        self.link_extractor=link_extractor
        self.unscanned_pages=[site_url]
    def get_links(self,page):
        # returns new links from page
        links=remove_multiple(self.link_extractor(page.text))
        return [x for x in links if (x not in (self.pagelist+self.unscanned_pages))]
    def scan_page(self):
        # scans the next unscanned_pages url
        page=requests.get(self.unscanned_pages[0])
        print(page.url)
        self.pages.append(page)
        self.pagelist.append(page.url)
        self.unscanned_pages.extend(self.get_links(page))
        self.unscanned_pages=self.unscanned_pages[1:]
    def full_scan(self):
        # scans pages until self.unscanned_pages != [] and len(self.pages) <= 5 o
        while self.unscanned_pages != [] and len(self.pages) <= 5:
            self.scan_page()
            print(str(self.unscanned_pages))
    def output(self):
        r=[self.pages]
        return r
    def save_output(self):
        # saves the html pages to files in sitedata folder
        file_fns.make_site_dir_1(self.sitename)
        for x in self.pages:
            file_fns.save_page(x.text, x.url, self.sitename)
        path='/site data/'+self.sitename
        file_fns.save_file('pagelist.txt',str([self.pagelist,self.unscanned_pages]),path)
        return 1
    def page_filter(self):
        self.pages.remove(self.sitename)





url="https://twigserial.wordpress.com/2014/12/24/taking-root-1-1/"
scan1=site_data('Twig', url, linktest.link_fn_twig)
scan1.full_scan()
scan1.save_output()
file_fns.get_sitelist()

# url="http://esr.ibiblio.org/"
# scan1=site_data('ESR', url, link_fn1)
# scan1.full_scan()
# f_out=open('test.txt', "w", encoding='utf-8')
# f_out.write(str(scan1.pagelist))
# f_out.close
# scan1.save_output()
# get_sitelist()



    
# def linktest_2(link):
#     r=1
#     linktest=[]
#     linktest+=["http://slatestarcodex.com/20" in link]
#     linktest+=['#' not in link]
#     linktest+=['?' not in link]
#     linktest+=[link[-1]==r"/"]
#     linktest+=['"' not in link]
#     linktest+=['feed' not in link]
#     # print('test2')
#     for x in linktest:
#         if x==False:
#             r=0
#     return r

# def link_fn2(text):
#     links=extract_links.extract_m(text)
#     print(len(links))
#     vaild_links=[x for x in links if linktest_2(x)==1]
#     return vaild_links

# url="http://slatestarcodex.com/"
# scan1=site_data('SSC', url, link_fn2)
# scan1.full_scan()
# f_out=open('test.txt', "w")
# f_out.write(str(scan1.pagelist))
# f_out.close
# scan1.save_output()
# get_sitelist()











