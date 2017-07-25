### Benchmarking HD video decoding using mplayer which is running on Ubuntu machine outside docker container

This file will be updated soon. This file does not have docker logs explanation. Also, I find mplayer statistics logging soon, if possible. 

Output produced by mplayer at the end of video decoding

```

BENCHMARKs: VC: 465.920s VO:  0.055s A:   4.806s Sys: 437.682s =  908.463s
BENCHMARK%: VC: 51.2866% VO:  0.0060% A:  0.5291% Sys: 48.1783% = 100.0000%

```

### Benchmarking HD video decoding using mplayer which is running inside docker container

Here, I am running the mplayer container inside docker. The output produced when running the mplayer docker container standalone is:

```
BENCHMARKs: VC:   7.532s VO:  38.374s A:   5.240s Sys: 837.806s =  888.951s
BENCHMARK%: VC:  0.8472% VO:  4.3168% A:  0.5895% Sys: 94.2465% = 100.0000%

```

### Benchmarking HD video decoding while running mplayer container and cpu memory hog container simultaneously

Running mplayer conatiner along with the hog application container. The output I got at the end of decoding is:

```
BENCHMARKs: VC:  26.026s VO:  44.054s A:  22.969s Sys: 799.289s =  892.338s
BENCHMARK%: VC:  2.9166% VO:  4.9369% A:  2.5740% Sys: 89.5724% = 100.0000%

```












