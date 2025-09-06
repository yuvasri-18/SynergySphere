from app import create_app
from pyngrok import ngrok

app = create_app()

# Start ngrok tunnel
public_url = ngrok.connect(5000)
print(" * ngrok URL:", public_url)

app.run(debug=True)
