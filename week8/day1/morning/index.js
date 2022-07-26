const express = require("express");
const app = express();
const PORT = 3010;
const users = require("./user");
const restaurantRoutes = require("./restaurants");

app.use(express.json());

// request object:
/// {
//  "username": "oliviaisawesome"
//  "password": "password123
//  }

// req.body.password -> "password123"

// encryption takes time and is done async

// app.post("/create_user", async (req, res) => {
//   const { username, password } = req.body;
//   console.log(password);
//   try {
//     const salt = await bcrypt.genSalt(5);
//     const hashedPassword = await bcrypt.hash(password, salt);
//     console.log("salt", salt);
//     console.log("hashedPassword", hashedPassword);
//     const encryptedUser = {
//       username: username,
//       password: hashedPassword,
//       createdAt: new Date(),
//       updatedAt: new Date(),
//     };
//     const createUser = await User.create(encryptedUser);
//     res.send(createUser);
//   } catch (error) {
//     console.error(error);
//     res.send(error);
//   }
// });

// app.post("/login", async (req, res) => {
//   const { username, password } = req.body;
//   try {
//     const findUser = await User.findOne({
//       where: {
//         username: username,
//       },
//     });
//     console.log(findUser);
//     res.send(findUser.datavalues);
//   } catch (error) {
//     res.send(error);
//   }
// });

// app.post("/changepassword", async (req, res) => {
//   const { username, password } = req.body;
//   try {
//     const findUser = await User.findOne({
//       where: {
//         username: username,
//       },
//     });
//     console.log(findUser);
//     res.send(findUser.datavalues);
//   } catch (error) {
//     res.send(error);
//   }
// });

// app.post("/delete", async (req, res) => {
//   const { username, password } = req.body;
//   try {
//     const findUser = await User.findOne({
//       where: {
//         username: username,
//       },
//     const newPassword =
//     });
//     console.log();
//     res.send();
//   } catch (error) {
//     res.send(error);
//   }
// });

app.use("/users", users);
app.use("/restaurants", restaurantRoutes);

app.listen(PORT, console.log(`listening on port ${PORT}`));
