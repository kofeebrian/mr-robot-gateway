make generate-proto

filepath=./app/protos/amass/**/*_pb2*.py
2to3 -wn -f import ${filepath}