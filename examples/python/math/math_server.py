from concurrent import futures
import time

import grpc

import math_pb2
import math_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Calculator(math_pb2_grpc.CalculatorServicer):

    def DoMath(self, request, context):
        result = eval('{} {} {}'.format(request.a, request.operator, request.b))
        return math_pb2.MathReply(result=int(result))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    math_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
