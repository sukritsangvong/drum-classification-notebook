# drum-classification-notebook

### Background: 

    I started this project at the beginning of the spring term of my freshman year and finished it when the term ended. I did not have much prior experience in CS before coming to Carleton College, so I was very excited to explore what CS has to offer. 
    
    Feeling that there are a lot that could be learned outside of the classroom, I started my first online course on Coursera- Machine Learning course taught by Andrew Ng. Well, the main reason I started with this course was because it was free. I didn't have any particular interest in Machine Leaning back then. However, After a solid 10-week of trying to complete the course, I got very into it but also felt like I was just following along the class without being exposed to the topic as much.
    
    Hence, with some basis I got from the course, I decided to start my own project from ground-up(that is by starting with a blank python page and collecting all the data by myself) to get a grasp of what it means to do machine learning. 
    
    I play drumset since middle school, and, unfortunately, the drum has no music notes available online like other instruments do. Therefore, I had to listen to the songs and come up with the notes by myself when my band wanted to play something. With that thought, I set my goal to build a model that would classify each part of the drums(kick, snare, hi-hats, tom, and cymbal).
    
Goal:

    The intention of this project is not to find the best model for this problem, but rather to set a goal to stick to one model and learn everything related to it along the way. I just wanted to learn.
    
    I chose the Convolutional Neural Network(CNN) because doing it means that I would be learning audio processing, image classification, and neural network at the same time. It would best satisfy my goal of learning new things at the same time.

### Acknowledgement:

    After I decided to do an audio classification problem, there weren't many options for me to learn from. Fortunately, I stumbled upon Valerio Velardo's youtube channel--The Sound of AI.-- He made a series teaching the very basics of audio processing and deep learning in general which helped me get started on the topic. His series also includes music_genres classification problems that I got the idea of how to create a CNN model from.

### Accomplishments:

    While writing up the code, I tried my best to understand everything I wrote. Writing one line of code sometimes made me go through several articles and videos just to, at the very least, know why it is there(BatchNormalization, batch_size vs epoch, etc). This project made me more comfortable with machine learning, deep learning, and the new computer science fields in general. Being exposed to these new fields incentivized me to look more into other CS fields that I have yet to get into. Moreover, I got a chance to use Notebook and do some data visualization that I always thought was boring, but when there is a purpose to it, it is kind of fun. Even though not everything in the code makes sense to me, this is a great stepping stone I took for my first-ever CS project.
    
### Improvements:

amount of hidden layers:

    The three layers seem to be a "recommended" number for some reasons. Decreasing the layer resulted in a less accurate model while adding more layers caused an error.
    
batch_size VS epoch:

    This gave me a headache. With the epoch, I tried to increase the size by a small value and make sure that the test accuracy on the validation set is leveling off and not decreasing. With pure labor-intensive guesses, 120 seems to do okay with the accuracy on the validation set and yield a good accuracy on the test set. 
    
    On the other hand, playing with batch size seems to be correlating with the epoch, where decreasing the batch size allows me to also decrease the epoch. Changing the batch_size to 16(from 32) allows me to bring the epoch down to 50(from 120) and still gets a good result on the validation set. However, when it comes to the test set, this version yields a lower accuracy on average. Therefore I decided to just keep the batch_size constant and play with the epoch.
    
    With more experience, it would be easier to start with "starter values" and know what to modify when something happens. As for this project, my labor-intensive result worked fine.
    
Data Processing:

    The way I split the data to test and train made it so that there isn't a proportional amount of each part of drums in the test and train. Sometimes, only 2 data points for a drum part made it to the test set, and if one fails, the percentage for that particular part drops to 50 percent. Although this doesn't affect the overall accuracy as much, it creates a little misleading result when it comes to analyzing how the model does on individual parts. With more background on Stat, there might be a better way to set up this project.
    
Data Collection:
    
    It was a painful process. The parts like kick and snare were relatively easier to find, but parts like tom and cymbal are not. I tried to pick data that I can identify that it is that part of the drum. Those that were not recorded by an actual drum(ones that made by computer) would not be added to the dataset. It was time-consuming.

### Future Project:

    The far-fetch goal that I had for this project was to write a program that by selecting an audio file of any music, with multiple instruments and vocal, it would be able to recognize drum from the music and return drum notes for the entire file. This classification is, possibly, a small step for that.


