# @title Load the imports
import keras
import numpy as np
import pandas as pd
import plotly.express as px

# The following lines adjust the granularity of reporting.
pd.options.display.max_rows = 10
pd.options.display.float_format = "{:.1f}".format

# @title Load the dataset
rice_dataset_raw = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/Rice_Cammeo_Osmancik.csv")

print(rice_dataset_raw.head())

# @title Read and provide statistics on the dataset.
rice_dataset = rice_dataset_raw[[
    'Area',
    'Perimeter',
    'Major_Axis_Length',
    'Minor_Axis_Length',
    'Eccentricity',
    'Convex_Area',
    'Extent',
    'Class',
]]

print(rice_dataset.describe())

# @title Statistical analysis of the dataset

print(
    f'The shortest grain is {rice_dataset.Major_Axis_Length.min():.1f}px long,'
    f' while the longest is {rice_dataset.Major_Axis_Length.max():.1f}px.'
)
print(
    f'The smallest rice grain has an area of {rice_dataset.Area.min()}px, while'
    f' the largest has an area of {rice_dataset.Area.max()}px.'
)
print(
    'The largest rice grain, with a perimeter of'
    f' {rice_dataset.Perimeter.max():.1f}px, is'
    f' ~{(rice_dataset.Perimeter.max() - rice_dataset.Perimeter.mean())/rice_dataset.Perimeter.std():.1f} standard'
    f' deviations ({rice_dataset.Perimeter.std():.1f}) from the mean'
    f' ({rice_dataset.Perimeter.mean():.1f}px).'
)
print(
    f'This is calculated as: ({rice_dataset.Perimeter.max():.1f} -'
    f' {rice_dataset.Perimeter.mean():.1f})/{rice_dataset.Perimeter.std():.1f} ='
    f' {(rice_dataset.Perimeter.max() - rice_dataset.Perimeter.mean())/rice_dataset.Perimeter.std():.1f}'
)

# Create five 2D plots of the features against each other, color-coded by class.
for x_axis_data, y_axis_data in [
    ('Area', 'Eccentricity'),
    ('Convex_Area', 'Perimeter'),
    ('Major_Axis_Length', 'Minor_Axis_Length'),
    ('Perimeter', 'Extent'),
    ('Eccentricity', 'Major_Axis_Length'),
]:
  px.scatter(rice_dataset, x=x_axis_data, y=y_axis_data, color='Class').show()

#@title Plot three features in 3D by entering their names and running this cell
x_axis_data = 'Eccentricity'  # @param {type: "string"}
y_axis_data = 'Major_Axis_Length'  # @param {type: "string"}
z_axis_data = 'Area'  # @param {type: "string"}

px.scatter_3d(
    rice_dataset,
    x=x_axis_data,
    y=y_axis_data,
    z=z_axis_data,
    color='Class',
).show()

# Calculate the Z-scores of each numerical column in the raw data and write
# them into a new DataFrame named df_norm.
feature_mean = rice_dataset.mean(numeric_only=True)
print("Mean:", feature_mean)
feature_std = rice_dataset.std(numeric_only=True)
print("Standard Deviation:", feature_std)
numerical_features = rice_dataset.select_dtypes('number').columns
print("Numerical Features:", numerical_features)
normalized_dataset = (
    rice_dataset[numerical_features] - feature_mean
) / feature_std

# Copy the class to the new dataframe
normalized_dataset['Class'] = rice_dataset['Class']

# Examine some of the values of the normalized training set. Notice that most
# Z-scores fall between -2 and +2.
print("Normalized Dataset:\n")
print(normalized_dataset.head())

keras.utils.set_random_seed(42)

# Create a column setting the Cammeo label to '1' and the Osmancik label to '0'
# then show 10 randomly selected rows.
normalized_dataset['Class_Bool'] = (
    # Returns true if class is Cammeo, and false if class is Osmancik
    normalized_dataset['Class'] == 'Cammeo'
).astype(int)

print("Normalized Dataset Sample:\n")
print(normalized_dataset.sample(10))

# Create indices at the 80th and 90th percentiles
number_samples = len(normalized_dataset)
index_80th = round(number_samples * 0.8)
index_90th = index_80th + round(number_samples * 0.1)

# Randomize order and split into train, validation, and test with a .8, .1, .1 split
shuffled_dataset = normalized_dataset.sample(frac=1, random_state=100)
print("Shuffled Dataset Sample:\n")
print(shuffled_dataset.sample(10))
train_data = shuffled_dataset.iloc[0:index_80th]
validation_data = shuffled_dataset.iloc[index_80th:index_90th]
test_data = shuffled_dataset.iloc[index_90th:]

# Show the first five rows of the Test Data
print("Test Data Sample:\n")
print(test_data.head())

# Show the first five rows of the Train Data
print("Train Data Sample:\n")
print(train_data.head())

# Show the first five rows of the Validation Data
print("Validation Data Sample:\n")
print(validation_data.head())

label_columns = ['Class', 'Class_Bool']
#Showing the Train Features
train_features = train_data.drop(columns=label_columns)
print("Train Features Sample:\n")
print(train_features.head())
#Showing the Train Labels
train_labels = train_data['Class_Bool'].to_numpy()
print("Train Labels Sample:\n")
print(train_labels[:5])
#Showing the Validation Features
validation_features = validation_data.drop(columns=label_columns)
print("Validation Features Sample:\n")
print(validation_features.head())
#Showing the Validation Labels
validation_labels = validation_data['Class_Bool'].to_numpy()
print("Validation Labels Sample:\n")
print(validation_labels[:5])
#Showing the Test Features
test_features = test_data.drop(columns=label_columns)
print("Test Features Sample:\n")
print(test_features.head())
#Showing the Test Labels
test_labels = test_data['Class_Bool'].to_numpy()
print("Test Labels Sample:\n")
print(test_labels[:5])



