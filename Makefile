.PHONY: generate-proto

generate-proto:
	python3 -m grpc_tools.protoc -I../capamass --python_out=./app --grpc_python_out=./app ../capamass/protos/amass/**/*.proto