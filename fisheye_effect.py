import numpy as np
import cv2
import math

img = cv2.imread( "Bug.bmp", -1)

def fisheyes( img_suc ) :
    img = img_suc.copy()
    m, n, c = img.shape
    xc = m / 2
    yc = n / 2

    # 到4個點最遠距離
    R = math.sqrt( xc**2 + yc**2 )
    x_prime = np.zeros( (m,n), dtype= "float32")
    y_prime = np.zeros( (m,n), dtype= "float32")

    for x in range( m ) :
        for y in range( n ) :
            r = (x - xc) ** 2 + (y - yc) ** 2
            sita = math.atan2(y - yc, x - xc)
            x_prime[x,y] = (r/R)*math.cos(sita) + xc
            y_prime[x,y] = (r/R)*math.sin(sita) + yc

    img_out = cv2.remap( img, y_prime, x_prime, cv2.INTER_LINEAR)

    return img_out

new_img = fisheyes( img )
cv2.imwrite( "fisheye_bug.jpg", new_img )
cv2.imshow('fish',new_img)
cv2.waitKey( 0 )
cv2.destroyAllWindows()