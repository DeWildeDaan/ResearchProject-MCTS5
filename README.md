# ResearchProject-MCTS5

In this repo you'll find:

- User manual in the 'Manuals' folder.
- Installation manual in the 'Manuals' folder.
- All files used for the demo (Data, labels, config files) in the 'AL-demo-files.zip' folder.
- All results I got in the 'Results' folder.
- The python script used to select the correct labels to upload to google colabs (select-annotations.py).
- (A backup of the Google Colab notebook)


---


The code for using active learning with MaskAL and Detectron2 can be found in Google Colabs:
https://colab.research.google.com/drive/1reLQL3lLC-KrqVCQT9PAd6ouKhmDPDwN?usp=sharing

If you'd like to learn more about active learning and how the MaskAL software works, you can read my blogpost here:
https://medium.com/@daandw5/active-learning-what-is-it-and-how-does-it-work-c002f52ff3f2?source=friends_link&sk=80a47662dfd07c06852b5c80734494e4


---


In the demo we compared training a Detectron2 model with active learning to training a model with random image sampling. 
You can see we get better results much faster and with less images when using active learning.

![maskAL_graph](./Results/Plot_AL_vs_Random.jpg?raw=true)

### How to interpret this graph?
The green line are the results from our first test with Active Learning;
this is where the input pictures where selected by MaskAL.

The red line are the results of our second test with random sampling;
this is where the input images are completely randomly selected.

x-axis: the amount of training images the model was trained on

y-axis: the mean average precision of the model

In this example, our model trained with active learning already had a better result with only 75% of our training data and had maximum results with 83,3% of our total training data.



### What is mAP (mean average precision)?
mAP formula is based on the following sub metrics:

- Confusion Matrix
- Intersection over Union(IoU)
- Recall
- Precision
