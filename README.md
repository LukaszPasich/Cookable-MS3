# __Cookable__ - Your Online Recipe Manager

_Cookable_ is your very own personal recipe organiser. Save your favourite recipes from websites, magazines, recipe books or simply those from your head, all in one place, accessible on all of your devices, anytime. Quickly search for recipes uploaded by other users to discover new culinary frontiers.

<img src="static/images_readme/ms3-readme-overview.png" alt="Cookable - website overview">

# Link to live project - [CLICK HERE](http://cookable.herokuapp.com/landing)

#### Contents
1. [UX](#ux)
	- [User Goals (Strategy)](#user-goals)
	- [Stakeholder Goals (Strategy)](#stakeholder-goals)
	- [User Stories (Strategy)](#user-stories)
	- [Project Scope (Scope)](#project-scope)
	- [Information Architecture - Website Flow Chart (Structure)](#information-architecture---website-flow-chart)
	- [Wireframes (low fidelity wireframes) (Skeleton)](#wireframes-(low-fidelity))
	- [Prototype (high fidelity wireframes) (Skeleton)](#prototype-(high-fidelity))
	- [Design (Surface)](#design)
2. [Features](#features)
	- [Landing page](#landing-page)
    - [All Recipes](#all-recipes)
	- [My Recipes](#my-recipes)
	- [Full Recipe page](#full-recipe-page)
	- [Add Recipe](#add-recipe)
	- [Search Recipes](#search-recipes)
	- [Edit Recipe](#edit-recipe)
	- [Delete Recipe](#delete-recipe)
	- [Categories](#categories)
	- [Non registered user access](#non-registered-user-access)
	- [Registered user access](#registered-user-access)
	- [Admin access](#admin-access)
	- [Log in](#log-in)
	- [Sign up](#sign-up)
	- [Log out](#log-out)
	- [Website interaction feedback](#website-interaction-feedback)
	- [Email](#email)
	- [Advertising](#advertising)
	- [Broken image link handling](#broken-image-link-handling)
	- [Broken URL handling](#broken-url-handling)
	- [Features to Implement in the future](#features-to-implement-in-the-future)
3. [Technologies](#technologies)
	- [Tools](#tools)
	- [Libraries and frameworks](#libraries-and-frameworks)
	- [Languages](#languages)
	- [Database platform](#database-platform)
4. [Testing](#testing)
	- [Automated Testing](#automated-testing)
	- [UX Testing](#ux-testing)
	- [Manual Testing](#manual-testing)
	- [Bugs](#bugs)
5. [Deployment](#deployment)
    - [Github Pages Deployment](#github-pages-deployment)
    - [Cloning](#cloning)
6. [Credits](#credits)
	- [Content](#content)
	- [Media](#media)
	- [Code](#code)
    - [Resources](#resources)
	- [Acknowledgements](#acknowledgements)
7. [Contact](#contact)


---


## UX

### User Goals.
- Upload, store and easily access own cooking recipes on the _Cookable_ recipe manager.
- Browse and find recipes uploaded by other users.
<br>
<br>

### Stakeholder Goals
- Promote the 'Schmickser' brand of kitchen mixers.
- Creating a crowd-populated resource for cooking recipes.
<br>
<br>

### User Stories

1. As a first time user, I want the website to be simple and easy to navigate, I want all links to be available in the navbar.
2. As a website user that accesses internet primarily via mobile, I want the website to be fully responsive, with clean and simple layout and also easy to navigate.
3. As a user who looks only for cooking inspiration, I would like to be able to browse and find other people's recipes. It would be ideal if I could do it without having to create an account myself. 
4. As a person who likes to cook from recipes I find online, I expect the recipes to have at the minimum all the basic information needed for the meals to be actually possible to cook. Any nutritional information would be a nice bonus.
5. As a user who is looking for specific recipes, I expect the website to have some form of search feature, so I can find recipes by a particular ingredient or any other keyword.
6. As a visitor who is looking to become a registered user, I would like to see an easy way to register my account. I also make typos easily..., I would like to see some defensive mechanism preventing me confusing the password at the registration, or alternatively, I would like to see password recovery feature.
7. As a registered user, I expect an easy way to upload and view my recipes. I would like to share my recipes with other users, both registered and unregistered.
8. As a registered user, I would like an easy way to update and delete my recipes. However, I would like to make sure that other users could not modify or delete my recipes. 
9. As a registered user, I would like to receive a feedback from the website at any point that my account has been affected in any way (uploading/ updating/ deleting recipe confirmation etc.)
10. As a registered user, I would like to have some way of categorising recipes, so that it is easier to search for a group of similar recipes (or similar ingredients, etc.)
11. As a user, I would like to be able to get in touch with the website owner, to ask a question, perhaps to suggest a new recipe category or leave any other feedback.
12. As the website owner, I would like to advertise the 'Schmickser' brand of mixers in some way.
13. As the website owner, I want some form of validation of any entry by the users, so that the website layout or database content doesn't break or doesn't get corrupted.
14. As the website owner, I want some form of validation of usernames and passwords entries at the sign up level, so that the database doesn't get populated by possibly corrupting entries. Also I don't want users to get frustrated and leave the website when they forget passwords, therefore some form of prevention from using overly complicated entries must be in place.
15. As the website owner, I want the features that are available to registered users to be concealed from non-registered users.
16. As the website owner I expect to be able to add new recipe categories, and edit or delete existing categories.
17. As the website owner I want the '404 - page not found' error to be handled in the way that makes visitors stay on Cookable website, so that accidental mispellings in the web address bar or any other issues don't take them elsewhere.
<br>
<br>

### Project Scope
Features within the scope:
1. Website responsive - importance: 3, feasibility: 3, __TOTAL: 6__
2. Recipes basic details: 3, feasibility: 3, __TOTAL: 6__
3. Recipes (CRUD) - importance: 3, feasibility: 3, __TOTAL: 6__
4. Recipe categories (CRUD)	- importance: 2, feasibility: 3, __TOTAL: 5__
5. Non-registered user access - importance: 3, feasibility: 3, __TOTAL: 6__
6. Registered user access - importance: 3, feasibility: 2, __TOTAL: 5__
7. Admin access - importance: 2, feasibility: 2, __TOTAL: 4__
8. All forms validation - importance: 3, feasibility: 2, __TOTAL: 5__
9. Website interaction feedback - importance: 3, feasibility: 2, __TOTAL: 5__
10. Email - importance: 2, feasibility: 2, __TOTAL: 4__
11. 'Schmickser' advertising - importance: 2, feasibility: 2, __TOTAL: 4__
12. Broken image link handling - importance: 2, feasibility: 2, __TOTAL: 4__
13. Broken URL handling - importance: 1, feasibility: 2, __TOTAL: 3__

Features outside of the scope:
1. Recipe advanced details - importance: 2, feasibility: 1, __TOTAL: 3__
2. Admin dashboard for various recipe statistics - importance: 2, feasibility: 1, __TOTAL: 3__
3. Recipes rating - importance: 1, feasibility: 1, __TOTAL: 2__
4. Saving other users recipes - importance: 1, feasibility: 1, __TOTAL: 2__
<br>
<br>

### Information Architecture
#### Sitemap

- [Sitemap showing access to the website at different levels of user registration CLICK HERE](https://documentcloud.adobe.com/link/review?uri=urn:aaid:scds:US:422f87e3-8884-4cff-89ce-3132d03dc50c)


#### Database

- [Database structure CLICK HERE](https://documentcloud.adobe.com/link/review?uri=urn:aaid:scds:US:b27eda61-45f0-40e5-a1f5-37fafdde079a)
<br>
<br>

### Wireframes (low fidelity)
Through these low-fidelity wireframes I have created the basic structure of my website and I've explored responsive behaviour of the website.
- [Wireframes for the website AVAILABLE HERE](https://documentcloud.adobe.com/link/review?uri=urn:aaid:scds:US:d9c1842d-6455-47cd-9d43-5ec8fa26a981)
<br>
<br>

### Prototype (high fidelity)
Through the hi-fidelity prototype I have explored more the interconnectivity of all pages and I've answered most of the questions regarding the visual aspect of my website.
- [Prototype - desktop version of the website AVAILABLE HERE](https://xd.adobe.com/view/75bb1733-15a2-4748-a139-57bad492aab1-20e8/)
- [Prototype - mobile version of the website AVAILABLE HERE](https://xd.adobe.com/view/5eaa5182-9fe0-496e-bd45-1b6818eebac4-0bf9/)
<br>
<br>

### Design

#### The Name
The name came after brainstorming around the word 'Cookbook', however I didn't want to be as obvious as that, plus I found an actual app for managing recipes called 'Cookbook', so the name was off the table. I was looking at a lot of chess matches on youtube and somehow through ads I came across the website of one of the chess grand masters Magnus Carlsen - it was called Chessable. That instant I decided on the name _Cookable_. It had the sounding of the 'Cookbook', felt like it was full of things possible to cook (all cookable things), and also felt inviting, like anyone was able to cook them (you're able to cook).

#### Logo
I settled on the idea of the casual script font pretty early. I've seen few examples of that type of font working well with the cooking theme. The logotype was supposed to be it, but the moment I saw the double 'o' together in that font, I realised it was asking for a smile underneath (amazon logo style) to make it a friendly happy looking logo - perfect for the purpose.

<img src="static/images_readme/ms3-readme-logo.png" alt="Cookable logo">

#### Colours
I was exploring colours around more 'mature greens' to evoke feelings of healthy and good quality food in users.

<img src="static/images_readme/ms3-readme-colours.png" alt="Cookable logo">

#### Typography
- _Zilla Slab_ font was used  for all headlines.

	Zilla Slab is contemporary slab serif, constructed with smooth curves and true italics, which gives text an unexpectedly sophisticated industrial look and a friendly approachability in all weights.

- _Montserrat_ font was used for all body text.

	Montserrat is very versatile and can be used in multiple domains such as websites, the publishing world, branding, editorial, logos, print, posters, etc. It is a typeface that can be used basically anywhere because of the geometric and elegant simplicity with nice large x-height.

[Back to top](#contents)

---

## Features
### Landing page
Home page for the website, features a brief overview of the Cookable website, a main banner with a call to action to sign up and an advert for "Schmickser" mixer.

<img src="static/images_readme/ms3-readme-overview.png" alt="Cookable - website landing page">
&nbsp;

### All Recipes
This page features all recipes uploaded by all registered users. The page is available to view by any visitor to the website. Each recipe is represented by a card with the recipe image and the name.

<img src="static/images_readme/ms3-readme-allrecipes.png" alt="Cookable - website recipes page">

### My Recipes
This page features all recipes uploaded by the user who is currently in session and is available only to that user. It looks similar to the page featuring all recipes. If the current user has not uploaded any recipe yet the appropriate message is displayed.

<img src="static/images_readme/ms3-readme-myrecipes.png" alt="Cookable - website my recipes page">
&nbsp;

### Full Recipe page
This page displays the full recipe and includes:
	- recipe name
	- recipe category
	- number of servings
	- cooking time
	- image
	- ingredients
	- preparation method
	- user owner of the recipe

If the full recipe page is being viewed by the user that uploaded the recipe, the aditional options for editing and deleting the recipe are displayed.

Also, if the recipe has 'mix' or 'mixer' keywords in it, the advertisement for 'Schmickser' mixer will appear underneath the recipe.

<img src="static/images_readme/ms3-readme-fullrecipe.png" alt="Cookable - website full recipe page">
&nbsp;

### Add Recipe
This page presents the user with the form to fill out all the spaces with relevant information to create the recipe.

<img src="static/images_readme/ms3-readme-addrecipe.png" alt="Cookable - website add recipe page">
&nbsp;

### Search Recipes
The search bar appears on the page with all recipes. It has the search button (it's equivalent to hitting enter/return on the keyboard) and search reset that simply reloads the page. If the keyword given doesn't appear in any recipe, the message 'No results found' is displayed and all recipes are reloaded underneath.

<img src="static/images_readme/ms3-readme-search.png" alt="Cookable - website search field">
&nbsp;

### Edit Recipe
Comes up after hitting the 'Edit' button on the full recipe that belongs to the user and gives the user similar form as Add Recipe function does, but this time the information is already populated.

<img src="static/images_readme/ms3-readme-editrecipe.png" alt="Cookable - website edit recipe feature">
&nbsp;

### Delete Recipe
Deleting recipe is possible after hitting the 'Delete' button on the full recipe that belongs to the user. There is defense mechanism in the form of the modal popping up, which prevents accidental deleting of the recipe by just hitting the 'Delete' button. The modal asks for additional Yes/No confirmation whether the recipe should be deleted.

<img src="static/images_readme/ms3-readme-deleterecipe.png" alt="Cookable - website delete recipe feature">
&nbsp;

### Categories
(Create, Read, Update and Delete Categories)

This series of pages is available only to the admin user. They allow admin to view all the recipe categories, add new categories, and edit and delete the old categories. Categories help to bundle up groups of recipes of similar kind under one common keyword (ex. a bunch of icecream recipes could have different ingredients, but they would all come up together in the search under 'dessert' keyword - provided the user used the correct category name).  

<img src="static/images_readme/ms3-readme-categories.png" alt="Cookable - website recipe categories page">
<img src="static/images_readme/ms3-readme-editcategories.png" alt="Cookable - website edit category page">
&nbsp;

### Non registered user access
The navigation bar and available links throughout the page let the visitor access all recipes, log in and sign up pages only.

<img src="static/images_readme/ms3-readme-user.png" alt="Cookable - website navigation bar with links available to not regisered visitors">
&nbsp;


### Registered user access
The navigation bar and available links throughout the page let the registered user access all recipes, my recipes and add recipe pages. Log in is not available and sign up page is accesible from the home page. The registered user also has also additional privilages of being able to add, edit and delete his/her own recipes.

<img src="static/images_readme/ms3-readme-reguser.png" alt="Cookable - website navigation bar with registered user access links">
&nbsp;

### Admin access
Admin can access all the same features as the registered user plus can view, add, edit and delete recipe categories. 

<img src="static/images_readme/ms3-readme-adminuser.png" alt="Cookable - website navigation bar with admin access links">
&nbsp;

### Log in
(With validation)

Log in page allows users to log in to their accounts and access registered users' expanded priviliges. The log in form validates the minimum and maximum characters lengths and makes sure that characters entered are within alpha-numeric values only (lowercase and uppercase for letters). If the user doesn't exist or password for user doesn't match database value, then the 'Incorrect username and/or password' message is displayed.

<img src="static/images_readme/ms3-readme-login.png" alt="Cookable - website log in page">
&nbsp;

### Sign up
(With validation and password confirmation)

Sign up page allows visitor to create an account on the website and become a registered user. The sign up form validates the minimum and maximum characters lengths and makes sure that characters entered are within alpha-numeric values only (both lowercase and uppercase for letters).
The password confirmation checks if the 'password' and 'confirm password' fields are the same (at least one character needs to be entered to make sure that the visitor didn't just click through the fields, making 2 empty fields match at equality test) and only then the 'Sig up' button becomes available.

<img src="static/images_readme/ms3-readme-signup.png" alt="Cookable - website sign up page">
&nbsp;

### Log out
Log out link brings the user back to the basic website without all expanded features available to registered users and admin.
&nbsp;

### Website interaction feedback
Cookable website gives the users feedback when certain actions are taken, especially when these actions are affecting the back-end of the website and the MongoDB database itself, and would not be very apparent at first otherwise. The feedback is manifested as a pop up 'flash' message (lasting 5 seconds). These messages happen when:
- users log in to their accounts, the message: "Welcome, {{user_name}}!"
- users sign up to the website, the message: "You have signed up successfully!"
- users, try to sign up using existing username, the message: "Username already exists"
- users try to log in with incorrect username or password, the message: "Incorrect username and/or password"
- users log out, the message: "You have been logged out"
- users add new recipe, the message: "Recipe Successfully Added"
- users edit the recipe, the message: "Recipe Successfully Updated"
- users, delete the recipe, the message: "Recipe Successfully Deleted"
- admin user adds a new recipe category, the message: "New Category Added"
- admin user edits a recipe category, the message: "Category Successfully Updated"
- admin user deletes a category, the message: "Category Successfully Deleted"
- users send email from the contact page, the message: "Messsage sent successfully". This is the only message not done through Python, but rather with JavaScript.

<img src="static/images_readme/ms3-readme-flash.png" alt="Cookable - website flash messages">
&nbsp;

### Email
Through the contact form on the Contact us page users can send emails to the website owner's mailbox. The feature is supported by EmailJS service.

<img src="static/images_readme/ms3-readme-email.png" alt="Cookable - website contact page">
&nbsp;

### Advertising
The home page features an ad for the 'Schmickser' brand of kitchen mixers. This ad gets also inserted on the bottom of each recipe (thinking now.. perhaps positioning of the ad should be better) that contains, anywhere in the text, keywords 'mix' or 'mixer'.

<img src="static/images_readme/ms3-readme-mixer.png" alt="Cookable - website 'Schmickser' ads">
&nbsp;

### Broken image link handling
Because MongoDB supports only textual content, users can add the images to their recipes only by providing URL link to the image hosted on a 3rd party website. In the event of user entering an incorrect link, or in case of the image not being available anymore, a special placeholder image gets inserted instead of the default 'broken image link' icon. The placeholder image is hosted on [www.imgur.com](https://imgur.com/). This image responds to the css styling better than the default 'broken link' icon, blends in better with other images and doesn't break the nice grid layout of the recipe pages.

<img src="static/images_readme/ms3-readme-brokenlink.png" alt="Cookable - recipe image broken link">
&nbsp;

### Broken URL handling
If the user manually enters incorrect web address, or if 'error 404' happens for any other reason, the website redirects user to the 'Sorry.. Page not found' page. The good thing is that the user is still on the _Cookable_ website.

<img src="static/images_readme/ms3-readme-404.png" alt="Cookable - website page not found">
&nbsp;

### Features to Implement in the future
- Nutritional information for each recipe (ex. calorie count, vegan, vegetarian, gluten-free labels).
- Recipe rating feature - for users to rate other users recipes.
- Saving other users recipes.
- Admin dashboard for various recipe statistics.
- Timer (perhaps?)
- Meal planner (perhaps?)


[Back to top](#contents)

---

## Technologies
### Tools
- [GitHub](https://github.com) was an IDE used for the project.
- [GitPod](https://gitpod.io/workspaces/) was used for version control.
- [Heroku](https://heroku.com) was used for website deployment.
- [Balsamiq](https://balsamiq.com) was used to create low fidelity wireframes.
- [Adobe XD](https://www.adobe.com/ie/products/xd.html) was used to build the high fidelity prototypes.
- [Adobe Illustrator](https://www.adobe.com/ie/products/illustrator.html) was used to create logo.
- [Adobe Photoshop](https://www.adobe.com/ie/products/photoshop.html) was used to edit, crop and save images.
- [Adobe InDesign](https://www.adobe.com/ie/products/indesign.html) was used to creadit some of the graphics for the website (ex. 'Schmickser' ad).
- [Am I Responsive](http://ami.responsivedesign.is) was used to create the images of each page displayed on different screen sizes in this _Readme_ file.

### Libraries and frameworks
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) was used as a Python framework. A number of features was imported from flask - render_templates amongst one of them.
- [jQuery](https://jquery.com/) was used as JavaScript framework. A number of components from Materialize was activated via jQuery.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) tool was used for hashing and unhashing back the passwords.
- [Materialize](https://materializecss.com/) grids were used in particular to create and maintain the design layout across different screen/viewport sizes and make the website responsive easily. Some dynamic components from Materialize were also used.
- [Google Fonts](https://fonts.google.com) was used to link the "Montserrat" and "Zilla Slab" fonts.
- [Font Awesome](https://fontawesome.com) was used for icons.

### Languages
- HTML5
- CSS3
- JavaScript
- Python

### Database platform
- MongoDB - a NoSQL database cloud-based program - was used to store data captured from the user.

[Back to top](#contents)

---

## Testing

### Automated Testing
- [W3C Markup Validator](https://validator.w3.org/) was used for HTML validation:
	- _Home page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Flanding) - Errors: 0
	- _Recipes page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Fget_recipes) - Errors: 3 (deliberate 3 broken links for test purposes)
	- _Full recipe page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Ffull_recipe) - Errors: 0
	- _My recipes page_ validator result [HERE](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcookable.herokuapp.com%2Fmy_recipes) - Errors: 0
	- _Edit recipe page_ validator result [HERE](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcookable.herokuapp.com%2Fedit_recipe) - Errors: 0
	- _Add recipe page_ validator (via direct input, as page password protected) result - Errors: 0
	- _Categories page_ validator (via direct input, as page password protected) result - Errors: 0
	- _Edit category page_ validator (via direct input, as page password protected) result - Errors: 0
	- _Add category page_ validator (via direct input, as page password protected) result - Errors: 0
	- _Sign up page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Fsignup) - Errors: 0
	- _Log in page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Flogin) - Errors: 0
	- _Contact page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Fcontact) - Errors: 0
	- _Error 404 page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Fcontacta) - Errors: 0

&nbsp;

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used for CSS validation:
	- CSS validation result [HERE](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcookable.herokuapp.com%2Fstatic%2Fstyle%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) - Errors: 1 (error related to Materialize library)

&nbsp;

- [JSHint](https://jshint.com/) was used for JavaScript validation (New JavaScript features (ES6) and jQuery were selected in configuration):
    - script.js - JavaScript validation - Errors: 0
	- sendEmail.js - JavaScript validation - Errors: 0

&nbsp;

- [Web Accessibility](https://www.webaccessibility.com) was used to validate website's accessibility:
	- _Home page_ website accessibility score: 100%
	- _Recipes page_ website accessibility score: 100%
	- _Full recipe page_ website accessibility score: 100%
	- _My recipes page_ - password protected, could not be assessed
	- _Edit recipe page_ - password protected, could not be assessed
	- _Add recipe page_ - password protected, could not be assessed
	- _Categories page_ - password protected, could not be assessed
	- _Edit category page_ - password protected, could not be assessed
	- _Add category page_ - password protected, could not be assessed
	- _Sign up page_ website accessibility score: 100%
	- _Log in page_ website accessibility score: 100%
	- _Contact page_ website accessibility score: 98%
	- _Error 404 page_ website accessibility score: 100%

&nbsp;

    
- [Google Mobile Friendly Test](https://search.google.com/test/mobile-friendly) was used to test responsiveness of the website:
	- _Home page_ - mobile friendly
	- _Recipes page_ - mobile friendly
	- _Full recipe page_ - mobile friendly
	- _My recipes page_ - password protected, could not be assessed
	- _Edit recipe page_ - password protected, could not be assessed
	- _Add recipe page_ - password protected, could not be assessed
	- _Categories page_ - password protected, could not be assessed
	- _Edit category page_ - password protected, could not be assessed
	- _Add category page_ - password protected, could not be assessed
	- _Sign up page_ - mobile friendly
	- _Log in page_ - mobile friendly
	- _Contact page_ - mobile friendly
	- _Error 404 page_ - mobile friendly

&nbsp;
	
- Python code was verified through GitPod's linter, showing only 1 error:
```	
"env" imported but unused
```
This has to do with the fact that env.py file contains all the sensitive data and could not be pushed to GitHub repository.

&nbsp;

### UX Testing
#### User Stories Testing

1. _As a first time user, I want the website to be simple and easy to navigate, I want all links to be available in the navbar._

	The website is quite clear and easy to follow through the minimalistic layout and consistent use of simple colours and limited amount of legible fonts. The navbar has all links necessary to navigate the website and access all necessary features.

2. _As a website user that accesses internet primarily via mobile, I want the website to be fully responsive, with clean and simple layout and also easy to navigate._

	The website is responsive using Materialize grids. The responsive layout is also supported by buttons' text turning into intuitive icons and navbar collapsing into a hamburger menu and turning into 'slide from the side' navigation. The whole design of the website is done with mobile user first approach.

3. _As a user who looks only for cooking inspiration, I would like to be able to browse and find other people's recipes. It would be ideal if I could do it without having to create an account myself._

	All recipes created by all registered users are available under 'Recipes' link in the navbar. A visitor can get inspired by other cooking recipes without signing up to the service.

4. As a person who likes to cook from recipes I find online, I expect the recipes to have at the minimum all the basic information needed for the meals to be actually possible to cook. Any nutritional information would be a nice bonus.

	Every recipe features:
	- recipe name,
	- picture of the dish that the recipe is for,
	- recipe category (under which it is easier to classify and bundle together similar recipes),
	- amount of serving portions,
	- cooking time,
	- list of ingredients,
	- method of preparation

	These are all the basic details needed to prepare a dish from the recipe. Unfortunatelly, the nutritional information didn't get into the scope of this project.

5. As a user who is looking for specific recipes, I expect the website to have some form of search feature, so I can find recipes by a particular ingredient or any other keyword.

	There is a search bar on the 'Recipes' page that allows user to find recipe by keyword. Any phrase will be treated as separate keywords at the moment unfortunatelly. The empty search returns alternative suggested recipes, which at the moment is all the recipes, but can be changed upon deciding what the alternatives should be.

6. As a visitor who is looking to become a registered user, I would like to see an easy way to register my account. I also make typos easily..., I would like to see some defensive mechanism preventing me confusing the password at the registration, or alternatively, I would like to see password recovery feature.

	Registering is easy with the 'Sign up' button in the navbar or in the header of the home page taking visitors to the 'Sign up' page which requires visitors to fill out only 3 fields:
	- username
	- password
	- confirm password

	The 'password' and 'confirm password' entry fields are obscured, so that the visitor can't see the entry, but there is a feature that compares both entries and checks for equality, which is some form of defense from creating accidentally passwords with mistakes. Only when both passwords match, the 'Sign up' button for registering gets revealed.
	
	There is no password recovery feature at the moment.

7. As a registered user, I expect an easy way to upload and view my recipes. I would like to share my recipes with other users, both registered and unregistered.

	Uploading recipe as a registered user is very easy through 'Add Recipe' page that is available from the nav bar or clicking the link on 'My Recipes' page. Every added recipe gets automatically added to 'My Recipes' page of the user who has added it.

	Every uploaded recipe gets also into the 'Recipes' page that is available to all users, both registered and unregistered.

8. As a registered user, I would like an easy way to update and delete my recipes. However, I would like to make sure that other users could not modify or delete my recipes.

	Every registered and ONLY regisered users can access 'update' or 'delete' recipe options ONLY on the full recipe page of ONLY their own recipes.

9. As a registered user, I would like to receive a feedback from the website at any point that my account has been affected in any way (uploading/ updating/ deleting recipe confirmation etc.)

	Cookable website features flash messages that appear on top of the page in distinctive colour that provide good feedback to the user of what is happening in the background of the website, when users perform actions that for ex. change the records in database or when users make mistakes at sign up/ log in process.

	For full list of flash messages, refer to the [Features](#features) section and [Website interaction feedback](#website-interaction-feedback) part in particular.

10. As a registered user, I would like to have some way of categorising recipes, so that it is easier to search for a group of similar recipes (or similar ingredients, etc.)

	All recipes are saved under specific, user chosen category (from the list of available categories created by admin user), to make it easier to group recipes and search them later under that category keyword.
	This is useful when users want their recipe to come up under certain keyword, but the keyword doesn't exist anywhere in the name, ingredients or method (ex., user would like a prawn cocktail recipe to come up whenever search for 'fish' is performed).

11. As a user, I would like to be able to get in touch with the website owner, to ask a question, perhaps to suggest a new recipe category or leave any other feedback.

	There is a link to the Contact page in the footer ('Get in touch'), which brings users to the contact form that sends emails directly to the owner of the website. Visitors can get more information and give further feedback on the social media. Links to various social media pages also available in the footer. 

12. As the website owner, I would like to advertise the 'Schmickser' brand of mixers in some way.

	Any recipe that contains the keywords 'mix' or 'mixer' gets an advert for the 'Schmickser' brand of mixers inserted at the bottom of the full recipe page. In addition, there is also an advert for 'Schmickser' mixers on the home page.

13. As the website owner, I want some form of validation of any entry by the users, so that the website layout or database content doesn't break or doesn't get corrupted.

	All insert fields have appropriate validation mechanisms present:
	- Sign up form:
		- username, password and confirm password fields - require alphanumeric entries and min/max amount of characters,
		- form - checks if username already exists in the database and resets the form if it does, plus flash message is displayed
		- form - verifies that password and confirm password entries are equal and makes 'Sign in' button available only if they are,
		- form - all fields filled out required to send the form
	- Log in form:
		- username, and password fields - require alphanumeric entries and min/max amount of characters,
		- form - checks if password entered and the username entered match any database record, and if it doesn't, the form is reset and apropriate flash message is displayed
		- form - all fields filled out required to send the form
	- Contact form:
		- email field - requires correct email format input,
		- form - all fields filled out required to send the form
	- Add/Edit recipe:
		- recipe category - is required,
		- recipe name - max 40 characters allowed
		- serves - max 2 digit number using any digits allowed
		- cooks in - max 4 digit number using any digits allowed
		- form - all fields filled out required to send the form
	- Add/Edit category:
		- category - min 2, max 20 characters, entry required

14. As the website owner, I want some form of validation of usernames and passwords entries at the sign up level, so that the database doesn't get populated by possibly corrupting entries. Also I don't want users to get frustrated and leave the website when they forget passwords, therefore some form of prevention from using overly complicated entries must be in place.

	Sign up form has validation mechanism present (see point 13 of User Stories Testing, above).

15. As the website owner, I want the features that are available to registered users to be concealed from non-registered users.

	There are 3 levels of access to the website, at every level there is a different set of features that can be accessed by the user:

	| Non-registered user | Registered user   | Admin user          |
	|---------------------|-------------------|---------------------|
	|Home                 |Home                |Home                |
	|Recipes              |Recipes             |Recipes             |
	|Search               |Search              |Search              |
	|-                    |My Recipes          |My Recipes          |
	|-                    |Add/Edit Recipes    |Add/Edit Recipes    |
	|-                    |-                   |Add/Edit Categories |
	|Log in               |-                   |-                   |
	|Sign up              |Sign up             |Sign up             |
	|-                    |Log out             |Log out             |
	|Get in touch (email) |Get in touch (email)|Get in touch (email)|


16. As the website owner I expect to be able to add new recipe categories, and edit or delete existing categories.

	All CRUD operations for recipe categories are possible for the admin user.

17. As the website owner I want the '404 - page not found' error to be handled in the way that makes visitors stay on Cookable website, so that accidental mispellings in the web address bar or any other issues don't take them elsewhere.

	There is a template included for handling error 404, so that in case of web address misspellings or long periods of inactivity the website is redirected to error 404 page, but the user is still within the Cookable website.

&nbsp;

### Manual Testing
#### Features Working Correctly (in various screen sizes) Check
1. Navbar (Desktop):
	- TEST 1.1 - _Cookable_ logo links to the _Home_ page - YES
	- TEST 1.2 - _Recipes_ link goes to _Recipes_ page - YES
	- TEST 1.3 - _My Recipes_ link goes to _My Recipes_ page - YES
	- TEST 1.4 - _Add Recipe_ link goes to _Add Recipe_ page - YES
	- TEST 1.5 - _Categories_ link goes to _Categories_ page - YES
	- TEST 1.6 - _Sign up_ link goes to _Sign up_ page - YES
	- TEST 1.7 - _Log in_ link goes to _Log in_ page - YES
	- TEST 1.8 - _Log out_ logs user in session out of the session and redirects user to the _Log in_ page - YES
	- TEST 1.9 - Non-registered user can see only: _Recipe_, _Sign_up_ and _Log in_ navbar links - YES
	- TEST 1.10 - Registered user can see: _Recipe_, _My Recipes_, _Add Recipe_ and _Log out_ navbar links - YES
	- TEST 1.11 - Admin user can see: _Recipe_, _My Recipes_, _Add Recipe_, _Categories_ and _Log out_ navbar links - YES

&nbsp;

2. Navbar (Mobile):
	- TEST 2.1 - _Recipes_ link goes to _Recipes_ page - YES
	- TEST 2.2 - _My Recipes_ link goes to _My Recipes_ page - YES
	- TEST 2.3 - _Add Recipe_ link goes to _Add Recipe_ page - YES
	- TEST 2.4 - _Categories_ link goes to _Categories_ page - YES
	- TEST 2.5 - _Sign up_ link goes to _Sign up_ page - YES
	- TEST 2.6 - _Log in_ link goes to _Log in_ page - YES
	- TEST 2.7 - _Log out_ logs user in session out of the session and redirects user to the _Log in_ page - YES
	- TEST 2.8 - Non-registered user can see only: _Recipe_, _Sign_up_ and _Log in_ navbar links - YES
	- TEST 2.9 - Registered user can see: _Recipe_, _My Recipes_, _Add Recipe_ and _Log out_ navbar links - YES
	- TEST 2.10 - Admin user can see: _Recipe_, _My Recipes_, _Add Recipe_, _Categories_ and _Log out_ navbar links - YES

&nbsp;

3. Footer:
	- TEST 3.1 - _Get in touch_ link goes to _Contact us_ page - YES
	- TEST 3.2 - _Facebook_ link opens Facebook page in a new browser window - YES
	- TEST 3.3 - _Twitter_ link opens Twitter page in a new browser window - YES
	- TEST 3.4 - _Pinterest_ link opens Pinterest page in a new browser window - YES

&nbsp;

4. Home page:
	- TEST 4.1 - _Sign up_ call to action button goes to _Sign up_ page - YES
	- TEST 4.2 - _Latest recipes_ any of the 3 images links to _Recipes_ page - YES

&nbsp;

5. Recipes page:
	- TEST 5.1 - _Search_ field takes keyboard input- YES
	- TEST 5.2 - _Search_ fiels _search_ button (magnifying glass icon) performs search for the keyword entered - YES
	- TEST 5.3 - _Search_ field _reset_ button resets the search field (reloads the page) - YES
	- TEST 5.4 - Search using a keyword that exists in recipe(s) returns that(those) recipe(s) - YES
	- TEST 5.5 - Search using a keyword that doesn't exist in any recipe returns 'No results found' message with suggested recipes displayed underneath - YES
	- TEST 5.6 - Clicking on any recipe listed on the _Recipes_ page brings user to the full recipe description page of that particular recipe - YES
	- TEST 5.7 - Clicking on _'Back to top click here'_ link underneath the recipes scrolls the page back to the top - search bar level - YES
	
&nbsp;

6. Full Recipe page:
	- TEST 6.1 - All information displayed properly as per designed format - YES
	- TEST 6.2 - If recipe contains word 'mix' or 'mixer', the add for "Schmickser' mixer is displayed on the bottom - YES
	- TEST 6.3 - If the user in session is the owner of the recipe additional buttons: _Edit_ and _Delete_ are displayed at the end of the recipe - YES
	- TEST 6.4 - If the user in session is the owner of the recipe clicking on _Edit_ button takes user to the _Edit Recipe_ page - YES
	- TEST 6.5 - If the user in session is the owner of the recipe clicking on _Delete_ brings up the _Delete this recipe_ modal - YES
	- TEST 6.6 - _Delete this recipe_ modal: clicking on 'yes' deletes the recipe and brings user to _My Recipes_ page - YES
	- TEST 6.7 - _Delete this recipe_ modal: clicking on 'no' cancels the modal and leaves user on the full current recipe page - YES

&nbsp;

7. My Recipes page:
	- TEST 7.1 - _Add new recipe_ button on top of the page brings user to the _Add Recipe_ page - YES
	- TEST 7.2 - _'To browse all recipes click here'_ link on the bottom of the page brings user to the _Recipes_ page - YES
	- TEST 7.3 - Clicking on any recipe listed on _My Recipes_ page brings user to the full recipe description page of that particular recipe - YES
	- TEST 7.4 - If user doesn't have any recipes uploaded the 'No recipes uploaded' message is displayed on the page- YES

&nbsp;

8. Add Recipe page:
	- TEST 8.1 - Choosing _Recipe Category_ selects chosen category, input validation green (valid) - YES
	- TEST 8.2 - Clicking on _Recipe Category_ and leaving "Choose Category" in (nit selecting any category) makes input validation red (invalid) - YES
	- TEST 8.3 - _Recipe Name_ input space doesn't take more than 40 characters - YES
	- TEST 8.4 - _Recipe Name_ input space takes less or equal to 40 characters, validation green (valid) - YES
	- TEST 8.5 - _Recipe Name_ input doesn't validate leaving the space blank, validation red (invalid) - YES
	- TEST 8.6 - _Serves_ input space takes 1 or 2 digits as input, validation green (valid) - YES
	- TEST 8.7 - _Serves_ input space doesn't take non-digit values as input, validation red (invalid) - YES
	- TEST 8.8 - _Serves_ input space doesn't take more than 2 digits as input, validation red (invalid) - YES
	- TEST 8.9 - _Cooking time_ input space takes 1-4 digits as input, validation green (valid) - YES
	- TEST 8.10 - _Cooking time_ input space doesn't take non-digit values as input, validation red (invalid) - YES
	- TEST 8.11 - _Cooking time_ input space doesn't take more than 4 digits as input, validation red (invalid) - YES
	- TEST 8.12 - _Ingredients_ input doesn't validate leaving the space blank, validation red (invalid) - YES
	- TEST 8.13 - _Method_ input doesn't validate leaving the space blank, validation red (invalid) - YES
	- TEST 8.14 - _Image_ input doesn't validate leaving the space blank, validation red (invalid) - YES
	- TEST 8.15 - _Add Recipe_ button doesn't add recipe to the database if at least one input space is invalid, and scrolls to the first invalid space - YES
	- TEST 8.16 - _Add Recipe_ button adds recipe to database if all input fields are valid, and redirects user to _My Recipes_ page (with new recipe displayed there as well) - YES
	- TEST 8.17 - _Unsplash_ link opens Unsplash page in a new browser window - YES
	- TEST 8.18 - _Imgur_ link opens Imgur page in a new browser window - YES
	- TEST 8.19 - _Pixabay_ link opens Pixabay page in a new browser window - YES
	- TEST 8.20 - _Pexels_ link opens Pexels page in a new browser window - YES

	&nbsp;

9. Edit Recipe page:
	- TEST 9.1 - _Edit Recipe_ page is always populated with the correct data - YES
	- TEST 9.2 - _Recipe Category_ let's user choose from the selection of all categories - YES
	- TEST 9.3 - _Recipe Name_ input space doesn't take more than 40 characters - YES
	- TEST 9.4 - _Recipe Name_ input space takes less or equal to 40 characters, validation green (valid) - YES
	- TEST 9.5 - _Recipe Name_ input doesn't validate leaving the space blank, validation red (invalid) - YES
	- TEST 9.6 - _Serves_ input space takes 1 or 2 digits as input, validation green (valid) - YES
	- TEST 9.7 - _Serves_ input space doesn't take non-digit values as input, validation red (invalid) - YES
	- TEST 9.8 - _Serves_ input space doesn't take more than 2 digits as input, validation red (invalid) - YES
	- TEST 9.9 - _Cooking time_ input space takes 1-4 digits as input, validation green (valid) - YES
	- TEST 9.10 - _Cooking time_ input space doesn't take non-digit values as input, validation red (invalid) - YES
	- TEST 9.11 - _Cooking time_ input space doesn't take more than 4 digits as input, validation red (invalid) - YES
	- TEST 9.12 - _Ingredients_ input doesn't validate leaving the space blank, validation red (invalid) - YES
	- TEST 9.13 - _Method_ input doesn't validate leaving the space blank, validation red (invalid) - YES
	- TEST 9.14 - _Image_ input doesn't validate leaving the space blank, validation red (invalid) - YES
	- TEST 9.15 - _Save_ button doesn't update recipe in the database if at least one input space is invalid, and scrolls to the first invalid space - YES
	- TEST 9.16 - _Save_ button updates recipe in the database if all input fields are valid, and redirects user to _My Recipes_ page (with updated recipe displayed there as with changes included) - YES
	- TEST 9.17 - _Unsplash_ link opens Unsplash page in a new browser window - YES
	- TEST 9.18 - _Imgur_ link opens Imgur page in a new browser window - YES
	- TEST 9.19 - _Pixabay_ link opens Pixabay page in a new browser window - YES
	- TEST 9.20 - _Pexels_ link opens Pexels page in a new browser window - YES
	- TEST 9.21 - _Cancel_ button cancels all changes and redirects user to _Recipes_ page - YES

	&nbsp;

10. Categories page:
	- TEST 10.1 - All categories are displayed and each category with _Edit_ and _Delete_ button beside the name - YES
	- TEST 10.2 - Clicking on _Edit_ button takes user to the _Edit category_ page - YES
	- TEST 10.3 - Clicking on _Delete_ button deletes the corresponding category immediately - YES
	- TEST 10.4 - Clicking on _Add category_ button takes user to the _Add category_ page - YES

	&nbsp;

11. Add Category page:
	- TEST 11.1 - _Category name_ input field takes maximum of 20 characters - YES
	- TEST 11.2 - _Category name_ input field doesn't take less than 2 characters, validation red (invalid) - YES
	- TEST 11.3 - _Add Category_ button doesn't add category to the database if the input space is invalid, the input space asks for the correct input instead - YES
	- TEST 11.4 - _Add Category_ button adds category to the database if the input space is valid, the user is redirected to the _Categories_ page, where the newly added category is displayed (in it's correct alphabetical position) - YES

12. Edit Category page:
	- TEST 12.1 - _Edit Category_ page is always populated with the correct data - YES
	- TEST 12.1 - _Category name_ input field takes maximum of 20 characters - YES
	- TEST 12.2 - _Category name_ input field doesn't take less than 2 characters, validation red (invalid) - YES
	- TEST 11.3 - _Save_ button doesn't update the category in the database if the input space is invalid, the input space asks for the correct input instead - YES
	- TEST 12.4 - _Save_ button adds category to the database if the input space is valid, the user is redirected to the _Categories_ page, where the updated category is displayed (in it's correct alphabetical position) - YES
	- TEST 12.5 - _Cancel_ button cancels all changes and redirects user to the _Categories_ page - YES

13. Sign up page:
	- TEST 13.1 - _Sign up_ button appears faded out and is inactive when form first loaded - YES (apart from Safari web browser), see [bugs not fixed](#bugs-not-fixed) section
	- TEST 13.2 - _Username_ input space does not allow more than 15 characters - YES
	- TEST 13.3 - _Username_ input space does not validate inputs with less than 5 characters, validation red (invalid) - YES
	- TEST 13.4 - _Username_ input space does not validate inputs with non alphanumeric values, validation red (invalid) - YES
	- TEST 13.5 - _Username_ input space validates inputs with alphanumeric values, and between 5 and 15 characters, validation green (valid) - YES
	- TEST 13.6 - _Password_ input space does not allow more than 15 characters - YES
	- TEST 13.7 - _Password_ input space does not validate inputs with less than 5 characters, validation red (invalid) - YES
	- TEST 13.8 - _Password_ input space does not validate inputs with non alphanumeric values, validation red (invalid) - YES
	- TEST 13.9 - _Password_ input space validates inputs with alphanumeric values, and between 5 and 15 characters, validation green (valid) - YES
	- TEST 13.10 - _Confirm Password_ input space does not allow more than 15 characters - YES
	- TEST 13.11 - _Confirm Password_ input space does not validate inputs with less than 5 characters, validation red (invalid) - YES
	- TEST 13.12 - _Confirm Password_ input space does not validate inputs with non alphanumeric values, validation red (invalid) - YES
	- TEST 13.13 - _Confirm Password_ input space validates inputs with alphanumeric values, and between 5 and 15 characters, validation green (valid) - YES
	- TEST 13.14 - While _Password_ and _Confirm Password_ inputs are different or are both empty, the 'Sign up' button reamains faded out and 'Passwords don't match' message is displayed  - YES
	- TEST 13.15 - While _Password_ and _Confirm Password_ inputs are both same, the 'Sign up' button becomes active and 'Passwords match' message is displayed  - YES
	- TEST 13.16 - Clicking on _Sign up_ button when at least one of the input spaces is invalidated, does not create a new user in the database and the first invalid space asks for the correct input to be entered - YES
	- TEST 13.17 - Clicking on _Sign up_ button when all of the input spaces are validated, creates a new user in the database and redirects user to _My Recipes_ page - YES
	- TEST 13.18 - Signing up with user name that already exists in the database reloads the _Sign up_ page and generates the appropriate flash message - YES

14. Log in page:
	- TEST 14.1 - _Username_ input space does not allow more than 15 characters - YES
	- TEST 14.2 - _Username_ input space does not validate inputs with less than 5 characters, validation red (invalid) - YES
	- TEST 14.3 - _Username_ input space does not validate inputs with non alphanumeric values, validation red (invalid) - YES
	- TEST 14.4 - _Username_ input space validates inputs with alphanumeric values, and between 5 and 15 characters, validation green (valid) - YES
	- TEST 14.5 - _Password_ input space does not allow more than 15 characters - YES
	- TEST 14.6 - _Password_ input space does not validate inputs with less than 5 characters, validation red (invalid) - YES
	- TEST 14.7 - _Password_ input space does not validate inputs with non alphanumeric values, validation red (invalid) - YES
	- TEST 14.8 - _Password_ input space validates inputs with alphanumeric values, and between 5 and 15 characters, validation green (valid) - YES
	- TEST 14.9 - Clicking on _Log in_ button when at least one of the input spaces is invalidated, does not log user in, and the first invalid space asks for the correct input to be entered - YES
	- TEST 14.10 - Clicking on _Log in_ button when all of the input spaces are validated, logs the user in, and redirects user to _My Recipes_ page - YES
	- TEST 14.11 - Logging in with the non-existing username or password reloads the _Log in_ page and generates the appropriate flash message - YES

15. Contact page:
	- TEST 15.1 - _Email_ input space validates only appropriate email format input - YES
	- TEST 15.2 - _Submit_ button does not send email if at least one of the input spaces is left blank - YES
	- TEST 15.3 - _Submit_ button does sends an email if at all of the input spaces are filled out and the _email_ space has the correct email format - YES

16. Flash messages:
	- TEST 16.1 - Flash message: "Welcome, {{user_name}}!" displayed when users log in to their accounts - YES
	- TEST 16.2 - Flash message: "You have signed up successfully!" displayed when users sign up and create account - YES
	- TEST 16.3 - Flash message: "Username already exists" displayed when users try to sign up using existing username - YES
	- TEST 16.4 - Flash message: "Incorrect username and/or password" displayed when users try to log in with incorrect username or password  - YES
	- TEST 16.5 - Flash message: "You have been logged out" displayed when users log out - YES
	- TEST 16.6 - Flash message: "Recipe Successfully Added" displayed when users add new recipe - YES
	- TEST 16.7 - Flash message: "Recipe Successfully Updated" displayed when users edit the recipe - YES
	- TEST 16.8 - Flash message: "Recipe Successfully Deleted" displayed when users delete the recipe - YES
	- TEST 16.9 - Flash message: "New Category Added" displayed when admin user adds a new recipe category - YES
	- TEST 16.10 - Flash message: "Category Successfully Updated" displayed when admin user edits a recipe category - YES
	- TEST 16.11 - Flash message: "Category Successfully Deleted" displayed when admin user deletes a category - YES
	- TEST 16.12 - Flash message: "Messsage sent successfully" displayed when users send email from the contact page - YES

17. Broken image link:
	- TEST 17.1 - When the link to the recipe image is not broken, the correct image gets displayed on small card recipe preview and the full recipe page - YES
	- TEST 17.1 - When the link to the recipe image is broken, the default image ("...oops, the link to your image seems to be broken") gets displayed on small card recipe preview and the full recipe page - YES

18. 404 page:
	- TEST 18.1 - Misspelling the address of the website in the address bar, redirects user to the "404 Sorry... Page not found" page - YES
	- TEST 18.2 - Clicking on 'To go back to home page click here' link brings user to the _Home_ page - YES


#### Various Internet Browsers Check

Website has been tested on the following Internet Browsers:

- Google Chrome - no issues detected
- Safari - one issue with the Sign up button on _Sign up_ page, see [bugs not fixed](#bugs-not-fixed) section
- Mozilla Firefox - no issues detected
- Microsoft Edge - no issues detected
	
#### Various Devices Check

Website has been checked on Desktop, Laptop, and iPhone6 and iPhone7.
No issues specific to devices were discovered.

&nbsp;

### Bugs

#### Bugs Fixed
1.	- PROBLEM:

        content ...
        
        <img src="assets/images_readme/ms3-readme-testing-bugfix1.png" alt="Cookable website - bugs fixed 1">

	- SOLUTION:
    
        content ...
    
        ```
        JS

        code block
        ```
    
#### Bugs not Fixed
I was able to fix all of the problems that I was aware of.

[Back to top](#contents)

### Username on the navbar
This is clumsily implemented at the moment as the username appears only on pages rendered by functions that take _username_ argument anyway. All pages that 

---


## Deployment

### GitHub Pages Deployment

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com).
2. At the top of the Repository, locate the _Settings_ button on the menu and click on it.

<img src="assets/images_readme/ms2-readme-deployment-one.png" alt="Now We Flip website - deployment instructions">

3. Scroll down the Settings page until you locate the _GitHub Pages_ section.

4. Under _Source_, click the dropdown _Branch: None_ and select _Branch: Master_.

<img src="assets/images_readme/ms2-readme-deployment-two.png" alt="Now We Flip website - deployment instructions">

5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site link in the _GitHub Pages_ section.

<img src="assets/images_readme/ms2-readme-deployment-three.png" alt="Now We Flip website - deployment instructions">

7. The project has been now deployed - the link can be opened in the browser.


### Cloning

1. Find this project [repository](https://github.com/LukaszPasich/Now-We-Flip-MS2-) on github.
2. Under the repository name, click on "Code" button.
3. In the Clone/ Download unfolded tab click on HTTPS (to clone with HTTPS).
4. Click on the 'clipboard' icon to copy the URL of your project.

<img src="assets/images_readme/ms2-readme-cloning-one.png" alt="Now We Flip website - cloning instructions">

5. Open your IDE, open terminal.
6. Change the current working directory to the location where you want the cloned directory.
7. In the terminal type <code>git clone</code>, and then paste the URL you copied earlier.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```
8. Press _ENTER_ to create your local clone.


[Back to top](#contents)


---

## Credits
### Content
content ...


### Media
- image - by artist, downloaded from [www.vecteezy.com](https://www.vecteezy.com/...)

### Code
- Feature taken from this tutorial: [https://www.youtube.com/...](https://www.youtube.com/...), (script.js file, array declared in line 013).

### Resources
Websites I have accessed for solutions/ questions and extra resources:
- [www.w3schools.com](https://www.w3schools.com)
- [www.stackoverflow.com](https://stackoverflow.com)
- [www.developer.mozilla.org](https://developer.mozilla.org/en-US/)
- [www.css.tricks.com](https://css-tricks.com)
- [Code Institute course content](https://codeinstitute.net/)
- [Kevin Powell youtube channel](https://www.youtube.com/user/KepowOb)
- [Web Dev Simplified youtube channel](https://www.youtube.com/c/WebDevSimplified)

### Acknowledgements
- Thank you to my mentor __Nishant Kumar__ for his guidance, support and continuous helpful feedback throughout this project.
- Tutor Support at Code Institute and the Slack Community for a solution to any question at any time.

[Back to top](#contents)

---

## Contact
For any queries related to this project, you can contact me at: lukas (dot) zed81 (at) gmail (dot) com.

[Back to top](#contents)

---

## THANK YOU FOR TAKING TIME TO VIEW THIS PROJECT!