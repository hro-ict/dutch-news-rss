import feedparser
import re
from flask import Flask
from flask import render_template, request, redirect
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)





regex = re.compile(r'<[^>]+>')
#print(blog_feed["entries"])

def ad_news():
    ad= "https://www.ad.nl/binnenland/rss.xml"
    ad_feed= feedparser.parse(ad)
    rss_feeds= []
    for x in ad_feed["entries"]:
        link= x.link
        title= x.title
        summary= x.summary
        image= x["media_content"][0]["url"]
        time= time= x["published"].strip("+0100")
        current_icon= "/static/ad.png"
        rss_feeds.append({"title": title, "summary": summary,
        "link": link, "image": image, "time":time, "current_icon": current_icon
        })
    return rss_feeds

def volkskrant_news():
    volkskrant= "https://www.volkskrant.nl/voorpagina/rss.xml"
    ad_feed= feedparser.parse(volkskrant)
    rss_feeds= []
    for x in ad_feed["entries"]:
        link= x.link
        title= x.title
        summary= x.summary
        image= x["media_content"][0]["url"]
        time= time= ""
        current_icon="/static/volks_mobile.jpg"
        rss_feeds.append({"title": title, "summary": summary,
        "link": link, "image": image, "time": time, "current_icon": current_icon
        })
    return rss_feeds



# volkskrant= "https://www.volkskrant.nl/voorpagina/rss.xml"
# ad_feed= feedparser.parse(volkskrant)

# for x in ad_feed["entries"]:
#     for y in x.keys():
#         print(x[y])
#         print("*"*130)




# def parool_news():
#     parool= "https://www.parool.nl/nederland/rss.xml"
#     ad_feed= feedparser.parse(parool)
#     rss_feeds= []
#     for x in ad_feed["entries"]:
#         link= x.link
#         title= x.title
#         summary= x.summary
#         image= x["media_content"][0]["url"]
#         rss_feeds.append({"title": title, "summary": summary,
#         "link": link, "image": image
#         })
#     return rss_feeds

def enson_news():
    enson= "https://www.ensonhaber.com/rss/ensonhaber.xml"
    enson_feed = feedparser.parse(enson)
    feeds= []
    #for x in enson_feed["feed"]: 
    for x in enson_feed["entries"]:
        im= x["summary_detail"]["value"]
        index= im.index("src")
        new= im[index:-1]
        image= new.split("/></p>")[0][5:-2]
        if "jpg" in image:
            new_image= image.split("jpg")[0]
            image= "{}jpg".format(new_image)
        if "jpeg" in image:
            new_image= image.split("jpeg")[0]
            image= "{}jpeg".format(new_image)
        summary= x.summary.split("</a>")[-1]
        title= x.title
        link= x.link
        time= x["published"].strip("+0300")
        feeds.append({"title": title, "summary": summary,
        "link": link, "image": image, "time": time, "current_icon": current_icon
        })
    return feeds


# enson_news()

        
def parool_news():
    parool= "https://www.parool.nl/nederland/rss.xml"
    ad_feed= feedparser.parse(parool)
    rss_feeds= []
    for x in ad_feed["entries"]:
        link= x.link
        title= x.title
        summary= x.summary
        image= x["media_content"][0]["url"]
        time= time= x["published"].strip("+0100")
        current_icon= "/static/parool_mobile.PNG"
        rss_feeds.append({"title": title, "summary": summary,
        "link": link, "image": image, "time": time, "current_icon": current_icon
        })
    return rss_feeds

def trouw_news():
    trouw= "https://www.trouw.nl/voorpagina/rss.xml"
    ad_feed= feedparser.parse(trouw)
    rss_feeds= []
    for x in ad_feed["entries"]:
        link= x.link
        title= x.title
        summary= x.summary
        image= x["media_content"][0]["url"]
        time= time= x["published"].strip("+0100")
        current_icon= "/static/trouw.PNG"
        rss_feeds.append({"title": title, "summary": summary,
        "link": link, "image": image, "time": time, "current_icon": current_icon
        })
    return rss_feeds

# enson_news()

