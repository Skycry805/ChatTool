import { Form } from 'react-bootstrap';
import { useState } from 'react';

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
        <Form.Label>{label}</Form.Label>
        <Form.Control
          type='text'
          placeholder={placeholder}
          value={value}
          onChange={(e) => setValue(e.target.value)}
        />
      </Form.Group>
      <button onClick={handleButtonClick}>{buttonText}</button>
    </>
  );
};

export default InputField;