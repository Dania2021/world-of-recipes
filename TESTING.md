# Testing

## Table of Contents

* Testing user stories
* Manual Testing
* [Validator Testing](#validator-testing)
  * [W3C HTML Validator](#w3c-html-validator)
  * [W3C CSS Validator](#w3c-css-validator)
  * [JSHint JavaScript validator](#jshint-javascript-validator)
  * [Python Validation](#python-validation)
* [Lighthouse Testing](#lighthouse-testing)
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

## Lighthouse Testing
  
   All pages were ran through Lighthouse on Chrome Devtools for both desktop and mobile device display and ran in incognito mode. 

   * ### Home Page

     * Lighthouse report for desktop

       ![lighthouse-desktop-home](/readme_docs/lighthouse-home.png)

     * Lighthouse report for mobile

       ![lighthouse-mobile-home](/readme_docs/lighthouse-mobile-home.png)  

   * ### Recipe List Page    

      * Lighthouse report for desktop

       ![lighthouse-desktop-recipe-list](/readme_docs/lighthouse-recipes.png)

      * Lighthouse report for mobile
     
        ![lighthouse-mobile-recipe-list](/readme_docs/lighthouse-mobile-recipes.png)

   * ### Login Page

       * Lighthouse report for desktop

         ![lighthouse-desktop-login](/readme_docs/lighthouse-login.png)

       * Lighthouse report for mobile

          ![lighthouse-mobile-login](/readme_docs/lighthouse-mobile-login.png)

   * ### Signup Page

       * Lighthouse report for desktop

         ![lighthouse-desktop-signup](/readme_docs/lighthouse-signup.png)

       * Lighthouse report for mobile  

          ![lighthouse-mobile-signup](/readme_docs/lighthouse-mobile-signup.png)

   * ### Recipe Detail Page

       * Lighthouse report for desktop
     
           ![lighthouse-desktop-recipe-detail](/readme_docs/lighthouse-recipe-detail.png)

       * Lighthouse report for mobile
         
           ![lighthouse-mobile-recipe-detail](/readme_docs//lighthouse-mobile-recipe-detail.png)

   * ### Recipe Add Page

       * Lighthouse report for desktop

           ![lighthouse-desktop-recipe-add](/readme_docs/lighthouse-recipe-add.png)

       * Lighthouse report for mobile   

           ![lighthouse-mobile-recipe-add](/readme_docs/lighthouse-mobile-add-profile.png)

   * ### Recipe View Page    

       * Lighthouse report for desktop   

          ![lighthouse-desktop-recipe-view](/readme_docs/lighthouse-recipe-view.png)

       * Lighthouse report for mobile    

          ![lighthouse-mobile-recipe-view](/readme_docs/lighthouse-mobile-recipe-view.png) 

  * ### My Recipes Page

    * Lighthouse report for desktop      

        ![lighthouse-desktop-my-recipes](/readme_docs/lighthouse-mobile-my-recipes.png)

    * Lighthouse report for mobile   

        ![lighthouse-mobile-my-recipes](/readme_docs/lighthouse-mobile-my-recipes.png)

  * ### Profile Edit Page

    * Lighthouse report for desktop     

        ![lighthouse-desktop-profile-edit](/readme_docs/lighthouse-edit-profile.png)

    * Lighthouse report for mobile 

        ![lighthouse-mobile-profile-edit](/readme_docs/lighthouse-mobile-edit-profile.png)  