########################################################################################
######################          Import packages    #####################################
########################################################################################
import cv2

def convert_images(path_import, image_name):
    ##############################################################################
    ############# Import images
    ##############################################################################
    color_image = cv2.imread(path_import)

    ##############################################################################
    ############# cartoonify images
    ##############################################################################
    cartoon_image = cv2.stylization(color_image, sigma_s=150, sigma_r=0.01)

    ##############################################################################
    ############# pencilfy images
    ##############################################################################
    cartoon_image1, cartoon_image2  = cv2.pencilSketch(color_image, sigma_s=60, sigma_r=0.5, shade_factor=0.01)

    ##############################################################################
    ############# export results images
    ##############################################################################
    cv2.imwrite('./results/'+image_name+'_pencil1'+'.jpg', cartoon_image1)
    cv2.imwrite('./results/'+image_name+'_pencil2'+'.jpg', cartoon_image2)
    cv2.imwrite('./results/'+image_name+'_cartoon'+'.jpg', cartoon_image)

