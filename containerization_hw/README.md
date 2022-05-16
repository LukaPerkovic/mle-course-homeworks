# Docker container for the StarSpace model

To build a Docker image, run the following command:

`docker build -t nlp/starspace .`


To run a container, train the model and receive a word embedding file (output.tsv), run the following command:

`docker run -v $(pwd)/containerization_hw/volume:/data nlp/starspace`


Your word embedding file should be in ./volume folder.
