FROM python:3.8-slim

ARG USER_ID
ARG GROUP_ID

 
RUN	apt-get update && \
	apt-get install -y wget unzip git make g++ libboost-all-dev && \
	wget https://boostorg.jfrog.io/artifactory/main/release/1.79.0/source/boost_1_79_0.zip && \
	unzip boost_1_79_0.zip && \
	mv boost_1_79_0 /usr/local/bin && \
	git clone https://github.com/facebookresearch/Starspace.git && \
	cd Starspace && \
	make && \
	echo "DONE!" 
	
RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user
