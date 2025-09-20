import subprocess
import concurrent.futures

def test_config(config_line):
    # فرض می‌کنیم هر کانفیگ یک URL یا VMess است
    try:
        result = subprocess.run(['ping', '-c', '1', config_line.split('@')[-1]], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            return config_line
    except:
        return None

if __name__ == '__main__':
    with open('all_configs.txt') as f:
        configs = f.read().split('\n')

    valid_configs = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(test_config, configs)
        for r in results:
            if r:
                valid_configs.append(r)

    with open('valid_configs.txt', 'w') as f:
        for c in valid_configs:
            f.write(c + '\n')