def metro_news():
    metro= "https://www.metronieuws.nl/in-het-nieuws/feed/"
    blog_feed = feedparser.parse(metro)
    counter= 0
    rss_feeds= []
    for x in blog_feed["entries"]:
        counter+=1
        # if counter==16: break
        summary= regex.sub('', x.summary).strip()
        link= x.link
        title= x.title
        im= x["summary_detail"]["value"]
        index= im.index("src")
        new= im[index:-1]
        image= new.split("/></p>")[0][5:-2]
        time= time= x["published"].strip("+0100")
        current_icon= "/static/metro_mobile.png"
    
        #image= "/static/noimage.jpg"
        # print("TITLE: ", title)
        
        # print("SUMMARY: ", summary)
        # print("LINK: ", link)
        # print("IMAGE: ", image)
        # print("*"*100)
        rss_feeds.append({"title": title, "summary": summary,
        "link": link, "image": image, "time":time, "current_icon": current_icon
        })
    return rss_feeds


def haberturk():
    link="https://www.haberturk.com/rss"
    feeds= feedparser.parse(link)
    rss_feeds= []
    for x in feeds["entries"]:
        # print(x["description"].split("</a>")[-1])
        # # print(x["image"])
        # #print(x.keys())
        image= x["links"][0]["href"]
        title= x["title"]
        summary= x["summary"].split("</a>")[-1]
        link= x["guid"]
        # print(image)
        # print(title)
        # print(summary)
        print(len(image))
        rss_feeds.append({"title": title, "summary": summary,
        "link": link, "image": image, "current_icon": current_icon
        })
    return rss_feeds





# metro= "https://www.metronieuws.nl/in-het-nieuws/feed/"
# blog_feed = feedparser.parse(metro)

# for x in blog_feed["entries"]:
#     im= x["summary_detail"]["value"]
#     # print(im)
#     # print("*"*100)
#     index= im.index("src")
#     new= im[index:-1]
#     image= new.split("/></p>")[0]
#     # index2= new.index("/></p>")
#     # #print(index2)
#     # # print(index)
#     # # print(index2)
#     # print(im[index:index2])
#     image= new.split("/></p>")[0]
  


    # print("*"*100)
    # print(im.index("src"), "--", im.index("jpg"))

def nu_news():
    nu_nl = "https://www.nu.nl/rss/Algemeen"
    blog_feed = feedparser.parse(nu_nl)
    counter= 0
    rss_feeds= []
    for x in blog_feed["entries"]:
        # counter+=1
        # if counter==6: break
        summary= regex.sub('', x.summary).strip()
        link= x.link
        title= x.title
        image= x["links"][1]["href"]
        time= time= x["published"].strip("+0100")
        current_icon= "/static/nu_mobile.png"
        # print("TITLE: ", title)
        
        # print("SUMMARY: ", summary)
        # print("LINK: ", link)
        # print("IMAGE: ", image)
        # print("*"*100)
        rss_feeds.append({"title": title, "summary": summary,
        "link": link, "image": image, "time":time, "current_icon": current_icon
        })
    return rss_feeds
        
# nu_nl = "https://www.nu.nl/rss/Algemeen"
# test= feedparser.parse(nu_nl)
# for x in test["entries"]:
    
def tweakers_news():
    #tweakers= "https://feeds.feedburner.com/tweakers"
    tweakers= "https://feeds.feedburner.com/tweakers/mixed"
    ad_feed= feedparser.parse(tweakers)
    rss_feeds= []
    for x in ad_feed["entries"]:
        #print(x.keys())
        title= x.title
        summary= x.summary
        link= x.link
        #time= time= x["published"].strip("GMT").strip("on,")
        ime= time= x["published"].strip("GMT").strip("ue,")
        current_icon= "/static/tweakers_mobile.png"

        # link= x.link
        # title= x.title
        # summary= x.summary
        # image= x["media_content"][0]["url"]
        # time= time= x["published"].strip("+0100")
        rss_feeds.append({"title": title, "summary": summary,
        "link": link, "time": time, "current_icon": current_icon
        })
    return rss_feeds

