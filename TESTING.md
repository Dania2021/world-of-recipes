# Testing

## Table of Contents

* [Testing user stories](#testing-user-stories)
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

## Testing User Stories

   * ### As a user I can create an account so that I can interact with other user content and create my own.

      * User is able to register an account by clicking Signup. 
      * User is able to fill in the Signup form with personal information to register an account.

   * ### As a user I can select and view full recipe.

      * The recipe title in the Recipe List page is provided as a link so that Site Users can access the Recipe Detail page for each specific recipe.
      * A Recipe Detail page is provided for all Site Users to review the full recipe content.

   * ### As a user I can search recipes by title so that I can find recipes quickly.

      * A Recipe Search field has been provided to all Site Users in the top of all pages.
      * This search field allow all Site Users to search recipes using keyword Title.
      * The list gets paginated if the Search Results exceed 6 recipes.

   * ### As a user I can search recipes by ingredients so that I can find particular recipes.

      * This search field allow all Site Users to search recipes using keyword ingredients.
      * A Search Results page with a list of recipes matching the searched ingredient is provided.

   * ### As a user I can view paginated list of recipes so that I can easily select the recipe to view.

      * The Recipe List displayed in the Recipe list page is paginated every 6 recipes.
      * Navigation buttons are provided on the bottom of each page to navigate easily between pages.

   * ### As a first time user I can navigate the site easily so that I know what the site is about.

      * The site's pages clearly display the navigation menu so that user is able find sufficient information at the first time.  

   * ### As a first time user I can access the site easily so that I can view the site on any media screens with different browsers.

      * The site is responsive from 320px up to 4K screens.
      * The site works fine using Google Chrome, Microsoft Edge, Firefox and Safari browsers. 

   * ### As a user I can view comments on an individual recipe so that I read the conversation.

      * Recipe's comments are being listed inside the Recipe Detail page for each specific recipe under the recipe content.
      * Comments are being sorted from oldest to newset comment so that site user can view all comments.

   * ### As a registered user I can login in into my account so that I can access the site features.

      * If a user is not logged into an account, a login link is provided on the navbar.

   * ### As a registered user I can logout so that I can keep my account secure.

      * If a user wants to logout his/her account, a logout link is provided on the navbar.

   * ### As a registered user I can add and view my profile so that I know my account details.

      * An Add Profile page has been provided for registered Site Users.
      * A form is available in the Profile page for the Site Users to be able to add the profile.

   * ### As a registered user I can delete my profile from the site so that if longer use it.

      * Delete Profile modal has been provided for registered Site Users.
      * A modal is available inside Recipe page for the site users to be able to delete the profile.
      * Delete button is displayed on profile the user has created to access the Delete Profile modal.

   * ### As a registered user I can add recipes so that I can share it with others.

      * An Add Recipe page has been provided for registered Site Users. 
      * A form is available in the Add Recipe page for the Site Users to be able to upload new recipes.
      * An Add Recipe button is displayed to the registered Site Users at the top of the Recipe page to access the Add Recipe page.

   * ### As a registered user I can update my recipes so that I can manage my recipe content.

      * Edit Recipe page has been provided for registered Site Users. 
      * A form is available inside Edit Recipe page for the Site Users to be able to edit a specific recipe. 
      * The Edit Recipe form is prepopulated with the current data for the user to be able to edit the content.
      * Edit button is displayed on recipe the user has created to access the Edit Recipe page. 

   * ### As a registered user I can delete my recipes so that I can manage my recipes and also controls the recipe that I share.

      * Delete Recipe modal has been provided for registered Site Users.
      * A modal is available inside Recipes page for the site users to be able to delete a specific recipe.
      * Delete button is displayed on recipe the user has created to access the Delete Recipe modal. 

   * ### As a registered user I can update my profile so that I can update my details and manage my account as I wish.

      * Edit Profile page has been provided for registered Site Users. 
      * A form is available inside Edit Profile page for the Site Users to be able to edit the profile. 
      * The Edit Profile form is prepopulated with the current data for the user to be able to edit the content.
      * Edit button is displayed on profile the user has created to access the Edit Profile page.   

   * ### As a registered user I can comment on recipes so that I can give feedback and recommendations.

      * Add Comment page has been provided for registered Site Users.
      * A form is available in the Recipe Detail page for the Site Users to be able to add comments to the recipes.
      * An Add Comment button is displayed to the registered Site Users beside the Recipe content inside the Recipe Detail page.

   * ###  As a site admin I can approve or disapprove comments so that I can filter out objectionable comments.

      * The site has an admin site to manage the data.
      * The site admin can remove any comments that are offensive.

   * ### As an admin I can navigate the admin panel so that I can create, read, update and delete the data on the site.

      * An admin site has been provided so that the Site Admin can manage profile, recipes and comments.
      * Profile and recipes can be created, read, updated and deleted from the site.
      * Comments can be read and created from the site.
      * Profile, recipes and comments can be filtered and searched to narrow down a specific group.

   
              



               

    
         



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