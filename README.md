# World Of Recipes

  ![title-image](/readme_docs/title-img.png)

World of recipes is a recipe website that allows the user to create and share recipes with other users from around the world. The website design is responsive so it can be used on any device.

This website is built in Django using Python, JavaScript, CSS/Bootstrap and HTML. The main objective of this website is to allow the users who enjoy their food and like to share recipe with others. It allows the user to create recipes and their profile with an image. Authenticated user can create recipe and leaves comment on the recipes. It includes user authentication and full CRUD functionality to the Recipes and User Profile.

Live Site:

## Table Of Contents

 * [Strategy](#strategy)
   * [User Stories](#user-stories)
      * [New and unregisterd User](#new-and-unregistered-user)
      * [Registered User](#registered-user)
      * [Admin CRUD / superuser](#admin-crudsuperuser)
 * [Scope](#scope)    
    * [Site Owner Stories](#site-owner-stories)
    * [Agile Development Methodology](#agile-development-methodology)
 * [Structure](#structure)
    * [Database ERD](#database-erd) 
    * [Wireframes](#wireframes)
 * [Skeleton](#skeleton)  
    * [Features](#features)
       * [General](#general)
       * [Home Page](#home-page)
       * Login Page
       * SignUp Page
       * Profile Page
       * Recipes Page
       * Search page
       * Logout Page
       * Admin Site
       * Future Features
    * [Technologies Used](#technologies-used)
       * [Languages Used](#languages-used)
       * [Libraries and Frameworks](#libraries-and-frameworks)
       * [Packages/Dependencies Installed](#packages--dependecies-installed)
       * [Databases Used](#databases-used)
       * [Programs Used](#programs-used)
 * [Surface](#surface)
    * [Design](#design)
      * [Colour Schemes](#colour-schemes)
      * [Typography](#typography)  
      * [Imagery](#imagery)
    * [Deployment](#deployment)
 * [Testing](#testing)
 * Credits
      * Content
      * Media
      * Code
 * Acknowledgement   

## Strategy

 * ### User Stories

    * #### New and unregistered user

      * [#1](https://github.com/Dania2021/world-of-recipes/issues/1) As a user I can create an account so that I can interact with other user content and create my own.
      * [#6](https://github.com/Dania2021/world-of-recipes/issues/6) As a user I can select and view full recipe.
      * [#10](https://github.com/Dania2021/world-of-recipes/issues/10) As a user I can search recipes by title so that I can find recipes quickly.
      * [#11](https://github.com/Dania2021/world-of-recipes/issues/11) As a user I can search recipes by ingredients so that I can find particular recipes.
      * [#13](https://github.com/Dania2021/world-of-recipes/issues/13) As a user I can view paginated list of recipes so that I can easily select the recipe to view.
      * [#14](https://github.com/Dania2021/world-of-recipes/issues/14) As a first time user I can navigate the site easily so that I know what the site is about.
      * [#15](https://github.com/Dania2021/world-of-recipes/issues/15) As a first time user I can access the site easily so that I can view the site on any media screens with different browsers.
      * [#16](https://github.com/Dania2021/world-of-recipes/issues/16) As a user I can view comments on an individual recipe so that I read the conversation.
   
   * #### Registered User

      * [#2](https://github.com/Dania2021/world-of-recipes/issues/2) As a registered user I can login in into my account so that I can access the site features.
      * [#3](https://github.com/Dania2021/world-of-recipes/issues/3) As a registered user I can logout so that I can keep my account secure.
      * [#4](https://github.com/Dania2021/world-of-recipes/issues/4) As a registered user I can add and view my profile so that I know my account details.
      * [#5](https://github.com/Dania2021/world-of-recipes/issues/5) As a registered user I can delete my profile from the site so that if longer use it.
      * [#7](https://github.com/Dania2021/world-of-recipes/issues/7) As a registered user I can add recipes so that I can share it with others.
      * [#8](https://github.com/Dania2021/world-of-recipes/issues/8) As a registered user I can update my recipes so that I can manage my recipe content.
      * [#9](https://github.com/Dania2021/world-of-recipes/issues/9) As a registered user I can delete my recipes so that I can manage my recipes and also controls the recipe that I share.
      * [#12](https://github.com/Dania2021/world-of-recipes/issues/12) As a registered user I can update my profile so that I can update my details and manage my account as I wish.
      * [#18](https://github.com/Dania2021/world-of-recipes/issues/18) As a registered user I can comment on recipes so that I can give feedback and recommendations.

   * #### Admin CRUD/superuser

     * [#17](https://github.com/Dania2021/world-of-recipes/issues/17) As a site admin I can approve or disapprove comments so that I can filter out objectionable comments.
     * [#19](https://github.com/Dania2021/world-of-recipes/issues/19) As an admin I can navigate the admin panel so that I can create, read, update and delete the data on the site.

## Scope

   * ### Site Owner Stories

      * The website is accessible and responsive. It targets the user who enjoys cooking, who would like to share their own recipes with others.
      * The site offers different user interface that user can sign up an account, log in and log out as well as edit the user profile.
      * The site offers registered user to upload and view recipe.
      * The site offers registered user to view and edit their account profile.
      * The site offers registered user to make comment on recipes and give their feedback.


   * ### Agile Development Methodology

     GitHub issues and projects were used to document and track an agile development approach. An issue was created for each user story. With the MoSCoW techniques, the user stories were listed on Projects’ Kanban board and were labeled to prioritize the requirements.They were labelled as 'must have', 'could have' or 'should have'. They would be moved across the board from To do, In progress and Done in the end when all the tasks are completed. 
     The project board was captured near the mid-way through and at the end:
     
     ![user-stories](/readme_docs/us-image.png)

     ![user-stories-end-image](/readme_docs/us-stories-end.png)

## Structure

   * ### Database ERD

     ER diagram was created using dbdiagram that maps the database structure for creating models in Django. The ERD helps me to visualize the relationships between the tables which gives me better idea on how the database works for the project development.

     ![recipes-erd](/readme_docs/recipe-erd.png)

   * ### Wireframes

     I used Balsamiq to create the project’s wireframes that displays an overview of how the site looks like. However, the end result might be slightly different than the initial design due to the development of the project.

      * #### Homepage Wireframe

        ![homepage-wireframe](/readme_docs/home-wireframe.png)   

      * #### Profile page Wireframe

        ![profile-wireframe](/readme_docs/profile-wireframe.png)

      * #### My recipes Wireframe

        ![myrecipes-wireframe](/readme_docs/my-recipes-wireframe.png)   

      * #### Recipe View Wireframe

        ![recipe-view-wireframe](/readme_docs/recipe-view-wireframe.png)

      * #### Recipe Add Wireframe

         ![recipe-add-wireframe](/readme_docs/add-recipe-wireframe.png)  

      * #### Recipe Delete Wireframe

        ![delete-recipe-wireframe](/readme_docs/delete-recipe-wireframe.png)     

      * #### Recipes List Wireframe

        ![recipes-list-wireframe](/readme_docs/recipe-list-wireframe.png)

      * #### Recipe Detail Wireframe

        ![recipe-detail-wireframe](/readme_docs/comment-wireframe.png)  

## Skeleton

   * ### Features
     
       * #### General

           The website has been designed from a mobile first perspective. It has responsive design across all device sizes.

           ##### Navigation Bar

            The navigation bar contains the main logo, section links and search bar. 
            The site's navigation tabs are displayed Home, Recipes, Login, Signup when the user isn't logged in.

            ![Navigation bar](/readme_docs/header-img.png)

            The site's navigation tabs are changed to Home, Recipes, Profile, Logout when the user is logged in.

            ![Login Navigation bar](/readme_docs/header-login-img.png)

            The search bar provide the Site User an input field and a Search button to be able to search for specific recipes by using keyord title or ingredients.

           ##### Footer

            A footer is displayed on all pages of the website and contains the copyright and links to social media channels

            ![Footer](/readme_docs/footer-img.png)

       * #### Home Page

          
         

   * ### Technologies Used

      #### Languages Used

        * [HTML5](https://en.wikipedia.org/wiki/HTML)
        * [CSS3](https://en.wikipedia.org/wiki/CSS)
        * [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
        * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


      #### Libraries and Frameworks

        * [Django 3.2](https://www.djangoproject.com/) - Django was used as web framework.
        * [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - Templating engine.
        * [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - Bootstrap 5 was used throughout the website to help with styling and responsiveness.
        * [Google Fonts](https://fonts.google.com/) - To import the fonts used on the website.
        * [Font Awesome](https://fontawesome.com/) - Font Awesome was used throughout the website to add icons for aesthetic and UX purposes.
        * [Cloudinary](https://cloudinary.com/) - Libraries to enable storage of static files and media in Cloudinary
        * [Summernote](https://summernote.org/) - Summernote has been used as WYSIWYG editor.
        * [Psycopg2](https://pypi.org/project/psycopg2/) - Python PostgreSQL adapater
      
      #### Packages / Dependecies Installed

        * [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - User account management django application suite.
        * [Django Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/) - Django app to simplify form rendering
        * [Gunicorn](https://gunicorn.org/) - Python WSGI HTTP server
        * [dj-database-url](https://pypi.org/project/dj-database-url/) - Django utility to create an environment variable to configure the Django application

      #### Databases Used

        * [Heroku Postgres](https://www.heroku.com/postgres) - Heroku Postgres database was used in production, as a service based on PostgreSQL provided by Heroku.
        * [ElephantSql](https://www.elephantsql.com/) - Migrated database to ElephantSql.

      #### Programs Used

        * [Git](https://git-scm.com/) - For version control.
        * [Github](https://github.com/) - To save and store the files for the website.
        * [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot and test features, solve issues with responsiveness and styling.
        * [Balsamiq](https://balsamiq.com/) - Used to create wireframes.
        * [Heroku](https://dashboard.heroku.com/) - Heroku was used to deploy the website.
        * [Am I Responsive?](https://ui.dev/amiresponsive) - To show the website image on a range of devices.
        * [Favicon.io](https://favicon.io/) - To create the favicon.
        * [Birme](https://www.birme.net/?target_width=1400&target_height=1400&auto_height=true&image_format=webp&rename_start=1) - To resize images and convert to webP format for the site.
        * [dbdiagram.io](https://dbdiagram.io/) - To create the database schema.  


## Surface

   * ### Design
     
      * #### Colour Schemes

        ![colour-palette](/readme_docs/colour-palette.png)

        I used Cooler to help to check colour contrast. The colour scheme which I used earlier showing poor quality contrast. So, I update the colour scheme for good quality contrast. 

      * #### Typography

        Google Fonts was used to import the chosen fonts for use in the site. Headings are in Fredoka One with cursive as a fallback font. The body is in Roboto with sans-serif as a fallback font. This means the text will be easy to read on all device sizes.

      * #### Imagery

        * Images are uploaded by the users and stored in Cloudinary database.
        * There are placeholder images for both recipes and profiles, if user doesnot wants to upload an image.

   * ### Deployment

        #### Deploying on Heroku
        
        Worldofrecipes is deployed to Heroku, using an ElephantSQL Postgres database. To duplicate deployment to Heroku, follow these steps:
        * You will need a Cloudinary account to host user images and static files.
        * Login to Cloudinary.
        * Select the 'dashboard' option.
        * Copy the value of the 'API Environment variable' from the part starting cloudinary:// to the end. You may need to select the eye icon to view the full environment variable. Paste this value somewhere for safe keeping as you will need it shortly (but destroy after deployment).
        * Log in to Heroku.
        * Select 'Create new app' from the 'New' menu at the top right.
        * Enter a name for the app and select the appropriate region.
        * Select 'Create app'.
        * Select 'Settings' from the menu at the top.
        * Login to ElephantSQL.
        * Click 'Create new instance' on the dashboard.
        * Name the 'plan' and select the 'Tiny Turtle (free)' plan.
        * Select 'select region'.
        * Choose the nearest data centre to your location.
        * Click 'Review'.
        * Go to the ElephantSQL dashboard and click on the 'database instance name' for this project.
        * Copy the ElephantSQL database URL to your clipboard (this starts with postgres://).
        * Return to the Heroku dashboard.
        * Select the 'settings' tab.
        * Locate the 'reveal config vars' link and select.
        * Enter the following config var names and values:
             * CLOUDINARY_URL: your cloudinary URL as obtained above
             * DATABASE_URL: your ElephantSQL postgres database URL as obtained above
             * PORT: 8000
             * SECRET_KEY: your secret key
        * Select the 'Deploy' tab at the top.
        * Select 'GitHub' and confirm you wish to deploy using GitHub. You may be asked to enter your GitHub password.
        * Find the 'Connect to GitHub' section and use the search box to locate your repo.
        * Select 'Connect' when found.
        * Optionally choose the main branch under 'Automatic Deploys' and select 'Enable Automatic Deploys' if you wish your deployed site to be automatically redeployed every time you push changes to GitHub.
        * Find the 'Manual Deploy' section, choose 'main' as the branch to deploy and select 'Deploy Branch'.
        * Your site will shortly be deployed and you will be given a link to the deployed site when the process is complete.

     #### How to Fork
      By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

      1. Log into GitHub or create an account.
      2. Locate the GitHub Repository.
      3. At the top of the repository, on the right side of the page, select "Fork"
      4. You should now have a copy of the original repository in your GitHub account.

     #### How to Clone
      How to run this project locally:

      1. Log into GitHub or create an account.
      2. Locate the GitHub Repository.
      3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
      4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
      5. Type the following command in the terminal (after the git clone you will need to paste the link you copied in step 3 above):

         git clone { & THE LINK FROM STEP 3 }
      6. Set up a virtual environment (this step is not required if you are using the Code Institute Template in GitPod as this will already be set up for you).

      7. Install the packages from the requirements.txt file by running the following command in the Terminal:

         pip3 install -r requirements.txt
   
## Testing

   The testing documentation can be found [here](TESTING.md)