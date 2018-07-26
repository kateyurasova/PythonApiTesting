import os


def pytest_logger_config(logger_config):
    logger_config.add_loggers(['foo', 'bar', 'baz'], stdout_level='info')
    logger_config.set_log_option_default('foo,bar')


def pytest_logger_logdirlink(config):
    return os.path.join(os.path.dirname(__file__), 'mylogs')
