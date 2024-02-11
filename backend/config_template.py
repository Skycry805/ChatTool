# Config File

# Case Sensitve "Content-Type"

# Config for APIs
translate = {
             "url": "https://api-free.deepl.com/v2/translate",
             "auth_key": "INSERT_API_KEY_HERE"                   # Insert Key here
             }

llm = {
        "url": "https://api.openai.com/v1/chat/completions",
        "auth_key": "INSERT_API_KEY_HERE",                       # Insert Key here
        "model": "gpt-3.5-turbo-0125",
        "system_content": "Dein Name lautet 'BOB der Bot' und du bist ein freundlicher und hilfsbereiter Chatbot. Deine Aufgabe ist es die Eingaben der Nutzer zu lesen und die gestellten Fragen zu beantworten, in der Sprache, in der die Nachricht ankommt. Achte dabei aber immer eine freundliche Benutzeroberfläche zu bieten. Auf der die verschiedenen User miteinander interagieren können. Eingehende Nachrichten enthalen den Namen des Users vor dem ersten Doppelpunkt."
       }

sentiment = {
            "url": "https://twinword-sentiment-analysis.p.rapidapi.com/analyze/",
            "auth_key": "INSERT_API_KEY_HERE"                    # Insert Key here
}

# Header
translate_header = {
                "Authorization": f"DeepL-Auth-Key {translate['auth_key']}",
                "User-Agent": "VS-Chat/1.0.0",
                "Content-Type": "application/json"
                }

llm_header = {
                "Authorization": f"Bearer {llm['auth_key']}",
                "User-Agent": "VS-Chat/1.0.0",
                "Content-Type": "application/json"
                }

sentiment_header = {
    "X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com",
    "X-RapidAPI-Key": sentiment['auth_key'],
    "Content-Type": "application/x-www-form-urlencoded"
}