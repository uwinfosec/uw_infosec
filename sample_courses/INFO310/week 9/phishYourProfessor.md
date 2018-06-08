# Phish Your Professor Homework

It's time to apply what you learned from the social engineering unit in a practical setting! The goal of this exercise is to craft a clever delivery of a weaponized payload or to demonstrate that a weaponized payload could have been used. For the delievry method, the easiest is email, but you're free to use any avenue of entry!

## Delivery Method

Your delivery method should be:

* Covert. You should be discreet in enticing the user to open the payload. You don't want the email to look shady. Ideally it would come from a source that looks like a trusted service to someone who isn't paying attention to details.
* Targeted. You should scour the internet for intelligence on your professor and use this information to establish credibility. Things like commonly used usernames, other email address, family members, personal addresses, and personal interests can all be used to establish credibility as a trusted source an entice the professor to click.
* Convincing. If you're emulating a Google Security alert, you should generate one for yourself and copy the styling of the email exactly. You don't want to send a payload in an email that looks like you copy and pasted out of a .txt file.
* Enticing. You want to appeal to one of the principles of social engineered discussed in the lecture. For example, if you're appealing to their sense of urgency, you might create a fake Google password reset email that requires action immediately.

## Payload

You have some options for your payload. Ultimately it's up to you to decide which payload sounds most interesting to research and attempt on your own. You can either create a fake login page that will log the user's username and password on the backend or you can go for local execution on the victim's computer.

The website route is pretty straightforward so I won't provide any guidance there, but if you want to create a payload to execute locally and automatically, one commonly used avenue by real-world attackers is through Microsoft Word/Powerpoint macroes. From these, you can launch other programs and execute code to carry out post-exploitation techniques.

Extra Credit Opportunity: Instead of creating a non-weaponized alert as the payload,read [this](https://www.blackhillsinfosec.com/click-to-enable-content/) guide on how these post-exploitation techniques can be done in practice. Other ideas can be found [here](https://github.com/yeyintminthuhtut/Awesome-Red-Teaming#-initial-access). 

### Using PowerPoint Macroes to Automatically Execute VBAScripts Locally

First things first, we need to open our powerpoint presentation and add the “DEVELOPER” Tab if it isn’t already there.

![](\phishPics\powerpointOptions.png)

In the developer tab click the “Visual Basic” button on the far left and that will open up a new window. Next, go to Insert>Module and here you can add in your macros. For this example we will open a message box.

Of course, if you're creating your own weaponized payload, you would have put your antivirus evading payload here instead.

Save the powerpoint as a .pptm file and close it for now. First, you will want to unzip the powerpoint file into its own directory. 

I reccomend using a UNIX terminal for this. If you're on Windows, install the Kali For Windows subsystem and execute the following commands:

```bash

mkdir zipped
cd zipped
unzip PowerPayload.pptm

```

Note: In order to get to the Windows part of your computer from the Kali For Windows terminal, you need to navigate to the root directory and then go into the `mnt` directory.

Then you will need to edit the _rels/.rels file to add this line right before the last Relationships tag:

```xml

<Relationship Type="http://schemas.microsoft.com/office/2006/relationships/ui/extensibility" Target="/customUI/customUI.xml" Id="Rd6e72c29d34a427e"/>

```

![](/phishPics/relsedit.png)

Be careful of copy pasting special characters. I reccomend opening this file in Visual Studio Code to make sure everything checks out in terms of syntax.

Next, you will need to create a new directory on the same level as the _rels directory. Name this one customUI

Create a file named customUI.xml in this new directory and add the following text:

```xml

<customUI xmlns="http://schemas.microsoft.com/office/2006/01/customui" onLoad="Run_On_Open" ></customUI>

```

Once again be careful of special character copy pasting.

Zip your files back up and open it to see if your payload fires! 

```bash

zip -r newRunOnOpen.pptm . -x “*.DS_Store”

```

Once you do this, you can edit the VBSrcript as needed to make the payload more complex.



Credit: [Black Hills InfoSec](!https://www.blackhillsinfosec.com/phishing-with-powerpoint/)