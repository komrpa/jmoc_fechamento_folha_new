from subprocess import call
import os
import glob


def executar_exe_java():

    def get_download_path():
        """Returns the default downloads path for linux or windows"""
        if os.name == 'nt':
            import winreg
            sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
            downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                location = winreg.QueryValueEx(key, downloads_guid)[0]
            return location
        return os.path.join(os.path.expanduser('~'), 'downloads')

    path_downloads = get_download_path()

    try:
        # * means all if need specific format then *.csv
        list_of_files = glob.glob(path_downloads + os.sep + '*.jnlp')

        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)

        file_execute = os.path.join(
            'javaws', ' ', path_downloads, latest_file)
        print(file_execute)
        os.system(file_execute)
        # call([os.path.join(path_downloads, java_file)], timeout=5)
    except:
        pass

    # for java_file in os.listdir(path_downloads):
    #     if '.jnlp' in java_file:
    #         try:
    #             file_execute = os.path.join(
    #                 'javaws', ' ', path_downloads, latest_file)
    #             print(file_execute)
    #             os.system(file_execute)
    #             # call([os.path.join(path_downloads, java_file)], timeout=5)
    #         except:
    #             pass


if __name__ == '__main__':
    executar_exe_java()
