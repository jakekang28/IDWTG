"use strict";
const express = require("express")
const app = express()
const router = express.Router();


const ctrl = require("./home.ctrl")
const ctrlwrite = require("./write.ctrl")
router.get('/', ctrl.hello)
router.get('/write',ctrlwrite.hello)
module.exports = router;