import openai

class chatbot:

    def __init__(self):
        pass
    
    def get_responce(self, user_input):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
        )
        return response.choices[0].text.strip()
