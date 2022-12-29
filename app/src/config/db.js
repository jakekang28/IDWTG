const mysql = require("mysql")

const db = mysql.createConnection({
    host : "localhost",
    user: "root",
    password : "kjh0628^^",
    database : "articles",
})

db.connect()

module.exports = db