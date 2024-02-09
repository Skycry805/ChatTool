import { Dropdown} from 'react-bootstrap';


const SelectLanguage = ({
    handleSelect,
    selectedValue,
    handleButtonClick
    

}) => {
    return (

        <Dropdown className={'mt-3'} onSelect={handleSelect}>
        <Dropdown.Toggle variant='success' id='dropdown-basic'>
            {selectedValue || 'Sprache auswählen'}
            </Dropdown.Toggle>
        <Dropdown.Menu>
        <p>
        <Dropdown.Item onClick={handleButtonClick} eventKey='en'>Englisch</Dropdown.Item>
        </p>
        <p>
        <Dropdown.Item onClick={handleButtonClick} eventKey='de'>Deutsch</Dropdown.Item>
        </p>
        <p>
        <Dropdown.Item onClick={handleButtonClick} eventKey='es'>Spanisch</Dropdown.Item>
        </p>
        </Dropdown.Menu>
    </Dropdown>
    );
};


export default SelectLanguage;


