# create flask app
from flask import Flask , render_template
# Flask is a class

app = Flask(__name__)

class Movie :
    def __init__(self,t ,c,tu):
        self.title = t
        self.casts = c
        self.thumbnail_url = tu

m = Movie ("batman",
          " Christian Bale, Heath Ledger, Gary Oldman, Michael Caine, ...",
          "https://www.sideshowtoy.com/wp-content/uploads/2017/11/dc-comics-justice-league-batman-statue-prime1-studio-feature-903246-1.jpg"
          )

m2 = Movie ("ant man",
            "Paul Rudd. Scott Lang / Ant-Man. Michael Douglas. Dr. Hank Pym. Evangeline Lilly.",
            "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg"
            ) 

m3 = Movie ("the flash",
            "...",
            "https://vignette.wikia.nocookie.net/arrow/images/7/79/The_Flash_season_3_poster_-_Feel_The_Rush.png/revision/latest?cb=20161102204253"
            ) 

movie_list =[m, m2, m3]

@app.route("/casts")
def cast():
    return render_template ("cast.html", casts= ["cong ly","xuan bac", "tu long"])

@app.route("/")
def index():
    return render_template("index.html", name= "khanh", 
    image_url = "https://i.kym-cdn.com/photos/images/original/001/193/394/01c.jpg")

@app.route("/movie")
def movie():
    return render_template("movie.html", movies=movie_list)

@app.route("/about-me")
def about_me():
    return "I like dogs"

@app.route("/hello/<name>")
def hello(name):
    return "hello"+ name

# 2 run app
if __name__ == "__main__":
    app.run(debug=True)
