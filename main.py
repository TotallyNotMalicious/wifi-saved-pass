import os

networks = [
    line.split(': ')[1] for line in os.popen('netsh wlan show profile').read().splitlines()
    if 'User Profile' in line
]

for network in networks:
    print(f'SSID: {network}')

    os.system('cls && netsh wlan export profile folder=. key=clear >NUL')

    for file in os.listdir(os.curdir):
        if file.endswith('.xml'):
            network = file.replace('Wi-Fi-', '').replace('.xml', '')
            with open(file, 'r') as f:
                password = f.read().split('<keyMaterial>')[1].split(
                    '</keyMaterial>'
                )[0].replace('&lt;', '<').replace('&gt;', '>')
                print(f'SSID: {network.ljust(5)}\nPass: {password}\n-----------------------------------------')

    for file in os.listdir(os.curdir):
        if file.endswith('.xml'):
            os.remove(file)

os.system('pause >NUL')