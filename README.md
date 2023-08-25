# Web-scraping

##Setup to scrape using Scrapy

Install _requirements.txt_ in a virtual environment

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Get started with scrapy: https://docs.scrapy.org/en/latest/intro/tutorial.html

## Create a new project and a new spider

Scrapy has scaffolding that helps you get started with everything you need for a scraping project. Create a project and then a _spider_.

```
scrapy startproject bookclub
scrapy genspider sphagettibookclub sphagettibookclub.org
```
## Use the scrapy shell

To help you building the scraping, use the scrapy shell (an interactive scraping shell) to work with the HTML files. The scrapy CLI allows you to use absolute paths. Go to the root of this repo and run the following to open up the local HTML file:

```
scrapy shell  "https://www.spaghettibookclub.org"
```

Note that the quotes are required for the shell to work and escape the single quote within the HTML page. The shell uses a IPython as the shell (Jupyter-like output in the terminal) so be aware that when copying and pasting, you might need to reformat.

Confirm that the `response.url` points to the local path:

```

Note that the name of the project and the spider must be different. Otherwise the spider will not get created.

##Copying the webpage locally

```
wget -o sphagettibookclub.html https://www.spaghettibookclub.org/
```
COnfirm the html file is present in the folder

## Find query

Understand the html and find where the data is present and the tags associated. Use Scrapy shell to interact with scrapy.

We will extract the Books and authors and who reviewed the books.

```
response.xpath('//article').xpath('div/hgroup/h2/a').extract()[0]
```
<a href="review.php?review_id=12131">Judy Moody Declares Independence</a>'


```
response.xpath('//article').xpath('div/hgroup/h2/a/text()').extract()[0]
```
Judy Moody Declares Independence

## Script to notepad

Make required code changes to sphagettibookcub.py in the spider.



