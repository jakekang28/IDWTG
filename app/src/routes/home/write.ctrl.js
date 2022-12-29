const db = require("../../config/db")
const fs = require("fs")

const hello = (req, res)=> {
    res.render("home/writeview")
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
            
        var JsonData = document.getElementByID("myJsonData");
        var myJsonData = JSON.parse(jsonData);
            res.render('home/writeview',{data : jsonData})
         }
    })
    fs.readFile('writeview.ejs', 'utf8', function (err, data) {
        res.send(data)
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