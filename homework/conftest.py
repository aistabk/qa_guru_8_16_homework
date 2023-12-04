import pytest
from selene.support.shared import browser


@pytest.fixture(params=[(1920, 1080), (3440, 1440), (3840, 2160)])
def desktop_device(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(750, 1334), (720, 1280)])
def mobile_device(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(1920, 1080), (3440, 1440), (3840, 2160), (750, 1334), (720, 1280)])
def is_desktop_device(request):
    resolution = request.param
    if resolution in [(1920, 1080), (3440, 1440), (3840, 2160)]:
        width, height = resolution
        browser.config.window_width = width
        browser.config.window_height = height

        return True
    else:
        return False


@pytest.fixture(params=[(2560, 1440), (1920, 1080), (3440, 1440), (3840, 2160), (750, 1334), (720, 1280)])
def is_mobile_device(request):
    resolution = request.param
    if resolution in [(750, 1334), (720, 1280)]:
        width, height = resolution
        browser.config.window_width = width
        browser.config.window_height = height

        return True
    else:
        return False



