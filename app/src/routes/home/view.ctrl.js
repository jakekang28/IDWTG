const db = require("../../config/db")



const read = (req, res)=> {
    db.query('SELECT * FROM article', function(err, results) {
        if(err) {
            res.send(err)
        } else {
            //  res.render('home/admin',{data : results})
             res.send(results);
        }
    })  
}

module.exports = {
    read,
}