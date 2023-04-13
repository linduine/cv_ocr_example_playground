import cv2
import pytesseract
import datetime

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/5.3.0_1/bin/tesseract'
# check if Tesseract is installed and accessible
def check_pytesseract():
    print(pytesseract.get_languages(config=''))
    print(pytesseract.get_tesseract_version())

#check_pytesseract()    

# define a video capture object
vid = cv2.VideoCapture(0)

#list of words for the game
#words = ['WORD', 'SENTENCE', 'ITECHART', 'LOVE', 'HATE', 'TREE', 'DOG', 'CAT', 'CHALLENGE', 'LAUGHTER', 'VISION', 'IDENTITY']
  
while(True):
    #pass
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(grayImage, 0, 255, \
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # Display the resulting frame
    cv2.imshow('frame', thresh)
    # call pytesseract function to recognize text
    ocr_res = pytesseract.image_to_string(thresh, lang='eng')
    # take current time
    now = datetime.datetime.now()
    # print out the current time plus ocr results
    # amend this to print out only those words that are in the provided list
    print(f"{now} {ocr_res}")
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
