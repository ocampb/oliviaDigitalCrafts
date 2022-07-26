const express = require("express");
const { User } = require("../models");
const router = express.Router();
const bcrypt = require("bcrypt");

router.post("/create_user", async (req, res) => {
  const { username, password } = req.body;
  console.log(password);
  try {
    const salt = await bcrypt.genSalt(5);
    const hashedPassword = await bcrypt.hash(password, salt);
    console.log("salt", salt);
    console.log("hashedPassword", hashedPassword);
    const encryptedUser = {
      username: username,
      password: hashedPassword,
      createdAt: new Date(),
      updatedAt: new Date(),
    };
    const createUser = await User.create(encryptedUser);
    res.send(createUser);
  } catch (error) {
    console.error(error);
    res.send(error);
  }
});

router.get("/by_id/:id", async (req, res) => {
  const { id } = req.params;
  const usersToGet = await User.findAll({
    where: {
      id,
    },
  });

  res.send(usersToGet);
});

router.post("/login", async (req, res) => {
  const { username, password } = req.body;
  try {
    const findUser = await User.findOne({
      where: {
        username: username,
      },
    });
    console.log(findUser);
    res.send(findUser.datavalues);
  } catch (error) {
    res.send(error);
  }
});

module.exports = router;
