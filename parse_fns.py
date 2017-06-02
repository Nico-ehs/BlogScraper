##site=[[url,linktest_1],[fn_2,[get_fn1(e1[0],e1[1]),get_fn1(e2[0],e2[1]),get_fn1(e3[0],e3[1]),get_fn1(e4[0],e4[1])]]]


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



def get_post(text):
    r=1
    s='<article id="post'
    e='</article><!-- #post-## -->'
    r=selection(text,s,e)
    return [r]

def get_comments(text):
    r=1
    s='<li class="comment'
    e='<div class="reply">'
    r=multi_selection(text,s,e)
    return r

def selection_fn_gen(s,e):
    r = lambda x: remove_tags(selection(x,s,e))
    return r

def no_tags_selection_fn_gen(s,e):
    r = lambda x: remove_tags(selection(x,s,e))
    return r

def double_selection_fn_gen(s1,e1,s2,e2):
    r = lambda x: selection(selection(x,s1,e1),s2,e2)
    return r


# def format_name_ers(fn)
#     r = lambda x: selection(selection(x,s1,e1),s2,e2)
#     return r




# comments

# fn1 authour
# fn1=no_tags_selection_fn_gen('<div class="comment-author vcard">',
#                              ' |<span class="comment-meta commentmetadata">')
fn1=no_tags_selection_fn_gen('<div class="comment-author vcard">',
                             '</cite> |')
# fn2 date
fn2=double_selection_fn_gen('<span class="comment-meta commentmetadata">',
                            '</time>',
                            'datetime="',
                            '">')
# fn3 depth
fn3=double_selection_fn_gen('depth',
                            'id="li-comment',
                            '-',
                            ' ')
    
# fn4 text
fn4=no_tags_selection_fn_gen('<div class="comment-content">',
                             '</div>')
# fn5 html id
fn5=selection_fn_gen('<article id="comment-',
                     '" class="comment">')
# post 

# fn6 title
fn6=selection_fn_gen('<h1 class="entry-title">',
                     '</h1>')
# fn7 html id
fn7=selection_fn_gen('-',
                     '" class="post-')

# fn8 published_time
fn8=selection_fn_gen('class="entry-date" datetime="',
                     '" pubdate')

# fn9 author
fn9=no_tags_selection_fn_gen('<span class="author vcard">',
                             '</span>')
# fn10 text
fn10=no_tags_selection_fn_gen('<div class="entry-content">',
                              '</div><!-- .entry-content -->')

wordpress_functions_post_1=[fn6,
                                fn7,
                                fn8,
                                fn9,
                                fn10]
wordpress_functions_comments_1=[fn1,
                                fn2,
                                fn3,
                                fn4,
                                fn5]

fns_1=wordpress_functions_comments_1
fns_2=wordpress_functions_post_1