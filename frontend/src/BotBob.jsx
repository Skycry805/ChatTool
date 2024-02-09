import React, { useState } from 'react';

const BotBob = ({
 setBotBob,
        }) => {
  const [buttonColor, setButtonColor] = useState('black');

  const handleButtonClick = () => {
    setButtonColor('green');
    setBotBob(true);
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