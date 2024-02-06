docker buildx build --output type=docker --platform=linux/amd64 -t sparql-federate:0.0.1-amd .
docker tag sparql-federate:0.0.1-amd salva5297/sparql-federate:0.0.1
docker push salva5297/sparql-federate:0.0.1

docker buildx build --output type=docker --platform=linux/amd64 -t sparql-federate:latest-amd .
docker tag sparql-federate:latest-amd salva5297/sparql-federate:latest
docker push salva5297/sparql-federate:latest