"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, be, have


@pytest.mark.desktop
@pytest.mark.parametrize("desktop_device", [(1920, 1080), (3440, 1440), (3840, 2160)], indirect=True)
def test_sign_in_desktop(desktop_device):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()
    browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.mobile
@pytest.mark.parametrize("mobile_device", [(750, 1334), (720, 1280)], indirect=True)
def test_sign_in_mobile(mobile_device):
    browser.open('https://github.com')
    browser.element('.js-details-target.Button--link').should(be.clickable).click()
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()
    browser.element('#login').should(have.text('Sign in to GitHub'))
