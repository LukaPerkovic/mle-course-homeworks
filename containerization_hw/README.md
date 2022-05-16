#  Docker container for the StarSpace model

To build a Docker image, navigate to the folder containing the Dockerfile,  run the following command:

`docker build -t nlp/starspace .`


To run a container, train the model and receive a word embedding file (output.tsv), run the following command:

`docker run -v $(pwd)/volume:/data nlp/starspace`


Your word embedding file should be in volume sub-folder.
