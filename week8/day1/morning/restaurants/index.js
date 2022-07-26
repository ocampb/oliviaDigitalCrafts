const express = require("express");
const { Restaurants } = require("../models");
const router = express.Router();

router.post("/create_restaurant", async (req, res) => {
  const { name, address, reviewScore } = req.body;
  try {
    const newRestaurantName = {
      name: name,
      address: address,
      reviewScore: reviewScore,
    };
    const createRestaurant = await Restaurants.create(newRestaurantName);
    res.send(createRestaurant);
  } catch (error) {
    console.error(error);
    res.send(error);
  }
});

router.get("/by_id/:id", async (req, res) => {
  const { id } = req.params;
  const restaurantsToGet = await Restaurants.findAll({
    where: {
      id,
    },
  });

  res.send(restaurantsToGet);
});

router.get("/", async (req, res) => {
  const { address, name } = req.query;
  const restaurantsToGet = await Restaurants.findAll({
    where: {
      address,
      name,
    },
  });

  res.send(restaurantsToGet);
});

// update name by ID
// router.post("/update_name/", async (req, res) => {
//   const { id, name } = req.body;
//   const restaurantsToGet = await Restaurants.findOne({
//     where: {
//       id: id,
//     },
//   });
//   restaurantsToGet.update({
//     name: name,
//     updatedAt: new Date(),
//   });
//   res.send(restaurantsToGet);
// });

router.post("/update_restaurant", async (req, res) => {
  const { name } = req.body;
  try {
    const findUser = await Restaurants.findOne({
      where: {
        name: name,
      },
    });
    const updateRestaurant = Restaurants.name.update(req.body);
    res.send(updateRestaurant);
  } catch (error) {
    console.error(error);
    res.send(error);
  }
});

router.delete("/delete_restaurant_id/", async (req, res) => {
  const { id } = req.body;
  const restaurantsToGet = await Restaurants.findOne({
    where: {
      id: id,
    },
  });
  restaurantsToGet.destroy({
    id: id,
  });
  res.send(restaurantsToGet);
});

router.delete("/delete_restaurant_name/", async (req, res) => {
  const { name } = req.body;
  const restaurantsToGet = await Restaurants.findOne({
    where: {
      name: name,
    },
  });
  restaurantsToGet.destroy({
    name: name,
  });
  res.send(restaurantsToGet);
});

module.exports = router;
