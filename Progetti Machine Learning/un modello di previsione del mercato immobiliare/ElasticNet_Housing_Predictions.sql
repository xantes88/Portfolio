
CREATE TABLE ElasticNet_Housing_Predictions (
    area INT,
    bedrooms INT,
    bathrooms INT,
    stories INT,
    parking INT,
    Actual_Price FLOAT,
    Predicted_Price FLOAT
);

INSERT INTO ElasticNet_Housing_Predictions (area, bedrooms, bathrooms, stories, parking, Actual_Price, Predicted_Price) VALUES
(7420, 4, 2, 3, 2, 13300000, 12800000),
(8960, 4, 4, 4, 3, 12250000, 11900000),
(9960, 3, 2, 2, 2, 12250000, 12500000),
(7500, 4, 2, 2, 2, 12250000, 12000000),
(7420, 4, 2, 2, 2, 13300000, 13000000);