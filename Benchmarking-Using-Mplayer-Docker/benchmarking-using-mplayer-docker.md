### Benchmarking using mplayer

For this file experiment I am decoding video with mply. For the purpose of benchmarking the decode of video, I am using the below mentioned command and running it inside the docker conatiner. 

```
1) mplayer -benchmark -ao null -vo null filename.mp4
```
 - According to the man pages of mplayer [man pages of mplayer](https://www.google.com), the -benchmark option will print some statsictics regarding CPU usage and dropped frames.
- -ao means audio output, I am specifying null in the audio output. Similarly __-vo__ means video output, I am specifying __null__ for the video output too. It will containue decoding a video file but will not display the video since null is specified. 

The various other options for the purpose of benchmarking that can be used are  __-nosound__ and __-novideo__. But the problem with them is, they disable respective audio or video decoding which will result in less consumption of resources.

Apart from the above mentioned command, the other command that can be used for decoding inside the docker container is:

```
2) mplayer -benchmark -nosound -vo null filename.mp4
```
-nosound option will disable the audio decoding and so will result in less consumption of resources.f

There are of course other commands that can be used for decoding are:
1) mplayer -benchmark filename.mp4
2) mplayer -benchmark -nosound filename.mp4

Problem with above two commands arises when running mplayer inside docker container. I am not able to display video in mplayer when running inside docker container. 

#### Understanding the output of -benchmark option

__-benchmark__ will produce some real statistics regarding cpu usage for audio and video decoding. 
```
A: 20  V:20  A-V: 0.000  ct: 0.041  0/  0  30% 0%  0.9%  0  0
```
According to the website [https://arstechnica.com/civis/viewtopic.php?t=476203](https://arstechnica.com/civis/viewtopic.php?t=476203). Most of the above parameters are for debugging purpose only.
- A specifies audio position in seconds
- V specifies video position in seconds
- A-V gives delay (audio-video) difference in seconds
- ct specifies total A-V sync correction done
- frames played from last seek
- frames decoded from last seek
- video codec CPU usage in %  (30% in above example)
- Video output CPU usage (0% in above example, since -vo null so no video output)
- audio codec CPU usage in %
- audio output CPU usage (0% in above example, since -ao null so no audio output)
- frames dropped to maintain A-V sync
- current cache size used

Once the mplayer is finished with the task of decoding the video, due to -benchmark option following output is displayed.
```
BENCHMARKs: VC: 327.356s VO:  12.745s A:  11.342s Sys: 536.390s =  887.833s
BENCHMARK%: VC: 36.8714% VO:  1.4355% A:  1.2775% Sys: 60.4156% = 100.0000%
```
- As we can see from the first line, the total decode runtime of video 887.833s, While the length of the video is 888 s. This gives indication of some frames being dropped. This insight I obtained from the link.
- According to []() the first line gives insight on the time spent in various phases viz; 12.745 s in Video output, 11.342 in audio decode while 536.390s in sys.
- According to [Understand Benchmarking Output](http://mplayerhq.hu/pipermail/mplayer-users/2015-January/087887.html) sys signifies the time spent in other tasks other than audio and video decoding. 
- Mplayer's -benchmark option is not showing the % of no. of frames dropped.

 The other video player, I am trying to explore are:
- [MPV Player](https://github.com/mpv-player/), a new video player developed re-using the source code of Mplayer. The problem I found with this player is, the option -benchmark is deprecated. Uptill now, I have not found any usefull benchmarking option with this player
- I am yet to explore running VLC player inside docker container. I have found some Dockerfile that runs VLC player inside conatiner, but I am not able to understand the code and options specified for compiling the image



