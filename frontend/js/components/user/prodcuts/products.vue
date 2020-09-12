<template>
    <div id="products" class='shouldCollapse maxIs'>
        <div id="productsWrapper">
            <div class="singleProduct">
                <div class="img">
                    <img src="/images/1.jpg" alt="">
                </div>
                <div class="title">
                    <a href="#"><p>خط تولید فلان</p></a>
                </div>
                <div class="price">
                    <p>3200000 تومان</p>
                    <p>حداقل خرید : یک تن</p>
                </div>
                <div class="contactUs">
                    <button class="submit" @click.prevent='showConsulate($event)'>استعلام قیمت</button>
                </div>
                <consulate productName="خط تولید"></consulate>
            </div>

            <div class="singleProduct">
                <div class="img">
                    <img src="/images/ours1.png" alt="">
                </div>
                <div class="title">
                    <a href="#"><p>خط تولید فلان</p></a>
                </div>
                <div class="price">
                    <p>3200000 تومان</p>
                    <p>حداقل خرید : یک تن</p>
                </div>
                <div class="contactUs">
                    <button class="submit" @click.prevent='showConsulate($event)'>استعلام قیمت</button>
                </div>
                <consulate productName="خط تولید"></consulate>
            </div>
            <div class="singleProduct">
                <div class="img">
                    <img src="/images/1.jpg" alt="">
                </div>
                <div class="title">
                    <a href="#"><p>خط تولید فلان</p></a>
                </div>
                <div class="price">
                    <p>3200000 تومان</p>
                    <p>حداقل خرید : یک تن</p>
                </div>
                <div class="contactUs">
                    <button class="submit" @click.prevent='showConsulate($event)'>استعلام قیمت</button>
                </div>
                <consulate productName="خط تولید"></consulate>
            </div>
            <div class="singleProduct">
                <div class="img">
                    <img src="/images/1.jpg" alt="">
                </div>
                <div class="title">
                    <a href="#"><p>خط تولید فلان</p></a>
                </div>
                <div class="price">
                    <p>3200000 تومان</p>
                    <p>حداقل خرید : یک تن</p>
                </div>
                <div class="contactUs">
                    <button class="submit" @click.prevent='showConsulate($event)'>استعلام قیمت</button>
                </div>
                <consulate productName="خط تولید"></consulate>
            </div>
            <div class="singleProduct">
                <div class="img">
                    <img src="/images/1.jpg" alt="">
                </div>
                <div class="title">
                    <a href="#"><p>خط تولید فلان</p></a>
                </div>
                <div class="price">
                    <p>3200000 تومان</p>
                    <p>حداقل خرید : یک تن</p>
                </div>
                <div class="contactUs">
                    <button class="submit" @click.prevent='showConsulate($event)'>استعلام قیمت</button>
                </div>
                <consulate productName="خط تولید"></consulate>
            </div>
            <div class="singleProduct">
                <div class="img">
                    <img src="/images/1.jpg" alt="">
                </div>
                <div class="title">
                    <a href="#"><p>خط تولید فلان</p></a>
                </div>
                <div class="price">
                    <p>3200000 تومان</p>
                    <p>حداقل خرید : یک تن</p>
                </div>
                <div class="contactUs">
                    <button class="submit" @click.prevent='showConsulate($event)'>استعلام قیمت</button>
                </div>
                <consulate productName="خط تولید"></consulate>
            </div>
            <div class="singleProduct">
                <div class="img">
                    <img src="/images/1.jpg" alt="">
                </div>
                <div class="title">
                    <a href="#"><p>خط تولید فلان</p></a>
                </div>
                <div class="price">
                    <p>3200000 تومان</p>
                    <p>حداقل خرید : یک تن</p>
                </div>
                <div class="contactUs">
                    <button class="submit" @click.prevent='showConsulate($event)'>استعلام قیمت</button>
                </div>
                <consulate productName="خط تولید"></consulate>
            </div>
            <div class="singleProduct">
                <div class="img">
                    <img src="/images/1.jpg" alt="">
                </div>
                <div class="title">
                    <a href="#"><p>خط تولید فلان</p></a>
                </div>
                <div class="price">
                    <p>3200000 تومان</p>
                    <p>حداقل خرید : یک تن</p>
                </div>
                <div class="contactUs">
                    <button class="submit" @click.prevent='showConsulate($event)'>استعلام قیمت</button>
                </div>
                <consulate productName="خط تولید"></consulate>
            </div>
            <div class="singleProduct">
                <div class="img">
                    <img src="/images/1.jpg" alt="">
                </div>
                <div class="title">
                    <a href="#"><p>خط تولید فلان</p></a>
                </div>
                <div class="price">
                    <p>3200000 تومان</p>
                    <p>حداقل خرید : یک تن</p>
                </div>
                <div class="contactUs">
                    <button class="submit" @click.prevent='showConsulate($event)'>استعلام قیمت</button>
                </div>
                <consulate productName="خط تولید"></consulate>
            </div>
            
        </div>

    </div>
</template>

<style scoped>
#products{
    margin-top:50px
}
#productsWrapper{
    display:flex;
    flex-wrap: wrap;
    justify-content: center;
}
.singleProduct{
    width:23%;
    margin:10px;
    width:300px
}
img{
    height:300px;
    width:300px;
    
}
.title{
    height:100px
}
.contactUs{
    display:flex;
    justify-content: center;
}

</style>

<script>
    import {mapActions} from 'vuex'
    import consulate from "./consulate.vue"
    import filtering from "./filtering.vue"
     import {adjustElFromTop} from "../../user/mixIns/adjustElFromTop.js"
    export default{
        components:{
            consulate,
            filtering
        },
        mixins:[adjustElFromTop],
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
            },
            showConsulate(e){
                const el=e.target;
                const parent=el.closest(".singleProduct")
                const consulate=parent.querySelector(".consulateWrapper")
                console.log(parent)
                consulate.style.display="flex"
                this.adjustFromTop(consulate,false)
                
            }
        }
    }
</script>