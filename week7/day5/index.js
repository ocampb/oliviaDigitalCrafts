const express = require("express");
const { rest } = require("lodash");
const { default: isEmail } = require("validator/lib/isEmail");
const { Clients, Longboard, Order } = require("./database/models");
const app = express();
const PORT = 3000;
app.listen(PORT, console.log(`listening on port ${PORT}`));

app.use(express.json());

app.post("/user", async (req, res) => {
  try {
    const user = await Clients.create({
      name: "Test Name",
      email: "testemail@email.com",
      password: "133558",
      createdAt: new Date(),
      updatedAt: new Date(),
    });
    res.status(200).send(user);
  } catch (error) {
    res.status(400).send(error);
  }
});
