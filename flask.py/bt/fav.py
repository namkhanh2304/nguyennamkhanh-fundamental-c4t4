from flask import Flask,render_template

app=Flask(__name__)

class Hobby:
    def __init__(self,h_name,h_infos):
        self.name=h_name
        self.infos=h_infos
hobby=Hobby("gaming",
    {
    "LOL": 
        {
            "info": "League of Legends is a multiplayer online battle arena video game developed and published by Riot Games.",
            "img":"https://yt3.ggpht.com/a-/ACSszfHrVg3LnUS0kehYSHasuGAlW_AZ6ZUR-69VFw=s900-mo-c-c0xffffffff-rj-k-no",
            "page": "https://play.na.leagueoflegends.com/en_US"
        },
    "PUBG":
        {
            "info":  "PlayerUnknown's Battlegrounds is an online multiplayer battle royale game developed and published by PUBG Corporation",
            "img": "https://cdn.gamerant.com/wp-content/uploads/playerunknowns-battlegrounds-golden-chests-logo.jpg.optimal.jpg",
            "page": "https://www.pubg.com/"
        },
    "Overwatch":
        {
            "info": "Overwatch is a team-based multiplayer first-person shooter video game developed and published by Blizzard Entertainment",
            "img": "https://d3hmvhl7ru3t12.cloudfront.net/img/logos/overwatch-share-3d5a268515283007bdf3452e877adac466d579f4b44abbd05aa0a98aba582eeaebc4541f1154e57ec5a43693345bebda953381a7b75b58adbd29d3f3eb439ad2.jpg",
            "page": "https://playoverwatch.com/en-us/"
        }
    })

@app.route("/favorite")
def index():
    return render_template("homeworktemplate.html",hobby=hobby)   

if __name__ == "__main__":
    app.run(debug=True)