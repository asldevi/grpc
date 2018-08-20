from __future__ import print_function

import grpc

import math_pb2
import math_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = math_pb2_grpc.CalculatorStub(channel)
        response = stub.DoMath(math_pb2.MathRequest(a=1, operator='+', b=2))
        print("Client received: {}".format(response.result))

if __name__ == '__main__':
    run()
