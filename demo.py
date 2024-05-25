from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data with 20 detailed Indian recipes
recipes = {
    "butter chicken": {
        "ingredients": [
            "500g chicken breast",
            "100g butter",
            "1 cup tomato puree",
            "1 cup cream",
            "2 onions",
            "3 cloves garlic",
            "1 inch ginger",
            "1 tbsp garam masala",
            "1 tbsp chili powder",
            "Salt to taste"
        ],
        "steps": [
            "Marinate chicken with salt and chili powder for 1 hour.",
            "In a pan, melt butter and sauté onions, garlic, and ginger until golden.",
            "Add tomato puree and cook until oil separates.",
            "Add marinated chicken and cook until done.",
            "Stir in cream and garam masala, simmer for 10 minutes.",
            "Serve hot with naan or rice."
        ]
    },
    "palak paneer": {
        "ingredients": [
            "200g paneer",
            "250g spinach",
            "2 onions",
            "2 tomatoes",
            "3 cloves garlic",
            "1 inch ginger",
            "2 green chilies",
            "1 tsp cumin seeds",
            "1 tsp turmeric powder",
            "Salt to taste",
            "2 tbsp cream"
        ],
        "steps": [
            "Blanch spinach in boiling water for 2 minutes, then blend to a puree.",
            "In a pan, heat oil and sauté cumin seeds, onions, garlic, ginger, and green chilies.",
            "Add tomatoes and cook until soft.",
            "Add turmeric and salt, then stir in spinach puree.",
            "Add paneer cubes and cook for 5-7 minutes.",
            "Finish with cream and serve with roti or rice."
        ]
    },
    "biryani": {
        "ingredients": [
            "500g basmati rice",
            "1kg chicken",
            "2 onions",
            "2 tomatoes",
            "4 cloves garlic",
            "1 inch ginger",
            "2 green chilies",
            "1 cup yogurt",
            "1 tsp turmeric powder",
            "2 tbsp biryani masala",
            "Salt to taste",
            "Fresh coriander and mint leaves",
            "Saffron strands",
            "Fried onions",
            "Ghee"
        ],
        "steps": [
            "Marinate chicken with yogurt, turmeric, and biryani masala for 1 hour.",
            "Cook basmati rice until 70% done, then drain.",
            "In a large pot, layer marinated chicken, rice, saffron, fried onions, and herbs.",
            "Seal the pot with dough and cook on low heat for 45 minutes.",
            "Serve hot with raita."
        ]
    },
    "masala dosa": {
        "ingredients": [
            "2 cups rice",
            "1 cup urad dal",
            "1/2 tsp fenugreek seeds",
            "Salt to taste",
            "4 potatoes",
            "2 onions",
            "1 tsp mustard seeds",
            "1 tsp turmeric powder",
            "Curry leaves",
            "3 green chilies",
            "Oil"
        ],
        "steps": [
            "Soak rice, urad dal, and fenugreek seeds overnight, then grind to a smooth batter and ferment for 8 hours.",
            "Boil potatoes and mash them.",
            "In a pan, heat oil and temper mustard seeds, curry leaves, and green chilies.",
            "Add onions and sauté until golden, then add turmeric and mashed potatoes. Mix well.",
            "Spread dosa batter on a hot griddle, cook until crispy, then add potato filling and fold.",
            "Serve with coconut chutney and sambar."
        ]
    },
    "chole bhature": {
        "ingredients": [
            "2 cups chickpeas",
            "2 onions",
            "2 tomatoes",
            "3 cloves garlic",
            "1 inch ginger",
            "2 green chilies",
            "1 tsp cumin seeds",
            "1 tbsp chole masala",
            "Salt to taste",
            "2 cups flour",
            "1/2 cup yogurt",
            "Oil for frying"
        ],
        "steps": [
            "Soak chickpeas overnight and pressure cook until soft.",
            "In a pan, heat oil and sauté cumin seeds, onions, garlic, ginger, and green chilies.",
            "Add tomatoes and cook until soft.",
            "Add cooked chickpeas, chole masala, and salt, then simmer for 20 minutes.",
            "For bhature, mix flour, yogurt, and water to make a dough. Rest for 2 hours.",
            "Roll into discs and deep fry until golden.",
            "Serve hot with chole."
        ]
    },
    "paneer butter masala": {
        "ingredients": [
            "200g paneer",
            "100g butter",
            "1 cup tomato puree",
            "1 cup cream",
            "2 onions",
            "3 cloves garlic",
            "1 inch ginger",
            "1 tbsp garam masala",
            "1 tbsp chili powder",
            "Salt to taste"
        ],
        "steps": [
            "In a pan, melt butter and sauté onions, garlic, and ginger until golden.",
            "Add tomato puree and cook until oil separates.",
            "Add paneer cubes, garam masala, and chili powder, cook for 5-7 minutes.",
            "Stir in cream and simmer for 10 minutes.",
            "Serve hot with naan or rice."
        ]
    },
    "dal makhani": {
        "ingredients": [
            "1 cup whole black lentils",
            "1/4 cup kidney beans",
            "2 onions",
            "2 tomatoes",
            "3 cloves garlic",
            "1 inch ginger",
            "2 green chilies",
            "1 tsp cumin seeds",
            "1 tbsp garam masala",
            "1 cup cream",
            "Salt to taste",
            "Butter"
        ],
        "steps": [
            "Soak lentils and kidney beans overnight, then pressure cook until soft.",
            "In a pan, heat butter and sauté cumin seeds, onions, garlic, ginger, and green chilies.",
            "Add tomatoes and cook until soft.",
            "Add cooked lentils and beans, garam masala, and salt. Simmer for 30 minutes.",
            "Stir in cream and simmer for another 10 minutes.",
            "Serve hot with naan or rice."
        ]
    },
    "samosa": {
        "ingredients": [
            "2 cups flour",
            "4 potatoes",
            "1 cup peas",
            "2 onions",
            "3 cloves garlic",
            "1 inch ginger",
            "2 green chilies",
            "1 tsp cumin seeds",
            "1 tsp garam masala",
            "1 tsp turmeric powder",
            "Salt to taste",
            "Oil for frying"
        ],
        "steps": [
            "For the dough, mix flour, salt, and water to make a stiff dough. Rest for 30 minutes.",
            "Boil potatoes and mash them.",
            "In a pan, heat oil and sauté cumin seeds, onions, garlic, ginger, and green chilies.",
            "Add peas, mashed potatoes, garam masala, turmeric, and salt. Mix well.",
            "Roll the dough into circles, fill with potato mixture, and fold into triangles.",
            "Deep fry until golden brown.",
            "Serve with chutney."
        ]
    },
    "rogan josh": {
        "ingredients": [
            "500g lamb",
            "2 onions",
            "2 tomatoes",
            "3 cloves garlic",
            "1 inch ginger",
            "2 green chilies",
            "1 cup yogurt",
            "1 tsp cumin seeds",
            "1 tbsp garam masala",
            "1 tsp turmeric powder",
            "Salt to taste",
            "Fresh coriander",
            "Oil"
        ],
        "steps": [
            "Marinate lamb with yogurt, garam masala, and turmeric for 1 hour.",
            "In a pan, heat oil and sauté cumin seeds, onions, garlic, ginger, and green chilies.",
            "Add tomatoes and cook until soft.",
            "Add marinated lamb and cook until tender.",
            "Garnish with fresh coriander.",
            "Serve hot with rice or naan."
        ]
    },
    "kheer": {
        "ingredients": [
            "1/2 cup rice",
            "1 litre milk",
            "1 cup sugar",
            "1/4 tsp cardamom powder",
            "2 tbsp chopped nuts",
            "1 tbsp raisins",
            "Saffron strands"
        ],
        "steps": [
            "Wash and soak rice for 30 minutes.",
            "In a heavy-bottomed pan, boil milk.",
            "Add soaked rice and cook on low heat until rice is soft and milk thickens.",
            "Add sugar, cardamom powder, nuts, raisins, and saffron.",
            "Cook for another 10 minutes.",
            "Serve chilled or warm."
        ]
    },
    "tandoori chicken": {
        "ingredients": [
            "4 chicken legs",
            "1 cup yogurt",
            "2 tbsp lemon juice",
            "1 tbsp ginger-garlic paste",
            "1 tbsp tandoori masala",
            "1 tsp chili powder",
            "Salt to taste",
            "Oil"
        ],
        "steps": [
            "Make slits on the chicken legs.",
            "Marinate with yogurt, lemon juice, ginger-garlic paste, tandoori masala, chili powder, and salt for at least 4 hours.",
            "Preheat oven to 200°C.",
            "Place chicken on a baking tray and drizzle with oil.",
            "Bake for 25-30 minutes until cooked through and slightly charred.",
            "Serve with mint chutney and onion rings."
        ]
    },
    "mutter paneer": {
        "ingredients": [
            "200g paneer",
            "1 cup peas",
            "2 onions",
            "2 tomatoes",
            "3 cloves garlic",
            "1 inch ginger",
            "2 green chilies",
            "1 tsp cumin seeds",
            "1 tsp garam masala",
            "1 tsp turmeric powder",
            "Salt to taste",
            "Fresh coriander",
            "Oil"
        ],
        "steps": [
            "In a pan, heat oil and sauté cumin seeds, onions, garlic, ginger, and green chilies.",
            "Add tomatoes and cook until soft.",
            "Add peas, paneer cubes, garam masala, turmeric, and salt. Mix well and cook for 5-7 minutes.",
            "Garnish with fresh coriander.",
            "Serve hot with roti or rice."
        ]
    },
    "aloo gobi": {
        "ingredients": [
            "4 potatoes",
            "1 small cauliflower",
            "2 onions",
            "2 tomatoes",
            "3 cloves garlic",
            "1 inch ginger",
            "2 green chilies",
            "1 tsp cumin seeds",
            "1 tsp turmeric powder",
            "1 tsp garam masala",
            "Salt to taste",
            "Fresh coriander",
            "Oil"
        ],
        "steps": [
            "Cut potatoes and cauliflower into small florets.",
            "In a pan, heat oil and sauté cumin seeds, onions, garlic, ginger, and green chilies.",
            "Add tomatoes and cook until soft.",
            "Add potatoes, cauliflower, turmeric, garam masala, and salt. Mix well and cook until vegetables are tender.",
            "Garnish with fresh coriander.",
            "Serve hot with roti or rice."
        ]
    },
    "chicken tikka_masala": {
        "ingredients": [
            "500g chicken breast",
            "1 cup yogurt",
            "2 onions",
            "2 tomatoes",
            "3 cloves garlic",
            "1 inch ginger",
            "2 green chilies",
            "1 tsp cumin seeds",
            "1 tsp turmeric powder",
            "1 tbsp garam masala",
            "1 cup cream",
            "Salt to taste",
            "Fresh coriander",
            "Oil"
        ],
        "steps": [
            "Marinate chicken with yogurt, garam masala, and turmeric for 1 hour.",
            "In a pan, heat oil and sauté cumin seeds, onions, garlic, ginger, and green chilies.",
            "Add tomatoes and cook until soft.",
            "Add marinated chicken and cook until done.",
            "Stir in cream and simmer for 10 minutes.",
            "Garnish with fresh coriander.",
            "Serve hot with naan or rice."
        ]
    },
    "rajma": {
        "ingredients": [
            "1 cup kidney beans",
            "2 onions",
            "2 tomatoes",
            "3 cloves garlic",
            "1 inch ginger",
            "2 green chilies",
            "1 tsp cumin seeds",
            "1 tsp turmeric powder",
            "1 tbsp garam masala",
            "Salt to taste",
            "Fresh coriander",
            "Oil"
        ],
        "steps": [
            "Soak kidney beans overnight and pressure cook until soft.",
            "In a pan, heat oil and sauté cumin seeds, onions, garlic, ginger, and green chilies.",
            "Add tomatoes and cook until soft.",
            "Add cooked kidney beans, garam masala, turmeric, and salt. Mix well and simmer for 20 minutes.",
            "Garnish with fresh coriander.",
            "Serve hot with rice."
        ]
    },
    "pav bhaji": {
        "ingredients": [
            "4 potatoes",
            "1 cup peas",
            "2 onions",
            "2 tomatoes",
            "3 cloves garlic",
            "1 inch ginger",
            "2 green chilies",
            "1 tsp cumin seeds",
            "1 tsp turmeric powder",
            "1 tbsp pav bhaji masala",
            "Salt to taste",
            "Butter",
            "Bread rolls"
        ],
        "steps": [
            "Boil potatoes and peas, then mash them.",
            "In a pan, heat butter and sauté cumin seeds, onions, garlic, ginger, and green chilies.",
            "Add tomatoes and cook until soft.",
            "Add mashed potatoes, peas, pav bhaji masala, turmeric, and salt. Mix well and cook for 10 minutes.",
            "Serve hot with toasted bread rolls."
        ]
    },
    "poha": {
        "ingredients": [
            "2 cups flattened rice (poha)",
            "1 onion",
            "1 potato",
            "2 green chilies",
            "1 tsp mustard seeds",
            "1 tsp turmeric powder",
            "Salt to taste",
            "Fresh coriander",
            "Lemon juice",
            "Oil"
        ],
        "steps": [
            "Rinse poha in water and drain.",
            "In a pan, heat oil and temper mustard seeds, then sauté onions, green chilies, and potatoes until cooked.",
            "Add turmeric, salt, and poha. Mix well and cook for 2-3 minutes.",
            "Garnish with fresh coriander and lemon juice.",
            "Serve hot."
        ]
    },
    "bhindi masala": {
        "ingredients": [
            "500g okra (bhindi)",
            "2 onions",
            "2 tomatoes",
            "3 cloves garlic",
            "1 inch ginger",
            "2 green chilies",
            "1 tsp cumin seeds",
            "1 tsp turmeric powder",
            "1 tsp garam masala",
            "Salt to taste",
            "Fresh coriander",
            "Oil"
        ],
        "steps": [
            "Wash and chop okra into pieces.",
            "In a pan, heat oil and sauté cumin seeds, onions, garlic, ginger, and green chilies.",
            "Add tomatoes and cook until soft.",
            "Add okra, turmeric, garam masala, and salt. Mix well and cook until okra is tender.",
            "Garnish with fresh coriander.",
            "Serve hot with roti or rice."
        ]
    },
    "kadhi pakora": {
        "ingredients": [
            "1 cup gram flour (besan)",
            "2 cups yogurt",
            "1 onion",
            "1 tsp cumin seeds",
            "1 tsp mustard seeds",
            "1 tsp turmeric powder",
            "1 tsp garam masala",
            "Salt to taste",
            "Fresh coriander",
            "Oil"
        ],
        "steps": [
            "For pakoras, mix gram flour, chopped onions, salt, and water to make a batter. Deep fry spoonfuls until golden.",
            "For kadhi, mix yogurt, gram flour, turmeric, and salt. Add water to make a smooth mixture.",
            "In a pan, heat oil and temper cumin and mustard seeds, then add kadhi mixture and simmer for 20 minutes.",
            "Add fried pakoras and cook for another 10 minutes.",
            "Garnish with fresh coriander.",
            "Serve hot with rice."
        ]
    }
}

@app.route('/recipe', methods=['GET'])
def get_recipe():
    recipe_name = request.args.get('name')
    
    if not recipe_name:
        return jsonify({"error": "Please provide a recipe name."}), 400

    recipe = recipes.get(recipe_name)
    
    if not recipe:
        return jsonify({"error": "Recipe not found."}), 404

    return jsonify(recipe), 200

if __name__ == '__main__':
    app.run(debug=True)
