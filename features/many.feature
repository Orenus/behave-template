 @many_scenario
 Feature: many scenarios feature

    Scenario: 1st scenario out of many...
        Given we have behave installed
        When we implement a test
        Then behave will test it for us!
    @sanity
    Scenario: 2nd scenario out of many...
        Given we have behave installed
        When we implement a test
        Then behave will test it for us!

    @wip
    Scenario: 3rd scenario out of many...
        Given we have behave installed
        When we implement a test
        Then my variable should be "ok"