ts config

npm install typescript ts-node @types/node --save-dev


npx tsc --init



npm install @types/express --save-dev


nodemon.json 

{
    "watch": ["./"],
    "ext": ".ts,.js",
    "ignore": [],
    "exec": "ts-node ./server.ts"
}

  "scripts": {
    "dev": "nodemon",
    "build": "rimraf ./build && tsc",
    "start": "npm run build && node build/server.js"
  },

