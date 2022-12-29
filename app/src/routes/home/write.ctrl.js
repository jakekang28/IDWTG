const db = require("../../config/db")
const fs = require("fs")
function sleep(ms) {
    const wakeUpTime = Date.now() + ms;
    while (Date.now() < wakeUpTime) {}
  }
const hello =(req, res) => {
    res.render("home/webcam_capture")
    sleep(10000)
    fs.readFile("../current_emotion.txt",'utf-8',function (err, data) {
        if(err){
            console.log(err)
        }
        else{
            if(data == 'good'){
                console.log(data)
                return res.render("home/homeview")
            }
            else{
                console.log(data)
                return res.render("home/writeview")
            }
        }
    })
    
}
const menu = (req, res) => {
    res.redirect("/view")
}
const read = (req,res) => {
    db.query('SELECT * FROM article', function(err, results) {
        if(err) {
            res.send(err)
        } else {
             res.send(results);
        }
    })
}
const getinsert = (req, res) => {
    db.query('SELECT * FROM article;',function(err, data, fields){
        if(err){
            console.log(err)
            res.status(500).send('Internal Server Error')
        }else{
           res.render("home/writeview.ejs")
         }
    })
    
}
const insert = (req, res, next) => {
    var title = req.body.title
    var content = req.body.content
    
    var data = [title, content]
    db.query("INSERT INTO article (title, article) values (?,?);",[title,content],function(err,row){
        if(err){
            console.log("err : " + err);
            res.status(500).send('Internal Server Error');
        }
        else{
            console.log("rows " + JSON.stringify(row));
            res.send({
                title : title,
                content : content,
            })
        }
    })
}
module.exports = {
    hello,
    menu,
    insert,
    getinsert,
}