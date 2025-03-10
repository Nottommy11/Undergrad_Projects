// YouTube Tutorial: https://youtu.be/2jqok-WgelI

const express = require("express");
const app = express();
const mongoose = require("mongoose");
const dotenv = require("dotenv");

//Import Routes
const authRoute = require("./routes/auth");
const postRoute = require("./routes/posts");

dotenv.config();

mongoose.set("strictQuery", false);

//Connext to DB
mongoose.connect(process.env.DB_CONNECT, { useNewUrlParser: true }, (err) => {
  if (err) console.log(err);
  else console.log("Connected to DB");
});

//Middleware
app.use(express.json());

//Route Middleware
app.use("/api/user", authRoute);
app.use("/api/posts", postRoute);

app.listen(3006, () => {
  console.log("Server listening on port 3006");
});
