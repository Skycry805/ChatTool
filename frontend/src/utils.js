

//Checking Server for new Messages
export const reciveMessage = async () => {

  try {
    const response = await fetch('http://127.0.0.1:5000/update_message',{
      method: 'POST',
      headers: {
        'Content-Type': 'application/json' 
      },
    })
    .then((response) => response.json())
    .then(data => {
      console.log(data.message)
      return (data)
      
  })
  }      
      catch(error) {
        console.error('Error:', error);
        return('An error occurred.');
      };
  };





  //Sending Message to Server
  export const sendMessage = async (jsonMessage) => {
      // debug
    console.log(`Hier ist die Json`, jsonMessage);
  try {
    return await fetch('http://127.0.0.1:5000/send_message_to_server', {
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


