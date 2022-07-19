var http = require("http");
var fs = require("fs");

http.createServer(function (req, res) {
  fs.readFile("hello.txt", function (err, data) {
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.write(data);
    return res.end();
  });
});

const hostname = "127.0.0.1";
const port = 3000;

// const server = http.createServer((req, res) => {
//   res.statusCode = 200;
//   res.setHeader("Content-Type", "text/plain");
//   res.end("Hello World");
// });

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
