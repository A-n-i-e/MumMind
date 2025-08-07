import torch
import torch.nn as nn

# Recreate the model architecture
class InfantCryClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(InfantCryClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# Set the same values as during training
input_size = X_train.shape[1]  # e.g., 128
hidden_size = 64               # whatever you used
num_classes = 5                # hungry, burping, discomfort, etc.

model = InfantCryClassifier(input_size, hidden_size, num_classes)
model.load_state_dict(torch.load('infant_cry_model_state.pt'))
model.eval()
