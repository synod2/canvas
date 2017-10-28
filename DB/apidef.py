import requests
import json 

api_key = "?api_key="+"RGAPI-d6241dc2-d2a7-4731-aba8-073325c9e332"

'''
def RetDataFromUrl(URL) : #URL로 호출한 페이지의 데이터를 텍스트 형태로 출력 후 json 데이터를 파싱 후 리턴.
        return json.loads(requests.get(URL).text)
        #필요 없는 부분, 간략화
'''
#함수별로 필요한 데이터를 파라미터로 사용하면, 해당 API를 통하여 받아온 데이터를 파싱해서 
#ret하는 함수들

def url_user(username) :  #소환사명 기반 소환사 정보 출력 url
        ret_url = "https://kr.api.riotgames.com/lol/summoner/v3/summoners/by-name/"+username+api_key
        return json.loads(requests.get(ret_url).text)
        
def url_RecMatchByID(accID) : #소환사 account id 기반 최근 20매치 출력 url 
        ret_url = "https://kr.api.riotgames.com/lol/match/v3/matchlists/by-account/"+accID+api_key
        return json.loads(requests.get(ret_url).text)

def url_GetMatchByID(matchID) : 
        ret_url = "https://kr.api.riotgames.com/lol/match/v3/matches/"+matchID+api_key
        return json.loads(requests.get(ret_url).text)
        