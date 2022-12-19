##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
