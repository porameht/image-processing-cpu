# Background Remover API

🐍 A FastAPI service that removes backgrounds from images using deep learning models, optimized for CPU and low-memory environments.

## Features
- High-quality background removal using CarveKit
- FastAPI-based REST API
- Docker support
- CPU-optimized processing
- Batch processing support
- Easy integration

## Model Details
This API uses CarveKit's Tracer-B7 model which provides:
- 90% accuracy (mean F1-Score, DUTS-TE)
- Optimized for general objects (people, animals, products etc.)
- CPU-friendly processing
- High-quality edge detection

## 🎓 Implemented Neural Networks

| Networks | Target | Accuracy |
|----------|---------|-----------|
| **Tracer-B7** (default) | **General** (objects, animals, etc) | **90%** (mean F1-Score, DUTS-TE) |
| U^2-net | **Hairs** (hairs, people, animals, objects) | 80.4% (mean F1-Score, DUTS-TE) |
| BASNet | **General** (people, objects) | 80.3% (mean F1-Score, DUTS-TE) |
| DeepLabV3 | People, Animals, Cars, etc | 67.4% (mean IoU, COCO val2017) |

> Note: This API currently uses Tracer-B7 as it provides the best general-purpose performance.

## Prerequisites
- Python 3.10+
- Docker (optional)

## Installation

### Local Development

1. Clone the repository
```bash
git clone <repository-url>
cd image-processing-cpu
```

2. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Setup environment variables
```bash
cp .env.example .env
```

5. Run the application
```bash
python main.py
```

### Using Docker

1. Build the image
```bash
docker build -t background-remover .
```

2. Run the container
```bash
docker run -p 8000:8000 background-remover
```

## API Endpoints

### Health Check
```http
GET /
```

### Remove Background
```http
POST /remove-bg
Content-Type: multipart/form-data

file: <image-file>
```

Example using curl:
```bash
curl -X POST -F "file=@image.jpg" http://localhost:8000/remove-bg
```

## Model Configuration
The service uses CarveKit with the following optimized settings:
- Segmentation Network: Tracer-B7
- Segmentation Mask Size: 640
- Trimap Parameters: 
  - Dilation: 30
  - Erosion: 5
- Post-processing: FBA Matting
- Device: CPU optimized

## Project Structure
```
.
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── background_remover.py
│   └── utils/
│       ├── __init__.py
│       └── file_handler.py
├── script/
│   └── download-weights
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── RemoveBackground.py
├── main.py
└── requirements.txt
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| API_HOST | API host address | 0.0.0.0 |
| API_PORT | API port number | 8000 |
| TEMP_DIR | Temporary files directory | temp |
| OUTPUT_DIR | Output files directory | output |
| CLOUDINARY_CLOUD_NAME | Cloudinary cloud name | - |
| CLOUDINARY_API_KEY | Cloudinary API key | - |
| CLOUDINARY_API_SECRET | Cloudinary API secret | - |

## Development

1. Create and activate virtual environment
2. Install dependencies
3. Copy .env.example to .env and adjust as needed
4. Run the application in development mode:
```bash
uvicorn main:app --reload
```

## Production Deployment

For production deployment, it's recommended to:
1. Use Docker
2. Set appropriate environment variables
3. Use a reverse proxy (e.g., Nginx)
4. Implement proper security measures

## Credits
This project uses [CarveKit](https://github.com/OPHoperHPO/image-background-remove-tool) for background removal.

## License
[MIT License](LICENSE)