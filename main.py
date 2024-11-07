


# 0. IMPORT KNJIŽNICE FLASK
from flask import Flask, render_template  #to je komanda za uvod flaska in da se naše dejanske html datoteke naloži

#flask deluje po principu objektno orientiranega programiranja

# 1. CREATE NEW FLASK object
app = Flask(__name__)  # ime tega modela je Flask, notri pa navedemo en paremeter

# Controler = HANDLER

# ROOT - to je izhodišče naše strani
@app.route("/")
def index():
    return render_template("index.html") # return nam gre v našo mapo spletnih strani html z imenom templates (deluje kot funkcija) in noter vpišemo, katero stran želimo odpreti


# ustvarimo templates - notri imamo pa vse HTML datoteke - hierarhija map je zelo pomembna

@app.route("/galerie")
def galerie():
    return render_template("galerie.html") # return nam gre v našo mapo spletnih strani html z imenom templates (deluje kot funkcija) in noter vpišemo, katero stran želimo odpreti


@app.route("/contact")
def contact():
    return render_template("contact.html") # return nam gre v našo mapo spletnih strani html z imenom templates (deluje kot funkcija) in noter vpišemo, katero stran želimo odpreti

if __name__=="__main__":
    app.run(use_reloader=True)  #s parametrom use_reloader=True se stran sproti posodablja
