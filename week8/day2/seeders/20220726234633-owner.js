"use strict";

module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.bulkInsert(
      "Owners",
      [
        {
          firstName: "Tyler",
          lastName: "Smith",
          email: "tylerisawesome@gmail.com",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          firstName: "Celena",
          lastName: "Sardothian",
          email: "winnieisawesome@gmail.com",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          firstName: "Olivia",
          lastName: "Marie",
          email: "olivia@gmail.com",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          firstName: "Mario",
          lastName: "Party",
          email: "marioisawesome@gmail.com",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          firstName: "Joe",
          lastName: "Frazier",
          email: "joeisawesome@gmail.com",
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
