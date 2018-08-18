# Behave Testing Automation Framework for Python

This repo demonstrates BDD in python using the Behave module.
It include examples to:

- Defining steps - with Gherkin's GWT (Given Then When)
- Steps impl - simple, using vars, using tables and using regular expressions
- Using tags to group scenarios and features
- reporting

## Installing

    pip install -r requirements.txt

## General guidlines for writing features and scenarios

1. Write your feature files under /features folder (you can nest them as much as you want. ex `/features/module1/subModule1` )
2. Always tag your scenarios with a unique tag first, then additional "grouping" tag.

- ex:
  `@stopAllServers @sanity # v correct`
  `@sanity @test # x incorrect`

3. The test implementation should go under the /steps folder.

- It is recommended for the steps files to correlate to the feature file names.
  Exception to the above should come when you are familiar enough with the basics, then
  one can break his steps into sparate files. ex:
  `/steps/system.step.py`
  `/steps/sub_system.step.py`
  `/steps/system_backgrounds.step.py`

## Running

1. All tests run:
   `> behave`

2. Running a tagged test (feature or scenario having @someTag):
   `> behave --tags=sanity,someOtherTag`

3. Running tests excludding specified tags:
   `> behave --tags=~excludeMe`

4. Running a specific feature file scenarios only:
   `> behave features/featureFile.feature`

## Reporting

You can use the followimng commandline options to generate a test report
`> behave -f json -o reports/report.json`

The generated reports can then be used by jenkins plugins or other reporters to visualize the results.
For additional formats see here: https://behave.readthedocs.io/en/latest/formatters.html

I have added an HTML report in the reports folder. Its an example of a cucumber html generated using the following procedure:

1. Install npm (nodejs) from https://www.npmjs.com/get-npm
2. From the commandline run `npm install cucumber-html-reporter -g`
3. Run `pip install behave2cucumber`
4. When running behave allow it to generate the json report as described above.
5. Then convert the behave json to cucumber format:
   `python -m behave2cucumber -i reports/report.json -o reports/cucumber.json -f`
6. Run the cucumber reports generator:
   `node reports/html_reporter.js`
