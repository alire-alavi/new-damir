<template>
    <div id="product" class='mainItemPerPage shouldCollapse'>
        <div id="productWrapper" class='maxis'>
            <prudctDetail></prudctDetail>
            <hr>
            <div class="chooseSection">
                <div class="section">
                    <p @click='currentComponent="technicalDetail",changeButtonColor($event)'>مشخصات فنی</p>
                </div>
                <div class="section">
                    <p @click='currentComponent="componyDetali",changeButtonColor($event)'>مشخصات شرکت</p>
                </div>

                <div class="section">
                    <p @click='currentComponent="productDescs",changeButtonColor($event)'>توضیحات محصول</p>
                </div>
            </div>
            <hr>
            <transition name="swapComp" mode="out-in">
                <component :is="currentComponent"></component>

            </transition>
            <comment-section></comment-section>
        </div>


    </div>


</template>

<script>
    import prudctDetail from "./productDetaile.vue"
    import commentSection from './commentSection.vue'
    import productDescs from './productDescs.vue'
    import componyDetali from "./componyDetail.vue"
    import technicalDetail from "./technicalDetatil.vue"
    import axios from 'axios'
    export default{
        data(){
            return{
                currentComponent:'productDescs'
            }
        },
        mounted(){
            axios({
                method: 'get',
                headers: { 'Content-Type': 'application/json','Accept':"*/*" },
                crossDomain: true,
                url: 'http://rlbapi.pythonanywhere.com/products-api/'
              }).then(function (response) {
                console.log(response.data);
            });
            // axios.get('http:/\/\rlbapi.pythonanywhere.com/products-api')
            //     .then(res=>{
            //         console.log(res.data)
            //     })
        },
        name:"product",
        components:{
            prudctDetail,
            commentSection,
            productDescs,
            componyDetali,
            technicalDetail
        },
        methods:{
            changeButtonColor(e){
                const secs=document.querySelectorAll(".chooseSection p")
                secs.forEach(sec=>{
                    sec.style.color="rgb(105, 98, 209)"
                })
                e.target.style.color="rgb(229,46,113)"
            }
        }

    }
</script>
<style>
    #product{
        background:white;
        display:flex;
        flex-direction:column;
        align-items:center
    }
    
    #productDetail{
        grid-area:productDetail
    }
    #productComments{
        grid-area:productComments
    }
    #productWrapper{
        display:flex;
        flex-direction:column;
        width:100%;
        max-width:1500px;
    }
    .chooseSection{
        display:flex;
        justify-content: center;
        border-bottom:1px solid rgb(209, 196, 196)
    }
    .section{
        border:1px solid rgb(209, 196, 196);
        margin:5px;
        cursor:pointer
    }
    .chooseSection p{
        padding:10px;
        color:rgb(105, 98, 209)
    }
    @media (max-width:509px)
    {
        .chooseSection{
            flex-direction:column;
            align-items: center;
        }
        .section{
            width:200px;
            display:flex;
            justify-content: center;
        }
        .section p{
            max-width:max-content
        }
    }
    .swapComp-enter-active{
        animation:comeIn 0.25s linear
    }
    .swapComp-leave-active{
        animation:comeOut 0.25s linear
    }
    @keyframes comeIn {
        from{
            opacity:0
        }
        to{
            opacity: 1;
        }
    }

    @keyframes comeOut {
        from{
            opacity:1
        }
        to{
            opacity: 0;
        }
    }

</style>