"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""

import pytest
from selene import browser, be, have


@pytest.mark.desktop
def test_sign_in_desktop(is_desktop_device):
    if not is_desktop_device:
        pytest.skip(reason='desktop devices test only')
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()
    browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.mobile
def test_sign_in_mobile(is_mobile_device):
    if not is_mobile_device:
        pytest.skip(reason='mobile devices test only')
    browser.open('https://github.com')
    browser.element('.js-details-target.Button--link').should(be.clickable).click()
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()
    browser.element('#login').should(have.text('Sign in to GitHub'))

