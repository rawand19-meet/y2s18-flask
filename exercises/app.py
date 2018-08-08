from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    movies = ["in time","the Immitation game"]
	
    return render_template(
    	"index.html",
    	movies = movies,
    	no_movies=False)


if __name__ == '__main__':
   app.run(debug = True)