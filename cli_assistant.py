from gemini_client import *

def main():
  client = GeminiClient()
  
  while True: 
    user_input = input("Talk to me!:")
    if user_input == "exit":
      print("Goodbye!")
      return
    
    response = client.generate_response(user_input)
    print("chatbot response: ", response)

if __name__ == "__main__":
  main()