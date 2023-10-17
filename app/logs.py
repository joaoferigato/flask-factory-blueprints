from logging import config
import datetime
import os


def create_logs_folder():
    logs_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))
    if not os.path.exists(logs_folder):
        print(f'Will create folder logs at: {logs_folder}')
        os.mkdir(logs_folder)

    return logs_folder


def log_file_name():
    logs_folder = create_logs_folder()
    now = datetime.datetime.now()
    file_name = now.strftime('%Y_%m_log.log')
    log_file = os.path.abspath(os.path.join(logs_folder, file_name))

    return log_file


def initialize_log():
    log_config = {
        'version': 1,
        'disable_existing_loggers': True,
        'loggers': {
            'app_log': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': False
            }
        },
        'handlers': {
            'file': {
                'formatter': 'std_out',
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'DEBUG',
                'filename': log_file_name(),
                'maxBytes': 5000000,
                'backupCount': 10,
                'encoding': 'utf-8'
            }
        },
        'formatters': {
            'std_out': {
                'format': '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s: %(lineno)d]',
            }
        },
    }

    config.dictConfig(log_config)
