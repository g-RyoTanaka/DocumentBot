from concurrent import futures
import document_search_pb2 as document_search_pb2
import document_search_pb2_grpc as document_search_pb2_grpc
import grpc

class DocumentSearchService(document_search_pb2_grpc.DocumentSearchServiceServicer):
    def SearchContents(self, request, context):
        print("RECV: %s" % request.msg)
        message = "Hello, %s!" % request.msg
        print("SEND: %s" % message)
        return document_search_pb2.SearchContentResult(message=message)
    
    def SearchNumber(self, request, context):
        print("RECV: %s" % request.msg)
        message = "Hello, %s!" % request.msg
        print("SEND: %s" % message)
        return document_search_pb2.SearchNumResult(message=message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    document_search_pb2_grpc.add_DocumentSearchServiceServicer_to_server(DocumentSearchService(), server)
    server.add_insecure_port('[::]:8000')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()