import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

class ImageAnalyzer:
    """Handles image analysis and processing operations"""
    
    @staticmethod
    def read_image(file_content: bytes) -> np.ndarray:
        """Convert bytes to OpenCV image"""
        nparr = np.frombuffer(file_content, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("Invalid image format")
        return img

    @staticmethod
    def calculate_blur_score(image: np.ndarray) -> float:
        """Calculate blur detection score (0-100)"""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
        blur_score = min(100, (laplacian_var / 500) * 100)
        return round(blur_score, 2)
    
    @staticmethod
    def calculate_brightness(image: np.ndarray) -> float:
        """Calculate average brightness (0-100)"""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        brightness = np.mean(gray)
        return round((brightness / 255) * 100, 2) 

    @staticmethod
    def count_objects(image: np.ndarray) -> int:
        """Detect and count objects in image"""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) #Changed alpha value orginally 255
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return len(contours)
    
    @staticmethod
    def calculate_contrast(image: np.ndarray) -> float:
        """Calculate image contrast (0-100)"""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        contrast = np.std(gray)
        return round((contrast / 128) * 100, 2)
    
    @staticmethod
    def enhance_image(image: np.ndarray) -> np.ndarray:
        """Auto-enhance image quality"""
        pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        enhancer = ImageEnhance.Contrast(pil_image)
        pil_image = enhancer.enhance(1.3)
        
        enhancer = ImageEnhance.Brightness(pil_image)
        pil_image = enhancer.enhance(1.1)
        
        enhancer = ImageEnhance.Sharpness(pil_image)
        pil_image = enhancer.enhance(1.2)
        
        enhanced = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
        return enhanced
    

    @staticmethod
    def get_quality_rating(blur: float, brightness: float, contrast: float) -> str:
        """Generate quality rating based on metrics"""
        score = (blur + brightness + contrast) / 3
        if score >= 70: #orignally 70
            return "Excellent"
        elif score >= 50:
            return "Good"
        elif score >= 30:
            return "Fair"
        else:
            return "Poor"
        

# ==================== TRANSFORMATION METHODS ====================
    
    @staticmethod
    def resize_image(image: np.ndarray, width: int, height: int) -> np.ndarray:
        """Resize image to specified dimensions (TODO: Implement in Sprint 2)"""
        raise NotImplementedError("Resize logic not yet implemented")
    
    @staticmethod
    def resize_by_percentage(image: np.ndarray, percentage: int) -> np.ndarray:
        """Resize image by percentage (TODO: Implement in Sprint 2)"""
        raise NotImplementedError("Percentage resize logic not yet implemented")