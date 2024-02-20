#!/usr/bin/node

const fs = require('fs');

if (process.argv.len < 3)
{
	console.error('Usage: node read_file.js <file_path>');
	process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
	if (err) {
		console.error(err);
	} else {
		console.log(data);
	}
});
