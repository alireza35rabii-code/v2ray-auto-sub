import requests

def fetch_configs():
    # منابع کانفیگ‌های رایگان
    sources = [
        'https://raw.githubusercontent.com/v2ray-sources/free-configs/main/configs.txt',
        # میتونی منابع بیشتر اضافه کنی
    ]
    configs = []
    for url in sources:
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                configs += r.text.strip().split('\n')
        except:
            continue
    return configs

if __name__ == '__main__':
    all_configs = fetch_configs()
    with open('all_configs.txt', 'w') as f:
        for c in all_configs:
            f.write(c + '\n')
