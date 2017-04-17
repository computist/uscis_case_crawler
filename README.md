# USCIS Case Crawler
A simple python tool to bash capture USCIS case result.  
The result will be printed to console.

### Install Dependency
```
sudo apt-get install nodejs-legacy
sudo apt install npm
sudo npm -g install phantomjs-prebuilt
sudo pip install -U selenium
```

### Usage
```
uscis.py -p <case prefix> -c <case number> -n <number of search> -u/-d (search up or down) -v (verbose: show case result details)
```
