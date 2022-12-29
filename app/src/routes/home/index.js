"use strict";
const express = require("express")
const app = express()

const router = express.Router();

const ctrl = require("./home.ctrl")
const ctrlwrite = require("./write.ctrl")
const ctrlview = require("./view.ctrl");
const { create } = require("domain");

router.get('/', ctrl.hello)
router.get('/',ctrl.write)
router.get('/write',ctrlwrite.hello)
router.get('/view',ctrlwrite.getinsert)
// router.get('/write', ctrlwrite.getinsert)
router.post('/view',ctrlwrite.insert)
module.exports = router