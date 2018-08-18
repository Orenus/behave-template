@regex_system
Feature: testing system requirements with regioun and price

    Scenario: testing tiny image and price in US
        Given number of CPUs is 1
        And deployment region is "us-east"
        And memory is 1
        Then image class should be tiny
        And price should be 0.41 per hour

    Scenario: testing xlarge image and price in Asia Pacific
        Given number of CPUs is 3
        And deployment region is "ap-northeast"
        And memory is 3
        Then image class should be xlarge
        And price should be 1.51 per hour

    @my_app_start_and_access @advanced_regex
    Scenario: starting 2 instances in Asia Pacific and verifying access
        When I start 2 xlarge instances with "my-application-image" in the "ap-northeast" region
        Then I should be able to access them on port 8080

    @mysql_start_and_access @advanced_regex
    Scenario: starting mysql instance in US West and verifying access
        When I start a tiny instance with "mysql-db-image" in the "us-west" region
        Then I should be able to access it on port 3306