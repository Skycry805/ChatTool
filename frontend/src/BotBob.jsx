import React, { useState } from 'react';

const BotBob = () => {
  const [buttonColor, setButtonColor] = useState('black');

  const handleButtonClick = () => {
    setButtonColor('green');
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