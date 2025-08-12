import os
import torch
import torchaudio
import torchaudio.transforms as T
import librosa
import numpy as np

# Label classes
classes = ['hungry', 'burping', 'discomfort', 'belly_pain', 'tired']



# Define the model again
class CryClassifier(torch.nn.Module):
    def __init__(self, num_classes=5):
        super(CryClassifier, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1)
        self.relu1 = torch.nn.ReLU()
        self.pool1 = torch.nn.MaxPool2d(2)

        self.conv2 = torch.nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.relu2 = torch.nn.ReLU()
        self.pool2 = torch.nn.MaxPool2d(2)

        self.flatten = torch.nn.Flatten()
        self.fc1 = torch.nn.Linear(32 * 32 * 32, 128)
        self.relu3 = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(128, num_classes)

    def forward(self, x):
        x = self.pool1(self.relu1(self.conv1(x)))
        x = self.pool2(self.relu2(self.conv2(x)))
        x = self.flatten(x)
        x = self.relu3(self.fc1(x))
        x = self.fc2(x)
        return x


# Load model weights
model_path = 'infant_cry_model_state_v2.pt'
model = CryClassifier()
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()

# Audio -> Spectrogram pipeline
def preprocess_for_model(file_path):
    waveform, sr = librosa.load(file_path)
    spectro = audio_to_spectrogram(waveform, sr)
    spectro_tensor = torch.tensor(spectro).unsqueeze(0).unsqueeze(0).float()
    
    return spectro_tensor  # shape: (1, 1, 128, 128)

def audio_to_spectrogram(waveform, sr, max_len=128):
    spectro = librosa.feature.melspectrogram(y=waveform, sr=sr, n_mels = 128)
    spectro_db = librosa.power_to_db(spectro)

    #Ensures each spectrogram is the same shape (128,128)
    if spectro_db.shape[1] < max_len:
        pad_width = max_len - spectro_db.shape[1]
        spectro_db = np.pad(spectro_db, pad_width=((0, 0), (0, pad_width)))
    else:
        spectro_db = spectro_db[:, :max_len]

    return spectro_db


# Inference function
def analyze_cry(audio_path):
    input_tensor = preprocess_for_model(audio_path)

    # Predict
    with torch.no_grad():
        output = model(input_tensor)
        predicted_class = torch.argmax(output, dim=1).item()

    probs = torch.nn.functional.softmax(output, dim=1)
    confidence = probs[0][predicted_class].item()
    
    return classes[predicted_class], confidence
    




label, confidence = analyze_cry("donateacry_corpus/hungry/2EE636FB-BD76-4118-A0EF-82FAFC32301F-1436586600-1.1-f-04-hu.wav")
print(f"Predicted cry: {label} ({confidence*100:.2f}%)")


