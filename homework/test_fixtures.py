"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

import pytest
from selene import browser, be, have


@pytest.mark.desktop
def test_sign_in_desktop(desktop_device):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()
    browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.mobile
def test_sign_in_mobile(mobile_device):
    browser.open('https://github.com')
    browser.element('.js-details-target.Button--link').should(be.clickable).click()
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()
    browser.element('#login').should(have.text('Sign in to GitHub'))
