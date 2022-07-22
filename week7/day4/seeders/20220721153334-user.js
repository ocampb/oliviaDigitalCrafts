"use strict";

module.exports = {
  async up(queryInterface, Sequelize) {
    /**
     * Add seed commands here.
     *
     * Example:
     * await queryInterface.bulkInsert('People', [{
     *   name: 'John Doe',
     *   isBetaMember: false
     * }], {});
     */

    await queryInterface.bulkInsert("Users", [
      {
        firstName: "John",
        lastName: "Doe1",
        email: "joe@john.com",
        createdAt: new Date(),
        updatedAt: new Date(),
      },
      {
        firstName: "Olivia",
        lastName: "Doe2",
        email: "joe2@email.com",
        createdAt: new Date(),
        updatedAt: new Date(),
      },
      {
        firstName: "Tyler",
        lastName: "Doe3",
        email: "joe3@john.com",
        createdAt: new Date(),
        updatedAt: new Date(),
      },
    ]);
  },

  async down(queryInterface, Sequelize) {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
    await queryInterface.bulkDelete("Users", null, {});
  },
};
