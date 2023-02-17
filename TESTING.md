# Testing

## Table of Contents

* Testing user stories
* Manual Testing
* [Validator Testing](#validator-testing)
  * [W3C HTML Validator](#w3c-html-validator)
  * [W3C CSS Validator](#w3c-css-validator)
  * [JSHint JavaScript validator](#jshint-javascript-validator)
  * [Python Validation](#python-validation)
* Lighthouse Testing
* Browser Compatibility Testing
* Tools Testing
* Bugs
    * Resolved Bugs
    * Unresolved Bugs

## Validator Testing

  * ### W3C HTML Validator

    The W3C HTML Validator service was used to validate the HTML code of the project in order to ensure there were no syntax errors.
    W3C HTML Validator found the following error:

    ![error-image](/readme_docs/error-img.png)

    The error was resolved by removing width and height attribute from img tag.

    ![html-validator](/readme_docs/html-validator.png)

  * ### W3C CSS Validator

    The custom CSS for the site passed through the W3C Jigsaw CSS validator with no issues

    ![css-validator](/readme_docs/css-validator.png)

  * ### JSHint JavaScript validator

    The small amount of custom JavaScript code for the project was passed through the JSHint validator. Note that JSHint flags an issue with an undefined bootstrap variable, however this is because JSHint does not have access to the Bootstrap CDN import defined within a script tag in the base.html template.  

    ![jshint-validator](/readme_docs/jshint-img.png)

  * ### Python Validation

    The PEP8 validator was down at the time this project was developed, therefore Python code was validated using the pycodestyle tool, which was installed to the IDE (GitPod). Any issues found have been rectified and all pages now pass with no errors or warnings to show.

    * worldofrecipes/settings.py
    * worldofrecipes/urls.py
    * worldofrecipes/wsgi.py
    * recipes/admin.py
    * recipes/apps.py
    * recipes/forms.py
    * recipes/models.py
    * recipes/signals.py
    * recipes/urls.py
    * recipes/views.py
