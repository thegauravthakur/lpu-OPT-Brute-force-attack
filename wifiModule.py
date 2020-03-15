import subprocess


class WifiModule:
    wifiName = ''

    @staticmethod
    def get_wifi_name():
        return subprocess.check_output(['iwgetid', '-r']).decode('utf -8')
