from flask import *
from database import Pupper

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bork")
def create_pup():
    number_of_pups = Pupper.select().count()
    pup = Pupper(
        name=str(request.args.get("name", "doggo{}".format(number_of_pups))),
        bork=str(request.args.get("bork", "Hearty Woof")),
        tail_speed=str(request.args.get("tail_speed", "slow")),
    )
    pup.save()
    return "Pup created: {}".format(pup.name)