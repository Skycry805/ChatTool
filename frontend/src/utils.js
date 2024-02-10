let messageID = 0;
let serverUrl = 'http://127.0.0.1:5000';

  //Sending Message to Server
export const sendMessage = async (jsonMessage) => {
  console.log("Message sent:", jsonMessage)
try {
  return await fetch(`${serverUrl}/send_message`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: (jsonMessage)
      ,
  })
    .then((response) => response.json())
    .then((data) => data.message)

  }
  catch(error) {
      console.error('Error:', error);
      return 'An error occurred.';
    };
}

//Checking Server for new Messages and get them from server
export const reciveMessage = async () => {
  let output = ''; 
  console.log("My messageID:", messageID);
  const result = await checkNewMessage(messageID)
  console.log("Server messageID:", messageID);
      if (result > messageID) {
        messageID++;
      try {
        const msg_id = messageID;
        const response = await fetch(`${serverUrl}/update_message/${msg_id}`,{
          method: 'POST',
          headers: {
            'Content-Type': 'application/json' 
          },
        })
        .then((response) => response.json())
        .then(data => {
          console.log(data)
          output = data;
      })
      messageID = result
      return (output);
      }      
          catch(error) {
            console.error('Error:', error);
            return('An error occurred.');
          };
    }
  else{
    const output = 'latest' ;
    return(output);
   }
  };

  //Check for new messageID
  const checkNewMessage = async () => {
    let output = '';
    try {
      const response = await fetch(`${serverUrl}/get_message_id`,{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json' 
        },
      })
      .then((response) => response.json())
      .then(data => {
        output = data.message_id;
        console.log('Output from Server:', data)
    })
    return (output);
    }      
        catch(error) {
          console.error('Error:', error);
          return('An error occurred.');
        };
  }
