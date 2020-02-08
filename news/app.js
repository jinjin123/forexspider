var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var axios = require("axios");
var io = require("socket.io-client");
var indexRouter = require('./routes/index');
// var usersRouter = require('./routes/users');

var app = express();

var tasks = []

function addTask(task) {
    tasks.push(task);
}

var getJten = {
    reconnI: function() {
        var t = this;
        t.initI();
    },
    reconnS: function() {
        var t = this;
        t.initS();
    },
    reconnF: function() {
        var t = this;
        t.initF();
    },

    initI: function() {
        var t = this;
        var socket = io.connect('https://sscpgpecdd.jin10.com:8082', {
            "force new connection": !0,
            "reconnection": !1
        })
        socket.on('connect', function() {
            console.log("index socket conn")
            socket.emit("switch_channel", 3, function() {})
        })
        socket.on('flash', function(data) {
            if (data.data) {
                let playload = {
                    content: data.data.content.replace("<b>", "").replace("</b>", "").replace("<br/>", ""),
                    tag: data.id,
                    time: data.time,
                    exttime: data.time.split(" ")[0]
                };
                syncPost(playload)
            }

        })
        socket.on('error', function(err) {
            console.log(err)
        })
        socket.on('connect_error', function(err) {
            console.log(err)
        })
        socket.on('disconnect', function() {
            console.log("index socket close")
            t.reconnI();
        })
        next()
    },
    initS: function() {
        var t = this;
        var socket = io.connect('https://sscpgpecdd.jin10.com:8082', {
            "force new connection": !0,
            "reconnection": !1
        })
        socket.on('connect', function() {
            socket.emit("switch_channel", 2, function() {})
            console.log("shop socket conn")
        })
        socket.on('flash', function(data) {
            if (data.data) {
                let playload = {
                    content: data.data.content.replace("<b>", "").replace("</b>", "").replace("<br/>", ""),
                    tag: data.id,
                    time: data.time,
                    exttime: data.time.split(" ")[0]
                };
                syncPost(playload)
            }
        })
        socket.on('error', function(err) {
            console.log(err)
        })
        socket.on('connect_error', function(err) {
            console.log(err)
        })
        socket.on('disconnect', function() {
            console.log("shop socket close")
            t.reconnS();
        })
        next()
    },
    initF: function() {
        var t = this;
        var socket = io.connect('https://sscpgpecdd.jin10.com:8082', {
            "force new connection": !0,
            "reconnection": !1
        })
        socket.on('connect', function() {
            socket.emit("switch_channel", 1, function() {})
            console.log("forex socket conn")
        })
        socket.on('flash', function(data) {
            if (data.data) {
                let playload = {
                    content: data.data.content.replace("<b>", "").replace("</b>", "").replace("<br/>", ""),
                    tag: data.id,
                    time: data.time,
                    exttime: data.time.split(" ")[0]
                };
                syncPost(playload)
            }
            console.log(data)
        })
        socket.on('error', function(err) {
            console.log(err)
        })
        socket.on('connect_error', function(err) {
            console.log(err)
        })
        socket.on('disconnect', function() {
            console.log("forex socket close");
            t.reconnF();
        })
    }
}


function next() {
    if (tasks.length > 0) {
        tasks.shift()();
    } else {
        return;
    }
}
addTask(getJten.initI);
addTask(getJten.initS);
addTask(getJten.initF);
next()

function syncPost(playload) {
    axios
        .post("http://192.168.50.100:8082/news/jten/", playload)
        .then(function(res) {
            // console.log(res);
        })
        .catch(function(error) {
            console.log(error);
        });
}


// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
// app.use('/users', usersRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
    next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get('env') === 'development' ? err : {};

    // render the error page
    res.status(err.status || 500);
    res.render('error');
});

module.exports = app;