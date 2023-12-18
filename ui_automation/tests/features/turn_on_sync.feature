@hotlink @turnonsync
  Feature: As a user,I want to use Chrome App on Android device.

    Background:
      Given The use launch the Chrome

    Scenario: The user want to use Chrome App on Android device.
      When The user launch Chrome to go the welcome page
      Then The user click no thanks button, and go to chrome notification page
