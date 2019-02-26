# Writeup 2 - OSINT

Name: Linda Yeung
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Linda Yeung

## Assignment Writeup

### Part 1 (45 pts)

v0idcache's real name is Elizabeth Moffet.

v0idcache works at 13/37th bank, located at Leeteinde 12 Broek Waterland 1151 AK, NL. The URL to her website is 1337bank.money.

v0idcache's phone number is 1.323331. This was found on WHOIS as the registered phone number required to make her website.
v0idcache's email address is v0idcache@protonmail.com. This can be found on her website as well as the registered email from WHOIS.
v0idcache's Twitter handle is @v0idcache. I used social-searcher.com to search for all social media accounts associated with v0idcache.
v0idcache is also taken on videobam but I was not able to access that site.

142.93.136.81 is her IP. I found this using Tracerroute.
The location of the server is in Amsterdam, Netherland. I found the location via iplocation.net. dnstrails.com showed that the website was set up through digitalocean.com. It showed that the website was created on 2/6/19. Other than that, there was no other history.

1. 1337bank.money/secret_directory (CMSC389R-{h1ding_fil3s_in_r0bots_L0L})
2. 1337bank.money/.git/COMMIT_EDITMSG (CMSC389R-{h1d3_s3cret_g1ts})

Open ports are:
22 -SSH
80 -HTTP
1337 -WASTE
I found these by running nmap -p 1-5000 142.93.136.81. Scanning 1-5000 ports allowed me to view more than the first 7 responsive ports so I was able to find 1337 as well.

The OS is Ubuntu-4ubuntu0.2. At first Nmap -O scan returned no results, so I ran the IP address on shodan.io since SSH service requires OS information.

Other flags:
CMSC389R-{h1dd3n_1n_plain_5ight} --found on source code of her website.
CMSC389R-{h0w_2_iNtO_DNS_r3c0Rd5} --found on txt portion of dnsdumper.com.
CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh} --found by viewing file AB4300.txt after logging into port 1337. AB4300.txt was the file she mentioned on her pastebin.


### Part 2 (75 pts)

From part1, I was able to find the open port 1337 from her website (through nmap). On the command line, I used Netcat by running "nc 142.93.136.81 1337" [netcat IP address Port] to test the server, to which I was prompted for a Username and Password. Since her usertag is v0idcache, that would be a logical place to start for her username. For the password, I needed to try a bunch of common words which Kali Linux comes conveniently with. The script already pointed to the path on my Kali system but I had to go there to extract the .gz file so it could read line by line. Using Python, I created a while loop which ran infinitely, reading in a new line for each iteration. I set the password to be the line read in, and set the username to always be v0idcache. I executed this script which sent the username and password to the socket upon being prompted.I noted that the response was "fail" when the incorrect log ins were provided. So in the while loop, I read back the response from the socket, stored in a variable called data, and inserted a line that said if data did not include "fail",break. This would ensure when the correct password was given, it will not return fail, thereby I would break out of sending data to the socket and not keep running infinitely even after finding the password. I printed out the password once it was found, and using that, I logged into the system. Since most files are stored in "home" folder, I went into that folder and found the flag.txt file!
