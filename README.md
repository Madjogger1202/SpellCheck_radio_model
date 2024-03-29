# SpellCheck_radio_model
tg: https://t.me/madjogger


An iteration of a neural network to correct characters in text that were broken during a radio broadcast The main task is to minimize the amount of data required for IoT devices to further minimize battery consumption
![image](https://github.com/Madjogger1202/SpellCheck_radio_model/assets/61242548/13e58a16-306b-4a3a-a693-c87da3899ca7)

**Big models and JamSpell corrector are in this repo: https://huggingface.co/datasets/Madjogger/JamSpell_dataset/tree/main**

The basic principle behind the idea is that there is ** no need to duplicate the message** in the presence of interference during the transmission of a radio signal. For full-fledged transmission of string information, **two packets** are transmitted: **messages** and **spaces**. This technique will reduce the size of the radio transmission by ** 1.5-3 times** in the case of an unstable connection
In addition, the algorithm can be used for **ultra low consumption** of the transmitter, for example, to make a device that will send data about the situation in the form of an alphabet of 10 characters, the values of which can be evenly distributed across the ACSII table and using a neural network to determine exactly what character was sent through a binary representation

The model can be easily scaled to a large number of features, and retraining can be carried out on any device, which makes it a universal solution


In this iteration I am using a Com Spell model that has been trained in 300k English sentences, examples of model training can be found in the project repository:
https://github.com/bakwc/JamSpell


Colab notebook with example of creating model: https://colab.research.google.com/drive/1S0sdKNiGr3O2YyVxORjYdgZWTpF1nNJN?usp=sharing

You may need to download some resources from the folder with large models and datasets, where there are already ready-made trained models: https://huggingface.co/datasets/Madjogger/JamSpell_dataset/tree/main
