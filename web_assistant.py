from flask import Flask, request
from gemini_client import GeminiClient

def main():
    app = Flask(__name__)
    client = GeminiClient()

    @app.route("/", methods=["GET"])
    def home():
        return """
        Talk to me:

        <form action="/prompt" method="post">
            <input type="text" name="text">
            <input type="submit" value="Submit">
        </form>
        """

    @app.route("/prompt", methods=["POST"])
    def prompt():
        user_input = request.form.get("text")

        if not user_input:
            return "No prompt provided. <br><a href='/'>Back</a>"

        response = client.generate_response(user_input)

        return f"""
        Prompt:
        {user_input}
        <br><br>
        Response:
        {response}
        
        <br><hr><br>
        
        Talk to me more:
        <form action="/prompt" method="post">
            <input type="text" name="text">
            <input type="submit" value="Submit">
        </form>
        <br>
        <a href="/">Back to Home</a>
        """

    app.run(debug=True)

if __name__ == "__main__":
    main()
