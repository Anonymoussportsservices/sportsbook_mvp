import React, { useEffect } from 'react';

function App() {
  useEffect(() => {
    console.log("About to call API");
    fetch(process.env.REACT_APP_API_URL + "//api/users")
      .then(response => response.json())
      .then(data => {
        console.log(data);
      })
      .catch(error => {
        console.error('Fetch error:', error);
      });
  }, []);

  return (
    <div>
      <h1>Sportsbook MVP Frontend</h1>
      <p>Check your browser console for the API response.</p>
    </div>
  );
}

export default App;
