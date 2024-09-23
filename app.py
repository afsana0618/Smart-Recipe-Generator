import requests
from flask import Flask, request, render_template

app = Flask(__name__)

# My Spoonacular API key
API_KEY = 'cc36549f888b4469a9437e7e069482b0'

# Fetch recipes based on ingredients
def get_recipes(ingredients):
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey={API_KEY}"
    response = requests.get(url)
    print(f"API Response Code: {response.status_code}")
    print(f"API Response Data: {response.json()}")
    return response.json()

@app.route('/')
def index():
    print("Index page accessed")
    return render_template('index.html')

@app.route('/recipes', methods=['POST'])
def recipes():
    ingredients = request.form['ingredients']  # Get ingredients from form
    print(f"Ingredients received: {ingredients}")
    recipes = get_recipes(ingredients)
    print(f"Recipes fetched: {recipes}")
    return render_template('recipes.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)

