import { Row } from 'react-bootstrap';

const Message = ({
    message,
    sender,
    sentiment,
    
    }) => {
        console.log(sentiment)
        const getMessageColor = () => {
        switch (sentiment) {
            case "positive": return "green";
            case "neutral": return "blue"
            case "negative": return "red"
         }
        }
    return(
        <Row>
            <p style={{backgroundColor: getMessageColor(), color: "white"}}><b>{sender}</b> - {message}</p>
        </Row> 
    
    )
    
}
export default Message