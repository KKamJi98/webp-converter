import os
from PIL import Image

def convert_images_to_webp(source_dir, destination_dir=None):
    """
    지정한 디렉토리(source_dir)에 있는 모든 이미지 파일을 webp 형식으로 변환합니다.
    destination_dir이 지정되지 않은 경우, source_dir 안에 webp 파일을 생성합니다.

    :param source_dir: 변환할 이미지들이 들어 있는 디렉토리 경로
    :param destination_dir: 변환된 webp 파일을 저장할 디렉토리 경로 (기본값: None)
    """
    # destination_dir이 None이면 source_dir과 동일한 디렉토리 내에 저장
    if not destination_dir:
        destination_dir = source_dir

    # 변환할 디렉토리가 존재하는지 확인
    if not os.path.isdir(source_dir):
        print(f"소스 디렉토리({source_dir})가 존재하지 않습니다.")
        return

    # 저장 디렉토리가 존재하지 않으면 생성
    os.makedirs(destination_dir, exist_ok=True)

    # 변환할 이미지 파일들 처리
    for filename in os.listdir(source_dir):
        # 파일 경로
        file_path = os.path.join(source_dir, filename)
        
        # 만약 서브 디렉토리가 있다면 스킵 혹은 재귀 호출 등 원하는 대로 처리
        if os.path.isdir(file_path):
            print(f"'{filename}'은 디렉토리이므로 스킵합니다.")
            continue
        
        # 이미지로 처리할 수 있는지 여부 확인
        # 확장자로 간단히 판별(또는 try-except로 PIL open 시도 가능)
        ext = os.path.splitext(filename)[1].lower()
        if ext in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"]:
            # 이미지 로딩
            try:
                img = Image.open(file_path).convert("RGB")  # webp는 RGB 모드 권장
                # 저장할 이름(webp 확장자)
                new_filename = os.path.splitext(filename)[0] + ".webp"
                save_path = os.path.join(destination_dir, new_filename)
                # webp 파일로 저장 (quality, optimize 등 옵션 조정 가능)
                img.save(save_path, "webp", quality=100, optimize=True)
                print(f"'{filename}' → '{new_filename}' 변환 완료")
            except Exception as e:
                print(f"'{filename}' 변환 중 오류 발생: {e}")
        else:
            print(f"'{filename}'는 지원되지 않는 이미지 형식입니다. 스킵합니다.")


if __name__ == "__main__":
    source_folder = "image_source"  # 변환할 이미지들이 모여 있는 디렉토리
    output_folder = "image_destination"  # 변환된 webp 파일을 저장할 디렉토리(선택)
    
    # 호출
    convert_images_to_webp(source_folder, output_folder)

