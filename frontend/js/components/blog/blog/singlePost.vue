<template>
    <div class="singleBlogPost">
        <div class="singlePostWrapper">
            <div class="title">
                <p>{{title}}</p>
            </div>
            <div class="img">
                <img :src="img">
            </div>
            <div class="descs">
                <p>{{getDescs(descs)}}</p>
            </div>
            <div class="show">
                <button class="specialBTN">مشاهده مطلب</button>
            </div>
        </div>
    </div>
    
</template>

<style scoped>


.singleBlogPost{
    width:280px;
    height:430px;
    margin:20px;
    margin-top:40px;
}
.singlePostWrapper{
    width:100%;
}
.title{
    margin-bottom:5px
}
.title p{
    color:rgb(236,57,68)
}
.img{
    width:280px;
}
.descs p{
    text-align:justify ;
    height:90px;
}
img{
    width:100%;
    border-radius: 10px;
}
</style>

<script>
export default {
    props:['title','img','descs'],
    methods:{
        getDescs(txt){
            return txt.length>100 ? `${txt.slice(0,100)}...` : txt
        }
    }
}
</script>
