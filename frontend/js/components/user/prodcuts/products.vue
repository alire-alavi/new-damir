<template>
    <div id="products" class='shouldCollapse'>
        <div class="filterText">
           <button class='submit' @click='toggleFiltering()'><img src="/images/filter.png" alt="" class="filterIcon"> فیلتر محصولات </button>
        </div>
        <div @click='toggleConsulate(),adjustConsulateTop()' class="speek">
            <p>مشاوره رایگان</p>
        </div>
        <div id="productsWrapper" class='maxis'>
            <div class="product">
                <div class="productImg">
                    <img src="/images/htest2.jpg" alt="">
                </div>
                <div class="descs">
                    <div class="productTitle">
                        <p><a href="#">امپلی فایر مدل PA system S30-/60M</a></p>
                    </div>
                    <div class="productDescs">
                        <p>{{getDescs(descs)}}</p>
                    </div>
                </div>
                <div class="productRegion">
                    <div class="compony">
                        <p>ساخت گلد  ایرن</p>
                    </div>
                    <div class="region">
                        <p>چین</p>
                        <img src="/images/china.png" alt="china"> 
                        
                    </div>
                    <div class="seeProduct">
                        <a class='submit' href="#">مشاهده محصول</a>
                    </div>
                </div>
            </div>


            <hr>


            <div class="product">
                <div class="productImg">
                    <img src="/images/ampl.jpg" alt="">
                </div>
                <div class="descs">
                    <div class="productTitle">
                        <p><a href="#">امپلی فایر مدل PA system S30-/60M</a></p>
                    </div>
                    <div class="productDescs">
                        <p>{{getDescs(descs)}}</p>
                    </div>
                </div>
                <div class="productRegion">
                    <div class="compony">
                        <p>ساخت گلد ایران ایران ایران ایرن</p>
                    </div>
                    <div class="region">
                        <p>چین</p>
                        <img src="/images/china.png" alt="china">
                        
                    </div>
                    <div class="seeProduct">
                        <a class='submit' href="#">مشاهده محصول</a>
                    </div>
                </div>
            </div>





        </div>
        <transition name="fade" mode='out-in'>
            <consulate></consulate>
        </transition>
        <keep-alive>
            <filtering v-if='shoudShow()'></filtering>
        </keep-alive>

    </div>
</template>

<style scoped>
    .speek{
        background: rgb(229,46,113);
        position:fixed;
        right:0;
        top:80%;
        z-index:665;
        cursor:pointer
    }
    .speek p{
        padding:10px;
        color:white;
        font-size:10pt;
        
    }
    .filterText{
        width:100%;
        display:flex;
        justify-content: center;
        margin-top:10px
    }
    #products{
        display:flex;
        flex-direction: column;
        align-items: flex-end;
        background: white;
        margin-top:20px
    }
    #productsWrapper{
        padding:10px;
    }
    .product{
        display:flex;
        justify-content: space-between;
    }
    .product:not(:first-child)
    {
        margin-top:20px
    }
    .descs{
        display:flex;
        flex-direction:column;
        align-items: flex-end;
        width:60%;
        order:2
    }
    .productTitle a{
        color:rgb(74, 96, 192)
    }

    .region img{
        width:40px;
        height: 30px;
    }
    .productImg{
        order:3;
        display:flex;
        justify-content: center;
        align-items: center;
        width:20%
    }
    .productDescs p{
        font-size:14pt
    }
    .compony p{
        font-size:12pt
    }
    .productImg img{
        width:100%;
    }
    .seeProduct{
        margin-top:20px
    }
    .productRegion{
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items: center;
        order:1;
        width:20%;
        border:5px solid rgb(211, 219, 221)
    }
    .productRegion div{
        padding:5px
    }
    .region{
        display:flex
    }
    .region p{
        margin-right:5px
    }
    .productImg img:hover{
        transform: scale(1.4);
    }
    @media (max-width:815px)
    {
        .product{
            flex-direction: column;
        }
        .descs
        {
            width:100%
        }
        .productRegion{
            order:3;
            height: 150px;
            width:300px;
            max-width: max-content;
            margin:auto;
            margin-top:20px
        }
        .productImg{
            order:1;
            width:100%;
        }
        .productImg img{
            width:250px;
        }
        .productTitle p{
            font-size: 15pt;
            line-height: 120%;
        }
        .productDescs p{
            line-height: 120%;
        }
    }
    .submit img.filterIcon{
        width:20px;
        height:20px
    }
    .submit{
        display: flex;
        align-items: center;
    }
    .fade-enter-active{
        animation: fadeIn 0.3s linear;
    }
    .fade-leave-active{
        animation: fadeOut 0.3s linear;
    }
    @keyframes fadeIn {
        from{
            opacity: 0;
        }
        to{
            opacity: 1;
        }
    }
    @keyframes fadeOut {
        from{
            opacity: 1;
        }
        to{
            opacity: 0;
        }
    }

</style>

<script>
    import {mapActions} from 'vuex'
    import consulate from "./consulate.vue"
    import filtering from "./filtering.vue"
    export default{
        components:{
            consulate,
            filtering
        },
        data(){
            return{
                descs:'محصول ساخت چین قدرت تولید صدا تا 1200 دسیبل دارای باتری 36 ولت فلان لان فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان  فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان فلان لان فلان فلان الن'
            }
        },
        methods:{
            ...mapActions([
               'toggleFiltering',
               'toggleConsulate'
            ]),
            getDescs(){
                return this.descs.length>100 ? this.descs.substring(0,200)+'...' : this.descs
            },
            adjustConsulateTop(){
                const consulate=document.querySelector("#consulateWrapper")
                consulate.style.top=window.scrollY+100+"px"
                document.body.style.overflow='hidden'
                const done=document.querySelector("#doneMessage")
                done.style.display='none'
            },
            shoudShow(){
                return this.$store.state.isShowFiltering
            }
        }
    }
</script>