* Telnet is an OLD protocol that acts in a similar way as SSH now days, but without encryption.
* One thing about this protocol is that when we input UserName & Password, each stroke in your keyboard is sent through the network in plain-text.
* IF my username is chang and Password is 1234, the Telnet protocol will send each character over network like this
c
h
a
n
g
\r
1
2
3
4

That means, if someone in your network is using Telnet protocol to log into something, you can sniff the credentials using Wireshark!!
I’ve prepared a Pcap file for everyone.
Inspect each Telnet Packet and find out what my Username & Password is!
I left a clue how to get to the next step!
