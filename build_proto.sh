#!/usr/bin/env bash
cd "$(dirname "$0")"
mkdir -p build

printf "Building all message modules..."
../node_modules/protobufjs/bin/pbjs -p shared -p control -p request -p stream -t static-module -o build/index.js --wrap es6 shared/*.proto control/*.proto request/*.proto stream/*.proto
../node_modules/protobufjs/bin/pbts -o build/index.d.ts build/index.js
printf "...done\n"

#printf "Building Request message module..."
#npx pbjs -t static-module -o build/request.js --wrap es6 request/*.proto
#npx pbts -o build/request.d.ts build/request.js
#printf "...done\n"
#
#printf "Building Stream message module..."
#npx pbjs -t static-module -o build/stream.js --wrap es6 stream/*.proto
#npx pbts -o build/stream.d.ts build/stream.js
#printf "...done\n"

cd ../node_modules
rm -f carta-protobuf
ln -s ../protobuf/build carta-protobuf