import base64

if __name__ == '__main__':
    with open('valid_configs.txt') as f:
        lines = f.read().split('\n')
    # تولید لینک سابسکریپشن Base64
    sub_link = base64.b64encode('\n'.join(lines).encode()).decode()
    with open('sub.txt', 'w') as f:
        f.write(sub_link)
