// get owners

const express = require("express");
const { Owners } = require("../../../models");
// const { Pets } = require("../../../models");
const router = express.Router();

//create
router.post("/create_owners", async (req, res) => {
  res.send("create owners");
});

//read
router.get("/get_owners", async (req, res) => {
  try {
    const owners = await Owners.findAll({ raw: true });
    res.render("index.html", { locals: { owners: owners } });
  } catch (error) {
    console.log(error);
  }
});

// update
router.put("/update_owners", async (req, res) => {
  res.send("update owners");
});

// destroy
router.delete("/destroy_owners", async (req, res) => {
  res.send("destroy owners");
});

module.exports = router;
