import requests
import redis

def handle_request(request):

    payload = {}
    headers = {}
    url = "https://api.mercadolibre.com/"

    response = requests.request(request.method, url+request.path,
                                data=request.get_json()).json()
    return response

def visit_count(request):
    redis_host = '10.115.152.244'
    redis_port =  6379
    redis_client = redis.Redis(
        host=redis_host, 
        port=redis_port, 
        db=0, 
        socket_connect_timeout=10
    )
    value = redis_client.incr('visits', 1)
    print('Visit count: {}'.format(value))
    redis_client.disconnect()