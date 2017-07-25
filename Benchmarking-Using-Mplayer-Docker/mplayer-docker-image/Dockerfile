FROM library/debian

RUN apt-get update && \ 
apt-get install -y mplayer && \
apt-get clean && apt-get autoclean && \
	rm -rf /var/lib/apt/lists/*
ADD Sintel.mp4 /

CMD ["mplayer","-benchmark","-vo","null","-ao","null","./Sintel.mp4"]
