const express = require("express");
const app = express();
const cors = require("cors");
const es6Renderer = require("express-es6-template-engine");
const sequelize = require("../models");
// const pets = require("./routes/pets");
const owners = require("./routes/owners");
const PORT = 3008;

//middleware:
app.use(express.static("public"));
app.engine("html", es6Renderer);
app.set("views", "./public/views");
app.set("view engine", "html");
// converts the json body to a javascript object:
app.use(express.json());
app.use(cors());
// app.use("/pets", pets);
app.use("/owners", owners);

sequelize.sequelize
  .sync({ force: false })
  .then((result) => {
    app.listen(PORT, console.log(`listening on port ${PORT}`));
  })
  .catch((err) => {
    console.log(err);
  });
