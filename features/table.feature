@image_class_table
Feature: testing system image classes with tables

    Scenario Outline: basic testing system images classes with tables
        Given number of CPUs is <cpu>
        And memory is <mem>
        Then image class should be <image_class>

        Examples: required resources
            | cpu | mem | image_class |
            | 1   | 1   | tiny        |
            | 1   | 2   | small       |
            | 2   | 2   | medium      |
            | 4   | 4   | large       |
            | 3   | 3   | xlarge      |
