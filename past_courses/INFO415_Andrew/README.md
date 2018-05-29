
```
    _____   ____________     __ __ _________
   /  _/ | / / ____/ __ \   / // /<  / ____/
   / //  |/ / /_  / / / /  / // /_/ /___ \  
 _/ // /|  / __/ / /_/ /  /__  __/ /___/ /  
/___/_/ |_/_/    \____/     /_/ /_/_____/  
    --- Web Application Security ---       

``` 

# Description
This course will cover the ins and outs of web application security from the perspectives of the developer, administrator, and attacker. We will cover attacks from the all too common Cross-Site Scripting (XSS) attack through Cross-Site Request Forgery (CSRF), SQL Injection (SQLi), all the way to more advanced topics.
 
The goals of this course centers around familiarizing students with how to recognize a possible vulnerability, write a proof-of-concept, and provide helpful remediation so that a developer can properly mitigate the issue. The emphasis will be on hands-on learning and the students will be expected to think creatively as they face common defenses and work with unfamiliar frameworks and languages.

# Grading
Grade breakdown:
- hw: 65%
- midterm: 15%
- final: 20%

# Late penalty: 
- 10% daily, incremented in 10% steps (24hrs from time due)
- stops at 50% deduction
- final turn in no later than 2 weeks from due date
- all assignments due by start of last day of class (May 31st - 5:30pm PST)

# Resources
- Suggested reading: Web Application Hacker's Handbook

# Correspondence:
- Please only use your UW email account
- Write: "INFO 415 - (your subject header here)" in the subject line

# Weekly Schedule

## Week 1 - Overview
- Tu - Introduction, overview, threat modeling
- La - Tools setup, traffic capture
- Th - Internet foundations
- HW - None
- Reading
	- For HW
		- https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
		- https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Evolution_of_HTTP
		- https://developer.mozilla.org/en-US/docs/Web/HTTP/Session
		- https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
		- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
		- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
		- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
	- For next week
		- https://excess-xss.com/
		- WAHH Chapter 12
		- WAHH Chapter 3

## Week 2 - XSS
- Tu - Client-server communications, browser basics, HTTP
- La - XSS introduction
- Th - XSS filter bypass techniques
- HW 
	- Browsing by hand
	- XSS challenges
- Reading
	- Manual HTTP
		- https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
		- https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Evolution_of_HTTP
		- https://developer.mozilla.org/en-US/docs/Web/HTTP/Session
		- https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
		- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
		- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
		- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
	- XSS
		- https://excess-xss.com/
		- WAHH Chapter 12
		- WAHH Chapter 3

## Week 3 - XSS
- Tu - Regular expressions (regex)
- La - Character encoding, unicode security, punycode domains
- Th - Advanced XSS payloads
- HW - Advanced XSS payloads
- Reading
	- WAHH Chapter 13 section on "Inducing User Action" (501-515)
	- http://www.troyhunt.com/2013/05/clickjack-attack-hidden-threat-right-in.html

## Week 4 - CSRF & Clickjacking
- Tu - CSRF introduction
- La - Tor
- Th - Janice guest lecture + Clickjacking
- HW - CSRF & Clickjacking challenges
- Reading
	- WAHH chapter 9

## Week 5 - SQLi
- Tu - SQLi introduction
- La - SQL and SQLi practice
- Th - Advanced SQLi techniques
- HW - SQLi challenges
- Reading
	- TBD

## Week 6 - SQLi
- Tu - Janice guest lecture + advanced SQLi
- La - SQLi to full control
- Th - Review for Midterm
- HW - Study for Midterm
- Reading
	- WAHH chapter 6
	- WAHH chapter 7

## Week 7 - Midterm & Crypto
- Tu - Midterm
- La - Lockpicking
- Th - Cryptography
- HW - None, enjoy the breather
- Reading
	- None

## Week 8 - Authentication & Pentest
- Tu - Authentication 2.0, OAuth 1.0, and business logic attacks
- La - Authentication 2.0, OAuth 1.0, and business logic attacks
- Th - HW review and web application practice pentest
- HW - Web application practice pentest
- Reading
	- None

## Week 9 - Blockchain
- Tu - Blockchain technologies
- La - Blockchain technologies
- Th - Cryptozombies + blockchain technologies
- HW - Ethereum contract exploitation
- Reading
	- TBD

## Week 10 - Review & Final
- Tu - Review HWs
- La - Review web app practice pentest HW
- Th - Final

## Final will be on the last day of class [2 hrs]