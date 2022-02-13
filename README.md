# olx-crawler
A python program that crawls Olx.pl for ad data

### About
This project was built python and contains one python file 'scraping.py':
the program which handles all functionality

It uses libraries 'requests' for making http requests and 
'BeautifulSoup' for pulling out html data

### Project Set up and running
Pipenv is required to run this program
To run the project all you need to do is unpack the contents of the repository into a directory and run 'pipenv install'

to run the program, in the directory where the file 'scraping.py' is located run 'python scraping.py' or 'python3 scraping.py' 
depending on your environment setup.

'Starting scraping': this will be displayed in the terminal when the program is run
'Finished scraping': On succesful completion of the program
A data.json file will be generated with the results
