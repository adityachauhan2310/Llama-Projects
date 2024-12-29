from groq import Groq
import streamlit as st

# Initialize Groq client
client = Groq(api_key='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')  # Replace 'your_api_key' with your Groq API key

# Function to generate responses using Groq and LLaMA
def generate_response(prompt, model="llama-3.1-70b-versatile", temperature=1, max_tokens=1024):
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1,
            stream=False,
            stop=None,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# Recipe generation function
def generate_recipe(ingredients, dietary_restrictions, preferences):
    recipe_prompt = (
        f"Create a personalized recipe using the following ingredients: {ingredients}. "
        f"Take into account these dietary restrictions: {dietary_restrictions}. "
        f"Preferences include: {preferences}. Provide detailed steps and serving suggestions."
    )
    return generate_response(recipe_prompt)

# Explanation function
def explain_recipe(recipe_text):
    explanation_prompt = f"Explain the following recipe in detail, including nutritional benefits and cooking tips: {recipe_text}"
    return generate_response(explanation_prompt)

# Streamlit UI
st.title("Smart Recipe Generator and Meal Planner 🍳")
st.write("Generate personalized recipes and get detailed explanations for meal planning by **Aditya Chauhan**.")

# User Inputs
ingredients = st.text_area("Enter available ingredients (comma-separated):", "chicken, spinach, garlic")
dietary_restrictions = st.text_input("Enter dietary restrictions (e.g., vegetarian, gluten-free):", "low-carb")
preferences = st.text_input("Enter preferences (e.g., Italian, spicy):", "Italian")

# Generate Recipe Button
if st.button("Generate Recipe"):
    if ingredients.strip():
        with st.spinner("Generating your recipe..."):
            recipe = generate_recipe(ingredients, dietary_restrictions, preferences)
            st.subheader("Generated Recipe:")
            st.write(recipe)

            # Generate Explanation
            with st.spinner("Analyzing the recipe..."):
                explanation = explain_recipe(recipe)
                st.subheader("Recipe Explanation:")
                st.write(explanation)
    else:
        st.warning("Please enter ingredients to generate a recipe!")

# Footer
st.markdown("Powered by **Groq Cloud** and **LLaMA 3.1**. Enjoy your cooking!")

