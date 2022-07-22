// default expess app is set to port 3000
const express = require("express");
const creds = require("./server/databaseConnection");
const app = express();
app.use(express.json());
const port = 3000;

app.get("/", (req, res) => {
  console.log(creds);
  creds.query("SELECT * FROM movies", (err, result) => {
    if (err) {
      console.log(err);
      res.status(500).send(err);
    } else {
      res.json(result.rows);
    }
    });
});

app.post("/create_anime", (req, res) => {
    console.log(req.body);
    creds.query(
      "INSERT INTO movies (movie_name, main_character, year_created) VALUES ($1, $2, $3)",
      [req.body.movie_name, req.body.main_character, req.body.year_created],
      (err, result) => {
        if (err) {
          console.log(err);
          res.status(500).send(err);
        } else {
          res.status(200).send(result);
        }
      }
    );
  });

  app.post("/update_anime", (req, res) => {
    creds.query(
      // -- UPDATE Cartoons SET year_created = '1990' WHERE id = 1;
      "UPDATE Movies SET movie_name = $1, main_character = $2 WHERE id = $3",
      [req.body.movie_name, req.body.main_character, req.body.id],
      (err, result) => {
        if (err) {
          res.status(500).send(err);
        } else {
          res.status(200).send(result);
        }
      }
    );
  });

  app.post("/delete_anime", (req, res) => {
    creds.query(
      // -- UPDATE Cartoons SET year_created = '1990' WHERE id = 1;
      "DELETE FROM Movies WHERE id = $1",
      [req.body.id],
      (err, result) => {
        if (err) {
          res.status(500).send(err);
        } else {
          res.status(200).send(result);
        }
      }
    );
  });

app.listen(port, () => console.log(`Example app listening on port ${port}!`));