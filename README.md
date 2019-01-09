# Project Kojak: Twitch Plays Data Science

![](twitch.png)

#### Background

In 2017, 355 billion minutes were spent watching live streams of gamers playing games. This is a rapidly developing space ripe for ads and sponsorships. Companies need to promote their services and products in a smarter way in this young field. 

#### Objective

* Create a MongoDB database setup on an AWS instance to store data.
* Develop a time series model for predicting game viewership.
* Create a flask app to make live viewership predictions for several games and individual streamers.

#### Results

* Created a MongoDB database setup on an AWS instance to store 2 million documents of Twitch API data.
* Developed a time series ensemble model for single game viewership with SARIMA and Facebook Prophet. (MAE ~ 6000 for 30k-50k viewership)
* Created a flask app demo to make for 24-hour viewership predictions for several games.

[Project Kojak Final Slides](kojak_twitch.pdf)
