import apidef
#import urllib2

def ret_url(URL) :
        return apidef.RetDataFromUrl(URL)


def userdata(username) : 
        URL = apidef.url_user(username)
        parsed = ret_url(URL)
        
        p_name = parsed['name']
        p_id = str(parsed['accountId'])
        
        print ("소환사명 : "+p_name)
        print ("Account id : "+p_id)
        
        URL = apidef.url_RecMatchByID(p_id)
        parsed = ret_url(URL)
        print (parsed)
        
        
userdata("안인읒")
        