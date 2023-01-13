# Table of contents
1. [Welcome](#welcome)
2. [Features](#features)
    - [Navigation](#navigation)
    - [Lists Page](#listspage)
    - [List Details Page](#listdetails)
    - [Registration](#registration)
    - [Shopping lists](#shoppinglists)
    - [List items](#listitems)
    - [Header and Footer](#footer)
3. [Testing](#testing)
    - [Feature testing](#featuretesting)
    - [Validator](#validatortesting)
    - [Responsiveness](#responsivetesting)
    - [Lighthouse](#lighthousetesting)
    - [Other testing](#othertesting)
4. [Technologies](#technologies)
4. [Deployment](#deployment)
5. [Content Credits](#credits)


<a name="uxdesign"></a>
## UX Design

Theme, Epic and User Stories

The purpose of the website is for users to be able to create shopping lists when they need them. Users can create as many lists as they need, for any different purpose. Inside the list, users can specify a title, a description and a due date, as well as the individual items. Users can mark the list as complete when these items have been purchased.

The User Stories can be found in Github Projects and are displayed in the Kanban board format. Each user story has an acceptance criteria and tasks. The User Stories are:

- Account registration: As a site user I can create an account so that I can create my shopping list
- Login: As a site user I can login to my account so that I can view/edit my lists
- Create list: As a site user I can create a list so that I can see items I need to buy
- View list: As a user I can view my lists so that I can see how many lists I have and what is in them
- Edit list: As a site user I can edit my shopping lists so that I can make any necessary changes
- Delete list: As a site user I can delete my lists so that I do not have to view lists that I no longer need
- Add item: As a user I can add items to lists so that I have all items I need
- Delete item: As a user I can delete items so that lists do not contain items no longer needed

Design and layout

For the design, a colour palette was selected from coolors.co. The idea was to keep the theme very simple, so the user can focus on the content of the page and on the content of their lists. One image is used on the homepage and the other pages just contain the necessary content.

Wireframes

![Alt text](static/media/wireframes.jpg "Title")

The original idea was to have the lists display all on one page, with the update and delete buttons. This was changed as it would be too much information on one page when the user has multiple lists and it would get confusing trying to read all of them at once. This page now has a neat list of all of the shopping lists with just the title, description and due date. Users can click on 'see details' to get into another page that has all of the actual items and more information.

<a name="features"></a>
## Features

<a name="navigation"></a>
### Navigation bar

![nav](static/media/nav2.jpg "Navigation")

![nav](static/media/nav.jpg "Navigation")

The navigation bar gives the user different options based on their logged in/out status. When users are signed out, or not yet registered, they will see the options for the homepage, to sign up or login. Once users register and/or login, the navigation bar changes to show the homepage, their lists page and a logout option. The purpose of these different navigation options is to provide a personalized experience to the user and to recognize their account status. The options presented to them are therefore relevant and useful to that specific user.

<a name="listspage"></a>
### Your Lists page

The 'your lists' page is also personalized and tailored to the specific user that is logged in. The views are user specific, meaning that only the lists that belong to the logged in user will be visible. On this page, users will see all of the lists they have created. The title, description and a 'see details' option will be shown to them. If the list has been marked as complete, the title will have a strike through it.

<a name="listdetails"></a>
### List Details page

When users click on the 'see details' link on the 'your lists' page, this will bring them into the list details page for that specific list. On this page, users can see all details related to that list such as title, description, date created, last updated, due date and items. Other than viewing, users can also take actions on this page with 3 different buttons.

The 'edit list' button brings up a form with the title, description, due date and complete status fields. Users can edit these fields and mark the list as complete, save the form and they will be redirected to the list details page which will now change to show the updates made.

The 'delete list' button will bring up a confirmation page asking if the user wants to delete the list. When this is confirmed, the list is deleted and the user is redirected to the 'your lists' page. The deleted list no longer shows there, as it has been deleted.

The 'edit items' button ...

<a name="registration"></a>
### Register/login/logout

These options are displayed on the navigation bar. Click on 'register' opens a form which asks the user to select a username and password. There is an option field for an email address. Once the fields are filled in, users can then click on the 'sign up' button and this will create their account.

If users click on the 'login' option, this brings up a form where they insert their username and password. When clicking on 'sign in', they are redirected back to the homepage with the updated navigation options and will see a success message confirming they have signed in.

When users have finished their session and are ready to logout, they can use the 'logout' option on the navigation bar. They are asked to confirm if they want to logout and then have to click on the 'sign out' button to confirm this. Again, users will see a success message to confirm that they have successfully been logged out.

<a name="shoppinglists"></a>
### Shopping lists: create, read, update, delete

<a name="listitems"></a>
### Shopping list items: add and remove items

<a name="footer"></a>
### Header and Footer

The header is a simple design with text that lets the user know what the purpose of the website is and what they can expect from the site.

The footer is again a simple design and contains links to social media sites and pages.


<a name="technologies"></a>
## Technologies

<a name="testing"></a>
## Testing

<a name="featuretesting"></a>
### Feature testing

Feature testing was done manually by going through each feature and ensuring it works as intended. Below are details of this manual testing:

Homepage

| Action        | Expected Behaviour  | Result | 
| ------------- | ------------- | ------------- | 
| Enter url of site in browser  | site shows homepage | pass | 
| Click register  | user registration page opens | pass | 
| Click login  | user login page opens | pass | 
| Submit register form | user is created | pass | 
| Submit login form | user is logged in, success message shows | pass | 
| User logs in | navigation links change to show 'logout' and 'your lists' | pass | 
| User logs out | navigation links change to show 'login' and 'register' | pass | 
| User logs out | success message shows | pass | 

Your Lists page

| Action        | Expected Behaviour  | Result | 
| ------------- | ------------- | ------------- | 
| View page  | Displays lists belonging only to logged in user | pass | 
| View page  | Completed lists show with a strike though title | pass | 
| View page  | Title, description and see details shows for all lists | pass | 
| New list button  | Form to create a new list opens with all fields | pass | 
| Submit new list form  | List is created and is added to the page | pass | 
| Click see details on any list  | Redirects to list details page (for that specific list) | pass | 

List Details page

| Action        | Expected Behaviour  | Result | 
| ------------- | ------------- | ------------- | 
| View page  | Displays details only for list clicked on | pass | 
| Edit list button  | Opens a form that allows to edit title, description, due date and complete status | pass | 
| Submit edit list form  | List details page updates with the new data | pass | 
| Mark list as complete on edit list form  | Strike appears through title on your lists page | pass | 
| Delete list button  | Opens form asking to confirm deletion | pass | 
| Confirm list deletion  | List is deleted, redirects to your lists page | pass | 
| Edit items button  |  | pass | 


<a name="validatortesting"></a>
### Validator testing

HTML validator testing passed (https://validator.w3.org/)
CSS validator testing passed (https://jigsaw.w3.org/css-validator/)
PEP8

<a name="responsivetesting"></a>
### Responsiveness

<a name="lighthousetesting"></a>
### Lighthouse

<a name="othertesting"></a>
### Other testing



<a name="deployment"></a>
## Deployment

<a name="credits"></a>
## References