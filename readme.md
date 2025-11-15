# Devops Activity Practice

## Addiontal endpoints

1. /goodbye [GET]
   - added another simple get method that returns goodbye to match the hello GET endpoint
2. /mood [POST]
   - added a mood POST endpoint to return a sentence of the user mood if given a valid json

## Struggles

    Codeql-analysis.yml
    - This didn't work at first for two reason deprecated version number and lack of permission
        - To use the most recent version number v4 and added a permission block in the test

    test.yml
        - accidentily removed the 'on' feature and syntax was malformed
    dependabot.yml
        - there's an issue with dependabot not reading UTF-16 files which is generated when using pip freeze to generate the requirements.txt. To fix, you have to write the requirements.txt yourself
