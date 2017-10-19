import apidef
#import urllib2

class matchPlayer(): 
        
        def __init__(self, partId):
                self.partId = partId  
        
        accId = 0
        sumName = ''
        champ = 0


def ret_url(URL) : #url로 페이지 호출시 텍스트 형식으로 리턴 
        return apidef.RetDataFromUrl(URL)

     
        
def GetMatchData(matchID) : 
        URL = apidef.url_GetMatchByID(matchID)
        parsed = ret_url(URL)
        cnt=0
        
        print ("매치 id : "+str(matchID))
        
        players = [ matchPlayer(i) for i in range(10) ]
        
        for data in parsed['participants'] : 
                cnt = cnt+1 
                #players = matchPlayer(cnt)
                players.champ = data['championId']
                
        print (players.partId)        
        
        cnt=0
        for data in parsed['participantIdentities'] :
                cnt = cnt+1
                p_SummonerName = str(data['player']['summonerName'])
                p_AccountId = str(data['player']['accountId'])
                print (str(cnt)+" 번째 소환사명 : "+p_SummonerName+", 계정 ID : "+p_AccountId)
                
                

def GetGameId(userid) : #유저 account ID를 받아서 해당 유저의 gid 출
        
        URL = apidef.url_RecMatchByID(userid)
        parsed = ret_url(URL)
        cnt = 0
        
        for data in parsed['matches'] : 
                cnt = cnt+1
                p_gid = str(data['gameId'])
                print (str(cnt)+"번쨰 게임 gid : "+p_gid)
                
        GetMatchData(p_gid)
 
def GetUserdata(username) : #소환사 명을 가지고 유저 accountID 받아오는 api
        URL = apidef.url_user(username)
        parsed = ret_url(URL)
        
        p_name = parsed['name']
        p_id = str(parsed['accountId'])
        
        print ("소환사명 : "+p_name)
        print ("Account id : "+p_id)
        
        GetGameId(p_id)
      #  print (parsed)
   
                
        
GetUserdata("안인읒")
        