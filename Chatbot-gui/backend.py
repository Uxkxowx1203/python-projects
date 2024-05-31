from openai import OpenAI
class ChatBot:
    #def __init__(self):
    
        
    def get_response(self,user_input):
        openai_api_key="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"
        self.client=OpenAI(openai_api_key)
        response = self.client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={ "type": "json_object" },
        messages=user_input
        )
        print(response.choices[0].message.content)
    
if __name__== "__main__":
    chatbot=ChatBot()
    response=chatbot.get_response("write a joke")
    print(response)
  

