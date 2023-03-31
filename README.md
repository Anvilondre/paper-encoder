# Cog container for encoding sentences
This is a very simple implementation of running Cog with sentence-transformers. Please refer to `encode.py` file to adjust model for your needs. Useful links:  
[Cog: Containers for machine learning](https://github.com/replicate/cog)  
[SentenceTransformers Documentation](https://www.sbert.net/index.html)

## Installation and setup
1. Refer to cog documentation for [installation](https://github.com/replicate/cog#install)
2. You will also need [docker](https://docs.docker.com/get-docker/)
3. Make sure docker daemon is running. If you have Docker Desktop, just opening it should work.
4. You can optionally change model in `encode.py`, and set  `gpu: true` in `cog.yaml`
5. Run the test prediction with  
`cog predict -i text="Hello World!"`
6. If that worked, you can build the container with   
`cog build -t encoder-model`
7. To run the docker container, use   
`docker run -d -p 5000:5000 encoder-model`  
or for M1 Mac  
`docker run -d -p 5000:5000 --platform=linux/amd64 encoder-model`  
8. Cog is now serving at `http://localhost:5000`
9. Sample API request  
`curl http://localhost:5000/predictions -X POST -H 'Content-Type: application/json' -d '{"input": {"text": "Hello World!"}}'`