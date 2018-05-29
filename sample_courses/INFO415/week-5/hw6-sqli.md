## SQLi HW Grading (50 points total)
Homework challenges can be found at https://sqli.websecurity.church/

To go to your individual challenges go to https://sqli.websecurity.church/[uw-netid]

Example: My UW NetID is amckenna so I would go to: https://sqli.websecurity.church/amckenna/

## Part 1 - Vulnerabilities (41 points)
- challenges 1-14: 28 points total (2 each)
- challenge 15: 5 points (pt1 2 points, pt2 3 points)
- challenge 16: 6 points
- challenge 17: (5 extra credit points)
- version number: 2 points

To earn full points on challenges 1-14 you must craft a payload that exfiltrates both the flag user's username and password. On several of the challenges the payload may only inconsistently exfiltrates the flag user's credentials (try hitting refresh a few times to verify). You must craft a reliable payload that exfiltrates the flag user's name and password every time. The payload should be in the form of a link that I can click on to see the results. An additional two points will be awarded if you can get the database version number and submit to me the payload used, as well as the correct version number. It doesn't matter which challenge number you use to exfiltrate the version number.

For challenge 15 you wont be exfiltrating the flag user's credentials, you will be playing a guessing game. You must craft a payload that "wins" the guessing game every time. Hint, you can do it without knowing your number (2 points). Additionally you must also craft a payload the exfiltrates the number that you are supposed to guess (3 points).

For challenge 16 you wont be directly exfiltrating the number from the guessing game. Instead you will be figuring out the number by manipulating the game's output and searching the correct number (blind SQL). You should be able to do this in less than 10 queries.

For challenge 17 is an extra credit problem should you so choose. Don't do a simple brute force search.

TL;DR - 18-19 URLs. 
	- One each for challenges 1-14 (each producing the flag user's name and password every time)
	- One that shows the version number of the database (you can use any vulnerable page for this)
	- One that "wins" the guessing game (challenge 15) every time, without knowing the number (2 points)
	- One that displays the number you had to guess for the guessing game v1 (3 points)
	- Several that can be used to find the number for the guessing game v2 (challenge 16) (6 points)
	- Optionally several that can be used to find the answer to the guessing game v3 (challenge 17) (5 extra credit points)

This part must be submitted in the form of a .txt file.

## Part 2 - The Report (9 points)
- Description (3 point)
	- A description of what SQL Injection is and why it's bad
- Test steps (4 points)
	- 1 set of test steps that include how you found the vuln and how it works.
	- This must be for the highest challenge you solve. If you solve up through 10, then this would be for the 10th challenge.
	- These should be detailed enough that someone in the class who didn't solve the challenges could walk through the steps, be able to reproduce the vulnerabilities, know how they worked, and why they happened.
	- No screenshots are necessary.
- Mitigations (2 points)
	- Give mitigation recommendations for 2 languages/frameworks
		- ASP.NET
		- Ruby on Rails
	- This should include a few sentences about how to properly mitigate SQLi and a code example for each framework/language
	- Include a link or two to further reading/reference for the "developer"

This must be submitted in the form of a .txt file!

## Due Date
17:30 Tuesday May 8th 2018

## Notes & Hints
Please include links to any pages, guides, tutorials, people, or anything you used to help you figure out these challenges. Please do not cheat or trade answers! If you gently/fairly help one another out make sure to credit the people that helped you in your report. Give credit where credit is due.

No automated tools!