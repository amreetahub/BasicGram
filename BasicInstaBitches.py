
# coding: utf-8

# In[465]:


import urllib2
import bs4
import pandas
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/baesic/<A>')
def baesic(A):
    url ="https://www.instagram.com/" + A +"/"
    response = urllib2.urlopen(url)


    # In[468]:


    xml_text = response.read()
    soup = bs4.BeautifulSoup(xml_text)
    #print soup.prettify()[:200]
    #print "..."


    # In[469]:


    listm = soup.findAll(response,{'class':'_4rbun'})
    allCaps = []
    for elem in listm:
        allCaps.append(elem('img')[0]['alt'])
        #print elem('img')[0]['alt']



    # In[470]:


    words = []
    for line in allCaps:
        linesplit = (line.split(" "))
        for item in linesplit:
            words.append(item)

    #print words


    # In[471]:


    basicwords = ["@faizanv", "time", "FORbes", "JKB" ,"30"]
    basiccount = 0
    for word in words:
        for basicword in basicwords:
            if basicword.lower() == word.lower():
                basiccount = basiccount + 1
    if basiccount > 4:
        return "bae$icc"
    else:
        return "nah"
