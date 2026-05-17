import re
import random

class SupportBot:
    def __init__(self):
        # A dictionary of predefined responses based on regex patterns
        
        self.responses = {
            r'(hi|hello|hey)': [
                "Hello! How can I help you today?", 
                "Hi there! What can I assist you with?"
            ],
            r'(order|status|track)': [
                "You can track your order by logging into your account and visiting the 'Orders' section.", 
                "Please provide your order ID, and I can check the status for you."
            ],
            r'(return|refund|exchange)': [
                "Our return policy allows returns within 30 days of purchase. Would you like a link to our return form?"
            ],
            r'(shipping|delivery|arrive)': [
                "Standard shipping usually takes 3-5 business days. Expedited options are available at checkout."
            ],
            r'(human|agent|person|representative)': [
                "I am a virtual assistant, but I can connect you with a human agent if you prefer. Shall I transfer you?"
            ],
            r'(thank|thanks)': [
                "You're welcome! Let me know if there's anything else.",
                "Happy to help! Have a great day!"
            ],
            r'(bye|goodbye|quit|exit)': [
                "Thank you for chatting with us! Have a great day!", 
                "Goodbye! Feel free to reach out if you have more questions."
            ]
        }

        
        # Fallback responses if the bot doesn't understand the input
        self.default_responses = [
            "I'm not quite sure I understand. Could you rephrase that?",
            "I'm still learning! Can you provide more details?",
            "Please check our FAQ section, or type 'agent' to speak with a human."
        ]


    def get_response(self, user_input):
        user_input = user_input.lower()
        
        # Check the user input against our defined patterns
        for pattern, responses in self.responses.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
                
        # Return a default response if no patterns match
        return random.choice(self.default_responses)


    def chat(self):
        print("="*50)
        print("Welcome to Customer Support! (Type 'quit' or 'exit' to end)")
        print("="*50)
        print("Bot: Hi! I'm your virtual assistant. How can I help you today?")
        
        while True:
            user_input = input("You: ")
            
            # Check for exit condition immediately
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print(f"Bot: {random.choice(self.responses[r'(bye|goodbye|quit|exit)'])}")
                break
                
            # Get the appropriate response
            response = self.get_response(user_input)
            print(f"Bot: {response}")


if __name__ == "__main__":
    bot = SupportBot()
    bot.chat()
