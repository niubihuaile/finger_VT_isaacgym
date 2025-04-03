import cv2

# 读取图像
image = cv2.imread('/home/sj/isaacgymenvs/isaacgymenvs/tacsl_sensors/tactile_utils/finger_data/bg.jpg')

# 旋转图像180度
rotated_image = cv2.rotate(image, cv2.ROTATE_180)

# 显示旋转后的图像
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
