import express from "express";
import cowsay from "cowsay";

const app = express();
const PORT = 3001;
app.use(express.json());
// routes
//by default the forward slash is the default in the internet address
//route will usually have its http method on it i.e. 'get'
//routes are just functions that are called when hit from front end
app.get("/", (req, res) => {
  res.send("javascript");
});

app.get("/benji", (req, res) => {
  res.send("lizard");
});

app.post("/beer", (req, res) => {
  res.send("beer12345");
  console.log(req.body);
});

app.post("/create_user", (req, res) => {
  res.send("");
});

app.listen(PORT, console.log(`Listening on port ${PORT}`));
