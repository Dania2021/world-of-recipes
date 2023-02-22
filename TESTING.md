# Testing

## Table of Contents

* [Testing user stories](#testing-user-stories)
* [Manual Testing](#manual-testing)
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

## Manual Testing 

   * ### Site testing

     | Feature | Expected Outcome | Testing Performed | Result |Pass/Fail |
     | --- | --- | --- | --- | --- |
     | Navbar |  |  |  |  |
     | WorldofRecipes Title | When clicked the user will be redirected to the home page | Clicked title  | Redirected to the home page | Pass |
     | Home Page Link | When clicked the user will be redirected to the home page | Clicked link | Redirected to the home page | Pass |
     | Recipes Page Link | When clicked the user will be redirected to the List of Recipes page | Clicked link |  Redirected to the list of recipes | Pass |
     | Login Page Link | When clicked the user will be redirected to the Login Page  | Clicked link  | Redirected to the login page | Pass |
     | SignUp Page Link | When clicked the user will be redirected to the Signup Page | Clicked link | Redirected to the signup page | Pass |
     | Search Link | When clicked the user will be redirected to the search page | Clicked link | Redirected to the search page | Pass |
     | Profile Link (Logged in users only) | When clicked the user will be redirected to the Recipe page | Clicked link | Redirected to the recipe page | Pass |
     | Logout Page Link(Logged in users only) | When clicked the user will be redirected to the logout page | Clicked link | Redirected to the logout page | Pass |
     | Footer |  |  |  |  |
     | Facebook icon | Clicking the link open Facebook page on a separate tab | Clicked link | Redirected to the facebook page | Pass |
     | Instagram icon | Clicking the link open Instagram page on a separate tab | Clicked link | Redirected to the instagram page | Pass |
     | Twitter icon | Clicking the link open Twitter page on a separate tab | Clicked link | Redirected to the twitter page | Pass |

   * ### Home Page Testing

       | Feature | Expected Outcome | Testing Performed | Result |Pass/Fail |
       | --- | --- | --- | --- | --- |
       | HomePage |  |  |  |  |
       | Recipe Link | When clicked the user will be redirected to the List of Recipes page | Clicked link | Redirected to the list of recipes | Pass |
       | Add Recipe Link |  When clicked the user will be redirected to the Login page | Clicked link | Redirected to the login page | Pass |
       | Add Recipe Link (Logged in users only) | When clicked the user will be redirected to the Recipe Add page | Clicked link | Redirected to the recipe add page | Pass | 

   * ### Login Page Testing    

       | Feature | Expected Outcome | Testing Performed | Result |Pass/Fail |
       | --- | --- | --- | --- | --- |
       | Login Page |  |  |  |  |
       | Username input - empty | This is a required field so the form should not submit if empty | Tried to submit the form with this field empty | Tooltip tells me this field is required | Pass |
       | Password input empty | This is a required field so the form should not submit if empty | Tried to submit the form with this field empty | Tooltip tells me this field is required | Pass |
       | Login button | Clicking the button authenticates the user and redirect to the Home page, Display message when user login successfully | Submitted form | Redirected to the home page and message shown | Pass |
       | Incorrect username or password used | Display message when credentials are not valid. | Incorrect username/password entered | Message display to let the user know they have entered an incorrect username/password | Pass |
       | Link to Signup page | This should redirect the user to the Signup page | Clicked link | Redirected to the signup page | Pass |

   * ### Signup Page Testing 

       | Feature | Expected Outcome | Testing Performed | Result |Pass/Fail |
       | --- | --- | --- | --- | --- |
       | Signup Page |  |  |  |  |
       | Username input - empty | The username is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
       | Username input | Username is in use, message should display to user | Entered an in use username | Message displayed to say username already in use | Pass |
       | Email input | The email input should include an email address | Entered plain text | Tooltip tells user to use an email address | Pass |
       | Email input | Email address is in use, message should display to user | Entered an in use email address | Message displayed to say email address already in use | Pass |
       | Password input | This field should be at least 8 characters | Entered password less than 8 characters | Tooltip tells user the password should be at least 8 characters | Pass |
       | Password input - empty | The password is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
       | Password (again) input | Display message if both passwords are not equal | Entered password and password(again) are not same | Tooltip tells user the password should same at each time | Pass |
       | Password (again) input - empty | The password is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
       | Signup Button | Should redirect user to the Profile page and display message that user is successfully created | Created new user and submitted form | Redirected to the profile page and message displayed | Pass |
       | Link to Login page | This should redirect the user to the Login page | Clicked link | Redirected to the login page | Pass |

   * ### Recipes List Page Testing

       | Feature | Expected Outcome | Testing Performed | Result |Pass/Fail |
       | --- | --- | --- | --- | --- |
       | Recipes List Page |  |  |  |  |
       | Recipe Title link | This should redirect the user to the Recipe Detail page | Clicked link | Redirected to the recipe detail page | Pass |
       | Pagination | Should paginate if more than 6 recipes are listed | Site Pagination | Pagination is occurring when more than 6 recipes are listed | Pass |
       | Pagination Buttons | Should redirect to next or previous page of Recipes List | Clicked Button | Redirect to the next or previous page of recipes list | Pass |

   * ### Recipe Detail Page Testing

       | Feature | Expected Outcome | Testing Performed | Result |Pass/Fail |
       | --- | --- | --- | --- | --- |
       | Recipe Detail Page |  |  |  |  |
       | Body Input- empty (Logged in users only) | Body is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
       | Add Comment Button (Logged in users only) | This should redirect the user to the Recipe Detail page and display message that comment added | Submitted form | Redirected to the recipe detail page and message displayed | Pass |
       | Cancel Link (Logged in users only) | This should redirect the user to the Recipes List page | Clicked Link | Redirect to the recipes list page | Pass |
       | Link to Login page | This should redirect the user to the Login page | Clicked link | Redirected to the login page | Pass |


   * ### Recipe Add Page Testing 

       | Feature | Expected Outcome | Testing Performed | Result |Pass/Fail |
       | --- | --- | --- | --- | --- |
       | Recipe Add Page (Logged in users only) |  |  |  |  |
       | Title Input- empty | Title is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
       | Ingredients Input- empty | Ingredients is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass | 
       | Steps Input- empty | Steps is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass | 
       | Serves Input- empty | Serves is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
       | Duration Input- empty | Duration is a required field, so should not submit with no value | Tried to submit form with no value entered | Tooltip lets user know this value is required | Pass |
       | Add Recipe Button | This should redirect the user to the Recipe page and display message that recipe added successfully | Submitted form | Redirected to the recipe page and message displayed | Pass |
       | Cancel Link | This should redirect the user to the Recipe page | Clicked Link | Redirect to the recipe page | Pass |  

   * ### Recipe Edit Page Testing 

       | Feature | Expected Outcome | Testing Performed | Result |Pass/Fail |
       | --- | --- | --- | --- | --- |
       | Recipe Edit Page (Logged in users only) |  |  |  |  |    
       | Title input | This is a required field so should ask for a value to be entered if empty. This field should be pre-populated with the recipe information saved to the database | Input was pre-populated. Cleared the input | Tooltip told me it is a required field | Pass |
       | Ingredients input | This is a required field so should ask for a value to be entered if empty. This field should be pre-populated with the recipe information saved to the database | Input was pre-populated. Cleared the input | Tooltip told me it is a required field | Pass |
       | Steps input | This is a required field so should ask for a value to be entered if empty. This field should be pre-populated with the recipe information saved to the database | Input was pre-populated. Cleared the input | Tooltip told me it is a required field | Pass | 
       | Serves input | This is a required field so should ask for a value to be entered if empty. This field should be pre-populated with the recipe information saved to the database | Input was pre-populated. Cleared the input | Tooltip told me it is a required field | Pass |
       | Duration input | This is a required field so should ask for a value to be entered if empty. This field should be pre-populated with the recipe information saved to the database | Input was pre-populated. Cleared the input | Tooltip told me it is a required field | Pass | 
       | Skill Level Dropdown | This field should be pre-populated with the recipe information saved to the database | Checked to see correct skill level was displayed | Correct skill level displayed | Pass |
       | Cuisine Name Dropdown | This field should be pre-populated with the recipe information saved to the database | Checked to see correct cuisine name was displayed | Correct cuisine name displayed | Pass |
       | Update Button | This should redirect the user to the Recipe page and display message that recipe updated | Submitted form | Redirected to the recipe page and message displayed | Pass |
       | Cancel Link | This should redirect the user to the Recipe page | Clicked Link | Redirect to the recipe page | Pass |  

   * ### Recipes Page Testing 

       | Feature | Expected Outcome | Testing Performed | Result |Pass/Fail |
       | --- | --- | --- | --- | --- |
       | Recipes Page (Logged in users only) |  |  |  |  |
       | Update Link | When the update link is clicked the user should be taken to the Recipe Edit page with the inputs pre-populated with the values stored in the database for that recipe | Clicked link | Redirected to the recipe edit page. Recipe details filled in with previously saved information | Pass |  
       | Delete button | When the user clicks this button a modal should pop up asking the user to confirm they want to delete this recipe | Clicked button | Modal popped up to confirm if I wanted to delete the recipe | Pass | 
       | Yes button on modal | When clicked the recipe should be deleted | Clicked button | Recipe Deleted from recipe page and recipes list page | Pass | 
       | No button on modal | When clicked the modal should close | Clicked button | Modal closed | Pass |

   * ### Profile Page Testing 

       | Feature | Expected Outcome | Testing Performed | Result |Pass/Fail |
       | --- | --- | --- | --- | --- |
       | Profile Page (Logged in users only) |  |  |  |  |
       | Add Profile Button | This should redirect the user to the Recipe page and display message that profile added successfully | Submitted form | Redirected to the recipe page and message displayed |  Pass |    

   * ### Profile Edit Page Testing 

       | Feature | Expected Outcome | Testing Performed | Result |Pass/Fail |
       | --- | --- | --- | --- | --- |
       | Profile Edit Page (Logged in users only) |  |  |  |  |
       | Update Button | This should redirect the user to the Recipe page and display message that profile updated successfully | Submitted form | Redirected to the recipe page and message displayed | Pass |
       | Cancel Link | This should redirect the user to the Recipe page | Clicked Link | Redirect to the recipe page | Pass |  
    
   * ### Recipe Page Testing 

       | Feature | Expected Outcome | Testing Performed | Result |Pass/Fail |
       | --- | --- | --- | --- | --- |
       | Recipe Page (Logged in users only) |  |  |  |  |
       | Update Link | When the update link is clicked the user should be taken to the Edit Profile page with the inputs pre-populated with the values stored in the database for that profile | Clicked link | Redirected to the edit profile page. Profile details filled in with previously saved information | Pass |  
       | Delete button | When the user clicks this button a modal should pop up asking the user to confirm they want to delete this profile | Clicked button | Modal popped up to confirm if I wanted to delete the profile | Pass | 
       | Yes button on modal | When clicked the profile should be deleted | Clicked button | 
       Profile Deleted | Pass | 
       | No button on modal | When clicked the modal should close | Clicked button | Modal closed | Pass |
       | Add Recipe Button | When the add button is clicked the user should be taken to the Recipe Add page | Clicked Button | Redirect to the recipe add page | Pass |
       | Recipe Title Link | When the link is clicked the user should be taken to the Recipes page | Clicked Link | Redirect to the recipes page | Pass |

   
   * ### Search Page Testing 

       | Feature | Expected Outcome | Testing Performed | Result |Pass/Fail |
       | --- | --- | --- | --- | --- |
       | Search Page |  |  |  |  |
       | Search Button | A search is performed when the user enters a search title | Submitted Form | The search returns recipe results | Pass |
       | Search Button | A search is performed when the user enters a search an ingredient | Submitted Form | The search returns recipe results | Pass |
       | Search - empty | When user submit no value in search field, displays you didnt search anything  | Submitted Form | Displayed message to the user | Pass | 
       | Search Doesnot Exist | When user submit value that doesnot exist, display message no results found | Submitted Form | Displayed message to the user | Pass |    
   
   * ### Logout Page Testing 

       | Feature | Expected Outcome | Testing Performed | Result |Pass/Fail |
       | --- | --- | --- | --- | --- |
       | Logout |  |  |  |  |
       | Log Out Button | Should redirect user to the Home page and display message that user is sign out successfully | submitted form | Redirected  to the home page and message displayed | Pass |
       | Cancel Link | Should redirect user to the Home page | Clicked Link | Redirect to the home page | Pass |

   * ### 404 Page Testing 

       | Feature | Expected Outcome | Testing Performed | Result |Pass/Fail |
       | --- | --- | --- | --- | --- |
       | 404 |  |  |  |  |
       | Home page link | Redirects the user to the home page | Clicked link | Redirected to home page | Pass |    

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