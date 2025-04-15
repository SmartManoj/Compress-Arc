import kagglehub
# Download selected version
path = kagglehub.dataset_download(r"boristown/darkagicompressarc/versions/4")

print("Path to dataset files:", path)