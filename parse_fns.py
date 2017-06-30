##site=[[url,linktest_1],[fn_2,[get_fn1(e1[0],e1[1]),get_fn1(e2[0],e2[1]),get_fn1(e3[0],e3[1]),get_fn1(e4[0],e4[1])]]]

def selection(text,start,end):
    # returns the first instance of a substring bordered by start and end
    r1=text.split(start,1)
    if len(r1)==2: return r1[1].split(end)[0]
    return ""
    

def multi_selection(text,start,end):
    #returns all instances of of a substring bordered by start and end
    r1=text.split(start)[1:0]
    # r1=r1[1:]
    r=[]
    for x in range(len(r1)):
        r=r+[r1[x].split(end)[0]]
    return r
    
def remove_tags(text):
    # removes html tags from a string
    for x in range(len(text)):
        if text[x]=='>' or text[x]=='<':
            if text[x]=='>': t=0
            if text[x]=='<': t=1
            break
    r=""""""
    t=0
    for x in range(len(text)):
        if text[x]=='>' or text[x]=='<':
            if text[x]=='>': t=0
            if text[x]=='<': t=1
        elif t==0: r=r+text[x]
    return r

def get_post(text):
    # extracts a string with the post data from the html page
    return [selection(text,'<article id="post','</article><!-- #post-## -->')]

def get_comments(text):
    # extracts strings with the comment data from the html page
    return multi_selection(text,'<li class="comment','<div class="reply">')

def selection_fn_gen(s,e):
    return lambda x: remove_tags(selection(x,s,e))

def no_tags_selection_fn_gen(s,e):
    return lambda x: remove_tags(selection(x,s,e))

def double_selection_fn_gen(s1,e1,s2,e2):
    return lambda x: selection(selection(x,s1,e1),s2,e2)

# def format_name_ers(fn)
#     r = lambda x: selection(selection(x,s1,e1),s2,e2)
#     return r

get_comment_author=no_tags_selection_fn_gen('<div class="comment-author vcard">',
                             '</cite> |')

get_comment_date=double_selection_fn_gen('<span class="comment-meta commentmetadata">',
                            '</time>',
                            'datetime="',
                            '">')

# fn3 depth
get_comment_depth=double_selection_fn_gen('depth',
                            'id="li-comment',
                            '-',
                            ' ')
    
# fn4 text
get_comment_text=no_tags_selection_fn_gen('<div class="comment-content">',
                             '</div>')
# fn5 html id
get_comment_html_id=selection_fn_gen('<article id="comment-',
                     '" class="comment">')
# post 

# fn6 title
get_post_title=selection_fn_gen('<h1 class="entry-title">',
                     '</h1>')
# fn7 html id
get_post_html_id=selection_fn_gen('-',
                     '" class="post-')

# fn8 published_time
get_post_date=selection_fn_gen('class="entry-date" datetime="',
                     '" pubdate')

# fn9 author
get_post_author=no_tags_selection_fn_gen('<span class="author vcard">',
                             '</span>')
# fn10 text
get_post_text=no_tags_selection_fn_gen('<div class="entry-content">',
                              '</div><!-- .entry-content -->')

wordpress_functions_post_1=[get_post_title,
                                get_post_html_id,
                                get_post_date,
                                get_post_author,
                                get_post_text]
wordpress_functions_comments_1=[get_comment_author,
                                get_comment_date,
                                get_comment_depth,
                                get_comment_text,
                                get_comment_html_id]
