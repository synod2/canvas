import requests
import json 

api_key = "?api_key="+"RGAPI-08c8a6ef-d288-454a-9efe-798590b2cb2a"


def RetDataFromUrl(URL) : #URL로 호출한 페이지의 데이터를 텍스트 형태로 출력 후 json 데이터를 파싱 후 리턴.
        return json.loads(requests.get(URL).text)

def url_user(username) :  #소환사명 기반 소환사 정보 출력 url
        ret_url = "https://kr.api.riotgames.com/lol/summoner/v3/summoners/by-name/"+username+api_key
        return ret_url
        
def url_RecMatchByID(accID) : #소환사 account id 기반 최근 20매치 출력 url 
        ret_url = "https://kr.api.riotgames.com/lol/match/v3/matchlists/by-account/"+accID+api_key
        return ret_url
        
        