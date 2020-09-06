<template>
    <div class="singleExpandingCard">
            <div class="img">
                <img :src='img'>
            </div>
            <div class="content">
                <a href="#"><p class="title">{{title}}</p></a>
                <p>{{getDescs(descs)}}</p>
            </div>
    </div>
</template>


<style scoped>
    .title{
        color:rgb(39, 39, 129)
    }
    .singleExpandingCard{
        max-width:300px;
        height:215px;
        position:relative;
        padding:20px 15px;
        display:flex;
        flex-direction:column;
        align-items:center;
        transition:0.5s ease-in-out;
        background: #fff;
        margin:20px;
        box-shadow:0 5px 202px rgba(0,0,0,0.5)
    }
    .singleExpandingCard:hover{
        height:420px
    }
    .img{
        position:relative;
        width:260px;
        height:260px;
        top:-80px;
        
        transform-style: preserve-3d;
        
    }
    img{
        width:100%;
        width:260px;
        height:260px;
        border-radius:4px;
    }
    .content{
        position:relative;
        margin-top:-140px;
        padding:10px 15px;
        text-align:center;
        opacity:0;
        visibility:hidden;
        transition:0.3s ease-in-out
    }
    .singleExpandingCard:hover .content{
        visibility: visible;
        opacity:1;
        margin-top:-40px
    }
    @media (max-width:679px){
        .singleExpandingCard:not(:first-child)
        {
            margin-top:100px
        }
    }
</style>


<script>
    import tilt from "../../vannilajs/tilt.js"
    export default{
        props:["img",'title','descs'],
        methods:{
            getDescs(txt){
                return txt.length>100 ? txt.slice(0,100) : txt
            }
        },
        mounted(){
            // VanillaTilt.init(document.querySelectorAll(".singleExpandingCard"), {
            //     max: 30,
            //     speed: 400,
            //     glare:false
            // });
        }

    }
</script>