import kaggle
import kagglehub

api = kaggle.api

def main():
    # Download latest version
    path = kagglehub.dataset_download("camnugent/california-housing-prices")    
    print("Path to dataset files:", path)

if __name__ == '__main__':
    main()