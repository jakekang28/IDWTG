const hello = (req, res)=> {
    res.render("home/homeview")
}
const write = (req, res) => {
    res.redirect("/write")
}

module.exports = {
    hello,
    write,
}