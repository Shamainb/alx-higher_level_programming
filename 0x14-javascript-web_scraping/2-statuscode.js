#!/usr/bin/node

// Make sure to install the 'request' module using npm install request
const request = require('request');

// Check if the URL is provided as an argument
if (process.argv.length < 3) {
  console.error('Please provide the URL as an argument');
  process.exit(1);
}

// Get the URL from command line arguments
const url = process.argv[2];

// Make the GET request
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  // Display the status code
  console.log(`code: ${response.statusCode}`);
});
