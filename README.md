# FactMap

Create a bot like application that provides interesting information about a 
location.


### Fonctionalities:

Upon reaching the web page, the user is presented with the following 
elements:

   - header: logo and branding
   - central zone: a dialogue history frame and a text entry box in order to 
   interact with the application
   - footer : copyright info

The user uses the text box to request if the application knows the address 
of a place. Once the question is sent, it is displayed in the dialogue 
history area and a spinner is displayed until the response is returned.

The application return a first response including the address of the location 
requested. A map is displayed with the location tagged.

A second response is returned with information collected from Wikipedia about 
the location requested and a link to the associated Wikipedia page.

The tone of the application response will be informal as the application is 
to imitate the interaction between a grandfather and his young grandson.


### Specifications:

The application interactions will be provided via AJAX: the requests and 
response are displayed in the main page, without reloading.

The reponse information will be provide by the Google Maps APi and the Media 
Wiki API.

The application will be stateless. Reloading the page will lose all previous 
interactions.


### Resources:

 - [Google Maps API](https://developers.google.com/maps/documentation/)
 - [Media Wiki API](https://www.mediawiki.org/wiki/API:Main_page)
 

### Deliveries:


 - [Application URL]()
 - [Github repository](https://github.com/slesouef/FactMap)
 - [Agile board location](https://trello.com/b/f5wgDaC1/factmap)
 - Project description document
 
 ## Version:
 
 0.1 : First alpha release. The bot replies with an address and a map in 
 response to the user entry (01/22/2019)
 
 0.2 : Second alpha release. Address displayed in fr and marker of location 
 is displayed on map (01/26/2019)