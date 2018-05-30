## XSS and SQLi Homework (36 points total)
XSS homework challenges can be found at: http://xss-challenges.r7.io/
SQLi homework challenges can be found at: http://sqli-challenges.r7.io/[your UW NetID]
- Example: My UW NetID is amckenna so I would go to: http://sqli-challenges.r7.io/amckenna/

Note: These challenges should be worked on individually. Do not share answers.

### Part 1 - XSS Vulnerabilities - 20 points
Each vulnerability will be worth 2 points. To earn 100% on this section you must complete the first 10 challenges (challenge 0-9). You're welcome to work on the later challenges, but they will not count towards your grade.

Each vulnerability must call "alert(0)" using a payload entered through the website in order to demonstrate script execution. It is preferable that the injected JavaScript execute automatically when the page loads, but that may not be possible in all cases. Please try to make it automatic where you can. Each answer must be in the form of a URL (link) that you could send to a victim to click on.

Note: 
- No importing external scripts or externally hosted files.
- Only 3 onmouseover style payloads are necessary, if you have more than 3 payloads that utilize onmouseover then there is room for improvement.
- If you have less than 3, let me know :)

### Part 2 - SQLi Vulnerabilities - 16 points
Notes: 
- You may have issues with this challenge if you are connecting from the UW network.
- No automated tools!

Each vulnerability is worth 2 points. To earn 100% on this section you must complete challenges 3-10. You're welcome to work on the later challenges, but they will not count towards your grade.

Each payload must result in the server displaying the flag user's username, email, and password. Other user's credentials can be dumpted too, but at least the flag user must be displayed and appear every time you run the payload. Try running the exploit 3-5 times to make sure the flag user apears every time. Each answer must be in the form of a URL (link) that you could send to a developer to prove you found a vulnerability.

### Due Date
5:30pm (17:30) Thursday February 16th 2017

### Note
Please include links to any pages, guides, tutorials, people, or anything you used to help you figure out these challenges. The submission document must be of type .txt