# coding:utf-8
import requests

api_key = '9ba1020a83e545bbff9286a2ec7e6cab'
geocode_api = 'http://restapi.amap.com/v3/geocode/geo'
bus_api = 'http://restapi.amap.com/v3/direction/transit/integrated'
walk_api = 'http://restapi.amap.com/v3/direction/walking'
distance_api = 'http://restapi.amap.com/v3/distance' 

header = {
    'Content-Type':'application/json'
}

def address_to_lon_lat(origin_address,distination_address):
    param = {
        'key':api_key,
        'address':origin_address + '|' + distination_address,
        'batch':'true'
    }
    geocode = requests.get(geocode_api,params = param,headers = header)
    return geocode.json()

def get_bus(origin = '',distination = ''):
    param = {
        'key':api_key,
        'origin':origin,
        'destination':distination,
        'city':''
    }
    response = requests.get(bus_api,params = param)
    print response.url
    return response.json()

def get_point_distance(origin = '',distination = ''):
     param = {
         'key':api_key,
         'origins':origin,
         'destination':distination,
         'type':'3'
     }
     response = requests.get(distance_api,params = param)

     print response.content
    

        

def search_route(origin = '' , distination = '' ):
   
    geocode_json = address_to_lon_lat(origin,distination)
    geocodes = geocode_json['geocodes']
    origin_lon_lat = ''
    distination_lon_lat = ''
    i = 0 
    for geocode in geocodes :
        if i == 0 :
            origin_lon_lat = geocode['location']
            i += 1
        else:
            distination_lon_lat = geocode['location']

    get_point_distance(origin_lon_lat,distination_lon_lat)            
        
    # bus_json = get_bus(origin_lon_lat,distination_lon_lat)        

    # print bus_json



if __name__ == '__main__':
    search_route('松滋市黄杰小学','松滋市实验小学')