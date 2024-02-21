#!/usr/bin/node
const request = require('request');

// Check if the movie ID is provided as an argument
if (process.argv.length < 3) {
  console.error('Please provide the movie ID as an argument');
  process.exit(1);
}

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Construct the URL for the API endpoint
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make the GET request
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  // Parse the JSON response
  const data = JSON.parse(body);

  // Check if the movie data is retrieved successfully
  if (response.statusCode === 200) {
    // Print the title of the movie
    console.log(`Title: ${data.title}`);
  } else {
    console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
    process.exit(1);
  }
});
