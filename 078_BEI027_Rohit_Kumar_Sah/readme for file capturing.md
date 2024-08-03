# Assignment 9 
Capture File Uploading on Web app in Wireshark

## What occured:
An web app made using Flask is created in this task. The web app allows user to upload file and save them to local storage.

## How to capture in Wireshark
- Open Wireshark
- Look for WiFi or Adapter for loopback traffic capture 
- Select one (I got to capture in Adapter for loopback traffic capture)
- Upload the File in Web App till this is captured by Wireshark
- Stop the captured once file uploading is done

## Filtering and following Stream
- To filter just type ```http``` in the Filter tab.
- To follow stream select any packet of http and right click on them and select ```HTTP Stream``` or ```TCP Stream``` (as required) in the Follow menu.


