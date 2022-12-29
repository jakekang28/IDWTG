"use strict";

const hello = (req, res)=> {
    res.render("home/homeview")
}
const write = (req, res) => {
    res.render("/write")
}

module.exports = {
    hello,
    write,
}