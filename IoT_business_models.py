'''
Created on Jan 14, 2024
@author: Néstor H. Bautista
A00394821@tec.mx
Tec de Monterrey
python script for business model analysis
'''

import matplotlib.pyplot as plt
from enum import Enum

# Enum representing service layers to categorize business models
class ServiceLayer(Enum):
    PLATFORM = 3
    MOBILE = 2
    HARDWARE = 1

# Class representing the business models
class BusinessModel:
    """
    Initializes a new instance of the BusinessModel class.

    :param title: str - The name of the business model.
    :param similarity: int - An integer score indicating the similarity of the business model with respect to the case analysis (0 = Not Similar, 100 = Very Similar).
    :param layer: ServiceLayer - The service layer category the business model falls into.
    :param degree: int - A degree of correlation of a business model with a service layer.
    """
    def __init__(self, title, similarity, layer, degree):
        self.title = title
        self.similarity = similarity
        self.layer = layer
        self.degree = degree

# List of business model instances
models = [
    BusinessModel(title="Platform Model", similarity=90, layer=ServiceLayer.HARDWARE, degree=100000),
    BusinessModel(title="Subscription Model", similarity=85, layer=ServiceLayer.MOBILE, degree=90000),
    BusinessModel(title="Outcome-Based \n Model", similarity=60, layer=ServiceLayer.HARDWARE, degree=50000),
    BusinessModel(title="Compliance \n Model", similarity=20, layer=ServiceLayer.PLATFORM, degree=5000),
    BusinessModel(title="Data-Driven Model", similarity=60, layer=ServiceLayer.PLATFORM, degree=100000),
]

plt.figure(figsize=(10, 8))

# Plot the representation of the business models
for model in models:
    plt.scatter(
        model.similarity,
        model.layer.value,
        s=model.degree,
        alpha=0.6
    )
    plt.annotate(
        model.title,
        (model.similarity, model.layer.value),
        fontsize=9,
        textcoords="offset points",
        xytext=(0,10),
        ha='center'
    )

# Adding gridlines
plt.grid(True, linestyle='--', alpha=0.5)

# Configuring the chart
layers = ["Web Platform", "Mobile", "Hardware"]
y_positions = [3, 2, 1]
plt.title('Similarity of IoT Business Models')
plt.xlabel('Business model similarity (0 = Not Similar, 100 = Very Similar)', fontsize=12)
plt.ylabel('Service Layer', fontsize=12)
plt.xlim(0, 100)
plt.ylim(0, 4)
plt.yticks(y_positions, layers)

# Show the plot
plt.show()
