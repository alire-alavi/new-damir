<template>
    <div class="singleDigicard">
        <div v-for="(img,i) in renderImgs" :key="i" class="singleDigicardWrapper">
            <img  :src="img" alt="">
        </div>
    </div>
</template>

<script>
    export default{
        props:['imgs'],
        computed:{
            renderImgs(){
                return JSON.parse(this.imgs)
            }
        }
    }
</script>

<style scoped>
    .singleDigicard{
        display:flex;
        flex-wrap: wrap;
        width:100%;
        justify-content: center;
        
    }
    .singleDigicardWrapper{
        margin:5px;
        width:350px        
    }
    img{
        border-radius: 16px;
        width:100%
    }
    @media (max-width:666px){
        img{
            width:100%
        }
        .singleDigicardWrapper{
            width:100%   
        }    

    }
</style>