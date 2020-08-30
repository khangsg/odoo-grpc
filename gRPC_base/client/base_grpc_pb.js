// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var base_pb = require('./base_pb.js');

function serialize_ProductRequest(arg) {
  if (!(arg instanceof base_pb.ProductRequest)) {
    throw new Error('Expected argument of type ProductRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_ProductRequest(buffer_arg) {
  return base_pb.ProductRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_ProductResponse(arg) {
  if (!(arg instanceof base_pb.ProductResponse)) {
    throw new Error('Expected argument of type ProductResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_ProductResponse(buffer_arg) {
  return base_pb.ProductResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


var ProductsService = exports.ProductsService = {
  getProductInfo: {
    path: '/Products/GetProductInfo',
    requestStream: false,
    responseStream: false,
    requestType: base_pb.ProductRequest,
    responseType: base_pb.ProductResponse,
    requestSerialize: serialize_ProductRequest,
    requestDeserialize: deserialize_ProductRequest,
    responseSerialize: serialize_ProductResponse,
    responseDeserialize: deserialize_ProductResponse,
  },
};

exports.ProductsClient = grpc.makeGenericClientConstructor(ProductsService);
