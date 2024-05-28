import yaml

config = yaml.load(open('../config.yml', 'r', encoding='utf-8'), Loader=yaml.FullLoader)

ACCESS_URL = "https://bots.qq.com/app/getAppAccessToken"
db_host = config['database']['host']
db_port = config['database']['port']
db_user = config['database']['username']
db_password = config['database']['password']
db_name = config['database']['table']


class BaseConfig(object):
    SELECT_KEY = 'YUDREAM'
    JWT_SECRET_KEY = 'YUDREAM'
    DEBUG = False
    TESTING = False
    STATIC_FOLDER = './application/static'
    STATIC_URL_PATH = 'static'

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
