<template>
    <div class="singleBlogPost">
        <div class="singlePostWrapper">
            <div class="img">
                <img :src="img">
            </div>
            <div class="descs">
                <p>{{getDescs(descs)}}</p>

                <p class='timeAndCat'>بسته بندی | مدت زمان خواندن 5 دقیقه</p>
            </div>
        </div>
    </div>
    
</template>

<style scoped>


.singleBlogPost{
    width:300px;
    height:400px;
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
    width:300px;
    height:200px
}
.descs{
    background: rgb(235,242,248);
    height:200px;
    display:flex;
    flex-direction:column;
    justify-content: space-between;
}
.descs p{
    text-align:justify ;
    padding:10px;    
}
img{
    width:100%;
    height:200px;
}
.timeAndCat{
    font-size: 15px;
    font-weight: 800;
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
