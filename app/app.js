const express = require("express")
const app = express()
const bodyParser = require("body-parser")
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json())

app.set("views","./src/views")
app.set("view engine","ejs")


const home = require("./src/routes/home")
app.use("/", home)

app.use(express.static(`${__dirname}/src/public`))

module.exports = app;