# REST API for the Pereval application
## A fully functional project written in Python and Django that makes it possible to add information about various mountain passes

### Description:
The project was developed for the `"ФСТР" Russian Sports Tourism Federation ` ( site - https://pereval.online/ ) to maintain a base of mountain passes, which is filled with tourists. In the mountains, people will enter data about the pass into the application and send it to the `"ФСТР"` as soon as Internet access is available. A moderator from the federation will verify and enter information received from users into the database, and they, in turn, will be able to see the moderation status in the mobile application and view the database with objects entered by others.

### Usage possibilities for the user:
1) Entering information about a new object (pass) into the object card.
2) Editing of object data not sent to the FSTR server in the application. The Internet does not always work at the pass.
3) Filling in the full name and contact details (phone and e-mail).
4) Sending data to the "ФСТР" server.
5) Receiving notification of the sending status (successful/unsuccessful).

### Data about the pass transmitted to the "ФСТР":
1) The coordinates of the object and its height;
2) The name of the object;
3) Some photos;
4) Information about the user who transmitted the data about the pass:
   * user name (full name in a string);
   * mail;
   * telephone. :shipit:

{
    "status": "",
    "beauty_title": "",
    "title": "",
    "other_title": "",
    "connect": "",
    "user": {
        "email": "",
        "fam": "",
        "name": "",
        "otc": "",
        "phone": ""
    },
    "coord": {
        "latitude": null,
        "longitude": null,
        "height": null
    },
    "level": {
        "winter": null,
        "spring": null,
        "summer": null,
        "autumn": null
    },
    "images": []
}
