import cv2

def canny_img_pro(img_path):
    img = cv2.imread(img_path ,cv2.IMREAD_GRAYSCALE)
    filter = cv2.Canny(img,100,200)
    #cv2.waitKey(0)
    #cv2.imwrite('static/canny01.png',filter)
    return filter
	
	
def sobel_img_pro(img_path):
    img  = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
 
    sobel_horizontal = cv2.Sobel(img,cv2.CV_64F,1,0,ksize = 5)
    sobel_vertical = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

    denoised = cv2.GaussianBlur(img,(5,5),0)
    filter = cv2.Laplacian(denoised,cv2.CV_64F)
    #cv2.waitKey(0)
    #cv2.imwrite('static/sobel01.png',filter)
    return filter

def save_image(path, imagefile):
    cv2.imwrite(path, imagefile)