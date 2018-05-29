## XSS Homework Grading (30 points total)
Homework challenges can be found at: http://xss.websecurity.church/

### Part 1 - Vulnerabilities - 25.5 points
Each vulnerability will be worth 1.5 points. To earn 100% on this section you must complete all 17 challenges. 

Each vulnerability must call "alert(document.domain)" via a payload entered through the website in order to demonstrate script execution. It is preferable that the injected JavaScript execute automatically when the page loads, but that may not be possible in all cases. Please try to make it automatic where you can. **Each answer must be in the form of a URL (link) that you could send to a victim to click on if possible.** One challenge cannot be triggered via a link. In that case supply the steps so I can re-create the attack.

Note: 
- No importing external scripts or externally hosted files.
- Only 5 onmouseover style payloads are necessary, if you have more than 5 payloads that utilize onmouseover then there is room for improvement.
- If you have less than 5, let me know :)

### Part 2 - The Report - 4.5 points
- Description (.5 point)
	- 2 to 3 sentences describing the type of vulernability (in this case: Reflected Cross-Site Scripting [XSS]), what it is, and why it's bad.
- Test Steps (2 points)
	- 1 set of test steps for the highest challenges you solved. These must include how you found the vulnerability, and why it happened.
		- If you solved 1-7, 9, 10, and 11 then you would write test steps for 11 (the highest)
		- These should be detailed enough that someone in the class who didn't solve the challenges could walk through the steps, be able to reproduce the vulnerabilities, know how it worked, and why it happened.
		- If for instance you know that the filter strips script tags, but you can still get script execution through the onerror event handler of the img tag, then explain that in the test steps.
- Mitigations (2 points)
	- Give mitigation recommendations for the following language
		- Ruby on Rails
		- PHP
	- This should include a few sentences about how to properly mitigate XSS (such as escaping user input) and a code example (should only be a line of code or two)
	- Include a link for futher reading/reference for the "developer"

### Deliverables
The URLS for Part 1 and the report for Part 2 should be in one file in .txt format (no Word Docs, PDFs, RTFs, or anything other than a .txt)!

### Due Date
17:30 Thursday April 12th 2018

### Note
Please include links to any pages, guides, tutorials, people, or anything you used to help you figure out these challenges. Please do not cheat or trade answers! If you gently/fairly help one another out make sure to credit the people that helped you in your report. Give credit where credit is due.

No automated tools!
