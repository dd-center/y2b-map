import requests
import csv

info = requests.get('https://api.vtbs.moe/v1/info').json()
info_sorted = sorted(info, key=lambda x: x['follower'], reverse=True)

with open('map.csv', 'r', newline='', encoding='utf8') as csvfile:
    fieldnames = ['name', 'mid', 'channelId']
    reader = csv.DictReader(csvfile, fieldnames=fieldnames)
    now_list = list(reader)

with open('map.csv', 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for entry in info_sorted:
        name = entry['uname']
        mid = entry['mid']
        channelId = ''
        for entry2 in now_list:
            if str(entry2['mid']) == str(mid):
                channelId = entry2['channelId']

        writer.writerow({
            'name': name,
            'mid': mid,
            'channelId': channelId
        })