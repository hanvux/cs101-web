from flask import Flask, request, render_template
import markovify

app = Flask(__name__, template_folder='template',static_folder='static')  
@app.route('/', methods =["GET", "POST"])
def gfg():
     if request.method == "POST":
          with open("moby-dick.txt") as f:
               text = f.read()
          count = float(request.form.get("quantity"))
          text_model = markovify.Text(text)
          while 'resultbutton' in request.form:
               for i in range(3):
                    result=text_model.make_short_sentence(count)
               return result
     return render_template("templates.html")
if __name__=='__main__':
   app.run(debug=True)