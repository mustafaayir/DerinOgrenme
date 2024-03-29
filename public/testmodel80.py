# -*- coding: utf-8 -*-
"""TestModel80.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qAHBMLVSZ0B-gTirWI17-Ftuan3la5ow
"""

from google.colab import drive
drive.mount('/content/drive')

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(32 * 56 * 56, 128)
        self.fc2 = nn.Linear(128, 2)

    def forward(self, x):
        x = nn.functional.relu(self.conv1(x))
        x = nn.functional.max_pool2d(x, 2, 2)
        x = nn.functional.relu(self.conv2(x))
        x = nn.functional.max_pool2d(x, 2, 2)
        x = x.view(-1, 32 * 56 * 56)
        x = nn.functional.relu(self.fc1(x))
        x = self.fc2(x)
        return x

def load_data():
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    data_transform = datasets.ImageFolder(root='/content/drive/MyDrive/Pneumonia/X-Ray', transform=transform)

    # Veri setini train, validation, test olarak bölecek şekilde ayarlayın
    train_size = int(0.8 * len(data_transform))  # %80 train
    test_size = len(data_transform) - train_size  # Geri kalan %20 test
    val_size = int(0.1 * train_size)  # %10 validation

    train_data, test_data = torch.utils.data.random_split(data_transform, [train_size, test_size])
    train_data, val_data = torch.utils.data.random_split(train_data, [train_size - val_size, val_size])

    train_loader = DataLoader(train_data, batch_size=32, shuffle=True)
    val_loader = DataLoader(val_data, batch_size=32)
    test_loader = DataLoader(test_data, batch_size=32)

    return train_loader, val_loader, test_loader

# CNN modelini eğitme ve değerlendirme fonksiyonu
def train_evaluate_cnn(model, train_loader, val_loader, test_loader, epochs=5):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(epochs):
        # Eğitim aşaması
        model.train()
        for inputs, labels in train_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

        # Doğrulama aşaması
        model.eval()
        total_val, correct_val = 0, 0
        for inputs, labels in val_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total_val += labels.size(0)
            correct_val += (predicted == labels).sum().item()

        val_accuracy = 100 * correct_val / total_val
        print(f"Epoch {epoch + 1}/{epochs}, Validation Accuracy: {val_accuracy:.2f}%")


    # Test aşaması
    model.eval()
    total_test, correct_test = 0, 0
    true_labels, predicted_labels = [], []
    with torch.no_grad():
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total_test += labels.size(0)
            correct_test += (predicted == labels).sum().item()

            true_labels.extend(labels.cpu().numpy())
            predicted_labels.extend(predicted.cpu().numpy())

    test_accuracy = 100 * correct_test / total_test
    print(f"Test Accuracy: {test_accuracy:.2f}%")

    # Accuracy, Precision, Recall, F1 Score, Confusion Matrix, Classification Report
    print(f"Accuracy: {accuracy_score(true_labels, predicted_labels)}")
    print(f"Precision: {precision_score(true_labels, predicted_labels)}")
    print(f"Recall: {recall_score(true_labels, predicted_labels)}")
    print(f"F1 Score: {f1_score(true_labels, predicted_labels)}")
    print(f"Confusion Matrix:\n{confusion_matrix(true_labels, predicted_labels)}")
    print(f"Classification Report:\n{classification_report(true_labels, predicted_labels)}")

# load_data() fonksiyonunu kullanarak veri kümesini yükleyin ve ayırın
train_loader, val_loader, test_loader = load_data()
cnn_model = CNN()
train_evaluate_cnn(cnn_model, train_loader, val_loader, test_loader)