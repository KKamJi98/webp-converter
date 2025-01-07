# **WebP 변환기**

Python의 [Pillow](https://pillow.readthedocs.io/en/stable/) 라이브러리를 활용하여 특정 디렉토리에 있는 이미지를 **WebP 형식**으로 일괄 변환하는 스크립트

---

## **기능**

- 다양한 이미지 형식(JPG, PNG, GIF 등)을 WebP로 변환
- 변환할 소스 디렉토리와 저장할 목적지 디렉토리 지정 가능
- 지원되지 않는 이미지 형식 및 하위 디렉토리는 자동으로 건너뜀
- WebP 이미지 품질(quality) 설정 가능 (기본값: 100)

---

## **설치 방법**

1. 스크립트 다운로드:

  ```bash
  git clone https://github.com/yourusername/webp-converter.git
  cd webp-converter
  ```

2. Pillow 라이브러리 설치:

  ```bash
  pip install Pillow
  ```

---

## **사용 방법**

### **1. 이미지 준비**

- 변환할 이미지를 `image_source` 폴더에 넣어 준비

### **2. 스크립트 실행**

Python으로 스크립트를 실행

```bash
python convert_to_webp.py
```

- 기본적으로 `image_source` 폴더에서 이미지를 읽어오고, 변환된 이미지를 `image_destination` 폴더에 저장

---

## **설정 변경**

### **소스 폴더**

변환할 이미지를 저장한 폴더 경로:

```python
source_folder = "image_source"
```

### **목적지 폴더**

변환된 WebP 파일을 저장할 폴더 경로:

```python
output_folder = "image_destination"
```

### **WebP 품질**

WebP 이미지의 품질을 설정 (기본값: `100`):

```python
img.save(save_path, "webp", quality=100, optimize=True)
```

---

## **지원되는 파일 형식**

다음 이미지 형식을 변환할 수 있습니다:

- `.jpg`
- `.jpeg`
- `.png`
- `.gif`
- `.bmp`
- `.tiff`
- `.webp`

---

## **예제**

### **디렉토리 구조**

**실행 전**:

```shell
project/
├── convert_to_webp.py
├── image_source/
│   ├── photo1.jpg
│   ├── photo2.png
│   └── subdir/        (자동으로 건너뜀)
└── image_destination/
```

**스크립트 실행 후**:

```shell
project/
├── convert_to_webp.py
├── image_source/
│   ├── photo1.jpg
│   ├── photo2.png
│   └── subdir/
└── image_destination/
    ├── photo1.webp
    ├── photo2.webp
```

---

## **오류 처리**

- 지원되지 않는 파일 형식이거나 읽기 불가능한 파일이 있을 경우, 해당 파일은 건너뛰며 아래와 같은 메시지를 출력합니다:

  ```shell
  'example.gif' 변환 중 오류 발생: <오류 메시지>
  ```
