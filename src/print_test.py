from logging import logger

def hello_world(who: str):
    logger.info('starting skynet')
    #skynet.init()

    print(f'--> debug, skynet init vector is {who}')
    return f'Hello, {who}'