// get pets

const express = require("express");
const { Pets } = require("../../../models");
const router = express.Router();

//create
router.post("/create_pets", async (req, res) => {
  res.send("create pets");
});

//read
router.get("/get_pets", async (req, res) => {
  const pets = await Pets.findAll({ raw: true });
  res.render("index.html", { locals: { pets: pets } });
});

// update
router.put("/update_pets", async (req, res) => {
  res.send("update pets");
});

// destroy
router.delete("/destroy_pets", async (req, res) => {
  res.send("destroy pets");
});

module.exports = router;
