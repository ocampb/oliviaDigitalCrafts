import express from "express";
const app = express();
const PORT = 3003;

import es6Renderer from "express-es6-template-engine";
app.engine("html", es6Renderer);
app.set("views", "templates");
app.set("view engine", "html");
app.use(express.static("to_do_public"));

// routes:
app.get("/home", (req, res) => {
  //   res.send("Hello from Express!");
  const user = { name: "Olivia" };
  res.render("home", {
    locals: { user: user, teacher: "Joe", students: ["Amanda", "Carlos"] },
  });
});

app.get("/file", (req, res) => {
  //   res.send("Hello from Express!");
  res.render("file");
});

// app.post("/home", (req, res) => {
//   res.send("Hello from Express!");
// });

app.listen(PORT, console.log(`listening on port ${PORT}`));
