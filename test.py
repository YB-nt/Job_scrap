import requests
from bs4 import BeautifulSoup
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
cookie = {'name': 'marisara'}
resp = requests.get("https://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx=45064382&recommend_ids=eJxVz8sNwzAMA9BpejdF6nfuINl%2FiwYOHLvHB0oiJFcPIK%2By%2FuRXzmJ2XQVMKtNCm8gwrmG1CoqV0j1NfvNJvavBRRcpxD41LGlvr%2B5a37206sLBHmEHgVn00ALkeDlS7GN3eJ%2FMiODe7Zbh%2F98jzTKbRT9orkAw&view_type=search&searchword=%EB%8D%B0%EC%9D%B4%ED%84%B0+%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4&searchType=recently&gz=1&t_ref_content=generic&t_ref=search&paid_fl=n&search_uuid=08be70aa-2dff-4e83-ba5c-31a66ab3b84d#seq=0",headers=header,cookies=cookie)

if(resp.status_code ==200):
    print(resp.text.decode('unicode-escape'))
