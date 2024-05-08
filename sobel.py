import cv2
import numpy as np
from scipy import ndimage as ndi



def sobel_edge_detection(image):
  """
  این تابع تصویر ورودی را گرفته و لبه‌های آن را با استفاده از الگوریتم Sobel تشخیص می‌دهد.

  Args:
    image: تصویر ورودی به صورت آرایه NumPy.

  Returns:
    تصویر لبه‌یابی شده به صورت آرایه NumPy.
  """
  image = ndi.gaussian_filter(image, 4)
  # تبدیل تصویر به مقیاس خاکستری
  grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # اعمال فیلترهای Sobel
  Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
  Gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

  Gx_filtered = cv2.filter2D(grayscale, cv2.CV_64F, Gx)
  Gy_filtered = cv2.filter2D(grayscale, cv2.CV_64F, Gy)

  # محاسبه بزرگی گرادیان
  magnitude = np.sqrt(Gx_filtered**2 + Gy_filtered**2)

  # جهت گرادیان
  angle = np.arctan2(Gy_filtered, Gx_filtered) * 180 / np.pi + 90

  # غیر حداکثر سازی
  magnitude = nms(magnitude, angle)

  # تبدیل مقادیر به 0 و 255
  magnitude = magnitude * 255
  magnitude = magnitude.astype(np.uint8)

  return magnitude

def nms(magnitude, angle):
  """
  این تابع غیرحداکثر سازی را برای نازک کردن لبه‌های تشخیص داده شده اعمال می‌کند.

  Args:
    magnitude: تصویر بزرگی گرادیان به صورت آرایه NumPy.
    angle: تصویر جهت گرادیان به صورت آرایه NumPy.

  Returns:
    تصویر لبه‌یابی شده نازک شده به صورت آرایه NumPy.
  """

  height, width = magnitude.shape
  thinned = np.zeros((height, width), dtype=np.uint8)

  for i in range(1, height - 1):
    for j in range(1, width - 1):
      p = magnitude[i, j]

      if p == 0:
        continue

      q = magnitude[i - 1, j]
      r = magnitude[i + 1, j]
      s = magnitude[i, j - 1]
      t = magnitude[i, j + 1]
      n = magnitude[i - 1, j - 1]
      m = magnitude[i + 1, j - 1]
      z = magnitude[i - 1, j + 1]

      a = (angle[i, j] - angle[i - 1, j - 1]) / 180
      b = (angle[i, j] - angle[i, j - 1]) / 180
      c = (angle[i, j] - angle[i + 1, j - 1]) / 180
      d = (angle[i, j] - angle[i + 1, j]) / 180
      e = (angle[i, j] - angle[i + 1, j + 1]) / 180
      f = (angle[i, j] - angle[i, j + 1]) / 180
      g = (angle[i, j] - angle[i - 1, j + 1]) / 180
      h = (angle[i, j] - angle[i - 1, j]) / 180

      first_condition = (a <= 0 and b >= 0) or (a >= 0 and b < 0)
      second_condition = (c <= 0 and d >= 0) or (c >= 0 and d < 0)
      third_condition = (e <= 0 and f >= 0) or (e >= 0 and f < 0)
      fourth_condition = (g <= 0 and h >= 0) or (g >= 0 and h < 0)

      if p >= q and p >= r and first_condition:
        thinned[i, j] = 1
      elif p >= s and p >= t and second_condition:
        thinned[i, j] = 1
      elif p >= n and p >= m and third_condition:
        thinned[i, j] = 1
      elif p >= z and p >= p and fourth_condition:
        thinned[i, j] = 1

  return thinned

# خواندن تصویر
image = cv2.imread("D:/my/Pic/Incredible_Mixed_Wallpapers_Set_181/10.jpg")




# تبدیل به مقیاس خاکستری
#grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# اعمال الگوریتم Sobel
magnitude = sobel_edge_detection(image)

# نمایش تصاویر
cv2.imshow('Original Image', image)
cv2.imshow('Sobel Edge Detection', magnitude)
cv2.waitKey(0)

