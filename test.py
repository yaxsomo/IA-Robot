import numpy as np
import cv2

#Write Menu
print('\t\t   *Welcome to the Simple Webcam Application*\n\n'
      'Select a Feature:\n',
      3*' ' + 'Press 1 to Save Photo in Color Mode\n',
      3*' ' + 'Press 2 to Save Photo in Grayscale Mode\n',
      3*' ' + 'Press 3 to Save Photo in Blur Filter\n',
      3*' ' + 'Press 4 to Save Video Recording and Quit the Application\n')

#Setting for Image Cap and Upper Value
a = 0
b = 0
c = 0
upper = [0,0,0]

#Find HSV Green Value 
green = np.uint8([[[0,255,0]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)

#Found Upper Value
for i in hsv_green:
    for j in i:
        upper[0] += (j[0])
        upper[1] += (j[1])
        upper[2] += (j[2])
    for i in range (len(upper)):
        if upper[i] == 255:
            pass
        else:
            upper[i] += 20
#Found Lower Value
lower = upper.copy()
for j in range (len(lower)):
    if lower[j] == 255:
        lower[j] = 10
    else:
        lower[j] -= 40

#Open Default Camera
cap = cv2.VideoCapture(0)

#Define the Codec and Create VideoWriter Object
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
vid = cv2.VideoWriter('Color Video.avi', fourcc, 20.0, (640,480))
vid2 = cv2.VideoWriter('Green Video.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    #Take each Frame
    ret, frame = cap.read()
    #Flip Video vertically (180 Degrees)
    frame = cv2.flip(frame, 180)
    #Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Define Range of Green Color in HSV
    upper_green = np.array(upper)
    lower_green = np.array(lower)
    # Threshold the HSV Image to Get only Green Color
    mask = cv2.inRange(hsv, lower_green, upper_green)   
    result = cv2.bitwise_and(frame, frame, mask = mask)
    #Showing Camera Cap
    cv2.imshow('Detect Green Color',result)
    cv2.imshow('Webcam',frame)
    #Record Video
    vid.write(frame)
    vid2.write(result)
    k = cv2.waitKey(1) & 0xFF
    if k == 49: #ord 1
        #Take a Photo
        a += 1
        colorName = "Result {}.png".format(a)
        #Save Photo
        cv2.imwrite(colorName, frame)
    elif k == 50: #ord 2           
        gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY )
        b += 1
        grayName = "Grayscale {}.png".format(b)
        #Save Photo
        cv2.imwrite(grayName, gray)
    elif k == 51 : #ord 3
        blur = cv2.blur(frame,(7,7))
        c += 1
        blurName = "Blur {}.png".format(c)
        cv2.imwrite(blurName, blur)
    elif k == 52 : #ord 4
        #Quit
        print ('Good Bye!')
        break

#Release the Cap and Video   
cap.release()
vid.release()
vid2.release()
cv2.destroyAllWindows()      