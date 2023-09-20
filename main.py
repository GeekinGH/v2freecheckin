import requests
import time
import argparse

def main(usr, pw):
    client = requests.Session()
    login_url = "https://w1.v2free.top/auth/login"
    sign_url = "https://w1.v2free.top/user/checkin"
    data = {
        "email": usr,
        "passwd": pw,
        "code": "",
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/76.0",
        "Referer": "https://w1.v2free.top/auth/login",
    }
    client.post(login_url, data=data, headers=headers)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/76.0",
        "Referer": "https://w1.v2free.top/user",
    }
    response = client.post(sign_url, headers=headers).json()
    print(response)

    msg = usr + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + response['msg']
    if response['ret'] == 1:
        msg +="剩余流量："+response['trafficInfo']['unUsedTraffic']
    return msg

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='V2free签到脚本')
    parser.add_argument('--username', type=str, help='账号')
    parser.add_argument('--password', type=str, help='密码')
    args = parser.parse_args()
    msg = main(args.username,args.password)
    print(msg)

