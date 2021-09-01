from flask import Flask,render_template
app=Flask(__name__)
@app.route("/anime")
def anime():
 return render_template("anime.html");
 if __name__=='main':
  app.run(debug=True)
