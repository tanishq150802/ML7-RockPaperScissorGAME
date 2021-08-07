# ML7-RockPaperScissorGAME
**ML Project By Kshitij M Bhat, Bhavya Dalal and Tanishq Selot for IITISoC'21**

Mentors - Aryan Rastogi, Bharat Gupta, Sakshee Patil, Kashish Bansal

Description: Implementing a simple game using CV.

**For Mid-Evaluation**, we have built a model to classify hand images as rock, paper and scissors. We primarily used Python along with Tensorflow and Keras Packages. We employed Convolutional Neural Networks (CNNs) to build this model. We tackled overfitting using [Data augmentation](https://www.tensorflow.org/tutorials/images/data_augmentation). 80% : 20% Training-Validation split. The dataset we used for this model is [Tensorflow Rock-Paper-Scissors Images](https://www.tensorflow.org/datasets/catalog/rock_paper_scissors).

Input size of images - 300x300 

Training Accuracy - 97.52%

Validation Accuracy - 99.40%

Test Accuracy - 94.35%

F1 Score - 94.95%

All the code can be accessed in the ML7_RockPaperScissors.ipynb file. It can be easily run in any IPython notebook editor.

**Some correctly predicted images :**

![paper1](https://user-images.githubusercontent.com/81608921/125164332-4babaa80-e1af-11eb-8f37-12f28b4291e4.jpg)

![theROCK](https://user-images.githubusercontent.com/81608921/125164432-ce346a00-e1af-11eb-8a02-fe922340c610.jpg)

![paper4](https://user-images.githubusercontent.com/81608921/125164492-19e71380-e1b0-11eb-97fc-0000e6985127.jpg)

![STONE](https://user-images.githubusercontent.com/81608921/125164523-561a7400-e1b0-11eb-8064-46006b9efa98.jpg)


**For the final submission:**

We used OpenCV for taking the input from the user via the webcam and labelling it using the classifier model. The computer randomly selects (**no chance of bias**) an image against the human opponent and the applies the conditional statement to predict that who should get the point. The Pygame gaming interface is used to display the responses and it also show the scoreboard at real-time. The interface looks like :

![bdde3a19-0f06-40ed-b763-c97ebaa93d1d](https://user-images.githubusercontent.com/81608921/128611161-7e568128-0d7e-4794-8518-7667c4e810fe.jpg)

