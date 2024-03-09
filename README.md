# Assginment 4
# Rohit George Rarichan 

This assignment required us to create a program that would be able to send a blog post to the IC232 server. We also had to use web APIs from which we would extract data and return favorable outputs.

In this project, we have 5 main files that are our a4, ds_client, ds_protocol, OpenWeather, and LastFM. 

ds_client: It is the file that contains the send function that will actually be directly interacting with the server so that the blog posts or in other words, the message that the user wants to send to the server can be sent with the timestamp and username. 

ds_protocol: This file contains the protocols that are used in the send function in the ds_client file. They contain the bio, post, and join protocols.

OpenWeather: This is the file that contains all the data regarding the weather API that we were tasked to use in the assignment. It has multiple parameters and options that describe the weather conditions and other related attributes and posts them onto the server based on a keyword given by the user.

LastFM: This is the file that contains the data regarding the music API that was provided to us in the assignment. It has 3 options you can get album info, top tracks of an artist, or the best artists on the billboard charts and then send them to the ICS 32 server to be posted. 

a4: This is the file that runs all the code that is present in these modules of code.