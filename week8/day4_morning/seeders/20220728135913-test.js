"use strict";

module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.bulkInsert(
      "User",
      [
        {
          username: "Mario",
          password: "12345",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          username: "Luigi",
          password: "6789",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          username: "Princess",
          password: "368634",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          username: "Bowzer",
          password: "53995",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          username: "Character5",
          password: "673985",
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
