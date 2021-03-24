# Online-Class-Environment
Django based E-learning Web-application similar to google classroom.

## https://onlineclassenv.herokuapp.com/

## Technologies Used and Dependencies
* Django Framework
* Django Google Drive Storage
* Django REST Framework (Handling AJAX requests)
* QRCode.js (QR Code generator)
* js-cookie (For easier csrf token fetching)
* waypoints (For infinite scrolling)

## Following are the features of the web-app

1. Create online classrooms with other users.
    * To join rooms, users should have the room's secret code (UUID)/Unique id shared by creator.
    * Room's secret codes can be shared through QR codes, and plain text.
2. User can join multiple classes.
3. Classrooms where you can upload files and download files.
  * Edit/ Delete option is present.
4. Classroom where anyone can post announcements and  other users can  see and get notification accordingly.
  * Edit/ Delete option is present.
5. Classroom creator's can manage the people joining in their room. They can ban any users they don't want inside their room.
6. Infinite scrolling is there in the announcement section.
7. Search bar where you can search the specific document/announcement.



