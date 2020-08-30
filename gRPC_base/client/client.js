const grpc = require('grpc');
const messages = require('./base_pb');
const services = require('./base_grpc_pb');

function main() {
  const client = new services.ProductsClient(
    'localhost:50052', grpc.credentials.createInsecure()
  );
  console.log(client);
  const ProductRequest = new messages.ProductRequest();
  ProductRequest.setProductId(3);

  console.log(ProductRequest.product_id);

  client.getProductInfo(ProductRequest, function (err, response) {
    if (err) {
      console.log('this thing broke!', err);
    } else {
      console.log('Product Name:', response.getName());
      console.log('Product Price:', response.getPublicPrice());
    }
  })
}

main();