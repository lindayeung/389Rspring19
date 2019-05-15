# Web

## Assignment details

This assignment has two parts. It is due by 5/10/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!

[http://1337bank.money:5000](http://1337bank.money:5000)

The flag I found was CMSC38R- {y0U-are_the_5ql_n1nja}
I found this flag after realizing that each row in the table corresponded with an id and there were only ids 0, 1, 2. The server will query for a row matching with the id based on the selected link, but what we want is to dump all the rows irregardless of id. Thus, because the query is a GET request, I manipulated the GET to inject an SQL injection. Instead of saying id = 1, I inserted ' || 1=1 -- . This uses the tautology that 1 is always equal to 1 and the ' to emulate code on the database server. So instead of querying for rows with the matching ID, the server queries for rows where id is empty (but we don't care about that), and the trivial statement 1=1 is true, which will dump all rows. Here, I had to use the pipe variation of the OR because the OR keyword was checked as a defense so the server detected the SQL injection in that case.  

### Part 2 (60 Pts)
Complete all 6 levels of:

[https://xss-game.appspot.com](https://xss-game.appspot.com)

1. I inserted the <script> alert()</script> into the search, so that when the server returned the HTML page after hitting search, it also echo back the input which is seen by the browser as code instead of a string of user input.

2. In this stage, the <script> trick didn't work so I played with the img tag and commented this to force the browser to sinking into loading the img tag as part of the HTML page. However, we don't actually want it to load an img; to get it to load an alert, I put an empty img tag img src='' followed by onerror, to get the tag to execute the onerror because the src is invalid. The onerror will run some javascript, which is where I inserted the alert(). Altogether, this looked like <img src='' onerror="alert()">.

3. From the source code, I could see that the javascript function will take as parameter num and generate an html tag to be rendered based on the value of num concatenated to <img src='/static/level3/cloud. Because the num is read by a GET request in the URL, I can manipulate the value of num by changing the URL. So instead of putting a valid value, I use the onerror trick again to make the input emulate code. So first inserted some trash value to make sure the img could not load, and then inserted an onerror line with it to trigger the alert.

4. From the source code, I could see that the vulnerable line was: <img src="/static/loading.gif" onload="startTimer('{{ timer }}');" />. The timer field is taking in user input, and as with the previous attack, the input could be formatted in such a way that it would look to the browser as code. So for this part, instead of inserting a valid time, because onload can perform more than one javascript function, we want to end the start Timer function by providing a single ' and ; . Then we will insert the alert function to follow. This looked like '; alert('. The original tag would finish the alert so that the HTML is still correctly formatted. With this one, I had to use percent encoding instead of the ; because the ; is a special character so it was not read in.

5. The vulnerable line for this stage was:  <a href="{{ next }}">Next >></a>.
Like stage 5, the next takes in unsanitized user input, so that we could construct that field in such a way that it would be treated as code within the href attribute of the a tag. Once again in this stage, we could change the value of next because it is a GET request so it is located in the URL. I simply made the value javascript:alert(), which would basically tell the HTML code that we are now calling the alert function from javascript when the link is clicked.

6. For this one, the vulnerable line was with the url not being properly check. The function simply ensures that the url doesn't begin with http:// to presumably prevent fetching from a new server (which could potentially execute anything) but instead I used data:text/javascript,alert('0') which is a URI media that includes the alert() script. The server will load this file. 

### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
