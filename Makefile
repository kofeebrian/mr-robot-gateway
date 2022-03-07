.PHONY: generate-proto

generate-proto:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./app/protos/amass/**/*.proto ./app/protos/amass/*.proto
