@image_class
Feature: testing system requirements

    Scenario: testing tiny image class
        Given number of CPUs is 1
        And memory is 1
        Then image class should be tiny

    Scenario: testing small image class
        Given number of CPUs is 1
        And memory is 2
        Then image class should be small

    Scenario: testing medium image class
        Given number of CPUs is 2
        And memory is 2
        Then image class should be medium

    Scenario: testing xlarge image class
        Given number of CPUs is 3
        And memory is 3
        Then image class should be xlarge