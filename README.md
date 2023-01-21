# ResearchProject-MCTS5

In this repo you'll find:

- All files used for the demo (Data, labels, config files).
- All results I got.
- The python script used to select the correct labels to upload to google colabs when MaskAL asks for them.

---

The demo for using active learning with MaskAL and Detectron2 can be found in Google Colabs:
https://colab.research.google.com/drive/1reLQL3lLC-KrqVCQT9PAd6ouKhmDPDwN?usp=sharing

A more detailed walkthrough with a more theoretical focus on active learning can be found here:
....

---

In the demo we compared training a Detectron2 model with active learning to training a model with random image sampling. 
You can see we get better results much faster and with less images when using active learning.
Green = mAP when using active learning.
Red = mAP when using random image sampling.
![maskAL_graph](./Results/Plot_AL_vs_Random.jpg?raw=true)

You can find all results in the 'Results' folder.
