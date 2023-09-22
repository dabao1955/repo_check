import requests

def filter_urls(file_path):
    filtered_urls = []
    with open(file_path, 'r') as f:
        for line in f:
            url = line.strip()
            response = requests.get(url)
            status_code = response.status_code
            if status_code == 301:
                new_url = response.headers['Location']
                url_pair = url + ' > ' + new_url
                filtered_urls.append(url_pair)
            if status_code == 404:
                filtered_urls.append(url)
    return filtered_urls

result = filter_urls('repos.txt')

print (result)
