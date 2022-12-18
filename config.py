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
