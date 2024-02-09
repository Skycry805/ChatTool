import { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Row, Col } from 'react-bootstrap';
import InputField from './InputField.jsx';
import SelectLanguage from './SelectLanguage.jsx';
import Message from './Message.jsx';
import { sendMessage } from './utils.js';
import { reciveMessage } from './utils.js';
import BotBob from './BotBob.jsx';


function App() {
  
  //safes the Username
  const [sender, setSender] = useState('');
  //Allows to set Username
  const [senderConfirmed, setSenderConfirmed] = useState(false);
  //safes the language
  const [language, setLanguage] = useState('en');
  //Allows User to change Language
  const [languageSelected, setLanguageSelected] = useState(false);
  //safes usermessage
  const [message, setMessage] = useState('');
  //safes recived Json 
  const [recivedMessages, setRecivedMessages] = useState([]);
  //start looking for new Messages
  const [newMessages, setNewMessages] = useState(false);
  //status of Bot Bob
  const [bob, setBob] = useState(false);

  //Wait for Name and Language to be set
  const handleSenderConfirmation = () => {
    if (sender.trim() !== '') {
      setSenderConfirmed(true);
    }
  };
  const handleLanguageSelect = (lang) => {
    setLanguage(lang);
  };
  const handleLanguageSelected = (lang) => {
    if (language.trim() !== '') {
    setLanguage(lang);
    setLanguageSelected(true);
    console.log(senderConfirmed)
    }
  }

  const handleBotBob = () => {
    setBob(true);
  }

//Sends message to server
  const handleSendMessage = async () => {
    console.log(`sender:`, sender, `Message:`, message, `Language:`, language, `Bob:`, bob);
    setMessage('');

    const preJsonMessage = {
      sender: sender,
      language: language,
      message: message,
      bob: bob
    };
    const jsonMessage = JSON.stringify(preJsonMessage)
    await sendMessage(jsonMessage);
    setNewMessages(true)
  };

  //Checking for new massages
  useEffect(() => {
    if (newMessages)
    {
      const lookForMessages = async () => {
        let response = await reciveMessage();
        if (response != 'latest')
        {
          response = transformJSON(response);
          for (const key in response) {
            if (response.hasOwnProperty(key)) {
          setRecivedMessages((prevMessages) => [...prevMessages, response[key]]);
          }
        }
        console.log("Recived Message: ", recivedMessages);
      };
    }
      const intervalId = setInterval(lookForMessages, 1000); 
      return () => clearInterval(intervalId);
    } 
    []});
//Transforms Json to 
  const transformJSON = (json) => {
    const transformedJSON = {};
    console.log("Transformed Message:", json)
    for (const key in json) {
      if (json.hasOwnProperty(key)) {
        const item = json[key];
        const transformedItem = {
          "message": item.message[language],
          "sender": item.sender,
          "sentiment": item.sentiment
        };
        transformedJSON[key] = transformedItem;
      }
    }
    console.log("transformed" ,transformedJSON)
    return transformedJSON;
  }

  return (
    <Container>
      <Row>
      <div id="window" style={{ marginTop: '20px', border: '1px solid black', padding: '300px' }}>         
          {recivedMessages.map((message, index) => {
            return <Message
            key={index}
            message={message.message}
            sender={message.sender}
            sentiment={message.sentiment}
             />
        })}
        </div>
      </Row>

        {!senderConfirmed || !languageSelected ? (
            <Row>
              <Col>
                <p id={'username'}>Ihr Name: {sender} </p>
                <p id={'standardLanguage'}>Aktuelle Sprache: {language} </p>
                <InputField
                  value={sender}
                  setValue={setSender}
                  placeholder={'Bitte geben Sie ihren Namen ein'}
                  handleButtonClick={handleSenderConfirmation}
                  buttonText={'Namen bestätigen'}
                />
                <SelectLanguage
                handleSelect={handleLanguageSelect}
                handleButtonClick={handleLanguageSelected}
                />
              </Col>
            </Row>

        ) : (
          <Row>
            <Col>
            <p id={'username'}>Ihr Name: {sender} </p>
                <p id={'selectedLanguage'}>Ihre ausgewählte Sprache: {language} </p>
                 <InputField
                    value={message}
                    setValue={setMessage}
                    placeholder={'Nachricht eingeben'}
                    handleButtonClick={handleSendMessage}
                    buttonText={'Nachricht senden'}
                  />
                  <BotBob
                  setBotBob = {handleBotBob}
                  />
               </Col>
            </Row>


      
      )}

    </Container>
  );
}
export default App;
