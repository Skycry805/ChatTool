import { Dropdown, Row} from 'react-bootstrap';

const SelectLanguage = ({
    handleSelect,
    selectedValue,
    handleButtonClick

}) => {
    return (
        <><Row style={{ marginBottom: '20px' }}>
                <Dropdown className={'mt-3'} onSelect={handleSelect}>
                <Dropdown.Toggle variant='success' id='dropdown-basic' style={{ padding: '0.6em 1.2em' }}>
                    {selectedValue || 'Sprache auswählen'}
                </Dropdown.Toggle>
                <Dropdown.Menu>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='ar'>Arabisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='bg'>Bulgarisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='zh'>Chinesich</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='da'>Dänisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='de'>Deutsch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='en'>Englisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='et'>Estnisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='fi'>Finnisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='fr'>Französisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='el'>Griechisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='id'>Indonesisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='it'>Italienisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='ja'>Japanisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='ko'>Koreanisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='lt'>Litauisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='nl'>Niederländisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='no'>Norwegisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='pl'>Polnisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='pt'>Portugiesisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='ro'>Rumänisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='ru'>Russisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='sv'>Schwedisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='sk'>Slowakisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='sl'>Slowenisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='es'>Spanisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='cs'>Tschechisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='tr'>Türkisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='uk'>Ukrainisch</Dropdown.Item></p>
                    <p><Dropdown.Item onClick={handleButtonClick} eventKey='hu'>Ungarisch</Dropdown.Item></p>                    
                </Dropdown.Menu>
            </Dropdown>
        </Row></>
    );
};


export default SelectLanguage;


