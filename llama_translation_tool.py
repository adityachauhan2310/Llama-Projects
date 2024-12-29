from groq import Groq
import streamlit as st


client = Groq(api_key='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')  

#groq to code connection
def generate_response(prompt, model="llama-3.1-70b-versatile", temperature=1, max_tokens=1024):
    
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        stream=False,  
        stop=None,
    )
    # Collect the output text using dot notation
    return completion.choices[0].message.content  

#translation
def llama_translate_groq(input_text, target_language="Spanish"):
    
    translation_prompt = f"Translate the following English text to {target_language}: '{input_text}'"
    translated_text = generate_response(translation_prompt)
    return translated_text

#explanation
def explain_translation_groq(translated_text):
    
    explanation_prompt = f"Explain the meaning, grammar rules, and any idioms in the following text: '{translated_text}'"
    explanation = generate_response(explanation_prompt)
    return explanation

#UI
st.title("LLaMA 3.1 Language Translation and Learning Tool")
st.write("Translate text using LLaMA 3.1 and get contextual explanations for language learning by **Aditya Chauhan**")

input_text = st.text_area("Enter text to translate:", "")
target_language = st.selectbox("Select target language:", ["Spanish", "French", "German", "Hindi", "Italian", "Japanese"])

#Button 
if st.button("Translate with LLaMA 3.1"):
    if input_text.strip() != "":
        translated = llama_translate_groq(input_text, target_language)
        st.write(f"**> Translated Text to {target_language}:** {translated}")

        #explanation
        explanation = explain_translation_groq(translated)
        st.write(f"**> Contextual Explanation:** {explanation}")
    else:
        st.warning("Please enter text to translate!")

st.markdown

