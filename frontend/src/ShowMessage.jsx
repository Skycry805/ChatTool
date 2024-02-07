import { useState } from 'react';


  const showMessage = (data) => {

    const message = data.message;
    const sender = data.sender;
    const sentiment = data.sentiment;

    //return <p><b>{message}</b><i>{sender}</i> - {sentiment}</p>
  }
  
  
  //Change color for sentiment
  const getMessageColor = (sentiment) => {
    switch (sentiment) {
        case "happy": return "green";
        case "neutral": return "blue"
        case "sad": return "red"
    }
}

export default showMessage;