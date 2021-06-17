from flask import Flask, request, render_template 
from fuzzywuzzy import fuzz, process

  
# Flask constructor
app = Flask(__name__)   
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       actor_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       actress_name = request.form.get("lname") 
       
       Token_Sort_Ratio = fuzz.token_set_ratio(actor_name,actress_name)
       print(Token_Sort_Ratio)

       
       return "Your score for " + actor_name + " and " + actress_name + " is " + str(Token_Sort_Ratio)

    return render_template("form.html")
  
if __name__=='__main__':
   app.run()