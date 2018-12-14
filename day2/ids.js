const fs = require("fs");

var input;

fs.readFile(__dirname + "/input.txt", function(err, data) {
  if (err) {
    throw err;
  }
  input = data.toString().split(/\n/);
  console.log(input);
});

ids = input.map(a => {
  input.forEach(b => {
    if(a === b) {
      
    }
  });
})