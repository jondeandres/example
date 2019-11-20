


def pytest_configure():
    from example import application
    application.initialize()
