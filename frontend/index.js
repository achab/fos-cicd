const express = require('express');
const fetch = require('node-fetch');
const app = express();
const PORT = 8090;

app.get('/', async (req, res) => {
  try {
    // Replace 'http://backend:5000/get_clubs' with your actual backend URL
    const response = await fetch('http://backend:5000/get_clubs');
    const clubs = await response.json(); // Assuming the backend returns JSON data

    // Start the HTML with a basic table structure
    let html = `<h1>Football Club Rankings</h1>`;
    html += `<table border="1"><tr><th>Rank</th><th>Club Name</th><th>Points</th></tr>`;

    // Loop through the clubs data and add rows to the table
    clubs.forEach((club, index) => {
      html += `<tr><td>${index + 1}</td><td>${club.club_name}</td><td>${club.points}</td></tr>`;
    });

    // Close the table tag
    html += `</table>`;

    // Send the generated HTML as the response
    res.send(html);
  } catch (error) {
    console.error('Error connecting to the backend service:', error);
    res.send('Error connecting to the backend service.');
  }
});

app.listen(PORT, () => {
  console.log(`Front-end service running on http://localhost:${PORT}`);
});
