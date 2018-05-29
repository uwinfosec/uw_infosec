## HTTP by Hand Homework
Homework challenges can be found at: http://http.websecurity.church/

### Browse by Hand - 10 points
The tool we will be using is called netcat. It is a tool for establishing a TCP or UDP session with a remote service so you can send arbitrary data - in this case HTTP. On Linux systems and OS X the tool is installed by default and you can access the tool via the command line (or terminal) and it is called: nc. If you are on Windows you need download tool from the following repo: https://github.com/diegocr/netcat though I would recommend using terminal on one of the lab computers. 

You can use the tool to send requests like this (by typing it on the command line):

```
nc -v http.websecurity.church 80
```

This connects to the ttp.websecurity.church web server on port 80 and turns on verbose output so you can see when you successfully connect. You can then type out a request and hit enter twice to send it. Try sending a malformed request to see what the server does (your command line prompt may look a little different):

```
12:01 $ nc -v http.websecurity.church 80
found 0 associations
found 1 connections:
     1:	flags=82<CONNECTED,PREFERRED>
	outif en0
	src 10.12.10.17 port 57590
	dst 162.243.137.118 port 80
	rank info not available
	TCP aux info available

Connection to http.websecurity.church port 80 [tcp/http] succeeded!
omg haiiiii!
<html>
<head><title>400 Bad Request</title></head>
<body bgcolor="white">
<center><h1>400 Bad Request</h1></center>
<hr><center>nginx/1.1.19</center>
</body>
</html>
```

In order to send a valid HTTP request you will need to write it out line by line, hitting enter twice when you have typed it all out and want to send it. The server will respond and the connection will close. You can look at the response if it was successful and determine what you should do next. Remember, a server will respond with response codes - those can help you a bit. The ultimate goal is to log in and get the flag.

Note: 
- No using any tools besides netcat (and maybe echo)
- Keep track of the requests you send so you can reproduce your findings

### Deliverables
You will need to write a small report in the .txt format (no Word Docs, PDFs, RTFs, or anything other than a .txt). The report should include:

- A copy of all of your requests
- The flag(s)

### Due Date
17:30 Tuesday April 10th 2018

### Note
Please include links to any pages, guides, tutorials, people, or anything you used to help you figure out these challenges. Please do not cheat or trade answers! If you gently/fairly help one another out make sure to credit the people that helped you in your report. Give credit where credit is due.