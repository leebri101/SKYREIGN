# **Geography Challenged**
## **Site Overview**

## Contents-Page:
1. [**Site Overview**](#site-overview)
1. [**Project-Planning**](#project-planning)
    * [**Target Audiences:**](#target-audiences)
    * [**User Stories**](#user-stories)
    * [**Site Objectives:**](#site-objectives)
    * [**How Is This Will Be Achieved:**](#how-will-this-be-achieved)
    * [**Wireframes**](#wireframes)
    * [**Color Scheme**](#color-scheme)
    * [**Reused Code**](#reused-code)
1. [**Current Features on all pages**](#current-features-on-all-pages)
    * [**Headers:**](#headers)
        * [*Title*](#Title)
        * [*Call To Action Button*](#call-to-action-button)
        * [*Start Game Section*](#start-game-section)
      * [**Quiz-Section**:](#quiz-section)
          * [*Quiz-Tracker*](#quiz-tracker)
      * [**Questions and Answers**:](#questions-and-answers)
          * [*Q and A*](#q-and-a)
    * [**Point-Tracker**](#point-tracker)
    * [**Results-Section**](#results-section)
    * [**Footer**](#footer)
    * [**Typsetting**](#typesetting)
1. [**Potential-Features**](#future-enhancements)
1. [**Testing Phase**](#testing-phase)
1. [**Deployment**](#deployment)
1. [**Credits**](#credits)
    * [**Honorable mentions**](#honorable-mentions)
    * [**General reference:**](#general-reference)
    * [**Content**](#content)
    * [**Media**](#media)

## **Project Planning**
### **Target Audiences:**
* For users who are interesting in a playing short games.
* For users who are learning about geography.

### **Site Objectives:**
* Allowing users to know of short fun facts about geography.
* Educating the user on using this as a fun way of educating themselves.

### **User Stories:**
* As a user I want to give feedback via the given social media links to further 
improve/enhance the quiz to the owner.
* As a user I want to be able to easily navigate the quiz with ease.
* As a user I want have fun on short quizs without being bored.
* as a user I want the quiz to be as simple easy to understnd.

### **How will this be achieved:**
* The landing page with have a simple CTA (Call To Action) input button at which the user must ineteract with to continue the quiz.
* The page will have the following things:
    * A large coloured CTA play button at which when the user/player hovers over, a small animation will occur and change colours briefly tempting the user to click it which leads to a different pop up to appear.
    * A small text box which the user has to input their name to start the quiz, if nothing has been inputted the quiz cannot start.
    * A series of questions out of ten which displays the question, and four different options at which the user must pick one correct answer to see if it is correct or not.
    * A results page which gives feedback to players as to how many questions they have answered correctly out of 10. 
    
### **WireFrames:**
* In order to prevent any digression to project aim & objectives I have made a few wire frames as a plan to refer back to from in case of any major changes.

[Wireframes](doc/wireframes/) were all designed in Balsamiq desktop.
* [Desktop-Landing-Page](doc/wireframes/desktop-landing-page.png)
* [Desktop-Quiz-Page](doc/wireframes/desktop-quiz-page.png)
* [Desktop-Results-Page](doc/wireframes/desktop-results-page.png)
* [Mobile-Landing-Page](doc/wireframes/mobile-landing-page.png)
* [Mobile-Quiz-Page](doc/wireframes/mobile-quiz-page.png)

There was small changes from the planned wireframes to enhance the UX (User Experience). 
Changes include:-
* An interactive CTA play button which is changes color upon hovering.
* A placeholder on the start-game section text box for players to input their names and warning to users if they start the game with no input in the text box.
* An animation on the timer clock which shows a small stop watch shake after each second to indicate the user that time is ticking.
* A hover animation over the 4 different choices of answers within the answers section of the quiz which change color whilst the animation occurs.
* The results page having a box which shows the player's score and a coloured gradient on the border of the box which constantly spins aorund the edge of the box.
* A small Favicon to act as an icon for the webpage.

### **Color Scheme:**
 * When creating the design of the quiz site I have went with this colour scheme to match the overall theme of georgraphy with the colors of the earth having blue and green elements.  

 ![Contrast Grid](doc/screenshots/color-scheme.png)

### **Reused Code:**
* Some code has been re-used in from the first milestone project due to the simplicity and effectiveness it has on the overall layout of the final design.
    * Which one of any said weblinks have an original colours.
    * Upon hovering over it or clicking it will change colours. 
    * After visting the said weblink it will change to a secondary color. With the hover effect in place.
![Reused Code](doc/screenshots/reused-code.png)

## **Current Features on all pages**
###  **Header**
* The header has been placed in the top center of the page to allow for a easy transition between desktop and mobile so it doesn't affect the page in huge way. 

 The header itself contains the following features: 

### *Title:*
* The Title is there to show the name of the page.

![Title](doc/screenshots/header.png)

#### *Call To Action Button:*
* The CTA is there with theme of the Earth to match the theme and catch the user's attention the moment that they enter the site. 
    
![CTA Button](doc/screenshots/cta-play-button.png)
    
* Mobile version of CTA button with header and footer.

![Mobile-version](doc/screenshots/mobile-version.png)

#### *Start Game Section:*
* The start game section has an autofocus placeholder on the text box which allows for more accessibilty to the user, which is useful on mobile devices as the text cursor is already highlighted in the text box which saves time for the user to manually navigate to it as. 
* Two interactive buttons for the user to input one of which is the Start Game, which upon text input and clicking the button will send the user to commence the geography quiz. The Quit button will send the user back to the main screen where the CTA button is displayed.
* A error handler which diplays a red border in the text box if the user hasn't provided any sort of text or name.
* An event listener where the user can press the ENTER key which has the same response as clicking the Start game button. 

  ![Start Game Section](doc/screenshots/placeholder-input.png)

### **Quiz-Section**:
#### *Quiz-tracker:*
Features used:
* A indicator display to track the current question number the user is on out of the total quiz questions.
* A countdown timer with a animation which moves each time a second is lost within the alloted time length.
* A countdown bar to also track time but visually display the length of time left in the bar.
![Quiz-section](doc/screenshots/tracker-update.png)

### **Questions and Answers**:
#### *Q and A:*
Features used:
* A question with a four choice option answer selector. 
* Users being able to select any answer before clicking next to proceed to the next question.
* Each answer having a hover animation with a color changing function,  the color also changes when the user clicks on answer. 
* The Fisher-Yates method used to shuffle all the questions and answers to any given random order out of ten. So no same question is used twice.

![Quiz-Questions](doc/screenshots/quiz-questions.png)

## **Point-Tracker**
* The point tracker is used to display to the user whether they have; answered the question correctly, gave an incorrect answer, did not give answer and to show which answer they are currently on.
* The point tracker is indicated in four different colors:
    * Green: Meaning the user has answered the question correctly.
    * Red: Meaning the user has answered incorrectly.
    * Gray: Meaning the user has ran out of time or can alternatively skip the question.
    * Yellow: To indicate to the user that they are on the current question.
![Point-Tracker](doc/screenshots/progress-tracker.png)

## **Results-Section**
* The results sections shows the following things:
    * The users score out of 10.
    * A feedback message to the user as to whatever associated score they have recieved.
    * A Play Again button if the users wishes to replay the quiz again.
![Resuts-Section](doc/screenshots/results-page.png)

## **Footer**
* All icons that were used in the footer is sourced from font awesome.
* A personal copyright has been added in-case of plagerism.
* A personal link to my GitHub page which users can track my coding journey.
![Footer-Page](doc/screenshots/footer.png)

## **Typesetting**
 Throughout the second project milestone only this font was used:
  * Poppins - for a more simplistic look to users so it not too much for them.
* Fonts that have used in the project have been sourced from Google Fonts (quoted in the credits).

## **Potential-Features**
* Due to the project deadlines being in a very tight timeframe the project had to be scaled down to a more simpler version of the geography quiz but these are the features that I would like to potentially add or implement in the near future:
    * An interactive version with sounds and unique animations.
    * Potentially adding a leaderboard system/table to challenge and rival other users.
    * A narration voice over for all the questions and answers for users with disablity issues.
    * A mixture of sound, images and text based questions and answers.
    * A shuffler for answer as well.
    * Different modes within the quiz for example:
        * A speed test to see how quick and accurate the user can answer the questions.
        * Different difficulites in place to challenge the user.

***
## **Testing-Phase**
Full details of the testing phase can be found here: [TESTING.md](TESTING.md)
***
## **Deployment**
The project has been deployed with the following steps: -

1. Within the project's [repository](https://github.com/leebri101/Geographically-Challenged), you select the **Settings** tab.
2. Then select the **Pages** menu tab on the left side.
3. Under **Source** then, select the **Main** branch from the drop-down menu and click **Save**.
4. A message will then pop up that the project has been successfully deployed with a live link.

You can visit the live link via this URL - [Geographically Challenged](https://leebri101.github.io/Geographically-Challenged/)
***

 ## **Credits**
### **Honorable mentions**
The second project was a very interesting but difficult challenge, which tested my understanding of HTML & CSS but to incorperate JavaScript too. However the more stuff that was being introduced to the project the more simpler and effective the project became due to time restraints of the course, but nonetheless it is a good way to show what i can do, but i must credit the following people:
 * [Can Sucullu](https://github.com/cansucullu) - My Code Institute mentor who is incredible at giving me insite and suggestions on further improving my project and is a huge help to continuously support me for any sort of technical issues within the project.
* The Slack community of Code Institute for helping me with JavaScript module as it is somewhat challenging due to the deadline and questions on the module.
* Code Institute Tutors for assisting me with the technical aspects of the project i.e the intergation from Gitpod to codeanywhere and general assitance to coding problems. 
* My older brother for always being available for being a personal guinea pig for my projects (and with many more to come) and giving me constant constructive feedback all the time.
* Huge thanks to my girlfriend for the constant support and nagging me to stay focussed whenever i get distacted and also giving me useful advice and insight.

### **General reference:**
* The project theme was inspired by the Code Institute's coding project called Love Maths. I have tried to change as much as possible but there may be some similarties within the codes.
* I have used W3Schools for a basic understanding and learning process for knowing JavaScript a bit better, and for general basic coding references and as general encyclopedia for any code related issues or ideas.

### **Content:**
* All icons that were used throughout the project are sourced from [Font-Awesome](https://fontawesome.com/)
* All fonts used have been imported from - [Google-Fonts](https://fonts.google.com/)

### **Media:**
* Background image on the landing-page: [World-Globe](https://www.wallpaperflare.com/globe-world-map-earth-global-travel-planet-geography-wallpaper-akzmf/download)
* Favicon for tab of page on index.html: [Favicon-Globe](https://www.flaticon.com/free-icon/earth-globe_616616)
* General RGB color Table used in style.css: [RGB-Table](https://www.rapidtables.com/web/color/RGB_Color.html)
* Image compressions: [TinyPNG](https://tinypng.com/) 
* Colored grid scheme: [EightShapes](https://contrast-grid.eightshapes.com/)
* Britannica-quizes for overall design idea and theme: [Britanica](https://www.britannica.com/quiz/name-that-world-flag)
* Webcode Tools for general key frame animation use: [Webcode.Tools](https://webcode.tools/generators/css/keyframe-animation?utm_content=cmp-true)
* HubSpot for different styling of animations on CSS: [HubSpot](https://blog.hubspot.com/website/css-hover-animation)
* World Population Review as a general reference to check information for the quiz: [WorldPopulationReview](
https://worldpopulationreview.com/country-rankings/smallest-countries)
* RapidTables for general encyclopedia for searching for colour themes: [RapidTables](https://www.rapidtables.com/web/color/RGB_Color.html)
* Mike Bostock's incredible method of shuffling: [Fisher-Yates](https://bost.ocks.org/mike/shuffle/)