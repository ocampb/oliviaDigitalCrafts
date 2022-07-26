const express = require("express");
const app = express();
const cors = require("cors");
const es6Renderer = require("express-es6-template-engine");
const pets = require("./routes/pets");
const PORT = 3008;

//middleware:
app.use(express.static("public"));
app.engine("html", es6Renderer);
app.set("views", "./public/views");
app.set("view engine", "html");
app.use(express.json());
app.use(cors());
app.use("/pets", pets);

app.listen(PORT, console.log(`listening on port ${PORT}`));
