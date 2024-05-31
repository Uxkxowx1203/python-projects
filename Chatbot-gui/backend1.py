import openai


class ChatBot:
  def __init__(self, model="gpt-3.5-turbo-0125"):
    openai.api_key = "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"
    self.model = model
  def get_response(self, user_input):

    messages = [
        { "role": "user", "content": user_input },
    ]

    response = openai.chat.completions.create(
        model=self.model,
        messages=messages,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()

if __name__== "__main__":
    chatbot=ChatBot()
    a="write a joke on future"
    response=chatbot.get_response(a)
    print(a)
    print(response)
  