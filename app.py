from flask import Flask, render_template, request
from fatsecret import Fatsecret

app = Flask(__name__)


FATSECRET_KEY = "653860841f8c43469c1852dd637e626f"
FATSECRET_SECRET = "1300580db1184d99b12feb836da6526d"


fatsecret = Fatsecret(FATSECRET_KEY, FATSECRET_SECRET)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_food', methods=['POST'])
def search_food():
    query = request.form.get('query')
    if not query:
        return render_template('index.html', error="Por favor ingresa un alimento.")

    try:
        
        foods = fatsecret.foods_search(query, max_results=5)
        return render_template('results.html', foods=foods, query=query)
    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
