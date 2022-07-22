"use strict";
const { Model } = require("sequelize");
module.exports = (sequelize, DataTypes) => {
  class Reviewer extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
      models.reviewers.hasMany(models.reviews, { foreignKey: "reviewerId" });
    }
  }
  Reviewer.init(
    {
      name: DataTypes.STRING,
      email: DataTypes.STRING,
      karma: {
        type: DataTypes.INTEGER,
        validate: { min: 1, max: 7 },
      },
    },
    {
      sequelize,
      modelName: "Reviewer",
    }
  );
  return Reviewer;
};
