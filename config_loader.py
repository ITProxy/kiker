import configparser

class Config:
    def __init__(self, config_file='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
    
    def get_flask_config(self):
        return {
            'SECRET_KEY': self.config['flask']['secret_key'],
            'SQLALCHEMY_DATABASE_URI': self.config['flask']['database_uri']
        }

    def get_server_config(self):
        return {
            'debug': self.config.getboolean('server', 'debug'),
            'port': self.config.getint('server', 'port'),
            'host': self.config['server']['host']
        }
