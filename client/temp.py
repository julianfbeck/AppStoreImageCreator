import requests


def get(ip):
    r = requests.get(f"http://ip-api.com/json/{ip}")
    response = r.json()
    if response["status"] != "fail":
        print(f'{ip}\t{r.json()["country"]}\t{r.json()["regionName"]}\t{r.json()["city"]}\t{r.json()["zip"]}' +
              f'\t{r.json()["lat"]}\t{r.json()["lon"]}\t{r.json()["isp"]}\t{r.json()["as"]}\t{r.json()["asname"]}\t{r.json()["mobile"]}')


get("192.168.96.1")
get("129.13.55.209")
get("193.196.36.1")
get("141.52.3.6")
get("193.197.63.6")
get("129.143.60.115")
get("129.143.200.42")
get("62.53.11.130")
get("62.53.0.198")
get("62.53.4.213")
get("62.53.8.31")
get("62.53.2.159")
get("46.114.149.213")
get("185.52.247.41")
get("87.137.247.61")
get("93.199.153.203")
get("80.157.200.197")
get("46.114.148.852")
get("46.114.151.161")
get("46.114.151.192")
get("62.53.11.132")
get("62.53.28.154")
get("62.53.3.53")
get("62.53.8.37")
get("62.53.2.127")
get("192.168.80.1")
get("192.168.96.1")
get("129.13.55.209")
get("193.196.36.1")
get("141.52.3.6")
get("193.197.63.6")
get("129.143.60.115")
get("129.143.200.42")
get("62.53.11.130")
get("62.53.0.198")
get("62.53.4.213")
get("62.53.8.31")
get("62.53.2.159")
get("46.114.149.213")
get("185.52.247.41")
get("87.137.247.61")
get("93.199.153.203")
get("80.157.200.197")
get("46.114.148.852")
get("46.114.151.161")
get("46.114.151.192")
get("62.53.11.132")
get("62.53.28.154")
get("62.53.3.53")
get("62.53.8.37")
get("62.53.2.127")
get("192.168.80.1")
