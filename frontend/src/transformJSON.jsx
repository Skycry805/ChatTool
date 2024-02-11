
export const transformJSON = (json, language) => {
    const transformedJSON = {};
    console.log("Transformed Message:", json)
    for (const key in json) {
      if (json.hasOwnProperty(key)) {
        const item = json[key];
        const transformedItem = {
          "message": item.message[language],
          "sender": item.sender,
          "sentiment": item.sentiment
        };
        transformedJSON[key] = transformedItem;
      }
    }
    console.log("transformed" ,transformedJSON)
    return transformedJSON;
  };

  export default transformJSON;