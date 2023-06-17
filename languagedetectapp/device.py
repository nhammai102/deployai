import torch

# Check if CUDA is available 
cuda_available = torch.cuda.is_available()

# Get the device name (cuda:0 for GPU 0, cpu for CPU)
if cuda_available:
    device_name = "cuda:0"
else: 
    device_name = "cpu"
    
# Create the device object 
device = torch.device(device_name)

# Print the device being used
print(f"Using device: {device}")