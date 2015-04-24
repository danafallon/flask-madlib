from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return render_template("index.html")

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    animal_dictionary = { "balloonicorn": "http://th03.deviantart.net/fs70/PRE/i/2012/186/3/4/balloonicorn_by_hokutto-d564r4n.png", 
                        "pegasus": "https://s-media-cache-ak0.pinimg.com/736x/a0/71/30/a07130ac0f2e7f4577f7caafce459228.jpg", 
                        "hippogriff": "http://i215.photobucket.com/albums/cc158/susansargies07/hippogriff.jpg", 
                        "kirby": "http://vignette4.wikia.nocookie.net/kirby/images/0/01/KDCol_Kirby_K64.png/revision/latest?cb=20120627075127&path-prefix=en"}

    animal_key = request.args.get("animal")
    animal_src = animal_dictionary[animal_key]

    return render_template("compliment.html", person=player, compliment=compliment, animal_src=animal_src)

@app.route('/game')
def show_game_form():
    response = request.args.get("gameplay")
    if response == "yes":
        return render_template("game.html")
    elif response == "no":
        return render_template("goodbye.html")

@app.route('/madlib', methods=['POST', 'GET'])
def show_madlib():
    if request.method == 'POST':
        person = request.form.get("person")
        color = request.form.get("color")
        noun = request.form.get("noun")
        adjective = request.form.get("adjective")
    elif request.method == 'GET':
        person = request.args.get("person")
        color = request.args.get("color")
        noun = request.args.get("noun")
        adjective = request.args.get("adjective")

    madlib_files = ["madlib.html", "madlib2.html"]
    madlib = choice(madlib_files)

    return render_template(madlib, person=person, color=color, noun=noun, adjective=adjective)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
