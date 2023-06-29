import requests

def get_timezones(latitude, longitude):
    api_key = 'YOUR_API_KEY'
    url = 'https://maps.googleapis.com/maps/api/timezone/json?location={},{}&timestamp=1331161200&key={}'.format(latitude, longitude, api_key)
    
    try:
        response = requests.get(url)
        response_data = response.json()

        if response_data['status'] == 'OK':
            timezone_id = response_data['timeZoneId']
            timezone_name = response_data['timeZoneName']
            return timezone_id, timezone_name
        else:
            return None, None
        

    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        return None, None
    
#テスト用の緯度経度
latitude = 35 #緯度
longitude = 135 #経度

#タイムゾーンの取得
timezone_id, timezone_name = get_timezones(latitude, longitude)

if timezone_id and timezone_name:
    print('タイムゾーンID: {}'.format(timezone_id))
    print('タイムゾーン名: {}'.format(timezone_name))
else:
    print('タイムゾーンの取得に失敗しました。')