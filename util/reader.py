def read_file(fname):
    f = open(fname)
    s = f.read()
    f.close()
    return s

def get_list(s,index):
    s = s.split("\n")
    return s[index].split(",")

def make_dic(s):#For Usernames and Passwords
    q = s.split("\n")
    result = {}
    for i in range(len(q)-1):
        w = q[i].split(",")
        result[w[0]] = [w[1],w[2]]
    return result

    

def make_postdic(s):
    s = read_file(s)
    q = s.split("\<end>\n")
    result = []
    for i in range(len(q)-1):
        tag_list = q[i][ q[i].find("[u"):q[i].find("']")+2 ]
        q[i] = q[i].replace("<,>" + tag_list,"")
        w = q[i].split("<,>")

        #print "w[3] = " + str(w[3])
        reply_list = w[4].split("{{,}}")[:-1] #Ignores last one.
        for i in range(len(reply_list)):
            reply_list[i] = reply_list[i].split("{,}") #This seperates comment and user.
        image_list = w[3].split(",")
        print "POTATO " + str(image_list)
        #print "POTATOES " + str(reply_list)
        #result[i] = {"title":w[0],"user":w[1],"tags":tag_list,"content":w[2],"replies":reply_list}
        result.append( {"title":w[0],"user":w[1],"tags":tag_list,"content":w[2],"images":image_list,"replies":reply_list} )
    #print "RESULT: " + str(result)
    return result


def make_taglist(s):
    result = []
    tag_list = get_tags(s)
    for i in tag_list:
        for j in i:
            if not (j in result) and j != "":
                result.append(str(j))
    return result


def get_tags(s):
    result = []
    tag_list = []
    for i in range(len(s)):
        #result.append([])
        q = s[i]["tags"]
        tag_list = q[ q.find("[u"):q.find("']")+2 ]
        tag_list = tag_list.replace("u'","")
        tag_list = tag_list.replace("[","")
        tag_list = tag_list.replace("]","")
        tag_list = tag_list.replace("'","")
        #print tag_list
        tag_list = tag_list.replace(" ","")
        tag_list = tag_list.split(",")
        #print "Potato: " + str(tag_list)
        result.append(tag_list)
        #result[i] = (tag_list)
    return result

def get_post_by_tag(posts,tag):
    result = []
    tag_list = get_tags(posts)
    for i in range(len(tag_list)):
        for j in tag_list[i]:
            if j == tag:
                result.append(i)
    return result



def get_post_by_user(posts,user):
    #print "POTATO POST: " + str(posts)
    user_post = []
    for i in range(len(posts)):
        if posts[i]["user"] == user:
            user_post.append(posts[i])
    return user_post


def make_messagelist(text):
    result = []
    text = read_file(text)
    s = text.split("/<end>\n")
    for i in s[:-1]:
        i = i.split("<,>")
        result.append({'user':i[0],'sender':i[1],'content':i[2],'read':i[3]})
    return result

def get_message_by_user(user,messages):
    result = []
    for i in messages:
        if i['user'] == user:
            result.append(i)
    return result

def get_unread_count(user,messages):
    messages = make_messagelist(messages)
    result = 0
    for i in messages:
        if i['user'] == user and i['read'] == "False":
            result+=1
    return result



#################TEXT WORKING####################
def string_at(index,string,text):
    for i in range(len(string)):
        if i+index > len(text):
            return False
        if text[i+index] != string[i]:
            return False
    return True


#######mode 'w' = write. mode 'a' = append (adds on to text file instead of replacing it).
def write_file(f,t):
    f = open(f,'a')
    f.write(t)
    f.close()

def replace_file(f,t):
    f = open(f,'w')
    f.write(t)
    f.close()

