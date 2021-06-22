from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/adoptionpage')
def adoption_page():
    cats = [
        {'id': 1, 'name': 'Nami', 'age': 3, 'breed':'Siamese'},
        {'id': 2, 'name': 'Baka', 'age': 2, 'breed': 'Domestic Short Hair'},
        {'id': 3, 'name': 'Kira', 'age': 1, 'breed':'Siamese'}
    ]
    return render_template('adoptionpage.html', cats=cats)




if __name__ == '__main__':
    app.run(debug=True)