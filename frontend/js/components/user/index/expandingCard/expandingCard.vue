<template>
    <div id="expandingCards">
        <div id="expandingCardsWrapper">

            <single-expanding-card
                img="/images/1.jpg"
                title="دستگاه برش آب چسب"
                descs='دستگاه اسکین پک نوعی بسته بندی برای قطعات ، ابزار ، مواد غذایی تازه و…است که با استفاده از فیلم های حساس به گرما و حرارت کار می کنند.'
            ></single-expanding-card> 


            <single-expanding-card
                img='/images/2.jpg'
                title="باندرول"
                descs='دستگاه باندرول وظیفه بستن یک نوار از جنس کاغذ یا پارچه و پلاستیک را به دور دسته ای از محصولات به عهده دارد 
این دستگاهها در بستن پول که باند رول های کاغذی آن را انجام می دهند نقش دارند تا بستن و دسته بندی کردن انواع بسته بندی های قابل بستن با نوار مثل لوازم التحریر ،صنایع غذایی و به صورت کلی هر محصولی که بصورت کارتی و یا بصورت میله ای بسته بندی می شود و قابلیت کنار هم قرار گرفتن دارد می تواند با این دستگاهها بسته بندی شود .'
            ></single-expanding-card>
            
        </div>
    </div>
</template>

<script>
    import singleExpandingCard from "./signleExpandingCard.vue"
    export default {
        components:{
            singleExpandingCard
        }
    }
</script>


<style scoped>
    #expandingCards{
        background:#16384c;
        width:100%;
    }
    #expandingCardsWrapper{
        display:flex;
        justify-content: center;
        flex-wrap:wrap;
        margin-top:100px;
    }
</style>>


</style>