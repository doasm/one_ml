from pathlib import Path
import shutil
import kagglehub

def main():
    # Download dataset
    data_set_name = 'camnugent/california-housing-prices'
    data_set_path = kagglehub.dataset_download(data_set_name)    
    src_path = Path(data_set_path)
    dest_path = Path('./kaggle') / data_set_name
    shutil.copytree(src_path, dest_path)

if __name__ == '__main__':
    main()