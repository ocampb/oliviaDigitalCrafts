"use strict";
const { Model } = require("sequelize");
module.exports = (sequelize, DataTypes) => {
  class Review extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
      //reviewer has many reviews
      // restaurant has many reviews
      // review has one reviewer
      models.reviews.belongsTo(models.reviewers, { foreignKey: "reviewerId" });
      models.reviews.belongsTo(models.restaurants, {
        foreignKey: "restaurant_id",
      });
    }
  }
  Review.init(
    {
      reviewerId: {
        type: DataTypes.INTEGER,
        references: {
          model: reviewer,
          key: "id",
        },
      },
      stars: {
        type: DataTypes.INTEGER,
        validate: { min: 1, max: 5 },
      },
      title: DataTypes.STRING,
      review: DataTypes.STRING,
      restaurantId: {
        type: DataTypes.INTEGER,
        references: {
          model: Bar,
          key: "id",
        },
      },
    },
    {
      sequelize,
      modelName: "Review",
    }
  );
  return Review;
};
