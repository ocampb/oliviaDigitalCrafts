const Sequelize = require("sequelize");
const { User } = require("./models");

// .create()
// .findAll()
// .findByPk()
// .update()
// .destroy()

// User.create({
//   firstName: "Olivia",
//   lastName: "Marie",
//   email: "email@gmail.com",
// });

// User.create({
//   firstName: "Tyler",
//   lastName: "Smith",
//   email: "emai2l@gmail.com",
// });

(async () => {
  const data = await User.findAll();
  console.log(data);
})();
