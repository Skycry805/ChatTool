import { useState } from 'react';

import 'bootstrap/dist/css/bootstrap.min.css';

import { Container, Row } from 'react-bootstrap';
import InputField from './InputField.jsx';
import SelectLanguage from './SelectLanguage.jsx';
import { sendMessage } from './utils.js';
import { reciveMessage } from './utils.js';
//import showMessage from './ShowMessage.jsx';


function App() {
  
  const [name, setName] = useState('');
  const [nameConfirmed, setNameConfirmed] = useState(false);
  const [language, setLanguage] = useState('de');
  const [languageSelected, setLanguageSelected] = useState(false);
  const [selectedLanguage, setSelectedLanguage] = useState('');
  const [message, setMessage] = useState('');




  //Removes Name 
  const handleNameConfirmation = () => {
    if (name.trim() !== '') {
      setNameConfirmed(true);
    }
  };

  //Remove Dropdown after selecting Language
  const handleLanguageSelected = () => {
    if (language.trim() !== '') {
    setLanguageSelected(true);
    }
  }
  const handleLanguageSelect = (lang) => {
    setLanguage(lang);
  };



  const handleSendMessage = async () => {
    console.log(`Name:`, name, `Message:`, message, `Language:`, language);
    setMessage('');

    const preJsonMessage = {
      name: name,
      language: language,
      message: message
    };
    const jsonMessage = JSON.stringify(preJsonMessage)
    await sendMessage(jsonMessage);
  };


  return (

    
    <Container>

      <Row>
      <div style={{ marginTop: '20px', border: '1px solid black', padding: '300px' }}>
      
        
      </div>
      </Row>
      <Row>
        {!nameConfirmed ? (
          <div>
            <p id={'username'}>Ihr Name: {name} </p>
            <InputField
              value={name}
              setValue={setName}
              placeholder={'Bitte geben Sie ihren Namen ein'}
              handleButtonClick={handleNameConfirmation}
              buttonText={'Namen bestätigen'}
            />
          </div>
        ) : (
          <div>
            <p id={'username'}>Ihr Name: {name} </p>
            <InputField
              value={message}
              setValue={setMessage}
              placeholder={'Nachricht eingeben'}
              handleButtonClick={handleSendMessage}
              buttonText={'Nachricht senden'}
            />
          </div>
        )}
          {!languageSelected ? (
          <div>
          <p id={'standardLanguage'}>Aktuelle Sprache: {language} </p>
          <SelectLanguage
          value={selectedLanguage}
          setValue={setSelectedLanguage}
          handleSelect={handleLanguageSelect}
          handleButtonClick={handleLanguageSelected}
            />
            
        </div>
        ) : (
        <p id={'selectedLanguage'}>Ihre ausgewählte Sprache: {language} </p>
        )}
        <button onClick={reciveMessage}>Nachricht empfangen</button>
        
      </Row>
    </Container>
  );
}
export default App;