def nos_news():
    nos= "https://feeds.nos.nl/nosnieuwsalgemeen"
    nos_feed= feedparser.parse(nos)
    feeds= []
    for x in nos_feed["entries"]:
        title= x.title
        link= x.title
        time= x.published.strip("+0100")
        summary= regex.sub('', x.summary).strip()
        image= x.links[1]["href"]
        current_icon= "/static/nos_mobile.PNG"
        feeds.append({"title": title, "summary": summary,
        "link": link, "image":image, "time": time, "current_icon": current_icon
        })
    return feeds


def securitynl_news():
    security= "https://www.security.nl/rss/headlines.xml"
    security_feed= feedparser.parse(security)
    feeds= []
    for x in security_feed["entries"]:
        title= x.title
        link= x.link
        summary= x.summary
        time= x.published.strip("+0100")
        current_icon= "/static/securitynl_mobile.png"
        image= ""
        feeds.append({"title": title, "summary": summary,
        "link": link, "image":image, "time": time, "current_icon": current_icon
        })
    return feeds
        #print(x.media_thumbnail[0]["url"])









@app.route("/krant/<krant>")
def test(krant):
    if krant=="ad":
        return render_template("test2.html", data= ad_news(), title= "Algemene Dagblaad")
    if krant=="nu":
        return render_template("test2.html", data= nu_news(), title= "NU.nl")
    if krant=="volkskrant":
        return render_template("test2.html", data= volkskrant_news(), title= "Volkskrant")
    if krant=="trouw":
        return render_template("test2.html", data= trouw_news(), title= "Trouw")
    if krant=="parool":
        return render_template("test2.html", data= parool_news(), title= "Parool")
    if krant=="metro":
        return render_template("test2.html", data= metro_news(), title= "Metro")
    if krant=="haberturk":
        return render_template("test2.html", data= haberturk(), title= "Haberturk")
    if krant=="ensonhaber":
        return render_template("test2.html", data= enson_news(), title= "Enson Haber")
    if krant=="samanyolu":
        return render_template("test2.html", data= samanyolu_news(), title= "Samanyolu Haber")
    if krant=="tweakers":
        return render_template("test2.html", data= tweakers_news(), title= "Tweakers")
    if krant=="nos":
        return render_template("test2.html", data= nos_news(), title= "NOS")
    if krant=="security":
        return render_template("test2.html", data= securitynl_news(), title= "Security.NL")





@app.route("/")
def index():
    return render_template("test2.html")

@app.route("/test2")
def test2():
    return render_template("test2.html")

@app.route("/nu", methods=["GET", "POST"])
def nu():
    blog_feed = feedparser.parse(nu_nl)
    counter= 0
    rss_feeds= []
    for x in blog_feed["entries"]:
        counter+=1
        # if counter==6: break
        summary= regex.sub('', x.summary).strip()
        link= x.link
        title= x.title
        image= x["links"][1]["href"]
        # print("TITLE: ", title)
        
        # print("SUMMARY: ", summary)
        # print("LINK: ", link)
        # print("IMAGE: ", image)
        # print("*"*100)
        rss_feeds.append({"title": title, "summary": summary,
        "link": link, "image": image
        })
    return rss_feeds


@app.route("/ad", methods=["GET", "POST"])
def ad():
    return ad_news()

@app.route("/volkskrant", methods=["GET", "POST"])
def volkskrant():
    return volkskrant_news()

# @app.route("/parool", methods=["GET", "POST"])
# def parool():
#     return parool_news()

# @app.route("/enson", methods=["GET", "POST"])
# def enson():
#     return enson_news()

@app.route("/parool", methods=["GET", "POST"])
def parool():
    return parool_news()

@app.route("/trouw", methods=["GET", "POST"])
def trouw():
    return trouw_news()



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8555, debug=True)

    

# for x in blog_feed["entries"]:
#     print(x["links"][1]["href"])
# returns title of the blog site

# returns the link of the blog
# and number of entries(blogs) in the site.
# blog_feed.feed.link
# len(blog_feed.entries)

# # Details of individual blog can
# # be accessed by using attribute name
# print(blog_feed.entries[0].title)
# print(blog_feed.entries[0].link)
# print(blog_feed.entries[0].author)
# print(blog_feed.entries[0].published)

# # Getting lists of tags and authors.
# tags = [tag.term for tag in blog_feed.entries[0].tags]
# authors= [author.name for author in blog_feed.entries[0].authors]

