import grpc
import document_search_pb2 as document_search_pb2
import document_search_pb2_grpc as document_search_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:8000') as channel:
        stub = document_search_pb2_grpc.DocumentSearchServiceStub(channel)
        responce = stub.SearchContents(document_search_pb2.SearchQuery(msg='Yamada'))
    print("RECV: %s" % responce.message)

if __name__ == '__main__':
    run()