from inspect import getsource
import tensorflow as tf
import numpy as np
import cv2 as cv
import statistics

#Importing the trained model
model = tf.keras.models.load_model("models/rock_paper_scissors.h5")

def evaluate_move(test_image):
    #Resizing the array according to the model requirement
    stretch_near = cv.resize(test_image,(300, 300),interpolation = cv.INTER_NEAREST)
    stretch_near = stretch_near[np.newaxis, :]

    #Evaluating the gesture made
    probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
    predictions = probability_model.predict(stretch_near)

    return np.argmax(predictions)

def main():
    result = ["rock", "paper", "scissor", "Wait..."]
    outcome_list = []
    outcome_mode = 3
    last_move = np.zeros((300, 300, 1), dtype = "uint8")

    
    camera = cv.VideoCapture(0)


    # Check if the webcam is opened correctly
    if not camera.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        #Getting webcam feed
        ret, frame = camera.read()
        #Making the gesture box (300x300)
        cv.rectangle(frame, (80, 0), (380, 300), (255, 0, 0), 2)
        
        

        input_img = frame[0:300, 80:380]        #The image array for evaluating gesture
        frame = frame[0:480, 80:560]            #The image array to display
        frame = cv.flip(frame, 1)
        
        
        c = cv.waitKey(1)

        #To evaluate the result
        if c == 32:
            outcome = evaluate_move(input_img)
            outcome_mode = outcome
            last_move = input_img
            #outcome_list.append(outcome)

            # if len(outcome_list) > 10:
            #     outcome_mode = statistics.mode(outcome_list)
            #     outcome_list = []

        frame = cv.putText(frame, result[outcome_mode], (0,100), cv.QT_FONT_NORMAL, 1, (255,0,0))
        frame = cv.putText(frame, "Press 'space' to update", (0,400), cv.QT_FONT_NORMAL, 1, (255,0,0))
        last_move = cv.putText(last_move, result[outcome_mode], (0,250), cv.QT_FONT_NORMAL, 1, (255,0,0))
        
        cv.imshow('Input', frame)
        cv.imshow('Last Move', last_move)
        #Press Esc to exit the window
        if c == 27:
            break

    camera.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()    
