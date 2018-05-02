#Python记录日志
import logging
import time
import os



'''

log_path = os.path.dirname(os.getcwd()) + '\logs\\'

print(log_path)
'''
class Logger(object):
    ''' '''
    def __init__(self,logger):
        rq = time.strftime('%Y%m%d',time.localtime(time.time()))
        base_dir=os.path.dirname(os.path.dirname(__file__))
        base_dir=str(base_dir)
        base_dir=base_dir.replace('\\', '/')
        log_path=base_dir+"/logs/"
        setting = {
                   'logpath':log_path,
                   'filename':'baiduyun_' + rq + '.log'
                   }

        self.path = setting['logpath']
        self.filename = setting['filename']
        self.logger = logger
        self.logger = logging.getLogger(self.logger)
        self.logger.setLevel(logging.INFO)
        self.fh = logging.FileHandler(self.path + self.filename)
        self.fh.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s-%(filename)s[line:%(lineno)d]-%(levelname)s - %(message)s')
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)

        self.ch=logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)
        self.ch.setFormatter(self.formatter)
        self.logger.addHandler(self.ch)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def close(self):
        self.logger.removeHandler(self.fh)

    def getlog(self):
        return self.logger