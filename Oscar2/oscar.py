from flask import Flask , render_template, request
from jokesapi import get_joke

app = Flask("Test")
def Oscar(oscar_year) : 
	oscar_movie='Unknow'

	if oscar_year == 2015:
		oscar_movie='Birdman'
	if oscar_year == 2016:
	 	oscar_movie='Spotlight'
	if oscar_year == 2017:
		oscar_movie='Moonlight'
	if oscar_year == 2018:
		oscar_movie='The Shape of  Water'
	if oscar_year == 2019:
		oscar_movie='Green Book'

	return oscar_movie


@app.route("/")
def default():
	data = get_joke()
	print (data)
	return render_template("index.html",  data=data)

@app.route("/movie", methods=["POST"])
def y():
	form_data = request.form 
	year = form_data["dob"]

	oscar_movie = Oscar(int(year))
	if oscar_movie == 'Birdman':
		return render_template("2015.html", movie=oscar_movie)
	elif oscar_movie == 'Spotlight':
		return render_template('2016.html', movie=oscar_movie)
	elif oscar_movie == 'Moonlight':
		return render_template('2017.html', movie=oscar_movie)
	elif oscar_movie == 'The Shape of  Water':
		return render_template('2018.html', movie=oscar_movie)
	elif oscar_movie == 'Green Book':
		return render_template('2019.html', movie=oscar_movie)
	else:
		return render_template('wrong.html', movie=oscar_movie)




if __name__ == "__main__":
	app.run()