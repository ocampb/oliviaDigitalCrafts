import express, { response } from "express";

const friends = ["Mary Ellen", "Tyler"];

const app = express();
const PORT = 3001;
app.use(express.json());

app.get(`/`, function (req, res) {
  res.send(friends);
});

app.post(`/`, function (req, res) {
  friends.push(req.body.name);
  res.send(friends);
});

app.get(`/uppercase`, function (req, res) {
  const friendsUppercase = [];

  for (let f of friends) {
    friendsUppercase.push(f.toUpperCase());
  }

  res.send(friendsUppercase);
});

app.listen(3001);
