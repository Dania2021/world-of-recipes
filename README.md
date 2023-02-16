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
 * Skeleton  
    * Features 
       * Home Page
       * Login Page
       * SignUp Page
       * Profile Page
       * Recipes Page
       * Search page
       * Logout Page
       * Admin Site
       * Future Features
    * Technologies Used
 * Surface
    * Design
      * Colour Schemes
      * Typography  
    * Deployment
 * Testing
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

## Surface

## Testing

   The testing documentation can be found [here](TESTING.md)