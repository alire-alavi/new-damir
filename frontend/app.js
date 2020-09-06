const path=require("path")
const express=require('express')
const b=require("body-parser")
const app=express()
var EJS  = require('ejs');
const fileUpload = require('express-fileupload');
app.set("view engine",'ejs')
app.set('views', 'views')
app.use(b.urlencoded({ extended: false }))
app.use(b.json())
app.use(fileUpload());
app.use(express.static(__dirname + '/public'))
const r=express.Router()
app.use('/scripts', express.static(__dirname + '/node_modules/bootstrap/dist/'));

app.get("/",(req,res)=>{
    res.render("index")
})
app.use('/userPanel',(req,res)=>{
    res.render("userPanel")
})


app.get("/singleProduct",(req,res)=>{
    res.render("product")
})
app.get("/products",(req,res)=>{
    res.render("products")
})

app.get("/signin",(req,res)=>{
    res.render("signin")
})

app.get("/signup",(req,res)=>{
    res.render("signup")
})
app.post('/testy',(req,res)=>{
    console.log(req.body)
})
app.post("/blob",(req,res)=>{
    console.log(req.body)
    
    res.redirect("back")
})
app.get("/blog",(req,res)=>{
    return res.render("blog")
})
app.get("/singleBlogPost",(req,res)=>{
    return res.render("singleblogPost")
})
app.use("/blobyImage",async (req,res)=>{
        const file=req.files.file
        console.log(file)
        await file.mv('public/chikmkmna.png', function(err) {
            if (err)
              {
                  console.log(err)
                  return res.status(500).send(err);
                }
        
                res.setHeader('Content-Type', 'application/json');
                res.end(JSON.stringify({ location:"/chikmkmna.png" }));
          })
})

app.listen(3000)