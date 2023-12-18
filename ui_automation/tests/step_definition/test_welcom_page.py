"""As a new-monitor user, feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers,
)

from ui_automation.page_objects.welcome_page.welcome_page_object import WelcomePageObject


@scenario("../features/turn_on_sync.feature", 'The user want to use Chrome App on Android device.')
def test_launch():
    """The user want to use Chrome App on Android device"""
    pass

@given('The use launch the Chrome')
def launch_chrome_app():
    """The user launch Chrome APP"""
    WelcomePageObject.launch_chrome("")


@when('The user launch Chrome to go the welcome page')
def check_navigation_in_welcome_page():
    """The user go to chrome welcome page"""
    WelcomePageObject.check_welcome_page("")


@then('The user click no thanks button and to go the turn on sync page')
def go_to_turn_on_page():
    """The user click no thanks button and to go the turn on sync page"""
    WelcomePageObject.go_to_welcome_page_with_no_thank_button("")


