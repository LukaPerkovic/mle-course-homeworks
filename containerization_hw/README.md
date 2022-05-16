#  Docker container for the StarSpace model

To build a Docker image, navigate to the folder containing the Dockerfile,  run the following command:

`docker build -t nlp/starspace .`


To run a container, train the model and receive a word embedding file (output.tsv), run the following command:

`docker run -v $(pwd)/volume:/data nlp/starspace Starspace/starspace train -trainFile /data/starspace_input_file.txt -model data/output`


At the end of optimization the program will save two files in the volume folder: model and output.tsv. output.tsv is a standard tsv format file containing the entity embedding vectors, one per line. output file is a binary file containing the parameters of the model along with the dictionary and all hyper parameters.
