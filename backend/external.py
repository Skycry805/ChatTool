# External requests - v1.0 - Niclas Sieveneck

import requests
import json

import config as config

# Get string from json attribute
def json_select(json_element: json, path: list) -> str:
    for element in path:
        try:
            json_element = json_element[element]
        except Exception as e:
            print(e)
            return None
    return json_element

# send a request
def send_request(url: str, header: list, data=None, filter=None):
    
    # Build data
    if "Content-Type" in header or data == None:
        if header["Content-Type"].lower() == "application/json":
            data = json.loads(json.dumps(data, ensure_ascii=False))
            request_parameter = {'url': url, 
                                'headers': header, 
                                'json': data}
        else:
            # Only post data
            request_parameter = {'url': url, 
                                 'headers': header, 
                                 'data': data}
        print("Outgoing Data: ")
        print(data)
    else:
        # No Data to API
        request_parameter = {'url': url, 
                             'headers': header}

    try:
        response = requests.post(**request_parameter)
    except requests.exceptions.RequestException as e:
        print("Error: " + str(e))
        return None
    
    # check 200 and json
    if response.status_code == 200:  
        # Error handling for non-JSON ourput
        try:
            print("Json Output: ")
            print(response.json())
            # Get string from json attribute
            if filter:
                output = json_select(response.json(), filter)
                print("Filterd Output: ")
                print(output)
                return output
            return response.json()
        except:
            print("No JSON or Error.")
            return None
    else:
        print("Http-Code: " + str(response.status_code))
        #print(response.text)
        return None

# translate via deepL
def translate(source_lang: str, target_lang: str, text: str) -> str:
    # Save Api cost for debug, if source=target language
    if(source_lang == target_lang):
        print("Source and target language are the same.")
        return text
    
    # Build data
    dict_data = {"source_lang":source_lang, "target_lang":target_lang, "text": [text]}
    filter = ['translations', 0, 'text']
    # Build request
    return send_request(config.translate['url'], config.translate_header, dict_data, filter)

# LLM GPT
def llm(input: str, system_content=config.llm['system_content']) -> str:
    # build data
    dict_data = {"model": config.llm['model'], 
                 "messages": [ {"role": "system", 
                                "content": system_content}, 
                                {"role": "user", 
                                 "content": input}]}
    filter = ['choices', 
              0, 
              'message', 
              'content']
    # Build request
    return send_request(config.llm['url'], config.llm_header, dict_data, filter)

# Sentiment
def sentiment(input: str) -> str:
    data = {"text": input}
    filter = ['type']
    return send_request(config.sentiment['url'], config.sentiment_header, data, filter)
