===========
USING gRPC IN ODOO
=========

The simple guide: how to get Odoo product from nodejs using gRPC.

Python 3.7

gRPC 1.14.0

##

Required see https://grpc.io/docs/languages/python/basics/
             https://grpc.io/docs/languages/node/basics/
             
##

## Install dependencies

```
pip install -r requirements.txt
```

## Start gRPC Server

```
1. Go to menu: Settings/GRPC Server
2. Create new record with <service name> and <listening port>
3. Click start button
```

## Request product data from nodejs

```
1. cd to gRPC_base/client
2. Edit client.js file and add product_id that you want to get data (Line 11)
3. Type: <node client.js>
```



