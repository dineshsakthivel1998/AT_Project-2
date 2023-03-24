import configparser

config = configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username=config.get('commonInfo', 'email')
        return username

    @staticmethod
    def getPassword():
        password=config.get('commonInfo', 'password')
        return password