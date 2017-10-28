import apidef
#import urllib2

class matchPlayer(): 
        
        def __init__(self, partId):
                self.partId = partId  
        
        accId = 0
        sumName = ''
        champ = 0

'''
def ret_url(URL) : #url로 페이지 호출시 텍스트 형식으로 리턴 
        return apidef.RetDataFromUrl(URL)
'''
     
        
def GetMatchData(matchID) : #매치id를 받아서 해당 매치 정보 받아오는 함수 
        #URL = apidef.url_GetMatchByID(matchID)
        parsed = apidef.url_GetMatchByID(matchID)
        cnt=0
        
        print ("매치 id : "+str(matchID))
        
        players = [ matchPlayer(i) for i in range(10) ]
        
        for data in parsed['participants'] : 
                #players = matchPlayer(cnt)
                players[cnt].champ = str(data['championId'])
                cnt = cnt+1
                
        #print (players.partId)        
        
        cnt=0
        for data in parsed['participantIdentities'] :
                players[cnt].sumName = str(data['player']['summonerName'])
                players[cnt].accId = str(data['player']['accountId'])
                cnt = cnt+1

        for data in players : 
                print (str(data.partId)+"번쨰 유저 \""+data.sumName+"\"가 선택한 챔피언 "+data.champ+"")

def GetGameId(userid) : #유저 account ID를 받아서 해당 유저의 gid 출력
        
       # URL = apidef.url_RecMatchByID(userid)
        parsed = apidef.url_RecMatchByID(userid)
        cnt = 0
        
        for data in parsed['matches'] : 
                cnt = cnt+1
                p_gid = str(data['gameId'])
                print (str(cnt)+"번쨰 게임 gid : "+p_gid)
                
                
        #예제를 위해 마지막 게임의 gid를 이용하기로 함 
        GetMatchData(p_gid)
 
def GetUserData(username) : #소환사 명을 가지고 유저 accountID 받아오는 api
       # URL = apidef.url_user(username)
        parsed = apidef.url_user(username)
        
        p_name = parsed['name']
        p_id = str(parsed['accountId'])
        
        print ("소환사명 : "+p_name)
        print ("Account id : "+p_id)
        
        GetGameId(p_id)
      #  print (parsed)
   

                
#동작순서 : 소환사명 -> GetUserdata가 accointID받아옴 -> GetGameId가 최근 게임 ID 받아옴 
#-> GetMatchData가 해당 매치 정보 받아옴


GetUserData("안인읒")

        