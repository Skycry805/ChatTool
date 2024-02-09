import { Form } from 'react-bootstrap';

const InputField = ({
  value,
  setValue,
  label,
  placeholder,
  handleButtonClick,
  buttonText,
}) => {
  return (
    <>
      <Form.Group className='mb-3' controlId='formBasicEmail'>
        <Form.Control
          type='text'
          placeholder={placeholder}
          value={value}
          onChange={(name) => setValue(name.target.value)}
        />
      </Form.Group>
        <button onClick={handleButtonClick}>{buttonText}</button>
    </>
  );
};

export default InputField;