
Purpose
This project analyzes the famous Fisher's Iris dataset to develop a classifier that can distinguish between three different species of the iris flower based on their physical measurements. The dataset includes measurements such as petal length, petal width, sepal length, and sepal width.

Class Design and Implementation
The project is structured as follows:
- DataLoader: A class designed to load and preprocess data from CSV files.
- DataAnalyzer: A class that encapsulates methods for statistical analysis.
- SpeciesComparator: A class used for comparing species based on statistical results.

Each class is designed to handle specific aspects of the data analysis process, ensuring that the code is modular, reusable, and easy to maintain.

Limitations
- The analysis assumes that the data distribution is normal, which may not hold for all attributes.
- The small sample size (50 samples per species) may not represent wider populations of each iris species.
