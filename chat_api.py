from openai import OpenAI

# Initialize OpenAI API key
def load_phrases(filename):
    """
    Load phrases from a text file and return them as a list.
    """
    with open(filename, 'r') as file:
        phrases = file.readlines()
    return [phrase.strip() for phrase in phrases]

def get_chatgpt_response(user_input, phrases):
    """
    Function to get response from ChatGPT based on user input and user's typical phrases.
    """
    client = OpenAI(project="proj_CPgWyEXMnDp1pijXGnXEMiwV")
    prompt = "You are an AI that responds like the user. Here are some phrases the user typically uses:\n"
    for phrase in phrases:
        prompt += f"- {phrase}\n"
    prompt += f"\nThe conversation should continue in the user's style."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,
            n=1,
            temperature=0.9
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Load phrases once at the start
phrases = load_phrases('my_phrases.txt')
