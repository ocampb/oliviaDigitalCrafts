"use strict";

module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.bulkInsert(
      "Pets",
      [
        {
          name: "Tiny",
          species: "dog",
          age: 4,
          weight: "140",
          health: "good",
          unitOfWeight: "kilos",
          owner: "Chad",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          name: "Ginger",
          species: "cat",
          age: 4,
          weight: "140",
          health: "good",
          unitOfWeight: "kilos",
          owner: "Chad",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          name: "Nutmeg",
          species: "dog",
          age: 4,
          weight: "20",
          health: "good",
          unitOfWeight: "kilos",
          owner: "Chad",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          name: "Pancho",
          species: "dog",
          age: 4,
          weight: "10",
          health: "good",
          unitOfWeight: "kilos",
          owner: "Chad",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          name: "Cooper",
          species: "dog",
          age: 4,
          weight: "40",
          health: "good",
          unitOfWeight: "kilos",
          owner: "Chad",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
      ],
      {}
    );
  },

  async down(queryInterface, Sequelize) {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
  },
};
