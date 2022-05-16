FROM python:3.8-slim
RUN     apt-get update && \
	apt-get install -y wget unzip git make g++ libboost-all-dev && \
	wget https://boostorg.jfrog.io/artifactory/main/release/1.79.0/source/boost_1_79_0.zip && \
	unzip boost_1_79_0.zip && \
	mv boost_1_79_0 /usr/local/bin && \

	git clone https://github.com/facebookresearch/Starspace.git && \
	cd Starspace && \
	make && \
	/Starspace/starspace train -trainFile /data/starspace_input_file.txt -model output && \
	echo "DONE!" 
	
