import os
import logging
import allure
import pytest


def pytest_logger_config(logger_config):
    logger_config.add_loggers(['foo', 'bar', 'baz'], stdout_level='info')
    logger_config.set_log_option_default('foo,bar')


def pytest_logger_logdirlink(config):
    return os.path.join(os.path.dirname(__file__), 'mylogs')


class AllureLoggingHandler(logging.Handler):
    def log(self, message):
        with allure.step('Log {}'.format(message)):
	        pass

    def emit(self, record):
        self.log("({}) {}".format(record.levelname, record.getMessage()))

class AllureCatchLogs:
    def __init__(self):
        self.rootlogger = logging.getLogger()
        self.allurehandler = AllureLoggingHandler()
    def __enter__(self):
        if self.allurehandler not in self.rootlogger.handlers:
            self.rootlogger.addHandler(self.allurehandler)
    def __exit__(self, exc_type, exc_value, traceback):
        self.rootlogger.removeHandler(self.allurehandler)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup():
    with AllureCatchLogs():
        yield

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call():
    with AllureCatchLogs():
        yield

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown():
    with AllureCatchLogs():
        yield