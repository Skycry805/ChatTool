import { Form } from 'react-bootstrap';

const InputField = ({
  value,
  setValue,
  placeholder,
  handleButtonClick,
  buttonText,
}) => {

  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      handleButtonClick();
    }
  }
  return (
    <>
      <Form.Group className='mb-3' controlId='formBasicEmail'>
        <Form.Control
          type='text'
          placeholder={placeholder}
          value={value}
          onChange={(name) => setValue(name.target.value)}
          onKeyDown={handleKeyPress}
        />
      </Form.Group>
        <button onClick={handleButtonClick} >{buttonText}</button>
    </>
  );
};

export default InputField;