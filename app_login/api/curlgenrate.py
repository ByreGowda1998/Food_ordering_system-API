import requests

def generate_curl_with_api_key(url, api_key):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    response = requests.get(url, headers=headers)
    
    
    curl_command = f"curl -X GET '{url}' -H 'Content-Type: application/json' -H 'Authorization: Bearer {api_key}'"
    
    return curl_command

