import React, { useState } from 'react';

const BotBob = ({
    handleClickedBotBob,
}) => {
  const [buttonColor, setButtonColor] = useState('black');
  const [bob, setBob] = useState(true);

  const handleButtonClick = () => {
    handleClickedBotBob();
    setBob(!bob);
    console.log('Wert: ' ,bob)
    if (bob == true)
    {
        setButtonColor('green');
    }
    else{
        setButtonColor('black');
    }

  };
  return (
    <button
      style={{ backgroundColor: buttonColor }}
      onClick={handleButtonClick}
    > Aktiviere Bot Bob
    </button>
  );
};

export default BotBob;