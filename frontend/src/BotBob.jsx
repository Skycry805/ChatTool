import React, { useState } from 'react';

const BotBob = ({
    handleClickedBotBob,
}) => {
  const [buttonColor, setButtonColor] = useState('black');
  const [bob, setBob] = useState(true);
  const [status, setStatus] = useState('Aktiviere');

  const handleButtonClick = () => {
    handleClickedBotBob();
    setBob(!bob);
    if (bob == true)
    {
        setButtonColor('green');
        setStatus('Deaktiviere');
    }
    else{
        setButtonColor('black');
        setStatus('Aktiviere');
    }

  };
  return (
    <button
      style={{ backgroundColor: buttonColor }}
      onClick={handleButtonClick}
    > {status} Bot Bob
    </button>
  );
};

export default BotBob;