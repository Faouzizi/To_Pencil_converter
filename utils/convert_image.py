########################################################################################
######################          Import packages    #####################################
########################################################################################
import cv2
import os 

class convert_images():
    def get_image_converted(self,path_import, image_name, path):
        ##############################################################################
        ############# Import images
        ##############################################################################
        print(path_import)
        color_image = cv2.imread(path_import)

        ##############################################################################
        ############# cartoonify images
        ##############################################################################
        cartoon_image = cv2.stylization(color_image, sigma_s=150, sigma_r=0.01)

        ##############################################################################
        ############# pencilfy images
        ##############################################################################
        img_cartoon, img_pencil  = cv2.pencilSketch(color_image, sigma_s=60, sigma_r=0.5, shade_factor=0.01)

        ##############################################################################
        ############# export results images
        ##############################################################################
        img_cartoon_url = ''.join([image_name,'_cartoon','.jpg'])
        img_pencil_url = ''.join([image_name,'_pencil','.jpg'])
        cv2.imwrite(os.path.join(path, img_cartoon_url), img_cartoon)
        cv2.imwrite(os.path.join(path, img_pencil_url), img_pencil)
