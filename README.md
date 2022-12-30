# Googerteller in Python
This Python script uses scapy to sniff out packets your PC is sending to Google servers. It's a quick Python implementation of [Bert Hubert's Googerteller idea using his IP list](https://github.com/berthubert/googerteller).

Video of script in action here: https://infosec.exchange/@marcchehab/109602104515539858

It's using winsound, so if you're on Unix systems, replace with adequate non-blocking sound library.

# Dependencies
Uses scapy to sniff network traffic
```
pip install scapy
```

# Run
Just run the script
```
python pathtoscript/googerteller.py
```
and Ctrl+C to abort

# Known issues
Printout of detected IPs isn't triggered. Because scapy.all.sniff() is blocking I'll have to find a way around that. (scapy.all.AsyncSniffer(), on the other hand, lacks performance)
