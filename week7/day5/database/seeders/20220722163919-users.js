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
    await queryInterface.bulkInsert(
      "Clients",
      [
        {
          name: "Olivia",
          email: "olivia@email.com",
          password: "12345",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          name: "Tyler",
          email: "tyler@email.com",
          password: "6789",
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
    await queryInterface.bulkDelete("Clients", null, {});
  },
};
